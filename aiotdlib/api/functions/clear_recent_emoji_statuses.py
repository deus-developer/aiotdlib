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
class ClearRecentEmojiStatuses(BaseObject):
    """
    Clears the list of recently used emoji statuses for self status
    """

    ID: typing.Literal["clearRecentEmojiStatuses"] = field(
        default="clearRecentEmojiStatuses", metadata={"alias": "@type"}
    )
