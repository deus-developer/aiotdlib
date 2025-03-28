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
class CloseStory(BaseObject):
    """
    Informs TDLib that a story is closed by the user

    :param story_sender_chat_id: The identifier of the sender of the story to close
    :type story_sender_chat_id: :class:`Int53`
    :param story_id: The identifier of the story
    :type story_id: :class:`Int32`
    """

    ID: typing.Literal["closeStory"] = field(default="closeStory", metadata={"alias": "@type"})
    story_sender_chat_id: Int53
    story_id: Int32
