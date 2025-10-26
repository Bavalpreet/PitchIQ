"""
PitchIQ Application
"""
import streamlit as st
import requests
import json
import os
import uuid
import time
import re

# Set page config
st.set_page_config(
    page_title="PitchIQ - AI Presentation Evaluator",
    page_icon="🎯",
    layout="centered"
)

## Apply custom CSS for white background with dark purple text theme
# from pathlib import Path
# css_path = Path(__file__).parent / "vision-theme.css"
# st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

# Constants
API_BASE_URL = "http://localhost:8000"
APP_NAME = "PitchIQ"

# Initialize session state variables
if "user_id" not in st.session_state:
    st.session_state.user_id = f"user-{uuid.uuid4()}"
    
if "session_id" not in st.session_state:
    st.session_state.session_id = None
    
if "messages" not in st.session_state:
    st.session_state.messages = []

if "audio_files" not in st.session_state:
    st.session_state.audio_files = []

if "mode" not in st.session_state:
    st.session_state.mode = "analysis"  # "analysis" or "presentation"

if "last_evaluation" not in st.session_state:
    st.session_state.last_evaluation = None

def extract_evaluation_scores(response_text):
    """
    Extract evaluation scores from the agent's response.
    
    Args:
        response_text: The response text from the agent
        
    Returns:
        dict: Structured evaluation data or None
    """
    try:
        # Try to find JSON structure in the response
        json_match = re.search(r'\{[^{}]*"total_score"[^{}]*\}', response_text, re.DOTALL)
        if json_match:
            json_str = json_match.group(0)
            # Handle nested braces more carefully
            brace_count = 0
            for i, char in enumerate(response_text[json_match.start():]):
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        json_str = response_text[json_match.start():json_match.start() + i + 1]
                        break
            
            evaluation_data = json.loads(json_str)
            return evaluation_data
    except:
        pass
    
    # Fallback: try to extract scores using regex patterns
    try:
        scores = {}
        total_match = re.search(r'total[_\s]?score[":\s]+(\d+(?:\.\d+)?)', response_text, re.IGNORECASE)
        if total_match:
            scores['total_score'] = float(total_match.group(1))
        
        # Look for individual criterion scores
        criteria_patterns = [
            (r'clarity[^:]*:[^\d]*(\d+(?:\.\d+)?)', 'clarity_communication'),
            (r'structure[^:]*:[^\d]*(\d+(?:\.\d+)?)', 'structure_organization'),
            (r'delivery[^:]*:[^\d]*(\d+(?:\.\d+)?)', 'delivery_presentation'),
            (r'content[^:]*:[^\d]*(\d+(?:\.\d+)?)', 'content_substance'),
            (r'visual[^:]*:[^\d]*(\d+(?:\.\d+)?)', 'visual_production'),
        ]
        
        criteria_scores = {}
        for pattern, key in criteria_patterns:
            match = re.search(pattern, response_text, re.IGNORECASE)
            if match:
                criteria_scores[key] = {'score': float(match.group(1))}
        
        if criteria_scores:
            scores['criteria_scores'] = criteria_scores
        
        if scores:
            return scores
    except:
        pass
    
    return None


def display_score_meter(label, score, max_score=3):
    """
    Display a visual score meter using Streamlit progress bar.
    
    Args:
        label: The label for the criterion
        score: The score achieved
        max_score: Maximum possible score
    """
    percentage = (score / max_score) * 100
    
    # Color coding based on percentage
    if percentage >= 80:
        color = "🟢"  # Green
    elif percentage >= 60:
        color = "🟡"  # Yellow
    else:
        color = "🔴"  # Red
    
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.write(f"{color} **{label}**")
    with col2:
        st.progress(percentage / 100)
    with col3:
        st.write(f"**{score}/{max_score}**")


def display_evaluation_results(evaluation_data):
    """
    Display comprehensive evaluation results with visual meters.
    
    Args:
        evaluation_data: Dictionary containing evaluation scores and feedback
    """
    if not evaluation_data:
        return
    
    st.markdown("---")
    st.subheader("📊 Presentation Evaluation Results")
    
    # Display total score prominently
    total_score = evaluation_data.get('total_score', 0)
    st.markdown(f"### Overall Score: **{total_score}/15**")
    
    # Display overall progress
    overall_percentage = (total_score / 15) * 100
    st.progress(overall_percentage / 100)
    
    # Determine grade
    if overall_percentage >= 90:
        grade = "A+ (Excellent)"
        emoji = "🌟"
    elif overall_percentage >= 80:
        grade = "A (Very Good)"
        emoji = "⭐"
    elif overall_percentage >= 70:
        grade = "B (Good)"
        emoji = "👍"
    elif overall_percentage >= 60:
        grade = "C (Satisfactory)"
        emoji = "👌"
    else:
        grade = "Needs Improvement"
        emoji = "📈"
    
    st.markdown(f"### {emoji} Grade: **{grade}**")
    
    st.markdown("---")
    
    # Display individual criteria scores
    st.subheader("📋 Detailed Breakdown")
    
    criteria_scores = evaluation_data.get('criteria_scores', {})
    
    criteria_labels = {
        'clarity_communication': 'Clarity & Communication',
        'structure_organization': 'Structure & Organization',
        'delivery_presentation': 'Delivery & Presentation Skills',
        'content_substance': 'Content & Substance',
        'visual_production': 'Visual Aids & Production'
    }
    
    for key, label in criteria_labels.items():
        if key in criteria_scores:
            score_data = criteria_scores[key]
            score = score_data.get('score', 0)
            feedback = score_data.get('feedback', '')
            
            display_score_meter(label, score)
            if feedback:
                with st.expander(f"View feedback for {label}"):
                    st.write(feedback)
    
    # Display strengths and improvements
    col1, col2 = st.columns(2)
    
    with col1:
        strengths = evaluation_data.get('strengths', [])
        if strengths:
            st.markdown("### ✅ Strengths")
            for strength in strengths:
                st.markdown(f"- {strength}")
    
    with col2:
        improvements = evaluation_data.get('areas_for_improvement', [])
        if improvements:
            st.markdown("### 🎯 Areas for Improvement")
            for improvement in improvements:
                st.markdown(f"- {improvement}")
    
    # Display overall feedback
    overall_feedback = evaluation_data.get('overall_feedback', '')
    if overall_feedback:
        st.markdown("---")
        st.subheader("💬 Overall Feedback")
        st.write(overall_feedback)
    
    # Display recommendations
    recommendations = evaluation_data.get('recommendations', [])
    if recommendations:
        st.markdown("---")
        st.subheader("💡 Recommendations")
        for rec in recommendations:
            st.markdown(f"- {rec}")


def create_session():
    """
    Create a new session with the speaker agent.
    
    This function:
    1. Generates a unique session ID based on timestamp
    2. Sends a POST request to the ADK API to create a session
    3. Updates the session state variables if successful
    
    Returns:
        bool: True if session was created successfully, False otherwise
    
    API Endpoint:
        POST /apps/{app_name}/users/{user_id}/sessions/{session_id}
    """
    session_id = f"session-{int(time.time())}"
    response = requests.post(
        f"{API_BASE_URL}/apps/{APP_NAME}/users/{st.session_state.user_id}/sessions/{session_id}",
        headers={"Content-Type": "application/json"},
        data=json.dumps({})
    )
    
    if response.status_code == 200:
        st.session_state.session_id = session_id
        st.session_state.messages = []
        st.session_state.audio_files = []
        return True
    else:
        st.error(f"Failed to create session: {response.text}")
        return False

def send_message(message):
    """
    Send a message to the speaker agent and process the response.
    
    This function:
    1. Adds the user message to the chat history
    2. Sends the message to the ADK API
    3. Processes the response to extract text and audio information
    4. Updates the chat history with the assistant's response
    
    Args:
        message (str): The user's message to send to the agent
        
    Returns:
        bool: True if message was sent and processed successfully, False otherwise
    
    API Endpoint:
        POST /run
        
    Response Processing:
        - Parses the ADK event structure to extract text responses
        - Looks for text_to_speech function responses to find audio file paths
        - Adds both text and audio information to the chat history
    """
    if not st.session_state.session_id:
        st.error("No active session. Please create a session first.")
        return False
    
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": message})
    
    # Send message to API
    response = requests.post(
        f"{API_BASE_URL}/run",
        headers={"Content-Type": "application/json"},
        data=json.dumps({
            "app_name": APP_NAME,
            "user_id": st.session_state.user_id,
            "session_id": st.session_state.session_id,
            "new_message": {
                "role": "user",
                "parts": [{"text": message}]
            }
        })
    )
    
    if response.status_code != 200:
        st.error(f"Error: {response.text}")
        return False
    
    # Process the response
    events = response.json()
    
    # Extract assistant's text response
    assistant_message = None
    audio_file_path = None
    
    for event in events:
        # Look for the final text response from the model
        if event.get("content", {}).get("role") == "model" and "text" in event.get("content", {}).get("parts", [{}])[0]:
            assistant_message = event["content"]["parts"][0]["text"]
        
        # Look for text_to_speech function response to extract audio file path
        if "functionResponse" in event.get("content", {}).get("parts", [{}])[0]:
            func_response = event["content"]["parts"][0]["functionResponse"]
            if func_response.get("name") == "text_to_speech":
                response_text = func_response.get("response", {}).get("result", {}).get("content", [{}])[0].get("text", "")
                # Extract file path using simple string parsing
                if "File saved as:" in response_text:
                    parts = response_text.split("File saved as:")[1].strip().split()
                    if parts:
                        audio_file_path = parts[0].strip(".")
    
    # Add assistant response to chat
    if assistant_message:
        message_data = {
            "role": "assistant", 
            "content": assistant_message, 
            "audio_path": audio_file_path
        }
        
        # Extract evaluation scores if in presentation mode
        if st.session_state.mode == "presentation":
            evaluation_data = extract_evaluation_scores(assistant_message)
            if evaluation_data:
                message_data["evaluation"] = evaluation_data
                st.session_state.last_evaluation = evaluation_data
        
        st.session_state.messages.append(message_data)
    
    return True

# UI Components
st.title("🎯 PitchIQ")
st.caption("Intelligent Video Analysis & Presentation Evaluation Platform")

# Mode selector
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    if st.button("📹 Video Analysis", use_container_width=True, type="primary" if st.session_state.mode == "analysis" else "secondary"):
        st.session_state.mode = "analysis"
        st.rerun()
with col2:
    if st.button("🎤 Presentation Evaluation", use_container_width=True, type="primary" if st.session_state.mode == "presentation" else "secondary"):
        st.session_state.mode = "presentation"
        st.rerun()

# Display current mode
if st.session_state.mode == "analysis":
    st.info("📹 **Mode:** Video Analysis - Extract insights, transcripts, and visual content from videos")
else:
    st.info("🎤 **Mode:** Presentation Evaluation - Score presentations out of 15 with detailed feedback")

st.markdown("---")

# Sidebar for session management
with st.sidebar:
    st.header("Session Management")
    
    if st.session_state.session_id:
        st.success(f"Active session: {st.session_state.session_id}")
        if st.button("➕ New Session"):
            create_session()
    else:
        st.warning("No active session")
        if st.button("➕ Create Session"):
            create_session()
    
    st.divider()
    
    # Show latest evaluation summary if in presentation mode
    if st.session_state.mode == "presentation" and st.session_state.last_evaluation:
        st.header("📊 Latest Score")
        eval_data = st.session_state.last_evaluation
        total_score = eval_data.get('total_score', 0)
        
        # Display score with color
        percentage = (total_score / 15) * 100
        if percentage >= 80:
            color = "green"
        elif percentage >= 60:
            color = "orange"
        else:
            color = "red"
        
        st.markdown(f"### :{color}[{total_score}/15]")
        st.progress(percentage / 100)
        
        st.divider()
    
    st.caption("This app interacts with the PitchIQ Agent via the ADK API Server.")
    st.caption("Make sure the ADK API Server is running on port 8000.")

# Chat interface
if st.session_state.mode == "analysis":
    st.subheader("🎬 Begin by Uploading a YouTube Video Link for Analysis")
    st.caption("Ask questions about the video content, request transcripts, or analyze specific aspects.")
else:
    st.subheader("🎯 Begin by Uploading a YouTube Video Link for Presentation Evaluation")
    st.caption("Get comprehensive feedback and scores (out of 15) on presentation quality.")

# Display messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.write(msg["content"])
            
            # Handle audio if available
            if "audio_path" in msg and msg["audio_path"]:
                audio_path = msg["audio_path"]
                if os.path.exists(audio_path):
                    st.audio(audio_path)
                else:
                    st.warning(f"Audio file not accessible: {audio_path}")
            
            # Handle evaluation results if in presentation mode
            if st.session_state.mode == "presentation" and "evaluation" in msg:
                display_evaluation_results(msg["evaluation"])

# Input for new messages
if st.session_state.session_id:  # Only show input if session exists
    user_input = st.chat_input("Type your message...")
    if user_input:
        send_message(user_input)
        st.rerun()  # Rerun to update the UI with new messages
else:
    st.info("⬅️ Create a session to start chatting")