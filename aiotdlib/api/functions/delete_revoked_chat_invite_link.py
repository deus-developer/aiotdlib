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
class DeleteRevokedChatInviteLink(BaseObject):
    """
    Deletes revoked chat invite links. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param invite_link: Invite link to revoke
    :type invite_link: :class:`String`
    """

    ID: typing.Literal["deleteRevokedChatInviteLink"] = field(
        default="deleteRevokedChatInviteLink", metadata={"alias": "@type"}
    )
    chat_id: Int53
    invite_link: String
