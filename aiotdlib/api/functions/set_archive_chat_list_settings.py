# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ArchiveChatListSettings,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetArchiveChatListSettings(BaseObject):
    """
    Changes settings for automatic moving of chats to and from the Archive chat lists

    :param settings: New settings
    :type settings: :class:`ArchiveChatListSettings`
    """

    ID: typing.Literal["setArchiveChatListSettings"] = field(
        default="setArchiveChatListSettings", metadata={"alias": "@type"}
    )
    settings: ArchiveChatListSettings
