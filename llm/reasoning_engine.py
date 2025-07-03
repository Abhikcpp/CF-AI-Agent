from llm_connector import LLMConnector

class ReasoningEngine:
    """
    Coordinates reasoning tasks using the LLM.
    """

    def __init__(self, llm_connector):
        self.llm_connector = llm_connector

    def analyze_behavior(self, user_data):
        """
        Analyzes user behavior and provides insights.

        :param user_data: Dictionary containing user submission data.
        :return: Analysis insights from the LLM.
        """
        # Load the behavior analysis prompt
        with open("prompt_templates/analyze_behavior.txt", "r") as file:
            prompt_template = file.read()

        # Format the prompt with user data
        prompt = prompt_template.format(submissions=user_data)

        # Send request to LLM
        return self.llm_connector.send_request(prompt)

    def recommend_problems(self, weak_areas):
        """
        Recommends problems based on weak areas.

        :param weak_areas: List of weak tags and difficulty levels.
        :return: Problem recommendations from the LLM.
        """
        # Load the problem recommendation prompt
        with open("prompt_templates/recommend_problems.txt", "r") as file:
            prompt_template = file.read()

        # Format the prompt with weak areas
        prompt = prompt_template.format(weak_areas=weak_areas)

        # Send request to LLM
        return self.llm_connector.send_request(prompt)