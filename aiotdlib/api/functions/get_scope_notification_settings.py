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
class GetScopeNotificationSettings(BaseObject):
    """
    Returns the notification settings for chats of a given type

    :param scope: Types of chats for which to return the notification settings information
    :type scope: :class:`NotificationSettingsScope`
    """

    ID: typing.Literal["getScopeNotificationSettings"] = field(
        default="getScopeNotificationSettings", metadata={"alias": "@type"}
    )
    scope: NotificationSettingsScope
