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
class GetThemedEmojiStatuses(BaseObject):
    """
    Returns up to 8 emoji statuses, which must be shown right after the default Premium Badge in the emoji status list for self status
    """

    ID: typing.Literal["getThemedEmojiStatuses"] = field(default="getThemedEmojiStatuses", metadata={"alias": "@type"})
