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
class SetStickerPositionInSet(BaseObject):
    """
    Changes the position of a sticker in the set to which it belongs. The sticker set must be owned by the current user

    :param sticker: Sticker
    :type sticker: :class:`InputFile`
    :param position: New position of the sticker in the set, 0-based
    :type position: :class:`Int32`
    """

    ID: typing.Literal["setStickerPositionInSet"] = field(
        default="setStickerPositionInSet", metadata={"alias": "@type"}
    )
    sticker: InputFile
    position: Int32
