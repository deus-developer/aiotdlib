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
class GetChatMessageByDate(BaseObject):
    """
    Returns the last message sent in a chat no later than the specified date. Returns a 404 error if such message doesn't exist

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param date: Point in time (Unix timestamp) relative to which to search for messages
    :type date: :class:`Int32`
    """

    ID: typing.Literal["getChatMessageByDate"] = field(default="getChatMessageByDate", metadata={"alias": "@type"})
    chat_id: Int53
    date: Int32
