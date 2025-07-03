def recommend_problems(tags):
    """
    Recommend practice problems based on weak tags.
    :param tags: Dictionary of tags and their frequency.
    """
    weak_tags = [tag for tag, count in tags.items() if count < 3]  # Example threshold
    recommendations = []
    for tag in weak_tags:
        # Fetch problems for the weak tag (this would call a Codeforces API endpoint)
        recommendations.append(f"Practice problems for tag: {tag}")
    return recommendations