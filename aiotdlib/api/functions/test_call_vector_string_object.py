# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    TestString,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class TestCallVectorStringObject(BaseObject):
    """
    Returns the received vector of objects containing a string; for testing only. This is an offline method. Can be called before authorization

    :param x: Vector of objects to return
    :type x: :class:`Vector[TestString]`
    """

    ID: typing.Literal["testCallVectorStringObject"] = field(
        default="testCallVectorStringObject", metadata={"alias": "@type"}
    )
    x: Vector[TestString]
