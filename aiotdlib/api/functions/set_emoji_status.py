# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    EmojiStatus,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetEmojiStatus(BaseObject):
    """
    Changes the emoji status of the current user; for Telegram Premium users only

    :param emoji_status: New emoji status; pass null to switch to the default badge, defaults to None
    :type emoji_status: :class:`EmojiStatus`, optional
    """

    ID: typing.Literal["setEmojiStatus"] = field(default="setEmojiStatus", metadata={"alias": "@type"})
    emoji_status: typing.Optional[EmojiStatus] = field(default=None)
