# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    MessageAutoDeleteTime,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetDefaultMessageAutoDeleteTime(BaseObject):
    """
    Changes the default message auto-delete time for new chats

    :param message_auto_delete_time: New default message auto-delete time; must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically
    :type message_auto_delete_time: :class:`MessageAutoDeleteTime`
    """

    ID: typing.Literal["setDefaultMessageAutoDeleteTime"] = field(
        default="setDefaultMessageAutoDeleteTime", metadata={"alias": "@type"}
    )
    message_auto_delete_time: MessageAutoDeleteTime = field(default=0)
