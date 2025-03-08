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
class ReadAllChatReactions(BaseObject):
    """
    Marks all reactions in a chat or a forum topic as read

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["readAllChatReactions"] = field(default="readAllChatReactions", metadata={"alias": "@type"})
    chat_id: Int53
