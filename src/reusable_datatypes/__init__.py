from collections.abc import Sequence
from os import PathLike
from io import BytesIO

import numpy as np

type FileLike = PathLike[str] | BytesIO

type IntOrFloat = int | float
type NumpyInt = int | np.integer
type NumpyFloat = float | np.floating
type Number = int | float | np.integer | np.floating

type JSONable = dict[str, "JSONable"] | Sequence["JSONable"] | str | int | float | bool | None

__all__ = [
    'FileLike',
    'IntOrFloat',
    'NumpyInt',
    'NumpyFloat',
    'Number',
    'JSONable',
]