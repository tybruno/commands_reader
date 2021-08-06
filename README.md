# commands_reader
Read a list of commands from a .txt file or a string.
#### Key Features:
* **Easy**: Designed to easily retrieve a list of hosts from a file or string.
* **There is More!!!**:
    * [hosts_reader](https://github.com/tybruno/hosts_reader): Read a list of hosts from a file or string.
    * [text_file_reader](https://github.com/tybruno/text_file_reader): Library that makes reading text files easy.
    * [file_reader](https://github.com/tybruno/file_reader): Created an abstraction for reading multiple types of files that hosts_reader, commands_reader, and text_file_reader inherit from.
### Usage
#### File example
commands.txt
```text
show cdp nei, show run | inc boot
```
commands2.txt
```text
show cdp neigh
show run | inc boot
```

```python
from commands_reader import CommandsFileReader

commands_file = "commands2.txt"

read_hosts_file = CommandsFileReader()

commands = read_hosts_file(commands_file)

print(tuple(commmands)) # ('show cdp nei', 'show run | inc boot')
```
#### String Example
```python
from commands_reader import CommandsParser
commands_str = "show cdp nei, show run | inc boot"

parse_commands = CommandsParser()

commands = parse_commands(commands_str)

print(list(commands)) # ['show cdp nei', 'show run | inc boot']
```

### Road Map
* Add support for excel files
* Add support for csv files
