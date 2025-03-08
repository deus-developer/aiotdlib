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
class SearchStickers(BaseObject):
    """
    Searches for stickers from public sticker sets that correspond to any of the given emoji

    :param sticker_type: Type of the stickers to return
    :type sticker_type: :class:`StickerType`
    :param emojis: Space-separated list of emojis to search for
    :type emojis: :class:`String`
    :param offset: The offset from which to return the stickers; must be non-negative
    :type offset: :class:`Int32`
    :param limit: The maximum number of stickers to be returned; 0-100
    :type limit: :class:`Int32`
    :param query: Query to search for; may be empty to search for emoji only
    :type query: :class:`String`
    :param input_language_codes: List of possible IETF language tags of the user's input language; may be empty if unknown, defaults to list()
    :type input_language_codes: :class:`Vector[String]`
    """

    ID: typing.Literal["searchStickers"] = field(default="searchStickers", metadata={"alias": "@type"})
    sticker_type: StickerType
    emojis: String
    offset: Int32
    limit: Int32
    query: String = field(default="")
    input_language_codes: Vector[String] = field(default_factory=list)
