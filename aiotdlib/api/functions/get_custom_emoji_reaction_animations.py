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
class GetCustomEmojiReactionAnimations(BaseObject):
    """
    Returns TGS stickers with generic animations for custom emoji reactions
    """

    ID: typing.Literal["getCustomEmojiReactionAnimations"] = field(
        default="getCustomEmojiReactionAnimations", metadata={"alias": "@type"}
    )
