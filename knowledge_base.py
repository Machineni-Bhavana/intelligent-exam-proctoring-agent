RULES = {
    "tab_switches": {
        "threshold": 2,
        "weight": 0.30,
        "description": "Frequent tab switching detected"
    },
    "head_turns": {
        "threshold": 5,
        "weight": 0.25,
        "description": "Excessive head movement detected"
    },
    "inactive_time": {
        "threshold": 90,
        "weight": 0.15,
        "description": "Long period of inactivity detected"
    },
    "multiple_faces": {
        "threshold": True,
        "weight": 0.40,
        "description": "Multiple faces detected"
    }
}
