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
class GetChatFolder(BaseObject):
    """
    Returns information about a chat folder by its identifier

    :param chat_folder_id: Chat folder identifier
    :type chat_folder_id: :class:`Int32`
    """

    ID: typing.Literal["getChatFolder"] = field(default="getChatFolder", metadata={"alias": "@type"})
    chat_folder_id: Int32
