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
class ProcessChatFolderNewChats(BaseObject):
    """
    Process new chats added to a shareable chat folder by its owner

    :param chat_folder_id: Chat folder identifier
    :type chat_folder_id: :class:`Int32`
    :param added_chat_ids: Identifiers of the new chats, which are added to the chat folder. The chats are automatically joined if they aren't joined yet
    :type added_chat_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["processChatFolderNewChats"] = field(
        default="processChatFolderNewChats", metadata={"alias": "@type"}
    )
    chat_folder_id: Int32
    added_chat_ids: Vector[Int53]
