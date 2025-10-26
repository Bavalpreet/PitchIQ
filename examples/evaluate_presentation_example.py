"""
Example: Using the Presentation Evaluator

This script demonstrates how to use the presentation evaluation feature
to analyze a YouTube video and get comprehensive scoring.
"""

import sys
import os
from pathlib import Path

# Add parent directory to path to import PitchIQ modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from PitchIQ.tools.presentationEvaluator import evaluate_presentation, evaluate_presentation_quick
import json


def main():
    """
    Example usage of the presentation evaluator.
    """
    
    print("=" * 60)
    print("🎯 PitchIQ Presentation Evaluator - Example")
    print("=" * 60)
    print()
    
    # Example YouTube URL (replace with your video)
    video_url = input("Enter YouTube video URL (or press Enter for demo): ").strip()
    
    if not video_url:
        print("\nNo URL provided. Using example workflow...\n")
        print_example_workflow()
        return
    
    print(f"\nEvaluating presentation: {video_url}")
    print("-" * 60)
    
    # Option 1: Quick evaluation with standard criteria
    print("\nRunning quick evaluation with standard criteria...")
    result = evaluate_presentation_quick(video_url)
    
    # Check if successful
    if not result.get("success"):
        print(f"\nError: {result.get('error')}")
        return
    
    # Display results
    print("\n" + "=" * 60)
    print("EVALUATION RESULTS")
    print("=" * 60)
    
    evaluation = result.get("evaluation", {})
    
    # Display structured evaluation if available
    if "structured_evaluation" in evaluation:
        structured = evaluation["structured_evaluation"]
        
        print(f"\n🎯 TOTAL SCORE: {structured.get('total_score', 'N/A')}/15")
        print("-" * 60)
        
        # Display criterion scores
        criteria_scores = structured.get("criteria_scores", {})
        if criteria_scores:
            print("\n📋 DETAILED BREAKDOWN:")
            for criterion, data in criteria_scores.items():
                score = data.get("score", "N/A")
                feedback = data.get("feedback", "")
                criterion_name = criterion.replace("_", " ").title()
                print(f"\n  {criterion_name}: {score}/3")
                if feedback:
                    print(f"    Feedback: {feedback[:100]}...")
        
        # Display strengths
        strengths = structured.get("strengths", [])
        if strengths:
            print("\n✅ STRENGTHS:")
            for strength in strengths:
                print(f"  • {strength}")
        
        # Display areas for improvement
        improvements = structured.get("areas_for_improvement", [])
        if improvements:
            print("\n🎯 AREAS FOR IMPROVEMENT:")
            for improvement in improvements:
                print(f"  • {improvement}")
        
        # Display recommendations
        recommendations = structured.get("recommendations", [])
        if recommendations:
            print("\n💡 RECOMMENDATIONS:")
            for rec in recommendations:
                print(f"  • {rec}")
        
        # Display overall feedback
        overall = structured.get("overall_feedback", "")
        if overall:
            print("\n💬 OVERALL FEEDBACK:")
            print(f"  {overall}")
    
    else:
        # Display raw evaluation if structured data not available
        print("\nRaw Evaluation:")
        print(evaluation.get("raw_evaluation", "No evaluation data available"))
    
    print("\n" + "=" * 60)
    print("Evaluation complete!")
    print("=" * 60)
    
    # Option to save results
    save = input("\nSave results to JSON file? (y/n): ").strip().lower()
    if save == 'y':
        output_file = "presentation_evaluation_results.json"
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"Results saved to: {output_file}")


def print_example_workflow():
    """
    Print an example workflow for using the evaluator.
    """
    
    example_code = """
# Example 1: Quick evaluation with standard criteria
from PitchIQ.tools.presentationEvaluator import evaluate_presentation_quick

result = evaluate_presentation_quick(
    source="https://youtube.com/watch?v=YOUR_VIDEO_ID"
)

if result["success"]:
    evaluation = result["evaluation"]
    structured = evaluation.get("structured_evaluation", {})
    
    total_score = structured.get("total_score")
    print(f"Total Score: {total_score}/15")
    
    # Access individual criterion scores
    criteria = structured.get("criteria_scores", {})
    print(f"Clarity: {criteria['clarity_communication']['score']}/3")
    print(f"Structure: {criteria['structure_organization']['score']}/3")
    # ... etc


# Example 2: Custom evaluation criteria
from PitchIQ.tools.presentationEvaluator import evaluate_presentation

custom_criteria = \"\"\"
Evaluate this presentation focusing on:
1. Technical accuracy (0-5 points)
2. Audience engagement (0-5 points)
3. Innovation (0-5 points)

Provide scores and detailed feedback for each.
\"\"\"

result = evaluate_presentation(
    source="https://youtube.com/watch?v=YOUR_VIDEO_ID",
    evaluation_criteria=custom_criteria
)


# Example 3: Evaluate local video file
result = evaluate_presentation_quick(
    source="/path/to/local/video.mp4",
    source_type="file"
)
"""
    
    print("EXAMPLE USAGE:")
    print("=" * 60)
    print(example_code)
    print("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nEvaluation cancelled by user.")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
