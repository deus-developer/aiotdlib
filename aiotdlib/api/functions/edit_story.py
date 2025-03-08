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
    InputStoryAreas,
    InputStoryContent,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class EditStory(BaseObject):
    """
    Changes content and caption of a story. Can be called only if story.can_be_edited == true

    :param story_sender_chat_id: Identifier of the chat that posted the story
    :type story_sender_chat_id: :class:`Int53`
    :param story_id: Identifier of the story to edit
    :type story_id: :class:`Int32`
    :param content: New content of the story; pass null to keep the current content, defaults to None
    :type content: :class:`InputStoryContent`, optional
    :param areas: New clickable rectangle areas to be shown on the story media; pass null to keep the current areas. Areas can't be edited if story content isn't changed, defaults to None
    :type areas: :class:`InputStoryAreas`, optional
    :param caption: New story caption; pass null to keep the current caption, defaults to None
    :type caption: :class:`FormattedText`, optional
    """

    ID: typing.Literal["editStory"] = field(default="editStory", metadata={"alias": "@type"})
    story_sender_chat_id: Int53
    story_id: Int32
    content: typing.Optional[InputStoryContent] = field(default=None)
    areas: typing.Optional[InputStoryAreas] = field(default=None)
    caption: typing.Optional[FormattedText] = field(default=None)
