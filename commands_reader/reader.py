from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Iterable,
)

from commands_parser import CommandsParser
from file_reader.file_readers import BasicFileReader
from text_file_reader.reader import (
    AbstractFileReader,
    TextFileReader,
)


@dataclass
class CommandsFileReader(BasicFileReader):
    parser: CommandsParser = field(default=CommandsParser(), init=False)
    file_readers: Iterable[AbstractFileReader] = field(
        default=(TextFileReader(),), init=False
    )
