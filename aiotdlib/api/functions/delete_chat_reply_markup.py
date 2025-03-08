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
class DeleteChatReplyMarkup(BaseObject):
    """
    Deletes the default reply markup from a chat. Must be called after a one-time keyboard or a replyMarkupForceReply reply markup has been used. An updateChatReplyMarkup update will be sent if the reply markup is changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_id: The message identifier of the used keyboard
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["deleteChatReplyMarkup"] = field(default="deleteChatReplyMarkup", metadata={"alias": "@type"})
    chat_id: Int53
    message_id: Int53
