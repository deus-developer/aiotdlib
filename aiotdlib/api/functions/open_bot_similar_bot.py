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
class OpenBotSimilarBot(BaseObject):
    """
    Informs TDLib that a bot was opened from the list of similar bots

    :param bot_user_id: Identifier of the original bot, which similar bots were requested
    :type bot_user_id: :class:`Int53`
    :param opened_bot_user_id: Identifier of the opened bot
    :type opened_bot_user_id: :class:`Int53`
    """

    ID: typing.Literal["openBotSimilarBot"] = field(default="openBotSimilarBot", metadata={"alias": "@type"})
    bot_user_id: Int53
    opened_bot_user_id: Int53
