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
class GetDefaultMessageAutoDeleteTime(BaseObject):
    """
    Returns default message auto-delete time setting for new chats
    """

    ID: typing.Literal["getDefaultMessageAutoDeleteTime"] = field(
        default="getDefaultMessageAutoDeleteTime", metadata={"alias": "@type"}
    )
