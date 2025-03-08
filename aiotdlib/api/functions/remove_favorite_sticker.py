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
class RemoveFavoriteSticker(BaseObject):
    """
    Removes a sticker from the list of favorite stickers

    :param sticker: Sticker file to delete from the list
    :type sticker: :class:`InputFile`
    """

    ID: typing.Literal["removeFavoriteSticker"] = field(default="removeFavoriteSticker", metadata={"alias": "@type"})
    sticker: InputFile
