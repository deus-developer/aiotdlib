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
class GetDefaultChatEmojiStatuses(BaseObject):
    """
    Returns default emoji statuses for chats
    """

    ID: typing.Literal["getDefaultChatEmojiStatuses"] = field(
        default="getDefaultChatEmojiStatuses", metadata={"alias": "@type"}
    )
