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
class SetAlarm(BaseObject):
    """
    Succeeds after a specified amount of time has passed. Can be called before initialization

    :param seconds: Number of seconds before the function returns
    :type seconds: :class:`Double`
    """

    ID: typing.Literal["setAlarm"] = field(default="setAlarm", metadata={"alias": "@type"})
    seconds: Double
