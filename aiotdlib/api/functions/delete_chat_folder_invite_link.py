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
class DeleteChatFolderInviteLink(BaseObject):
    """
    Deletes an invite link for a chat folder

    :param chat_folder_id: Chat folder identifier
    :type chat_folder_id: :class:`Int32`
    :param invite_link: Invite link to be deleted
    :type invite_link: :class:`String`
    """

    ID: typing.Literal["deleteChatFolderInviteLink"] = field(
        default="deleteChatFolderInviteLink", metadata={"alias": "@type"}
    )
    chat_folder_id: Int32
    invite_link: String
