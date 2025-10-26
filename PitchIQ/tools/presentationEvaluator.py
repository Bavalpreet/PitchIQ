# PitchIQ/tools/presentationEvaluator.py
from google.adk.tools.tool_context import ToolContext
from typing import Dict, Any, Optional
import os
import tempfile
from pathlib import Path
import json

# Google Cloud imports
import vertexai
from vertexai.generative_models import GenerativeModel, Part

# Import existing YouTube downloader
from .youtubeDownloader import _download_video_internal

"""
Presentation Evaluator Tool for ADK Agent
Evaluates video presentations and provides scores out of 15 across multiple criteria.
Uses Google Vertex AI Gemini for comprehensive presentation analysis.
"""

# Get the repository root
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _evaluate_presentation_with_gemini(
    video_path: str,
    evaluation_criteria: Optional[str] = None
) -> tuple[bool, Dict[str, Any], str]:
    """
    Evaluate presentation using Gemini multimodal model.
    
    Args:
        video_path: Path to the video file
        evaluation_criteria: Custom evaluation criteria (optional)
        
    Returns:
        tuple: (success: bool, evaluation_result: dict, error: str)
    """
    try:
        # Initialize Vertex AI
        project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
        location = os.getenv('GOOGLE_CLOUD_LOCATION', 'us-central1')
        
        if not project_id:
            return False, None, "GOOGLE_CLOUD_PROJECT environment variable not set"
        
        vertexai.init(project=project_id, location=location)
        
        # Use Gemini 2.0 Flash for video understanding
        model = GenerativeModel("gemini-2.0-flash-exp")
        
        # Read video file
        with open(video_path, 'rb') as f:
            video_data = f.read()
        
        # Create video part
        video_part = Part.from_data(
            data=video_data,
            mime_type="video/mp4"
        )
        
        # Default evaluation prompt
        if not evaluation_criteria:
            evaluation_criteria = """Evaluate this presentation video comprehensively and provide a detailed assessment with scores.

SCORING RUBRIC (Total: 15 points):

1. CLARITY & COMMUNICATION (0-3 points)
   - Voice clarity and articulation
   - Pace and rhythm of speech
   - Audio quality
   - Language proficiency and grammar

2. STRUCTURE & ORGANIZATION (0-3 points)
   - Logical flow and structure
   - Introduction, body, and conclusion
   - Time management
   - Smooth transitions between topics

3. DELIVERY & PRESENTATION SKILLS (0-3 points)
   - Confidence and presence
   - Eye contact and body language
   - Enthusiasm and engagement
   - Professional appearance

4. CONTENT & SUBSTANCE (0-3 points)
   - Depth of content
   - Relevance and accuracy
   - Problem-solution clarity
   - Innovation and creativity

5. VISUAL AIDS & PRODUCTION (0-3 points)
   - Slide quality and design (if applicable)
   - Visual demonstrations
   - Video production quality
   - Use of supporting materials

EVALUATION FORMAT:
Provide your evaluation in the following JSON structure:

{
    "total_score": [0-15],
    "criteria_scores": {
        "clarity_communication": {
            "score": [0-3],
            "feedback": "Detailed feedback on clarity and communication"
        },
        "structure_organization": {
            "score": [0-3],
            "feedback": "Detailed feedback on structure and organization"
        },
        "delivery_presentation": {
            "score": [0-3],
            "feedback": "Detailed feedback on delivery and presentation skills"
        },
        "content_substance": {
            "score": [0-3],
            "feedback": "Detailed feedback on content and substance"
        },
        "visual_production": {
            "score": [0-3],
            "feedback": "Detailed feedback on visual aids and production"
        }
    },
    "strengths": ["List 3-5 key strengths"],
    "areas_for_improvement": ["List 3-5 areas for improvement"],
    "overall_feedback": "Comprehensive summary of the presentation evaluation",
    "key_highlights": ["Notable moments or aspects of the presentation"],
    "recommendations": ["Specific actionable recommendations"]
}

Be objective, constructive, and thorough in your evaluation. Provide specific examples from the video to support your scores."""
        
        # Generate content
        response = model.generate_content([video_part, evaluation_criteria])
        
        # Parse response
        response_text = response.text
        
        # Try to extract JSON if present
        evaluation_result = {
            "raw_evaluation": response_text,
            "model_used": "gemini-2.0-flash-exp",
            "evaluation_criteria": evaluation_criteria
        }
        
        # Attempt to parse JSON from response
        try:
            # Look for JSON structure in the response
            start_idx = response_text.find('{')
            end_idx = response_text.rfind('}') + 1
            if start_idx != -1 and end_idx > start_idx:
                json_str = response_text[start_idx:end_idx]
                parsed_eval = json.loads(json_str)
                evaluation_result["structured_evaluation"] = parsed_eval
        except json.JSONDecodeError:
            # If JSON parsing fails, keep the raw evaluation
            pass
        
        return True, evaluation_result, None
        
    except Exception as e:
        return False, None, str(e)


def evaluate_presentation(
    source: str,
    source_type: str = "auto",
    evaluation_criteria: Optional[str] = None,
    tool_context: ToolContext = None
) -> Dict[str, Any]:
    """
    Evaluate a presentation video and provide comprehensive scoring out of 15 points.

    Args:
        source: Either a YouTube URL or path to local MP4 file
        source_type: Type of source - "youtube", "file", or "auto" (default: "auto")
        evaluation_criteria: Custom evaluation criteria (optional)
        tool_context: Tool context (optional for session actions)

    Returns:
        Dict with presentation evaluation results including scores and detailed feedback
    """
    temp_video_path = None
    cleanup_file = False
    
    try:
        # Determine source type
        if source_type == "auto":
            if source.startswith("http://") or source.startswith("https://") or "youtube.com" in source or "youtu.be" in source:
                source_type = "youtube"
            else:
                source_type = "file"
        
        # Get video file
        if source_type == "youtube":
            print(f"Downloading presentation video from YouTube: {source}")
            
            # Create temp directory for download
            temp_dir = tempfile.mkdtemp()
            success, video_path, error = _download_video_internal(source, temp_dir)
            
            if not success:
                return {
                    "success": False,
                    "error": f"Failed to download video: {error}",
                    "source": source,
                    "source_type": "youtube"
                }
            
            temp_video_path = video_path
            cleanup_file = True
            
        else:  # file
            # Handle relative paths from repo root
            if not os.path.isabs(source):
                video_path = os.path.join(REPO_ROOT, source)
            else:
                video_path = source
            
            if not os.path.exists(video_path):
                return {
                    "success": False,
                    "error": f"Video file not found: {source}",
                    "source": source,
                    "source_type": "file"
                }
            
            temp_video_path = video_path
            cleanup_file = False
        
        # Get video file info
        video_size = os.path.getsize(temp_video_path)
        video_size_mb = video_size / (1024 * 1024)
        
        print(f"Evaluating presentation: {temp_video_path} ({video_size_mb:.2f} MB)")
        
        # Perform evaluation
        success, evaluation, error = _evaluate_presentation_with_gemini(
            temp_video_path,
            evaluation_criteria
        )
        
        if not success:
            return {
                "success": False,
                "error": f"Presentation evaluation failed: {error}",
                "source": source,
                "source_type": source_type
            }
        
        result = {
            "success": True,
            "source": source,
            "source_type": source_type,
            "video_size_mb": round(video_size_mb, 2),
            "evaluation": evaluation,
            "message": "Presentation evaluation completed successfully"
        }
        
        return result
        
    except Exception as e:
        return {
            "success": False,
            "error": f"Error evaluating presentation: {str(e)}",
            "source": source
        }
    
    finally:
        # Cleanup temporary files if needed
        if cleanup_file and temp_video_path and os.path.exists(temp_video_path):
            try:
                os.remove(temp_video_path)
                # Also remove temp directory if empty
                temp_dir = os.path.dirname(temp_video_path)
                if os.path.exists(temp_dir) and not os.listdir(temp_dir):
                    os.rmdir(temp_dir)
            except Exception as e:
                print(f"Warning: Could not cleanup temp file: {e}")


def evaluate_presentation_quick(
    source: str,
    source_type: str = "auto",
    tool_context: ToolContext = None
) -> Dict[str, Any]:
    """
    Quick presentation evaluation with standard criteria (15 point scale).

    Args:
        source: Either a YouTube URL or path to local MP4 file
        source_type: Type of source - "youtube", "file", or "auto" (default: "auto")
        tool_context: Tool context (optional for session actions)

    Returns:
        Dict with presentation evaluation results
    """
    return evaluate_presentation(
        source=source,
        source_type=source_type,
        evaluation_criteria=None,  # Use default criteria
        tool_context=tool_context
    )
