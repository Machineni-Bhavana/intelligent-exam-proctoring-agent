Intelligent Exam Proctoring Agent Using Logical Reasoning
Overview

This project implements a utility-based intelligent agent for online exam monitoring in a simulated environment.
The agent observes exam-related behaviours, reasons using logical rules and utility values, and produces explainable risk assessments to assist human invigilators.

The system focuses on decision making under uncertainty rather than automatic punishment or real-time surveillance.

Key Features

Utility-based intelligent agent design

Rule-based logical reasoning

Handling of uncertain and partial observations

Explainable decision output (risk level + reasons)

Streamlit-based interactive interface for demonstration

Agent Architecture (PEAS)

Environment: Simulated online examination setting

Percepts: Tab switches, head movement, inactivity time, multiple face detection

Reasoning: Rule-based logic with utility weighting

Actions: Ignore, Flag for review, Alert invigilator with explanation

Technologies Used

Python

Streamlit

Git & GitHub

How It Works

The agent perceives simulated exam behaviour as input

Logical rules evaluate individual behaviours

Utility values are assigned to each behaviour

A risk score is computed by combining utilities

The agent selects an appropriate action

The decision is explained in human-readable form

Project Status

Core intelligent agent logic implemented

Utility-based reasoning engine completed

Explanation module implemented

Streamlit interface added for demonstration

Note

This project is simulation-based and developed for academic learning purposes to demonstrate Artificial Intelligence concepts such as intelligent agents, logical reasoning, uncertainty handling, and explainable AI.

Author

Machineni Bhavana
