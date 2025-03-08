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
class GetRecentEmojiStatuses(BaseObject):
    """
    Returns recent emoji statuses for self status
    """

    ID: typing.Literal["getRecentEmojiStatuses"] = field(default="getRecentEmojiStatuses", metadata={"alias": "@type"})
