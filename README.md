# 🎯 PitchIQ

## Intelligent Video Analysis & Presentation Evaluation Platform

> **Powered by Google Gemini AI** - Analyze videos, evaluate presentations, and get actionable feedback with AI-driven insights.

### About PitchIQ

PitchIQ is a next-generation intelligent video analysis and presentation evaluation platform that leverages Google Gemini AI to provide comprehensive insights from YouTube videos. Whether you're analyzing content, evaluating presentations, or scoring pitches, PitchIQ delivers actionable feedback powered by advanced multimodal AI. The system provides:

- **Video Content Analysis**: Deep understanding of both visual and audio content
- **AI-Powered Insights**: Extracts meaningful information from videos using advanced AI models
- **Custom Prompts**: Allows users to specify what they want to analyze in videos
- **File Management**: Automatically organizes project outputs in structured folders
- **Interactive Interface**: User-friendly Streamlit web application

### Features

- 🎤 **AI-Powered Presentation Evaluation** - Score presentations out of 15 points with detailed feedback
- 📊 **Visual Score Meters** - Intuitive progress bars and color-coded performance indicators
- 📹 **YouTube Video Analysis** - Analyze any YouTube video with custom prompts
- 🔍 **Multimodal Content Extraction** - Visual and audio content understanding
- 📝 **Automated Transcript Generation** - Extract complete transcripts from videos
- 📄 **Detailed Feedback Reports** - Strengths, improvements, and actionable recommendations
- 🎯 **5-Criteria Scoring System** - Clarity, Structure, Delivery, Content, and Visuals
- 🗂️ **Smart File Organization** - Automatically organized project outputs
- 🤖 **Powered by Google Gemini 2.0** - Advanced multimodal AI capabilities

---

## Setup Instructions

### Installation Steps

1. **Create Environment**
2. **Enter Environment**
3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install FFmpeg**

   ```bash
   choco install ffmpeg
   ```

---

## Usage

### Running the Application

```bash
# Web Interface
streamlit run .\PitchIQ\app.py

# ADK Web Interface
adk web
```

### Using PitchIQ

1. Start the application using one of the commands above
2. Create a new session in the web interface
3. Paste your YouTube video link here
4. Describe what you want to analyze from the video
5. Let PitchIQ process and provide insights

---

## Project Structure

```text
PitchIQ/
├── agent.py              # Main AI agent configuration
├── app.py                # Streamlit web application
├── tools/                # Analysis tools
│   ├── fileEditor.py     # File management utilities
│   └── videoAnalyzer.py  # Video processing and analysis
└── custom_utils/         # Utility functions
    └── prompts/          # AI prompt templates
```

## Presentation Evaluation 🎤

PitchIQ's advanced **AI-Powered Presentation Evaluator** provides:
- **15-Point Scoring System** across 5 comprehensive criteria
- **Detailed Feedback** on clarity, structure, delivery, content, and visuals
- **Visual Score Meters** with color-coded performance indicators
- **Actionable Recommendations** for improvement
- Perfect for **hackathon pitches**, **sales presentations**, **conference talks**, and **educational content**

[📖 Read Full Documentation](PRESENTATION_EVALUATION.md)

---

