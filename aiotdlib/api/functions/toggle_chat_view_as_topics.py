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
class ToggleChatViewAsTopics(BaseObject):
    """
    Changes the view_as_topics setting of a forum chat or Saved Messages

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param view_as_topics: New value of view_as_topics
    :type view_as_topics: :class:`Bool`
    """

    ID: typing.Literal["toggleChatViewAsTopics"] = field(default="toggleChatViewAsTopics", metadata={"alias": "@type"})
    chat_id: Int53
    view_as_topics: Bool
