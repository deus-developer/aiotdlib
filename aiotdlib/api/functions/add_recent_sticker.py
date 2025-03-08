# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    InputFile,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class AddRecentSticker(BaseObject):
    """
    Manually adds a new sticker to the list of recently used stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first. Only stickers belonging to a sticker set or in WEBP or WEBM format can be added to this list. Emoji stickers can't be added to recent stickers

    :param sticker: Sticker file to add
    :type sticker: :class:`InputFile`
    :param is_attached: Pass true to add the sticker to the list of stickers recently attached to photo or video files; pass false to add the sticker to the list of recently sent stickers
    :type is_attached: :class:`Bool`
    """

    ID: typing.Literal["addRecentSticker"] = field(default="addRecentSticker", metadata={"alias": "@type"})
    sticker: InputFile
    is_attached: Bool = field(default=False)
