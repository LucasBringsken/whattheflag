from rich.table import Table
from rich.console import Console

console = Console()


def display_flag_info(tool, flag_info: list[tuple[str, str, str]]):
    table = Table(title=f"{tool} flags")
    table.add_column("Flag", style="cyan", no_wrap=True)
    table.add_column("Long", style="green")
    table.add_column("Description", style="magenta")

    for (
        flag,
        long,
        description,
    ) in flag_info:
        table.add_row(flag, long, description)

    console.print(table)


def display_unknown_tool():
    console.print(
        "[red][bold]Error:[/bold][/red] The specified tool is unknown or not supported."
    )


def display_no_cmd():
    console.print(
        "[red][bold]Error:[/bold][/red] No command provided. Please specify a command to explain."
    )
