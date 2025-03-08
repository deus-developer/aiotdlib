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
class CanBotSendMessages(BaseObject):
    """
    Checks whether the specified bot can send messages to the user. Returns a 404 error if can't and the access can be granted by call to allowBotToSendMessages

    :param bot_user_id: Identifier of the target bot
    :type bot_user_id: :class:`Int53`
    """

    ID: typing.Literal["canBotSendMessages"] = field(default="canBotSendMessages", metadata={"alias": "@type"})
    bot_user_id: Int53
