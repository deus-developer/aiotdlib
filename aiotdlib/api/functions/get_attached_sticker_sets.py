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
class GetAttachedStickerSets(BaseObject):
    """
    Returns a list of sticker sets attached to a file, including regular, mask, and emoji sticker sets. Currently, only animations, photos, and videos can have attached sticker sets

    :param file_id: File identifier
    :type file_id: :class:`Int32`
    """

    ID: typing.Literal["getAttachedStickerSets"] = field(default="getAttachedStickerSets", metadata={"alias": "@type"})
    file_id: Int32
