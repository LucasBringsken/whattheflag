from .utils import get_flags_for_tool


def translate_long_flag(tool: str, flag: str) -> tuple[str, str]:
    flag = flag.split("=")[0]  # Remove any value assignments

    FLAGS = get_flags_for_tool(tool)

    if FLAGS and flag in FLAGS:
        description = FLAGS[flag]["description"]
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
    FLAGS = get_flags_for_tool(tool)

    for long_name, data in FLAGS.items():
        if data["short"] == short_flag:
            return long_name, data["description"]
    return None, "[red]unknown flag[/red]"
