# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    InputMessageContent,
    InputMessageReplyTo,
    MessageSender,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class AddLocalMessage(BaseObject):
    """
    Adds a local message to a chat. The message is persistent across application restarts only if the message database is used. Returns the added message

    :param chat_id: Target chat
    :type chat_id: :class:`Int53`
    :param sender_id: Identifier of the sender of the message
    :type sender_id: :class:`MessageSender`
    :param input_message_content: The content of the message to be added
    :type input_message_content: :class:`InputMessageContent`
    :param disable_notification: Pass true to disable notification for the message
    :type disable_notification: :class:`Bool`
    :param reply_to: Information about the message or story to be replied; pass null if none, defaults to None
    :type reply_to: :class:`InputMessageReplyTo`, optional
    """

    ID: typing.Literal["addLocalMessage"] = field(default="addLocalMessage", metadata={"alias": "@type"})
    chat_id: Int53
    sender_id: MessageSender
    input_message_content: InputMessageContent
    disable_notification: Bool = field(default=False)
    reply_to: typing.Optional[InputMessageReplyTo] = field(default=None)
