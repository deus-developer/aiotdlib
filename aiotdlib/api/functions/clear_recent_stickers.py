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
class ClearRecentStickers(BaseObject):
    """
    Clears the list of recently used stickers

    :param is_attached: Pass true to clear the list of stickers recently attached to photo or video files; pass false to clear the list of recently sent stickers
    :type is_attached: :class:`Bool`
    """

    ID: typing.Literal["clearRecentStickers"] = field(default="clearRecentStickers", metadata={"alias": "@type"})
    is_attached: Bool = field(default=False)
