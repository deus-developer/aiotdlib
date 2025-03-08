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
class DeleteStickerSet(BaseObject):
    """
    Completely deletes a sticker set

    :param name: Sticker set name. The sticker set must be owned by the current user
    :type name: :class:`String`
    """

    ID: typing.Literal["deleteStickerSet"] = field(default="deleteStickerSet", metadata={"alias": "@type"})
    name: String
