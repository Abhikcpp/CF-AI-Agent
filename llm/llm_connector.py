import os
import requests

class LLMConnector:
    """
    Handles interaction with the LLM API.
    """

    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def send_request(self, prompt, max_tokens=1000, temperature=0.7):
        """
        Sends a request to the LLM API.

        :param prompt: The text prompt to send to the LLM.
        :param max_tokens: Maximum number of tokens to generate.
        :param temperature: Sampling temperature for creativity.
        :return: Response from the LLM API.
        """
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }

        response = requests.post(self.base_url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"LLM API call failed: {response.status_code}, {response.text}")