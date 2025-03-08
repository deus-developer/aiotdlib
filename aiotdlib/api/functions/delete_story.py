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
class DeleteStory(BaseObject):
    """
    Deletes a previously sent story. Can be called only if story.can_be_deleted == true

    :param story_sender_chat_id: Identifier of the chat that posted the story
    :type story_sender_chat_id: :class:`Int53`
    :param story_id: Identifier of the story to delete
    :type story_id: :class:`Int32`
    """

    ID: typing.Literal["deleteStory"] = field(default="deleteStory", metadata={"alias": "@type"})
    story_sender_chat_id: Int53
    story_id: Int32
