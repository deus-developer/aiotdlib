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
class GetInstalledStickerSets(BaseObject):
    """
    Returns a list of installed sticker sets

    :param sticker_type: Type of the sticker sets to return
    :type sticker_type: :class:`StickerType`
    """

    ID: typing.Literal["getInstalledStickerSets"] = field(
        default="getInstalledStickerSets", metadata={"alias": "@type"}
    )
    sticker_type: StickerType
