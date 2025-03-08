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
class RemoveRecentSticker(BaseObject):
    """
    Removes a sticker from the list of recently used stickers

    :param sticker: Sticker file to delete
    :type sticker: :class:`InputFile`
    :param is_attached: Pass true to remove the sticker from the list of stickers recently attached to photo or video files; pass false to remove the sticker from the list of recently sent stickers
    :type is_attached: :class:`Bool`
    """

    ID: typing.Literal["removeRecentSticker"] = field(default="removeRecentSticker", metadata={"alias": "@type"})
    sticker: InputFile
    is_attached: Bool = field(default=False)
