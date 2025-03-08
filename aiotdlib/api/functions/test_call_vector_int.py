# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.base import *


@dataclass(slots=True, kw_only=True)
class TestCallVectorInt(BaseObject):
    """
    Returns the received vector of numbers; for testing only. This is an offline method. Can be called before authorization

    :param x: Vector of numbers to return
    :type x: :class:`Vector[Int32]`
    """

    ID: typing.Literal["testCallVectorInt"] = field(default="testCallVectorInt", metadata={"alias": "@type"})
    x: Vector[Int32]
