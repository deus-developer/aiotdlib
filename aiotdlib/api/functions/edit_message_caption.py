# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    FormattedText,
    ReplyMarkup,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class EditMessageCaption(BaseObject):
    """
    Edits the message content caption. Returns the edited message after the edit is completed on the server side

    :param chat_id: The chat the message belongs to
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message. Use messageProperties.can_be_edited to check whether the message can be edited
    :type message_id: :class:`Int53`
    :param show_caption_above_media: Pass true to show the caption above the media; otherwise, the caption will be shown below the media. May be true only for animation, photo, and video messages
    :type show_caption_above_media: :class:`Bool`
    :param reply_markup: The new message reply markup; pass null if none; for bots only, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    :param caption: New message content caption; 0-getOption("message_caption_length_max") characters; pass null to remove caption, defaults to None
    :type caption: :class:`FormattedText`, optional
    """

    ID: typing.Literal["editMessageCaption"] = field(default="editMessageCaption", metadata={"alias": "@type"})
    chat_id: Int53
    message_id: Int53
    show_caption_above_media: Bool = field(default=False)
    reply_markup: typing.Optional[ReplyMarkup] = field(default=None)
    caption: typing.Optional[FormattedText] = field(default=None)
