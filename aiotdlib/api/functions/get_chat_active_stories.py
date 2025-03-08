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
class GetChatActiveStories(BaseObject):
    """
    Returns the list of active stories posted by the given chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChatActiveStories"] = field(default="getChatActiveStories", metadata={"alias": "@type"})
    chat_id: Int53
