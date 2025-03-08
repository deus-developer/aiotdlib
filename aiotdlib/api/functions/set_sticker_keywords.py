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
class SetStickerKeywords(BaseObject):
    """
    Changes the list of keywords of a sticker. The sticker must belong to a regular or custom emoji sticker set that is owned by the current user

    :param sticker: Sticker
    :type sticker: :class:`InputFile`
    :param keywords: List of up to 20 keywords with total length up to 64 characters, which can be used to find the sticker
    :type keywords: :class:`Vector[String]`
    """

    ID: typing.Literal["setStickerKeywords"] = field(default="setStickerKeywords", metadata={"alias": "@type"})
    sticker: InputFile
    keywords: Vector[String]
