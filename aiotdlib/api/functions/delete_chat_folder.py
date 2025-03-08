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
class DeleteChatFolder(BaseObject):
    """
    Deletes existing chat folder

    :param chat_folder_id: Chat folder identifier
    :type chat_folder_id: :class:`Int32`
    :param leave_chat_ids: Identifiers of the chats to leave. The chats must be pinned or always included in the folder
    :type leave_chat_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["deleteChatFolder"] = field(default="deleteChatFolder", metadata={"alias": "@type"})
    chat_folder_id: Int32
    leave_chat_ids: Vector[Int53]
