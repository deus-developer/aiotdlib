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
class GetChatFolderDefaultIconName(BaseObject):
    """
    Returns default icon name for a folder. Can be called synchronously

    :param folder: Chat folder
    :type folder: :class:`ChatFolder`
    """

    ID: typing.Literal["getChatFolderDefaultIconName"] = field(
        default="getChatFolderDefaultIconName", metadata={"alias": "@type"}
    )
    folder: ChatFolder
