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
class StopBusinessPoll(BaseObject):
    """
    Stops a poll sent on behalf of a business account; for bots only

    :param business_connection_id: Unique identifier of business connection on behalf of which the message with the poll was sent
    :type business_connection_id: :class:`String`
    :param chat_id: The chat the message belongs to
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message containing the poll
    :type message_id: :class:`Int53`
    :param reply_markup: The new message reply markup; pass null if none, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["stopBusinessPoll"] = field(default="stopBusinessPoll", metadata={"alias": "@type"})
    business_connection_id: String
    chat_id: Int53
    message_id: Int53
    reply_markup: typing.Optional[ReplyMarkup] = field(default=None)
