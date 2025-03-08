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
class RateSpeechRecognition(BaseObject):
    """
    Rates recognized speech in a video note or a voice note message

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param is_good: Pass true if the speech recognition is good
    :type is_good: :class:`Bool`
    """

    ID: typing.Literal["rateSpeechRecognition"] = field(default="rateSpeechRecognition", metadata={"alias": "@type"})
    chat_id: Int53
    message_id: Int53
    is_good: Bool = field(default=False)
