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
class TestCallString(BaseObject):
    """
    Returns the received string; for testing only. This is an offline method. Can be called before authorization

    :param x: String to return
    :type x: :class:`String`
    """

    ID: typing.Literal["testCallString"] = field(default="testCallString", metadata={"alias": "@type"})
    x: String
