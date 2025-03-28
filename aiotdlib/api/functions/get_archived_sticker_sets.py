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
class GetArchivedStickerSets(BaseObject):
    """
    Returns a list of archived sticker sets

    :param sticker_type: Type of the sticker sets to return
    :type sticker_type: :class:`StickerType`
    :param offset_sticker_set_id: Identifier of the sticker set from which to return the result; use 0 to get results from the beginning
    :type offset_sticker_set_id: :class:`Int64`
    :param limit: The maximum number of sticker sets to return; up to 100
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getArchivedStickerSets"] = field(default="getArchivedStickerSets", metadata={"alias": "@type"})
    sticker_type: StickerType
    offset_sticker_set_id: Int64
    limit: Int32
