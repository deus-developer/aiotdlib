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
class ClickAnimatedEmojiMessage(BaseObject):
    """
    Informs TDLib that a message with an animated emoji was clicked by the user. Returns a big animated sticker to be played or a 404 error if usual animation needs to be played

    :param chat_id: Chat identifier of the message
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the clicked message
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["clickAnimatedEmojiMessage"] = field(
        default="clickAnimatedEmojiMessage", metadata={"alias": "@type"}
    )
    chat_id: Int53
    message_id: Int53
