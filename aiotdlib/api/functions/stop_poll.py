# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ReplyMarkup,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class StopPoll(BaseObject):
    """
    Stops a poll

    :param chat_id: Identifier of the chat to which the poll belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message containing the poll. Use messageProperties.can_be_edited to check whether the poll can be stopped
    :type message_id: :class:`Int53`
    :param reply_markup: The new message reply markup; pass null if none; for bots only, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["stopPoll"] = field(default="stopPoll", metadata={"alias": "@type"})
    chat_id: Int53
    message_id: Int53
    reply_markup: typing.Optional[ReplyMarkup] = field(default=None)
