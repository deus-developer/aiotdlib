# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ChatJoinRequest,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetChatJoinRequests(BaseObject):
    """
    Returns pending join requests in a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param query: A query to search for in the first names, last names and usernames of the users to return
    :type query: :class:`String`
    :param limit: The maximum number of requests to join the chat to return
    :type limit: :class:`Int32`
    :param invite_link: Invite link for which to return join requests. If empty, all join requests will be returned. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
    :type invite_link: :class:`String`
    :param offset_request: A chat join request from which to return next requests; pass null to get results from the beginning, defaults to None
    :type offset_request: :class:`ChatJoinRequest`, optional
    """

    ID: typing.Literal["getChatJoinRequests"] = field(default="getChatJoinRequests", metadata={"alias": "@type"})
    chat_id: Int53
    query: String
    limit: Int32
    invite_link: String = field(default="")
    offset_request: typing.Optional[ChatJoinRequest] = field(default=None)
