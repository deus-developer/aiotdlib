# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ChatFolder,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetChatFolderChatCount(BaseObject):
    """
    Returns approximate number of chats in a being created chat folder. Main and archive chat lists must be fully preloaded for this function to work correctly

    :param folder: The new chat folder
    :type folder: :class:`ChatFolder`
    """

    ID: typing.Literal["getChatFolderChatCount"] = field(default="getChatFolderChatCount", metadata={"alias": "@type"})
    folder: ChatFolder
