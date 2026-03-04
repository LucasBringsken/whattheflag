from rich.table import Table
from rich.console import Console
from rich.panel import Panel

console = Console()


def display_flag_info(tool, flag_info: list[tuple[str, str, str]]) -> None:
    table = Table(title=f"{tool} flags")
    table.add_column("Flag", style="cyan", no_wrap=True)
    table.add_column("Long", style="green")
    table.add_column("Description", style="magenta")

    seen = set()

    for flag, long_flag, description in flag_info:
        if flag not in seen:
            table.add_row(flag, long_flag, description)
            seen.add(flag)

    console.print(table)


def display_supported_tools(tool_list: list[str]) -> None:
    cols = 4
    grid = Table.grid(expand=True)

    for _ in range(cols):
        grid.add_column()

    rows = []

    for tool, count in tool_list:
        rows.append(
            f"[green]{tool}[/green] [dim]({count} flag{'s' if count != 1 else ''})[/dim]"
        )

    for i in range(0, len(rows), cols):
        grid.add_row(*rows[i : i + cols])

    panel = Panel(
        grid,
        title=f"[bold cyan]Supported Tools ({len(tool_list)})[/bold cyan]",
        border_style="cyan",
    )

    console.print(panel)


def display_unknown_tool() -> None:
    console.print(
        "[red][bold]Error:[/bold][/red] The specified tool is unknown or not supported."
    )
