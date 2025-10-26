# 🎯 PitchIQ

## Intelligent Video Analysis & Presentation Evaluation Platform

> **Powered by Google Gemini AI** - Analyze videos, evaluate presentations, and get actionable feedback with AI-driven insights.

### 🏆 Hackathon Achievement

This project was developed for the **Google Cloud x AI Tinkerers Toronto Hackathon - September 2025**

- 🥈 **Runner Up**
- 🎉 **Crowd Favorite**

### About the Project

PitchIQ is a next-generation intelligent video analysis and presentation evaluation platform that leverages Google Gemini AI to provide comprehensive insights from YouTube videos. Whether you're analyzing content, evaluating presentations, or scoring pitches, PitchIQ delivers actionable feedback powered by advanced multimodal AI. The system provides:

- **Video Content Analysis**: Deep understanding of both visual and audio content
- **AI-Powered Insights**: Extracts meaningful information from videos using advanced AI models
- **Custom Prompts**: Allows users to specify what they want to analyze in videos
- **File Management**: Automatically organizes project outputs in structured folders
- **Interactive Interface**: User-friendly Streamlit web application

### Features

- 📹 YouTube video analysis with custom prompts
- 🎤 **NEW: Presentation evaluation with scoring out of 15 points**
- 📊 **Visual score meters and detailed feedback**
- 🔍 Visual and audio content extraction
- 📝 Automated transcript generation
- 🗂️ Intelligent file organization
- 🤖 Powered by Google Cloud AI Platform and Gemini models

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

## New Feature: Presentation Evaluation 🎤

PitchIQ now includes an advanced **Presentation Evaluator** that:
- Scores presentations out of **15 points** across 5 criteria
- Provides detailed feedback on clarity, structure, delivery, content, and visuals
- Displays results with intuitive **visual score meters**
- Perfect for hackathon submissions, pitches, and educational content

[📖 Read Full Documentation](PRESENTATION_EVALUATION.md)

---

