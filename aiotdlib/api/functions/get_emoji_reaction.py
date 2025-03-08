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
class GetEmojiReaction(BaseObject):
    """
    Returns information about an emoji reaction. Returns a 404 error if the reaction is not found

    :param emoji: Text representation of the reaction
    :type emoji: :class:`String`
    """

    ID: typing.Literal["getEmojiReaction"] = field(default="getEmojiReaction", metadata={"alias": "@type"})
    emoji: String
