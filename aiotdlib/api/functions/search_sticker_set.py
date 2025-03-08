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
class SearchStickerSet(BaseObject):
    """
    Searches for a sticker set by its name

    :param name: Name of the sticker set
    :type name: :class:`String`
    :param ignore_cache: Pass true to ignore local cache of sticker sets and always send a network request
    :type ignore_cache: :class:`Bool`
    """

    ID: typing.Literal["searchStickerSet"] = field(default="searchStickerSet", metadata={"alias": "@type"})
    name: String
    ignore_cache: Bool = field(default=False)
