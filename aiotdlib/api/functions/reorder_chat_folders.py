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
class ReorderChatFolders(BaseObject):
    """
    Changes the order of chat folders

    :param chat_folder_ids: Identifiers of chat folders in the new correct order
    :type chat_folder_ids: :class:`Vector[Int32]`
    :param main_chat_list_position: Position of the main chat list among chat folders, 0-based. Can be non-zero only for Premium users
    :type main_chat_list_position: :class:`Int32`
    """

    ID: typing.Literal["reorderChatFolders"] = field(default="reorderChatFolders", metadata={"alias": "@type"})
    chat_folder_ids: Vector[Int32]
    main_chat_list_position: Int32
