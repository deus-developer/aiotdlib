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
class GetThemedChatEmojiStatuses(BaseObject):
    """
    Returns up to 8 emoji statuses, which must be shown in the emoji status list for chats
    """

    ID: typing.Literal["getThemedChatEmojiStatuses"] = field(
        default="getThemedChatEmojiStatuses", metadata={"alias": "@type"}
    )
