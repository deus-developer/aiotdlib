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
    ScopeNotificationSettings,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetScopeNotificationSettings(BaseObject):
    """
    Changes notification settings for chats of a given type

    :param scope: Types of chats for which to change the notification settings
    :type scope: :class:`NotificationSettingsScope`
    :param notification_settings: The new notification settings for the given scope
    :type notification_settings: :class:`ScopeNotificationSettings`
    """

    ID: typing.Literal["setScopeNotificationSettings"] = field(
        default="setScopeNotificationSettings", metadata={"alias": "@type"}
    )
    scope: NotificationSettingsScope
    notification_settings: ScopeNotificationSettings
