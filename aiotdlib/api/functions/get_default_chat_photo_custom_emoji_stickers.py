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
class GetDefaultChatPhotoCustomEmojiStickers(BaseObject):
    """
    Returns default list of custom emoji stickers for placing on a chat photo
    """

    ID: typing.Literal["getDefaultChatPhotoCustomEmojiStickers"] = field(
        default="getDefaultChatPhotoCustomEmojiStickers", metadata={"alias": "@type"}
    )
