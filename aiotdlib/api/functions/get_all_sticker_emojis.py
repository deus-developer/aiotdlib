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
class GetAllStickerEmojis(BaseObject):
    """
    Returns unique emoji that correspond to stickers to be found by the getStickers(sticker_type, query, 1000000, chat_id)

    :param sticker_type: Type of the stickers to search for
    :type sticker_type: :class:`StickerType`
    :param query: Search query
    :type query: :class:`String`
    :param chat_id: Chat identifier for which to find stickers
    :type chat_id: :class:`Int53`
    :param return_only_main_emoji: Pass true if only main emoji for each found sticker must be included in the result
    :type return_only_main_emoji: :class:`Bool`
    """

    ID: typing.Literal["getAllStickerEmojis"] = field(default="getAllStickerEmojis", metadata={"alias": "@type"})
    sticker_type: StickerType
    query: String
    chat_id: Int53
    return_only_main_emoji: Bool = field(default=False)
