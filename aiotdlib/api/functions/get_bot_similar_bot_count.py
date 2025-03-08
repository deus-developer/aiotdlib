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
class GetBotSimilarBotCount(BaseObject):
    """
    Returns approximate number of bots similar to the given bot

    :param bot_user_id: User identifier of the target bot
    :type bot_user_id: :class:`Int53`
    :param return_local: Pass true to get the number of bots without sending network requests, or -1 if the number of bots is unknown locally
    :type return_local: :class:`Bool`
    """

    ID: typing.Literal["getBotSimilarBotCount"] = field(default="getBotSimilarBotCount", metadata={"alias": "@type"})
    bot_user_id: Int53
    return_local: Bool = field(default=False)
