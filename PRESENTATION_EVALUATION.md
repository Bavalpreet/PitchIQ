# 🎯 PitchIQ Presentation Evaluation Feature

## Overview

**PitchIQ** is an intelligent video analysis and presentation evaluation platform that includes a comprehensive **AI-Powered Presentation Evaluator**. It analyzes video submissions and provides detailed scoring out of **15 points** across multiple criteria, powered by Google Gemini AI.

## Features

### 🎯 Comprehensive Scoring System

The evaluator assesses presentations across 5 key criteria, each worth 3 points:

1. **Clarity & Communication (0-3 points)**
   - Voice clarity and articulation
   - Pace and rhythm of speech
   - Audio quality
   - Language proficiency and grammar

2. **Structure & Organization (0-3 points)**
   - Logical flow and structure
   - Introduction, body, and conclusion
   - Time management
   - Smooth transitions between topics

3. **Delivery & Presentation Skills (0-3 points)**
   - Confidence and presence
   - Eye contact and body language
   - Enthusiasm and engagement
   - Professional appearance

4. **Content & Substance (0-3 points)**
   - Depth of content
   - Relevance and accuracy
   - Problem-solution clarity
   - Innovation and creativity

5. **Visual Aids & Production (0-3 points)**
   - Slide quality and design
   - Visual demonstrations
   - Video production quality
   - Use of supporting materials

### 📊 Visual Score Meters

Results are displayed with intuitive visual meters:
- **Color-coded progress bars** for each criterion
- **Overall score** with percentage and grade
- **Real-time scoring** displayed in the sidebar

### 📝 Detailed Feedback

Each evaluation includes:
- ✅ **Strengths**: 3-5 key strengths identified
- 🎯 **Areas for Improvement**: Specific areas to enhance
- 💬 **Overall Feedback**: Comprehensive summary
- 💡 **Recommendations**: Actionable next steps

## How to Use

### 1. Select Presentation Mode

Click the **🎤 Presentation Evaluation** button at the top of the interface to switch to evaluation mode.

### 2. Create a Session

In the sidebar, click **➕ Create Session** to start a new evaluation session.

### 3. Submit Video Link

Paste your YouTube video link in the chat input. The system supports:
- YouTube URLs (youtube.com/watch?v=...)
- YouTube short URLs (youtu.be/...)
- Direct video links

### 4. Get Evaluation

The AI agent will:
1. Download and analyze the video
2. Evaluate across all 5 criteria
3. Provide detailed scores and feedback
4. Display visual meters for easy understanding

### 5. Review Results

Review your presentation evaluation with:
- Total score out of 15
- Individual criterion scores (out of 3 each)
- Detailed feedback for each area
- Strengths and improvement suggestions
- Actionable recommendations

## Grading Scale

| Score Range | Grade | Description |
|-------------|-------|-------------|
| 13.5 - 15 | A+ | Excellent |
| 12 - 13.4 | A | Very Good |
| 10.5 - 11.9 | B | Good |
| 9 - 10.4 | C | Satisfactory |
| < 9 | Needs Improvement | Additional work recommended |

## API Integration

### Tools Available

Two evaluation tools are available:

1. **evaluate_presentation** - Full evaluation with custom criteria
   ```python
   evaluate_presentation(
       source="https://youtube.com/watch?v=...",
       source_type="auto",
       evaluation_criteria=None,  # Optional custom criteria
       tool_context=None
   )
   ```

2. **evaluate_presentation_quick** - Quick evaluation with standard criteria
   ```python
   evaluate_presentation_quick(
       source="https://youtube.com/watch?v=...",
       source_type="auto",
       tool_context=None
   )
   ```

### Response Format

The evaluation returns a structured dictionary:

```json
{
    "success": true,
    "source": "video_url",
    "source_type": "youtube",
    "video_size_mb": 25.4,
    "evaluation": {
        "raw_evaluation": "Full text response...",
        "structured_evaluation": {
            "total_score": 12.5,
            "criteria_scores": {
                "clarity_communication": {
                    "score": 2.5,
                    "feedback": "Clear voice with good pace..."
                },
                "structure_organization": {
                    "score": 2.5,
                    "feedback": "Well-organized content..."
                },
                "delivery_presentation": {
                    "score": 2.5,
                    "feedback": "Confident delivery..."
                },
                "content_substance": {
                    "score": 2.5,
                    "feedback": "Relevant and innovative..."
                },
                "visual_production": {
                    "score": 2.5,
                    "feedback": "Professional production quality..."
                }
            },
            "strengths": [
                "Excellent communication skills",
                "Well-structured content",
                "Engaging delivery"
            ],
            "areas_for_improvement": [
                "Could improve visual aids",
                "Add more examples"
            ],
            "overall_feedback": "Strong presentation overall...",
            "recommendations": [
                "Consider adding more visual elements",
                "Practice timing for smoother delivery"
            ]
        }
    }
}
```

## Technical Details

### Architecture

- **Tool**: `presentationEvaluator.py`
- **Prompt**: `presentation.prompt`
- **Model**: Gemini 2.0 Flash Exp (multimodal)
- **UI Components**: Visual meters, progress bars, score cards

### Processing Flow

1. Video download from YouTube (if URL provided)
2. Video uploaded to Gemini for multimodal analysis
3. AI evaluates across all criteria
4. JSON response parsed and structured
5. Visual results displayed with meters and feedback

### Dependencies

- `google-cloud-aiplatform` - Vertex AI integration
- `vertexai` - Gemini model access
- `yt-dlp` - YouTube video downloading
- `streamlit` - UI components

## Use Cases

- **Hackathon Submissions**: Evaluate pitch videos
- **Conference Presentations**: Score speaker performance
- **Educational Content**: Assess teaching videos
- **Sales Pitches**: Analyze presentation effectiveness
- **Training Sessions**: Evaluate instructor performance
- **Interview Recordings**: Score communication skills

## Tips for Best Results

1. **Video Quality**: Ensure clear audio and video
2. **Duration**: 2-10 minute presentations work best
3. **Content**: Have clear introduction, body, and conclusion
4. **Lighting**: Good lighting helps visual analysis
5. **Audio**: Clear audio improves speech analysis

## Customization

The evaluation criteria can be customized by:

1. Modifying the prompt in `presentation.prompt`
2. Adjusting scoring weights in `presentationEvaluator.py`
3. Adding custom evaluation criteria via the API

## Future Enhancements

Potential improvements:
- Multi-language support
- Custom rubric builder
- Batch evaluation of multiple videos
- Detailed timestamp analysis
- Comparison across multiple presentations
- Export evaluation reports (PDF, CSV)
