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
    MaskPosition,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetStickerMaskPosition(BaseObject):
    """
    Changes the mask position of a mask sticker. The sticker must belong to a mask sticker set that is owned by the current user

    :param sticker: Sticker
    :type sticker: :class:`InputFile`
    :param mask_position: Position where the mask is placed; pass null to remove mask position, defaults to None
    :type mask_position: :class:`MaskPosition`, optional
    """

    ID: typing.Literal["setStickerMaskPosition"] = field(default="setStickerMaskPosition", metadata={"alias": "@type"})
    sticker: InputFile
    mask_position: typing.Optional[MaskPosition] = field(default=None)
