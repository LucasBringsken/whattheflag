import typer

from whattheflag.core import translate_long_flag, translate_short_flag
from whattheflag.flags_db import FLAGS
from whattheflag.output import display_flag_info, display_no_cmd, display_unknown_tool

app = typer.Typer(
    help="Lightweight CLI tool for instantly explaining command-line flags without digging through man pages",
    add_completion=False,
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)


@app.command()
def explain(
    cmd: list[str] = typer.Argument(..., help="The command with flags to explain")
):
    if not cmd:
        display_no_cmd()
        raise typer.Exit()

    tool = cmd[0]
    args = cmd[1:]

    if tool not in FLAGS:
        display_unknown_tool()
        raise typer.Exit()

    flag_info = []
    for arg in args:

        if arg.startswith("--") and len(arg) > 2:
            flag, description = translate_long_flag(tool, arg[2:])
            flag_info.append((flag, None, description))

        elif arg.startswith("-") and len(arg) > 1:
            flag_info_list = translate_short_flag(tool, arg[1:])

            flag_info.extend(flag_info_list)

    display_flag_info(tool, flag_info)


if __name__ == "__main__":
    app()
