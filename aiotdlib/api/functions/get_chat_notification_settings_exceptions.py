# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    NotificationSettingsScope,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetChatNotificationSettingsExceptions(BaseObject):
    """
    Returns the list of chats with non-default notification settings for new messages

    :param compare_sound: Pass true to include in the response chats with only non-default sound
    :type compare_sound: :class:`Bool`
    :param scope: If specified, only chats from the scope will be returned; pass null to return chats from all scopes, defaults to None
    :type scope: :class:`NotificationSettingsScope`, optional
    """

    ID: typing.Literal["getChatNotificationSettingsExceptions"] = field(
        default="getChatNotificationSettingsExceptions", metadata={"alias": "@type"}
    )
    compare_sound: Bool = field(default=False)
    scope: typing.Optional[NotificationSettingsScope] = field(default=None)
