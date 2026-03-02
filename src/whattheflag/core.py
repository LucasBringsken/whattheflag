from .flags_db import FLAGS


def translate_long_flag(tool: str, flag: str) -> tuple[str, str]:
    flag = flag.split("=")[0]  # Remove any value assignments

    if tool in FLAGS and flag in FLAGS[tool]:
        description = FLAGS[tool][flag]["description"]
        return ("--" + flag, description)
    else:
        return ("--" + flag, "[red]unknown flag[/red]")


def translate_short_flag(tool: str, flag: str) -> list[tuple[str, str, str]]:
    output = []
    for f in flag:
        long, description = find_by_short(tool, f)

        if long:
            output.append(("-" + f, "--" + long, description))
        else:
            output.append(("-" + f, "", description))

    return output


def find_by_short(tool: str, short_flag: str):
    for long_name, data in FLAGS[tool].items():
        if data["short"] == short_flag:
            return long_name, data["description"]
    return None, "[red]unknown flag[/red]"
