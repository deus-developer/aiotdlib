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
class CheckStickerSetName(BaseObject):
    """
    Checks whether a name can be used for a new sticker set

    :param name: Name to be checked
    :type name: :class:`String`
    """

    ID: typing.Literal["checkStickerSetName"] = field(default="checkStickerSetName", metadata={"alias": "@type"})
    name: String
