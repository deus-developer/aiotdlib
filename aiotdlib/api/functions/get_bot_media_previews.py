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
class GetBotMediaPreviews(BaseObject):
    """
    Returns the list of media previews of a bot

    :param bot_user_id: Identifier of the target bot. The bot must have the main Web App
    :type bot_user_id: :class:`Int53`
    """

    ID: typing.Literal["getBotMediaPreviews"] = field(default="getBotMediaPreviews", metadata={"alias": "@type"})
    bot_user_id: Int53
