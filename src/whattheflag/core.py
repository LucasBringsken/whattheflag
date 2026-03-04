FlagInfo = tuple[str, str, str]


def translate_long_flag(flags: dict[str, dict[str, str]], flag: str) -> FlagInfo:
    flag = flag.split("=")[0]

    if flags and flag in flags:
        description = flags[flag]["description"]
        short = flags[flag].get("short")
        return (f"-{short}" if short else "", "--" + flag, description)
    else:
        return ("", "--" + flag, "[red]unknown flag[/red]")


def translate_short_flag(
    flags: dict[str, dict[str, str]],
    flag: str,
) -> list[FlagInfo]:
    output = []
    for f in flag:
        long_flag, description = find_by_short(flags, f)
        if long_flag:
            output.append(("-" + f, "--" + long_flag, description))
        else:
            output.append(("-" + f, "", description))

    return output


def find_by_short(flags: dict[str, dict[str, str]], short_flag: str) -> tuple[str, str]:
    for long_name, data in flags.items():
        if data["short"] == short_flag:
            return long_name, data["description"]
    return None, "[red]unknown flag[/red]"


def get_all_flags_info(flags: dict[str, dict[str, str]]) -> list[FlagInfo]:
    output = []

    for long_flag, data in sorted(flags.items()):
        short = data.get("short")
        description = data.get("description", "")

        short_flag = f"-{short}" if short else ""
        long_flag = f"--{long_flag}"

        output.append((short_flag, long_flag, description))

    return output
