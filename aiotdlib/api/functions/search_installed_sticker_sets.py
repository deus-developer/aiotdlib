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
class SearchInstalledStickerSets(BaseObject):
    """
    Searches for installed sticker sets by looking for specified query in their title and name

    :param sticker_type: Type of the sticker sets to search for
    :type sticker_type: :class:`StickerType`
    :param query: Query to search for
    :type query: :class:`String`
    :param limit: The maximum number of sticker sets to return
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["searchInstalledStickerSets"] = field(
        default="searchInstalledStickerSets", metadata={"alias": "@type"}
    )
    sticker_type: StickerType
    query: String
    limit: Int32
