# Meeting-to-Accountability System

## Introduction

Meetings are where teams discuss ideas, assign tasks, set deadlines, and make commitments. However, after a meeting, it can be difficult to remember what was promised, who was responsible, and whether the commitment changed later.

The Meeting-to-Accountability System addresses this problem by using Artificial Intelligence and Natural Language Processing to convert meeting conversations into structured and trackable commitments.

## Project Files

[View Google Drive Files](https://drive.google.com/drive/folders/XXXXXXXX)

## Project Motivation

Traditional meeting tools mainly focus on summarizing what was discussed. Our system focuses on what was actually committed and how that commitment changes over time.

For example, a team member may say:

> "I will complete the homepage by Thursday."

In a later meeting:

> "I'll try to finish the homepage by Friday."

The system identifies that both statements refer to the same task and detects the change in deadline and commitment strength.

## What the Project Does

The system extracts the task, responsible person, deadline, commitment strength, and status from meeting conversations. It stores the original information as Commitment DNA and compares it with future meeting statements to track changes and maintain accountability.

### Workflow

```text
Meeting
   ↓
Speech-to-Text
   ↓
NLP Processing
   ↓
Commitment Extraction
   ↓
Commitment DNA
   ↓
Historical Comparison
   ↓
Accountability Tracking
```

## AI Techniques

The system uses Natural Language Processing, Named Entity Recognition, temporal information extraction, semantic similarity, commitment classification, and commitment drift detection to understand and compare meeting commitments.

## Challenges

The main challenges include understanding different ways people express commitments, identifying the same task when different words are used, and interpreting relative deadlines such as "tomorrow" or "next week".

## What We Learned

This project helped us understand how AI and NLP can be applied to real-world conversations. We learned how unstructured meeting discussions can be converted into structured information and how maintaining historical data can improve accountability.

## Technology Stack

The project uses Python, Natural Language Processing, AI models, SQLite, speech-to-text technology, FFmpeg, Git, and GitHub.

## Future Scope

The system can be extended with real-time transcription, automatic reminders, calendar integration, collaboration platform integration, multilingual support, and an interactive accountability dashboard.

## Conclusion

The Meeting-to-Accountability System goes beyond meeting summarization by tracking what was promised, who was responsible, when it was due, and how the commitment changed over time. It aims to connect meeting discussions with measurable actions and continuous accountability.
