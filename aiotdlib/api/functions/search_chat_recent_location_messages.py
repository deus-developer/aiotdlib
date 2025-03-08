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
class SearchChatRecentLocationMessages(BaseObject):
    """
    Returns information about the recent locations of chat members that were sent to the chat. Returns up to 1 location message per user

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param limit: The maximum number of messages to be returned
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["searchChatRecentLocationMessages"] = field(
        default="searchChatRecentLocationMessages", metadata={"alias": "@type"}
    )
    chat_id: Int53
    limit: Int32
