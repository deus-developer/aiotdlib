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
class GetInlineGameHighScores(BaseObject):
    """
    Returns game high scores and some part of the high score table in the range of the specified user; for bots only

    :param inline_message_id: Inline message identifier
    :type inline_message_id: :class:`String`
    :param user_id: User identifier
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["getInlineGameHighScores"] = field(
        default="getInlineGameHighScores", metadata={"alias": "@type"}
    )
    inline_message_id: String
    user_id: Int53
