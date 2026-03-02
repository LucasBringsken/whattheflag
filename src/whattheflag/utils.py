import os
import json


def get_flags_for_tool(tool: str) -> dict[str, dict[str, str]]:
    tools_dir = os.path.join(os.path.dirname(__file__), "tools")
    tool_file = os.path.join(tools_dir, f"{tool}.json")

    if not os.path.isfile(tool_file):
        return {}

    with open(tool_file, "r", encoding="utf-8") as f:
        return json.load(f)
