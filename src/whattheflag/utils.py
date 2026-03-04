import os
import json

TOOLS_DIR = os.path.join(os.path.dirname(__file__), "tools")


def get_flags_for_tool(tool: str) -> dict[str, dict[str, str]]:
    tool_file = os.path.join(TOOLS_DIR, f"{tool}.json")

    if not os.path.isfile(tool_file):
        return {}

    with open(tool_file, "r", encoding="utf-8") as f:
        return json.load(f)


def get_supported_tools() -> list[tuple[str, int]]:
    tools = []

    for file in os.listdir(TOOLS_DIR):
        if file.endswith(".json"):
            tool = file.removesuffix(".json")

            flags = get_flags_for_tool(tool)

            tools.append((tool, len(flags)))

    return sorted(tools)
