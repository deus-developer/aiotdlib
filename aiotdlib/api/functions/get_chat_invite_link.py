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
class GetChatInviteLink(BaseObject):
    """
    Returns information about an invite link. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param invite_link: Invite link to get
    :type invite_link: :class:`String`
    """

    ID: typing.Literal["getChatInviteLink"] = field(default="getChatInviteLink", metadata={"alias": "@type"})
    chat_id: Int53
    invite_link: String
