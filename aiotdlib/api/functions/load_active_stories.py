# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    StoryList,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class LoadActiveStories(BaseObject):
    """
    Loads more active stories from a story list. The loaded stories will be sent through updates. Active stories are sorted by the pair (active_stories.order, active_stories.story_sender_chat_id) in descending order. Returns a 404 error if all active stories have been loaded

    :param story_list: The story list in which to load active stories
    :type story_list: :class:`StoryList`
    """

    ID: typing.Literal["loadActiveStories"] = field(default="loadActiveStories", metadata={"alias": "@type"})
    story_list: StoryList
