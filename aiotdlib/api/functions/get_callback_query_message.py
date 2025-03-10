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
class GetCallbackQueryMessage(BaseObject):
    """
    Returns information about a message with the callback button that originated a callback query; for bots only

    :param chat_id: Identifier of the chat the message belongs to
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    :param callback_query_id: Identifier of the callback query
    :type callback_query_id: :class:`Int64`
    """

    ID: typing.Literal["getCallbackQueryMessage"] = field(
        default="getCallbackQueryMessage", metadata={"alias": "@type"}
    )
    chat_id: Int53
    message_id: Int53
    callback_query_id: Int64
