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
class GetGameHighScores(BaseObject):
    """
    Returns the high scores for a game and some part of the high score table in the range of the specified user; for bots only

    :param chat_id: The chat that contains the message with the game
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param user_id: User identifier
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["getGameHighScores"] = field(default="getGameHighScores", metadata={"alias": "@type"})
    chat_id: Int53
    message_id: Int53
    user_id: Int53
