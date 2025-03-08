# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    EmojiStatus,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetUserEmojiStatus(BaseObject):
    """
    Changes the emoji status of a user; for bots only

    :param user_id: Identifier of the user
    :type user_id: :class:`Int53`
    :param emoji_status: New emoji status; pass null to switch to the default badge, defaults to None
    :type emoji_status: :class:`EmojiStatus`, optional
    """

    ID: typing.Literal["setUserEmojiStatus"] = field(default="setUserEmojiStatus", metadata={"alias": "@type"})
    user_id: Int53
    emoji_status: typing.Optional[EmojiStatus] = field(default=None)
