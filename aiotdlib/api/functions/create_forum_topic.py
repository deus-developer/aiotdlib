# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import MISSING, dataclass, field

from ..types.all import (
    ForumTopicIcon,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class CreateForumTopic(BaseObject):
    """
    Creates a topic in a forum supergroup chat; requires can_manage_topics administrator or can_create_topics member right in the supergroup

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param name: Name of the topic; 1-128 characters
    :type name: :class:`String`
    :param icon: Icon of the topic. Icon color must be one of 0x6FB9F0, 0xFFD67E, 0xCB86DB, 0x8EEE98, 0xFF93B2, or 0xFB6F5F. Telegram Premium users can use any custom emoji as topic icon, other users can use only a custom emoji returned by getForumTopicDefaultIcons
    :type icon: :class:`ForumTopicIcon`
    """

    ID: typing.Literal["createForumTopic"] = field(default="createForumTopic", metadata={"alias": "@type"})
    chat_id: Int53
    name: String = field(default=MISSING, metadata={"min_length": 1, "max_length": 128})
    icon: ForumTopicIcon
