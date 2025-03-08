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
    ReplyMarkup,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class EditInlineMessageMedia(BaseObject):
    """
    Edits the media content of a message with a text, an animation, an audio, a document, a photo or a video in an inline message sent via a bot; for bots only

    :param inline_message_id: Inline message identifier
    :type inline_message_id: :class:`String`
    :param input_message_content: New content of the message. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo
    :type input_message_content: :class:`InputMessageContent`
    :param reply_markup: The new message reply markup; pass null if none; for bots only, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["editInlineMessageMedia"] = field(default="editInlineMessageMedia", metadata={"alias": "@type"})
    inline_message_id: String
    input_message_content: InputMessageContent
    reply_markup: typing.Optional[ReplyMarkup] = field(default=None)
