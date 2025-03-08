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
class RemoveStickerFromSet(BaseObject):
    """
    Removes a sticker from the set to which it belongs. The sticker set must be owned by the current user

    :param sticker: Sticker to remove from the set
    :type sticker: :class:`InputFile`
    """

    ID: typing.Literal["removeStickerFromSet"] = field(default="removeStickerFromSet", metadata={"alias": "@type"})
    sticker: InputFile
