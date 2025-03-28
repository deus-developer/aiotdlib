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
class CreateChatFolderInviteLink(BaseObject):
    """
    Creates a new invite link for a chat folder. A link can be created for a chat folder if it has only pinned and included chats

    :param chat_folder_id: Chat folder identifier
    :type chat_folder_id: :class:`Int32`
    :param chat_ids: Identifiers of chats to be accessible by the invite link. Use getChatsForChatFolderInviteLink to get suitable chats. Basic groups will be automatically converted to supergroups before link creation
    :type chat_ids: :class:`Vector[Int53]`
    :param name: Name of the link; 0-32 characters
    :type name: :class:`String`
    """

    ID: typing.Literal["createChatFolderInviteLink"] = field(
        default="createChatFolderInviteLink", metadata={"alias": "@type"}
    )
    chat_folder_id: Int32
    chat_ids: Vector[Int53]
    name: String = field(default="", metadata={"max_length": 32})
