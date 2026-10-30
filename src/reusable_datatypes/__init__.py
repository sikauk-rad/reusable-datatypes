from collections.abc import Sequence
from datetime import date, datetime, time
from io import BytesIO
from os import PathLike
import re
from uuid import UUID

import numpy as np

type FileLike = PathLike[str] | BytesIO

type IntOrFloat = int | float
type NumpyInt = int | np.integer
type NumpyFloat = float | np.floating
type Number = int | float | np.integer | np.floating

type JSONable = dict[str, "JSONable"] | Sequence["JSONable"] | str | int | float | bool | date | datetime | time | UUID | None

JSON_INCOMPATIBLE_CHARS = '[^A-Za-z0-9_]+'

def normalise_string(string: str) -> str:

    return re.sub(
        pattern = JSON_INCOMPATIBLE_CHARS, 
        repl = '_', 
        string = string,
    ).strip('_')


__all__ = [
    'FileLike',
    'IntOrFloat',
    'JSONable',
    'NumpyInt',
    'NumpyFloat',
    'Number',
    'normalise_string',
]
