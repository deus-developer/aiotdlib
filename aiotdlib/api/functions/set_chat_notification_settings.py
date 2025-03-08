# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ChatNotificationSettings,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetChatNotificationSettings(BaseObject):
    """
    Changes the notification settings of a chat. Notification settings of a chat with the current user (Saved Messages) can't be changed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param notification_settings: New notification settings for the chat. If the chat is muted for more than 366 days, it is considered to be muted forever
    :type notification_settings: :class:`ChatNotificationSettings`
    """

    ID: typing.Literal["setChatNotificationSettings"] = field(
        default="setChatNotificationSettings", metadata={"alias": "@type"}
    )
    chat_id: Int53
    notification_settings: ChatNotificationSettings
