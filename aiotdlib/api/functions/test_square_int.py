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
class TestSquareInt(BaseObject):
    """
    Returns the squared received number; for testing only. This is an offline method. Can be called before authorization

    :param x: Number to square
    :type x: :class:`Int32`
    """

    ID: typing.Literal["testSquareInt"] = field(default="testSquareInt", metadata={"alias": "@type"})
    x: Int32
