<p align="center">
  <a href="https://github.com/LucasBringsken/whattheflag">
    <img src="https://raw.githubusercontent.com/LucasBringsken/whattheflag/main/docs/banner.png" alt="whattheflag banner"/>
  </a>
</p>

[![PyPI](https://img.shields.io/pypi/v/whattheflag)](https://pypi.org/project/whattheflag/)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
![License](https://img.shields.io/github/license/LucasBringsken/whattheflag)
[![Build](https://github.com/LucasBringsken/whattheflag/actions/workflows/release.yml/badge.svg)](https://github.com/LucasBringsken/whattheflag/actions/workflows/release.yml)

**Lightweight CLI tool for instantly explaining command-line flags without digging through man pages**

`whattheflag` helps you understand command-line flags and options for many popular CLI tools directly in your terminal.

Simply prepend `whattheflag` to a command to see what its flags mean.

---

## Features

- Explain command-line flags for many popular CLI tools
- Understand copied shell commands by translating their flags
- Expand combined short flags (e.g. `-fsSL`)
- Show both short and long flag versions when available
- Display explanations in a clean table format
- Show all known flags for a specific tool

---

## Installation

```bash
pip install whattheflag
```

---

## Usage

All functionality is available through the command line interface.

You can:

- Search for a specific tool (`whattheflag df`)
- Search for a specific flag or option (`whattheflag curl -fsSL --help`)
- Display an overview of all available options (`whattheflag tools`)

### Example Commands

#### Overview for a Tool

Shows all available flags and options for a tool.

```bash
whattheflag df
```

| Flag | Long             | Description                          |
| ---- | ---------------- | ------------------------------------ |
| -a   | --all            | Include dummy filesystems            |
| -B   | --block_size     | Specify block size                   |
| -h   | --human_readable | Print sizes in human readable format |
| -i   | --inodes         | List inode information               |
|      | --total          | Produce grand total                  |
| -T   | --type           | Print filesystem type                |

#### Explanation for a Specific Flag

Shows the meaning of the provided flags.

```bash
whattheflag curl -fsSL --help
```

| Flag | Long         | Description                            |
| ---- | ------------ | -------------------------------------- |
| -f   | --fail       | Fail silently on HTTP errors           |
| -s   | --silent     | Silent mode, do not show progress      |
| -S   | --show-error | Show error even when using silent mode |
| -L   | --location   | Follow HTTP redirects                  |
| -h   | --help       | Show help for curl                     |

#### List Supported Tools

Lists all supported tools.

```bash
whattheflag tools
```

## Supported Tools

|       |       |         |        |
| ----- | ----- | ------- | ------ |
| awk   | curl  | df      | docker |
| du    | find  | git     | grep   |
| gzip  | jq    | kubectl | nc     |
| ps    | rsync | sed     | ssh    |
| tar   | top   | unzip   | wget   |
| xargs | yq    | zip     |        |
