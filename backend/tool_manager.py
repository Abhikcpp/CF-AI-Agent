from typing import Any, Callable
from tools.data_fetcher import fetch_user_submissions
from tools.behavior_analyzer import analyze_behavior
from backend.tools.problem_recommender import recommend_problems

class ToolNotFoundError(Exception):
    """Custom exception for tool not found errors."""
    pass

TOOLS: dict[str, Callable] = {
    "fetch_user_data": fetch_user_submissions,
    "analyze_behavior": analyze_behavior,
    "recommend_problems": recommend_problems
}

def execute_tool(tool_name: str, *args: Any, **kwargs: Any) -> Any:
    """
    Execute a tool by name.
    
    Args:
        tool_name: Name of the tool.
        *args: Arguments for the tool.
        **kwargs: Keyword arguments for the tool.
    
    Returns:
        The result of the tool execution.
        
    Raises:
        ToolNotFoundError: If the specified tool doesn't exist.
    """
    if tool_name in TOOLS:
        return TOOLS[tool_name](*args, **kwargs)
    raise ToolNotFoundError(f"Tool '{tool_name}' not found.")