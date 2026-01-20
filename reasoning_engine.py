#rules + utility values
#what the agent knows rules

# What the reasoning engine must do (in plain terms)
# Take exam percepts (inputs)
# Check each rule
# If a rule is satisfied:
# add its utility (weight)
# store the reason
# Return:
# total risk score
# list of reasons
# That’s it. No ML. No complexity.

def evaluate_risk(percepts, rules):
    risk_score = 0.0
    reasons = []

    # Rule 1: Tab switching
    if percepts["tab_switches"] > rules["tab_switches"]["threshold"]:
        risk_score += rules["tab_switches"]["weight"]
        reasons.append(rules["tab_switches"]["description"])

    # Rule 2: Head movement
    if percepts["head_turns"] > rules["head_turns"]["threshold"]:
        risk_score += rules["head_turns"]["weight"]
        reasons.append(rules["head_turns"]["description"])

    # Rule 3: Inactivity
    if percepts["inactive_time"] > rules["inactive_time"]["threshold"]:
        risk_score += rules["inactive_time"]["weight"]
        reasons.append(rules["inactive_time"]["description"])

    # Rule 4: Multiple faces
    if percepts["multiple_faces"] == rules["multiple_faces"]["threshold"]:
        risk_score += rules["multiple_faces"]["weight"]
        reasons.append(rules["multiple_faces"]["description"])

    return risk_score, reasons


