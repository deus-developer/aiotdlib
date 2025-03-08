# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ChatMembersFilter,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SearchChatMembers(BaseObject):
    """
    Searches for a specified query in the first name, last name and usernames of the members of a specified chat. Requires administrator rights if the chat is a channel

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param query: Query to search for
    :type query: :class:`String`
    :param limit: The maximum number of users to be returned; up to 200
    :type limit: :class:`Int32`
    :param filter_: The type of users to search for; pass null to search among all chat members, defaults to None
    :type filter_: :class:`ChatMembersFilter`, optional
    """

    ID: typing.Literal["searchChatMembers"] = field(default="searchChatMembers", metadata={"alias": "@type"})
    chat_id: Int53
    query: String
    limit: Int32
    filter_: typing.Optional[ChatMembersFilter] = field(default=None, metadata={"alias": "filter"})
