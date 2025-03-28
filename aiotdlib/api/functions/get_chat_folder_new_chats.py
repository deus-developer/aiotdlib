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
class GetChatFolderNewChats(BaseObject):
    """
    Returns new chats added to a shareable chat folder by its owner. The method must be called at most once in getOption("chat_folder_new_chats_update_period") for the given chat folder

    :param chat_folder_id: Chat folder identifier
    :type chat_folder_id: :class:`Int32`
    """

    ID: typing.Literal["getChatFolderNewChats"] = field(default="getChatFolderNewChats", metadata={"alias": "@type"})
    chat_folder_id: Int32
