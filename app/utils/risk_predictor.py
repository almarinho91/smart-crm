def predict_risk(profile):
    # Dummy rule-based logic for demonstration
    if profile.age > 60 or profile.income < 30000 or profile.has_previous_claims:
        return "high"
    elif 40 <= profile.age <= 60 or 30000 <= profile.income < 70000:
        return "medium"
    else:
        return "low"
