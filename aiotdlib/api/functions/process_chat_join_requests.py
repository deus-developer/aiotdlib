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
class ProcessChatJoinRequests(BaseObject):
    """
    Handles all pending join requests for a given link in a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param invite_link: Invite link for which to process join requests. If empty, all join requests will be processed. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
    :type invite_link: :class:`String`
    :param approve: Pass true to approve all requests; pass false to decline them
    :type approve: :class:`Bool`
    """

    ID: typing.Literal["processChatJoinRequests"] = field(
        default="processChatJoinRequests", metadata={"alias": "@type"}
    )
    chat_id: Int53
    invite_link: String = field(default="")
    approve: Bool = field(default=False)
