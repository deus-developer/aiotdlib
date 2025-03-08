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
class EditMessageReplyMarkup(BaseObject):
    """
    Edits the message reply markup; for bots only. Returns the edited message after the edit is completed on the server side

    :param chat_id: The chat the message belongs to
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message. Use messageProperties.can_be_edited to check whether the message can be edited
    :type message_id: :class:`Int53`
    :param reply_markup: The new message reply markup; pass null if none, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["editMessageReplyMarkup"] = field(default="editMessageReplyMarkup", metadata={"alias": "@type"})
    chat_id: Int53
    message_id: Int53
    reply_markup: typing.Optional[ReplyMarkup] = field(default=None)
