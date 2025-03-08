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
class GetArchiveChatListSettings(BaseObject):
    """
    Returns settings for automatic moving of chats to and from the Archive chat lists
    """

    ID: typing.Literal["getArchiveChatListSettings"] = field(
        default="getArchiveChatListSettings", metadata={"alias": "@type"}
    )
