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
    short_index: dict[str, tuple[str, str]] = None,
) -> list[FlagInfo]:
    if short_index is None:
        short_index = build_short_index(flags)
    output = []
    for f in flag:
        long_flag, description = find_by_short(flags, f, short_index)
        if long_flag:
            output.append(("-" + f, "--" + long_flag, description))
        else:
            output.append(("-" + f, "", description))
    return output


def find_by_short(
    flags: dict[str, dict[str, str]],
    short_flag: str,
    short_index: dict[str, tuple[str, str]] = None,
) -> tuple[str, str]:
    if short_index and short_flag in short_index:
        return short_index[short_flag]
    for long_name, data in flags.items():
        if data["short"] == short_flag:
            return long_name, data["description"]
    return None, "[red]unknown flag[/red]"


def build_short_index(flags: dict[str, dict[str, str]]) -> dict[str, tuple[str, str]]:
    return {
        data["short"]: (long_name, data["description"])
        for long_name, data in flags.items()
        if "short" in data and data["short"]
    }


def get_all_flags_info(flags: dict[str, dict[str, str]]) -> list[FlagInfo]:
    output = []

    for long_flag, data in sorted(flags.items()):
        short = data.get("short")
        description = data.get("description", "")

        short_flag = f"-{short}" if short else ""
        long_flag = f"--{long_flag}"

        output.append((short_flag, long_flag, description))

    return output
