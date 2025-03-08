# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    TestInt,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class TestCallVectorIntObject(BaseObject):
    """
    Returns the received vector of objects containing a number; for testing only. This is an offline method. Can be called before authorization

    :param x: Vector of objects to return
    :type x: :class:`Vector[TestInt]`
    """

    ID: typing.Literal["testCallVectorIntObject"] = field(
        default="testCallVectorIntObject", metadata={"alias": "@type"}
    )
    x: Vector[TestInt]
