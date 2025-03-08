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
class RevokeChatInviteLink(BaseObject):
    """
    Revokes invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links. If a primary link is revoked, then additionally to the revoked link returns new primary link

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param invite_link: Invite link to be revoked
    :type invite_link: :class:`String`
    """

    ID: typing.Literal["revokeChatInviteLink"] = field(default="revokeChatInviteLink", metadata={"alias": "@type"})
    chat_id: Int53
    invite_link: String
