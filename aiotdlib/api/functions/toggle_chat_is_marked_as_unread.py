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
class ToggleChatIsMarkedAsUnread(BaseObject):
    """
    Changes the marked as unread state of a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param is_marked_as_unread: New value of is_marked_as_unread
    :type is_marked_as_unread: :class:`Bool`
    """

    ID: typing.Literal["toggleChatIsMarkedAsUnread"] = field(
        default="toggleChatIsMarkedAsUnread", metadata={"alias": "@type"}
    )
    chat_id: Int53
    is_marked_as_unread: Bool
