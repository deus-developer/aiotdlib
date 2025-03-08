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
class AllowBotToSendMessages(BaseObject):
    """
    Allows the specified bot to send messages to the user

    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`Int53`
    """

    ID: typing.Literal["allowBotToSendMessages"] = field(default="allowBotToSendMessages", metadata={"alias": "@type"})
    bot_user_id: Int53
