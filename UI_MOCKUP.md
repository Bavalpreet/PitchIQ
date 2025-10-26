# PitchIQ UI Mockup - Presentation Evaluation Mode

## Main Interface Layout

```
┌────────────────────────────────────────────────────────────────────┐
│                       🎯 PitchIQ                               │
│       Intelligent Video Analysis & Presentation Evaluation        │
│                         Platform                                  │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  ┌──────────────────────┐  ┌──────────────────────┐             │
│  │  📹 Video Analysis   │  │ 🎤 Presentation      │  [SELECTED] │
│  │                      │  │    Evaluation        │             │
│  └──────────────────────┘  └──────────────────────┘             │
│                                                                    │
│  ℹ️ Mode: Presentation Evaluation - Score presentations out of   │
│     15 with detailed feedback                                     │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│  🎯 Begin by Uploading a YouTube Video Link for                  │
│     Presentation Evaluation                                       │
│  Get comprehensive feedback and scores (out of 15) on            │
│  presentation quality.                                            │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  👤 User:                                                         │
│  https://youtube.com/watch?v=example123                          │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  🤖 Assistant:                                                    │
│  I'll evaluate this presentation video for you...                │
│                                                                    │
│  ───────────────────────────────────────────────────────         │
│  📊 Presentation Evaluation Results                               │
│  ───────────────────────────────────────────────────────         │
│                                                                    │
│  Overall Score: **12.5/15**                                       │
│  ████████████████░░░░ 83%                                        │
│                                                                    │
│  ⭐ Grade: **A (Very Good)**                                      │
│                                                                    │
│  ───────────────────────────────────────────────────────         │
│  📋 Detailed Breakdown                                            │
│  ───────────────────────────────────────────────────────         │
│                                                                    │
│  🟢 Clarity & Communication        ████████████░ 2.5/3          │
│  🟢 Structure & Organization       ████████████░ 2.5/3          │
│  🟡 Delivery & Presentation        ████████░░░░░ 2.0/3          │
│  🟢 Content & Substance            ████████████████ 3.0/3        │
│  🟡 Visual Aids & Production       ████████░░░░░ 2.5/3          │
│                                                                    │
│  ───────────────────────────────────────────────────────         │
│                                                                    │
│  ✅ Strengths                    🎯 Areas for Improvement        │
│  ─────────────                   ─────────────────────           │
│  • Excellent content depth       • Improve eye contact           │
│  • Clear articulation            • Add more visual aids          │
│  • Well-structured flow          • Work on body language         │
│  • Innovative approach                                           │
│                                                                    │
│  ───────────────────────────────────────────────────────         │
│  💬 Overall Feedback                                              │
│  ───────────────────────────────────────────────────────         │
│                                                                    │
│  Strong presentation overall with excellent content and          │
│  clarity. The structure was logical and easy to follow.          │
│  To reach the next level, focus on delivery confidence           │
│  and enhancing visual elements.                                  │
│                                                                    │
│  ───────────────────────────────────────────────────────         │
│  💡 Recommendations                                               │
│  ───────────────────────────────────────────────────────         │
│                                                                    │
│  • Practice maintaining eye contact with the camera              │
│  • Consider adding more slides or visual demonstrations          │
│  • Work on gestures and body language for emphasis               │
│  • Keep up the excellent content quality!                        │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
│                                                                    │
│  💬 Type your message...                                          │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

## Sidebar Layout

```
┌──────────────────────┐
│  Session Management  │
├──────────────────────┤
│                      │
│  ✓ Active session:   │
│    session-12345     │
│                      │
│  ┌──────────────────┐│
│  │  ➕ New Session  ││
│  └──────────────────┘│
│                      │
├──────────────────────┤
│                      │
│  📊 Latest Score     │
│                      │
│      12.5/15         │
│  ████████████░░░     │
│                      │
├──────────────────────┤
│                      │
│  This app interacts  │
│  with the PitchIQ    │
│  Agent via the ADK   │
│  API Server.         │
│                      │
│  Make sure the ADK   │
│  API Server is       │
│  running on port     │
│  8000.               │
│                      │
└──────────────────────┘
```

## Color Coding System

### Score Meters
- 🟢 **Green** (80-100%): Excellent performance
- 🟡 **Yellow** (60-79%): Good, room for improvement  
- 🔴 **Red** (0-59%): Needs significant work

### Grade Scale
- 🌟 **A+ (90-100%)**: Excellent
- ⭐ **A (80-89%)**: Very Good
- 👍 **B (70-79%)**: Good
- 👌 **C (60-69%)**: Satisfactory
- 📈 **<60%**: Needs Improvement

## Interactive Elements

### Expandable Sections
Each criterion has an expandable section for detailed feedback:

```
🟢 Clarity & Communication        ████████████░ 2.5/3
   ▼ View feedback for Clarity & Communication
   ─────────────────────────────────────────────
   The speaker demonstrated excellent clarity with
   well-articulated words and a steady pace...
   [Full detailed feedback shown here]
```

### Progress Bars
All scores are visualized with progress bars:
```
12.5/15  →  ████████████████░░░░ (83%)
2.5/3    →  ████████████░░░░ (83%)
```

## Mode Switching

Users can easily switch between modes:

```
┌──────────────────────┐  ┌──────────────────────┐
│ 📹 Video Analysis    │  │ 🎤 Presentation      │
│                      │  │    Evaluation        │
│ [Standard Mode]      │  │ [Active Mode]        │
└──────────────────────┘  └──────────────────────┘
```

Click to toggle between:
- **Video Analysis**: Original content analysis features
- **Presentation Evaluation**: New scoring system

## Evaluation Results Display Flow

```
1. User submits video URL
        ↓
2. Processing indicator appears
   "Evaluating presentation..."
        ↓
3. Results appear with animation:
   - Total score badge (large)
   - Grade indicator
   - Overall progress bar
        ↓
4. Detailed breakdown appears:
   - 5 criterion meters
   - Individual scores
   - Feedback sections
        ↓
5. Additional insights:
   - Strengths (left column)
   - Improvements (right column)
   - Overall feedback
   - Recommendations
        ↓
6. Sidebar updates:
   - Latest score displayed
   - Color-coded indicator
```

## Mobile/Responsive View

The UI adapts for smaller screens:
- Mode buttons stack vertically
- Criterion meters use full width
- Strengths/improvements shown sequentially
- Collapsible sections for long content

## Accessibility Features

- 🎨 High contrast colors (green, yellow, red)
- 📏 Clear visual hierarchy
- 📝 Descriptive labels and headers
- ⌨️ Keyboard navigation support
- 🔊 Screen reader friendly structure

## Example User Flow

1. **Launch App** → See PitchIQ homepage
2. **Select Mode** → Click "🎤 Presentation Evaluation"
3. **Create Session** → Click "➕ Create Session" in sidebar
4. **Submit Video** → Paste YouTube URL
5. **Wait for Processing** → See progress indicators
6. **Review Results** → Explore scores, feedback, recommendations
7. **Ask Follow-up** → Request specific improvements
8. **Get More Details** → Expand feedback sections

## Key UI/UX Principles

✅ **Visual Hierarchy**: Most important info (total score) is largest  
✅ **Progressive Disclosure**: Detailed feedback hidden in expandables  
✅ **Color Psychology**: Green (good), Yellow (okay), Red (needs work)  
✅ **Immediate Feedback**: Sidebar shows latest score at a glance  
✅ **Actionable Insights**: Specific recommendations provided  
✅ **Context Switching**: Easy mode toggle preserves session  

## Summary

The presentation evaluation UI provides:
- 🎯 Clear scoring visualization
- 📊 Detailed breakdown by criteria  
- ✅ Actionable feedback and recommendations
- 🎨 Intuitive color-coded meters
- 🔄 Seamless mode switching
- 📱 Responsive design
