# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    MessageSender,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class RemoveMessageSenderBotVerification(BaseObject):
    """
    Removes the verification status of a user or a chat by an owned bot

    :param bot_user_id: Identifier of the owned bot, which verified the user or the chat
    :type bot_user_id: :class:`Int53`
    :param verified_id: Identifier of the user or the supergroup or channel chat, which verification is removed
    :type verified_id: :class:`MessageSender`
    """

    ID: typing.Literal["removeMessageSenderBotVerification"] = field(
        default="removeMessageSenderBotVerification", metadata={"alias": "@type"}
    )
    bot_user_id: Int53
    verified_id: MessageSender
