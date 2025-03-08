from __future__ import annotations

import logging
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Any,
    NewType,
    Optional,
)

INT32_MAX_VALUE = 2**31  # Unsigned INT32
INT53_MAX_VALUE = 2**52  # Unsigned INT53
INT64_MAX_VALUE = DOUBLE64_MAX_VALUE = 2**63  # Unsigned INT64
INT32_MIN_VALUE = -INT32_MAX_VALUE
INT53_MIN_VALUE = -INT53_MAX_VALUE
INT64_MIN_VALUE = DOUBLE64_MIN_VALUE = -INT64_MAX_VALUE

type Bool = bool
type String = str
type Double = float
Int32 = NewType("Int32", int)
Int53 = NewType("Int53", int)
Int64 = NewType("Int64", int)
type Bytes = bytes
type Vector[T] = list[T]

logger = logging.getLogger("BaseObject")


@dataclass(slots=True, kw_only=True)
class BaseObject:
    EXTRA: Optional[dict[str, Any]] = field(default_factory=dict, metadata={"alias": "@extra"})
