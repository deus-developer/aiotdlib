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
class ToggleStoryIsPostedToChatPage(BaseObject):
    """
    Toggles whether a story is accessible after expiration. Can be called only if story.can_toggle_is_posted_to_chat_page == true

    :param story_sender_chat_id: Identifier of the chat that posted the story
    :type story_sender_chat_id: :class:`Int53`
    :param story_id: Identifier of the story
    :type story_id: :class:`Int32`
    :param is_posted_to_chat_page: Pass true to make the story accessible after expiration; pass false to make it private
    :type is_posted_to_chat_page: :class:`Bool`
    """

    ID: typing.Literal["toggleStoryIsPostedToChatPage"] = field(
        default="toggleStoryIsPostedToChatPage", metadata={"alias": "@type"}
    )
    story_sender_chat_id: Int53
    story_id: Int32
    is_posted_to_chat_page: Bool = field(default=False)
