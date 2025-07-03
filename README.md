# CF-AI-Agent

A Codeforces AI Agent that analyzes user submissions and provides insights for competitive programming improvement.

## Features

- **User Submission Analysis**: Fetches and analyzes Codeforces submissions
- **AI-Powered Insights**: Uses LLM to provide behavior analysis and recommendations  
- **Contest Strategy**: Suggests strategies for upcoming contests
- **Problem Recommendations**: Recommends practice problems based on weak areas
- **Web Interface**: Simple HTML frontend for easy interaction

## Project Structure

```
CF-AI-Agent/
├── backend/           # Flask backend application
│   ├── app.py        # Main Flask application
│   ├── llm/          # LLM integration and prompt templates
│   └── tools/        # Data fetching and analysis tools
├── frontend/         # HTML frontend interface
├── environment/      # Requirements and dependencies
├── docs/            # Documentation
└── runtime/         # Testing and runtime scripts
```

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r environment/requirements.txt
   ```

2. **Set Environment Variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Run the Application**
   ```bash
   cd backend
   python app.py
   ```

4. **Access the Frontend**
   - Open `frontend/index.html` in your browser
   - Or serve it with a local web server

## Repository Visibility

This repository can be public or private depending on your needs. If you need to change the repository visibility:

📖 **See the detailed guide**: [docs/REPOSITORY_VISIBILITY_GUIDE.md](docs/REPOSITORY_VISIBILITY_GUIDE.md)

## API Endpoints

- `GET /submissions/<handle>` - Fetch user submissions
- `GET /analyze/<handle>` - Analyze user behavior and get insights

## Configuration

Set the following environment variables in your `.env` file:
- `LLM_API_KEY` - Your LLM API key
- `LLM_BASE_URL` - LLM service base URL

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

[Add your license information here]

## Support

For repository visibility changes or other GitHub-related questions, see the [Repository Visibility Guide](docs/REPOSITORY_VISIBILITY_GUIDE.md).