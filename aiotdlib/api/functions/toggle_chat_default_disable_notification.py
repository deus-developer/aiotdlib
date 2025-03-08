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
class ToggleChatDefaultDisableNotification(BaseObject):
    """
    Changes the value of the default disable_notification parameter, used when a message is sent to a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param default_disable_notification: New value of default_disable_notification
    :type default_disable_notification: :class:`Bool`
    """

    ID: typing.Literal["toggleChatDefaultDisableNotification"] = field(
        default="toggleChatDefaultDisableNotification", metadata={"alias": "@type"}
    )
    chat_id: Int53
    default_disable_notification: Bool
