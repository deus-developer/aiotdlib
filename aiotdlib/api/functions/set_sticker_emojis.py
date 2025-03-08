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
class SetStickerEmojis(BaseObject):
    """
    Changes the list of emojis corresponding to a sticker. The sticker must belong to a regular or custom emoji sticker set that is owned by the current user

    :param sticker: Sticker
    :type sticker: :class:`InputFile`
    :param emojis: New string with 1-20 emoji corresponding to the sticker
    :type emojis: :class:`String`
    """

    ID: typing.Literal["setStickerEmojis"] = field(default="setStickerEmojis", metadata={"alias": "@type"})
    sticker: InputFile
    emojis: String
