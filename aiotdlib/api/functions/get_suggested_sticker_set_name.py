# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import MISSING, dataclass, field

from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetSuggestedStickerSetName(BaseObject):
    """
    Returns a suggested name for a new sticker set with a given title

    :param title: Sticker set title; 1-64 characters
    :type title: :class:`String`
    """

    ID: typing.Literal["getSuggestedStickerSetName"] = field(
        default="getSuggestedStickerSetName", metadata={"alias": "@type"}
    )
    title: String = field(default=MISSING, metadata={"min_length": 1, "max_length": 64})
