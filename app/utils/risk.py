def calculate_risk(issues):
    score = 0
    for issue in issues:
        if issue['severity'] == 'High':
            score += 3
        elif issue['severity'] == 'Medium':
            score += 2
        else:
            score += 1

    if score >= 6:
        return "High"
    elif score >= 3:
        return "Medium"
    else:
        return "Low"
