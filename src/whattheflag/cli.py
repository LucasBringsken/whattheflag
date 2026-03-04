import typer

from whattheflag.core import (
    translate_long_flag,
    translate_short_flag,
    get_all_flags_info,
)
from whattheflag.output import (
    display_flag_info,
    display_supported_tools,
    display_unknown_tool,
)
from whattheflag.utils import get_flags_for_tool, get_supported_tools

app = typer.Typer(
    help="""
Lightweight CLI tool for instantly explaining command-line flags.

Usage:

  whattheflag <tool>
      Show all flags for a tool

  whattheflag <tool> <flags>
      Explain specific flags

Examples:

  whattheflag curl
  whattheflag curl -fsSL
  whattheflag curl -v -I --silent
  whattheflag tools
""",
    add_completion=False,
    no_args_is_help=True,
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)


@app.callback(invoke_without_command=True)
def explain(
    ctx: typer.Context,
    cmd: list[str] = typer.Argument(None, help="The command with flags to explain"),
):

    if ctx.invoked_subcommand is not None:
        return

    if cmd[0] == "tools":
        ctx.invoke(tools)
        raise typer.Exit()

    tool = cmd[0]
    args = cmd[1:]

    flags = get_flags_for_tool(tool)

    if flags is None:
        display_unknown_tool()
        raise typer.Exit()

    if not args:
        all_flags_info = get_all_flags_info(flags)
        if not all_flags_info:
            display_unknown_tool()
            raise typer.Exit()
        display_flag_info(tool, all_flags_info)
        raise typer.Exit()

    flag_info = []
    for arg in args:

        if arg.startswith("--") and len(arg) > 2:
            flag_info_long = translate_long_flag(flags, arg[2:])
            flag_info.append(flag_info_long)

        elif arg.startswith("-") and len(arg) > 1:
            flag_info_list = translate_short_flag(flags, arg[1:])
            flag_info.extend(flag_info_list)

    display_flag_info(tool, flag_info)


@app.command()
def tools():
    """List all supported tools and the number of flags available for each."""
    tool_list = get_supported_tools()

    display_supported_tools(tool_list)


if __name__ == "__main__":
    app()
