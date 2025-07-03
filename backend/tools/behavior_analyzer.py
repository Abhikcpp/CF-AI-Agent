def analyze_behavior(submissions):
    """
    Analyze a user's Codeforces submissions and return insights.
    
    :param submissions: List of submission data from Codeforces API.
    :return: Dictionary with analysis and recommendations.
    """
    analysis = {
        "total_submissions": len(submissions),
        "verdicts": {},
        "weak_tags": {},
        "recommendations": []
    }
    
    # Analyze verdicts
    for submission in submissions:
        verdict = submission.get("verdict", "UNKNOWN")
        analysis["verdicts"][verdict] = analysis["verdicts"].get(verdict, 0) + 1
        
        # Analyze problem tags for weak areas
        if verdict != "OK":  # Count failed attempts
            tags = submission.get("problem", {}).get("tags", [])
            for tag in tags:
                analysis["weak_tags"][tag] = analysis["weak_tags"].get(tag, 0) + 1
    
    # Provide recommendations based on weak tags
    sorted_tags = sorted(analysis["weak_tags"].items(), key=lambda x: x[1], reverse=True)
    for tag, count in sorted_tags[:3]:  # Top 3 weak tags
        analysis["recommendations"].append(f"Practice problems on '{tag}' (failed {count} times).")
    
    return analysis