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
class SetStickerSetTitle(BaseObject):
    """
    Sets a sticker set title

    :param name: Sticker set name. The sticker set must be owned by the current user
    :type name: :class:`String`
    :param title: New sticker set title
    :type title: :class:`String`
    """

    ID: typing.Literal["setStickerSetTitle"] = field(default="setStickerSetTitle", metadata={"alias": "@type"})
    name: String
    title: String
