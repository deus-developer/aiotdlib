# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    StickerType,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SearchStickerSets(BaseObject):
    """
    Searches for sticker sets by looking for specified query in their title and name. Excludes installed sticker sets from the results

    :param sticker_type: Type of the sticker sets to return
    :type sticker_type: :class:`StickerType`
    :param query: Query to search for
    :type query: :class:`String`
    """

    ID: typing.Literal["searchStickerSets"] = field(default="searchStickerSets", metadata={"alias": "@type"})
    sticker_type: StickerType
    query: String
