from dotenv import load_dotenv
load_dotenv()  # load variables from .env

import os
from flask import Flask, jsonify, Response
from tools.data_fetcher import fetch_user_submissions
from llm.llm_connector import LLMConnector
from llm.reasoning_engine import ReasoningEngine
import logging

# Read the API key from environment variables.
API_KEY = os.environ.get("LLM_API_KEY")
if not API_KEY:
    raise Exception("Please set the LLM_API_KEY environment variable.")

# Correct Base URL (remove the model-specific part here)
BASE_URL = os.environ.get("LLM_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/")

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

# Initialize LLM Connector and Reasoning Engine
llm_connector = LLMConnector(API_KEY, BASE_URL)
reasoning_engine = ReasoningEngine(llm_connector)

# Initialize Flask app
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route("/submissions/<handle>", methods=["GET"])
def get_submissions(handle):
    try:
        logging.debug(f"Fetching submissions for handle: {handle}")
        submissions = fetch_user_submissions(handle)
        logging.debug(f"Submissions fetched: {submissions[:5]}")
        return jsonify({"status": "success", "submissions": submissions})
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/analyze/<handle>", methods=["GET"])
def analyze_user(handle):
    """
    Analyze user behavior and provide insights using the LLM.
    """
    try:
        logging.debug(f"Analyzing behavior for handle: {handle}")
        submissions = fetch_user_submissions(handle)

        if not submissions:
            raise Exception(f"No submissions found for handle: {handle}")

        logging.debug(f"Fetched submissions for analysis: {submissions[:2]}")

        with open("llm/prompt_templates/analyze_behavior.txt", "r") as file:
            prompt_template = file.read()

        prompt = prompt_template.format(submissions=submissions[:5])
        logging.debug(f"Constructed prompt: {prompt}")

        analysis = llm_connector.call_llm(prompt)
        logging.debug(f"Analysis result: {analysis}")

        return Response(analysis, mimetype="text/plain"), 200
    except Exception as e:
        logging.error(f"Error analyzing behavior for handle {handle}: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)