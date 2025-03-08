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
    StickerFormat,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetStickerSetThumbnail(BaseObject):
    """
    Sets a sticker set thumbnail

    :param user_id: Sticker set owner; ignored for regular users
    :type user_id: :class:`Int53`
    :param name: Sticker set name. The sticker set must be owned by the current user
    :type name: :class:`String`
    :param thumbnail: Thumbnail to set; pass null to remove the sticker set thumbnail, defaults to None
    :type thumbnail: :class:`InputFile`, optional
    :param format_: Format of the thumbnail; pass null if thumbnail is removed, defaults to None
    :type format_: :class:`StickerFormat`, optional
    """

    ID: typing.Literal["setStickerSetThumbnail"] = field(default="setStickerSetThumbnail", metadata={"alias": "@type"})
    user_id: Int53
    name: String
    thumbnail: typing.Optional[InputFile] = field(default=None)
    format_: typing.Optional[StickerFormat] = field(default=None, metadata={"alias": "format"})
