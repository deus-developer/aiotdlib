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
class GetStickerEmojis(BaseObject):
    """
    Returns emoji corresponding to a sticker. The list is only for informational purposes, because a sticker is always sent with a fixed emoji from the corresponding Sticker object

    :param sticker: Sticker file identifier
    :type sticker: :class:`InputFile`
    """

    ID: typing.Literal["getStickerEmojis"] = field(default="getStickerEmojis", metadata={"alias": "@type"})
    sticker: InputFile
