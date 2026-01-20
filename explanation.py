def generate_action(risk_score, reasons):
    if risk_score < 0.4:
        risk_level = "Low Risk"
        action = "No action required"
    elif risk_score < 0.7:
        risk_level = "Medium Risk"
        action = "Flag for review"
    else:
        risk_level = "High Risk"
        action = "Alert invigilator"

    return {
        "risk_level": risk_level,
        "confidence": round(risk_score * 100, 2),
        "action": action,
        "reasons": reasons
    }
