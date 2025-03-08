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
class CreateChatFolder(BaseObject):
    """
    Creates new chat folder. Returns information about the created chat folder. There can be up to getOption("chat_folder_count_max") chat folders, but the limit can be increased with Telegram Premium

    :param folder: The new chat folder
    :type folder: :class:`ChatFolder`
    """

    ID: typing.Literal["createChatFolder"] = field(default="createChatFolder", metadata={"alias": "@type"})
    folder: ChatFolder
