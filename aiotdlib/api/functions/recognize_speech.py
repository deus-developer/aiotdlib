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
class RecognizeSpeech(BaseObject):
    """
    Recognizes speech in a video note or a voice note message

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message. Use messageProperties.can_recognize_speech to check whether the message is suitable
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["recognizeSpeech"] = field(default="recognizeSpeech", metadata={"alias": "@type"})
    chat_id: Int53
    message_id: Int53
