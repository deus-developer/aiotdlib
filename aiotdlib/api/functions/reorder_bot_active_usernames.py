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
class ReorderBotActiveUsernames(BaseObject):
    """
    Changes order of active usernames of a bot. Can be called only if userTypeBot.can_be_edited == true

    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`Int53`
    :param usernames: The new order of active usernames. All currently active usernames must be specified
    :type usernames: :class:`Vector[String]`
    """

    ID: typing.Literal["reorderBotActiveUsernames"] = field(
        default="reorderBotActiveUsernames", metadata={"alias": "@type"}
    )
    bot_user_id: Int53
    usernames: Vector[String]
