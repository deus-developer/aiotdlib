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
class ReportStory(BaseObject):
    """
    Reports a story to the Telegram moderators

    :param story_sender_chat_id: The identifier of the sender of the story to report
    :type story_sender_chat_id: :class:`Int53`
    :param story_id: The identifier of the story to report
    :type story_id: :class:`Int32`
    :param option_id: Option identifier chosen by the user; leave empty for the initial request
    :type option_id: :class:`Bytes`
    :param text: Additional report details; 0-1024 characters; leave empty for the initial request
    :type text: :class:`String`
    """

    ID: typing.Literal["reportStory"] = field(default="reportStory", metadata={"alias": "@type"})
    story_sender_chat_id: Int53
    story_id: Int32
    option_id: Bytes
    text: String = field(default="", metadata={"max_length": 1024})
