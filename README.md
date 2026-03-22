# Logger MQTT

A command-line tool that subscribes to an MQTT topic and logs received messages to the terminal and optionally to a timestamped file.

## Requirements

- Python >= 3.12
- [paho-mqtt](https://pypi.org/project/paho-mqtt/) >= 2.1.0

## Installation

```bash
# Using uv (recommended)
uv sync

# Or with pip
pip install paho-mqtt
```

## Usage

```bash
python main.py [OPTIONS]
```

All parameters are optional. Defaults are used when not specified.

| Flag | Argument | Default | Description |
|------|----------|---------|-------------|
| `-x` | — | off | Enable file output |
| `-o` | `<path>` | `logs/logfile.txt` | Path or filename for the log file |
| `-i` | `<ip>` | `192.168.178.100` | IP address of the MQTT broker |
| `-p` | `<port>` | `1884` | Port of the MQTT broker |
| `-t` | `<topic>` | `climate/office/+` | Topic to subscribe to |

### Examples

Subscribe with defaults:
```bash
python main.py
```

Subscribe to a custom topic with file logging enabled:
```bash
python main.py -t "home/sensors/#" -i 192.168.1.10 -p 1883 -x
```

Log to a specific file:
```bash
python main.py -x -o /var/log/mqtt/output.txt
```

## File Output

When file output is active (`-x`), messages are appended to a date-stamped log file. For example, `logfile.txt` becomes `logfile_20260322.txt`. Log files are stored in the `logs/` directory by default.

Each line is written in the format:
```
[topic] message
```

## Project Structure

```
Logger_MQTT/
├── main.py          # Entry point, argument parsing
├── src/
│   ├── mqtt.py      # MQTT client wrapper (subscribe, callbacks, file output)
│   └── paramters.py # Parameters dataclass and CLI argument parsing
├── logs/            # Default directory for log files
└── pyproject.toml
```

## License

MIT