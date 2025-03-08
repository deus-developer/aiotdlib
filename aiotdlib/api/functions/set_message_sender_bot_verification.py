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
class SetMessageSenderBotVerification(BaseObject):
    """
    Changes the verification status of a user or a chat by an owned bot

    :param bot_user_id: Identifier of the owned bot, which will verify the user or the chat
    :type bot_user_id: :class:`Int53`
    :param verified_id: Identifier of the user or the supergroup or channel chat, which will be verified by the bot
    :type verified_id: :class:`MessageSender`
    :param custom_description: Custom description of verification reason; 0-getOption("bot_verification_custom_description_length_max"). If empty, then "was verified by organization "organization_name"" will be used as description. Can be specified only if the bot is allowed to provide custom description
    :type custom_description: :class:`String`
    """

    ID: typing.Literal["setMessageSenderBotVerification"] = field(
        default="setMessageSenderBotVerification", metadata={"alias": "@type"}
    )
    bot_user_id: Int53
    verified_id: MessageSender
    custom_description: String = field(default="")
