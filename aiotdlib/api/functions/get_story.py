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
class GetStory(BaseObject):
    """
    Returns a story

    :param story_sender_chat_id: Identifier of the chat that posted the story
    :type story_sender_chat_id: :class:`Int53`
    :param story_id: Story identifier
    :type story_id: :class:`Int32`
    :param only_local: Pass true to get only locally available information without sending network requests
    :type only_local: :class:`Bool`
    """

    ID: typing.Literal["getStory"] = field(default="getStory", metadata={"alias": "@type"})
    story_sender_chat_id: Int53
    story_id: Int32
    only_local: Bool = field(default=False)
