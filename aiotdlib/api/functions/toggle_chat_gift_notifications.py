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
class ToggleChatGiftNotifications(BaseObject):
    """
    Toggles whether notifications for new gifts received by a channel chat are sent to the current user; requires can_post_messages administrator right in the chat

    :param chat_id: Identifier of the channel chat
    :type chat_id: :class:`Int53`
    :param are_enabled: Pass true to enable notifications about new gifts owned by the channel chat; pass false to disable the notifications
    :type are_enabled: :class:`Bool`
    """

    ID: typing.Literal["toggleChatGiftNotifications"] = field(
        default="toggleChatGiftNotifications", metadata={"alias": "@type"}
    )
    chat_id: Int53
    are_enabled: Bool = field(default=False)
