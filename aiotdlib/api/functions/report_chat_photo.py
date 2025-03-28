# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ReportReason,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class ReportChatPhoto(BaseObject):
    """
    Reports a chat photo to the Telegram moderators. A chat photo can be reported only if chat.can_be_reported

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param file_id: Identifier of the photo to report. Only full photos from chatPhoto can be reported
    :type file_id: :class:`Int32`
    :param reason: The reason for reporting the chat photo
    :type reason: :class:`ReportReason`
    :param text: Additional report details; 0-1024 characters
    :type text: :class:`String`
    """

    ID: typing.Literal["reportChatPhoto"] = field(default="reportChatPhoto", metadata={"alias": "@type"})
    chat_id: Int53
    file_id: Int32
    reason: ReportReason
    text: String = field(default="", metadata={"max_length": 1024})
