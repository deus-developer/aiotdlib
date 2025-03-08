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
class TestCallVectorString(BaseObject):
    """
    Returns the received vector of strings; for testing only. This is an offline method. Can be called before authorization

    :param x: Vector of strings to return
    :type x: :class:`Vector[String]`
    """

    ID: typing.Literal["testCallVectorString"] = field(default="testCallVectorString", metadata={"alias": "@type"})
    x: Vector[String]
