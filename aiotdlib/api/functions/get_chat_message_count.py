# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import MISSING, dataclass, field

from ..types.all import (
    SearchMessagesFilter,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetChatMessageCount(BaseObject):
    """
    Returns approximate number of messages of the specified type in the chat

    :param chat_id: Identifier of the chat in which to count messages
    :type chat_id: :class:`Int53`
    :param filter_: Filter for message content; searchMessagesFilterEmpty is unsupported in this function
    :type filter_: :class:`SearchMessagesFilter`
    :param saved_messages_topic_id: If not 0, only messages in the specified Saved Messages topic will be counted; pass 0 to count all messages, or for chats other than Saved Messages
    :type saved_messages_topic_id: :class:`Int53`
    :param return_local: Pass true to get the number of messages without sending network requests, or -1 if the number of messages is unknown locally
    :type return_local: :class:`Bool`
    """

    ID: typing.Literal["getChatMessageCount"] = field(default="getChatMessageCount", metadata={"alias": "@type"})
    chat_id: Int53
    filter_: SearchMessagesFilter = field(default=MISSING, metadata={"alias": "filter"})
    saved_messages_topic_id: Int53 = field(default=0)
    return_local: Bool = field(default=False)
