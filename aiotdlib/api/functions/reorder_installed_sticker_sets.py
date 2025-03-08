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
class ReorderInstalledStickerSets(BaseObject):
    """
    Changes the order of installed sticker sets

    :param sticker_type: Type of the sticker sets to reorder
    :type sticker_type: :class:`StickerType`
    :param sticker_set_ids: Identifiers of installed sticker sets in the new correct order
    :type sticker_set_ids: :class:`Vector[Int64]`
    """

    ID: typing.Literal["reorderInstalledStickerSets"] = field(
        default="reorderInstalledStickerSets", metadata={"alias": "@type"}
    )
    sticker_type: StickerType
    sticker_set_ids: Vector[Int64]
