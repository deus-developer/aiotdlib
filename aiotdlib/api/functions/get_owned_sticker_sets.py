# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetOwnedStickerSets(BaseObject):
    """
    Returns sticker sets owned by the current user

    :param offset_sticker_set_id: Identifier of the sticker set from which to return owned sticker sets; use 0 to get results from the beginning
    :type offset_sticker_set_id: :class:`Int64`
    :param limit: The maximum number of sticker sets to be returned; must be positive and can't be greater than 100. For optimal performance, the number of returned objects is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getOwnedStickerSets"] = field(default="getOwnedStickerSets", metadata={"alias": "@type"})
    offset_sticker_set_id: Int64
    limit: Int32
