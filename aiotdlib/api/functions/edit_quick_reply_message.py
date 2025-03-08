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
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class EditQuickReplyMessage(BaseObject):
    """
    Asynchronously edits the text, media or caption of a quick reply message. Use quickReplyMessage.can_be_edited to check whether a message can be edited. Media message can be edited only to a media message. The type of message content in an album can't be changed with exception of replacing a photo with a video or vice versa

    :param shortcut_id: Unique identifier of the quick reply shortcut with the message
    :type shortcut_id: :class:`Int32`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param input_message_content: New content of the message. Must be one of the following types: inputMessageText, inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo
    :type input_message_content: :class:`InputMessageContent`
    """

    ID: typing.Literal["editQuickReplyMessage"] = field(default="editQuickReplyMessage", metadata={"alias": "@type"})
    shortcut_id: Int32
    message_id: Int53
    input_message_content: InputMessageContent
