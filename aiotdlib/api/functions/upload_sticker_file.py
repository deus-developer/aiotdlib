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
class UploadStickerFile(BaseObject):
    """
    Uploads a file with a sticker; returns the uploaded file

    :param user_id: Sticker file owner; ignored for regular users
    :type user_id: :class:`Int53`
    :param sticker_format: Sticker format
    :type sticker_format: :class:`StickerFormat`
    :param sticker: File file to upload; must fit in a 512x512 square. For WEBP stickers the file must be in WEBP or PNG format, which will be converted to WEBP server-side. See https://core.telegram.org/animated_stickers#technical-requirements for technical requirements
    :type sticker: :class:`InputFile`
    """

    ID: typing.Literal["uploadStickerFile"] = field(default="uploadStickerFile", metadata={"alias": "@type"})
    user_id: Int53
    sticker_format: StickerFormat
    sticker: InputFile
