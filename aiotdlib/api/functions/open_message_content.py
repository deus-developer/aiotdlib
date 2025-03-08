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
class OpenMessageContent(BaseObject):
    """
    Informs TDLib that the message content has been opened (e.g., the user has opened a photo, video, document, location or venue, or has listened to an audio file or voice note message). An updateMessageContentOpened update will be generated if something has changed

    :param chat_id: Chat identifier of the message
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message with the opened content
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["openMessageContent"] = field(default="openMessageContent", metadata={"alias": "@type"})
    chat_id: Int53
    message_id: Int53
