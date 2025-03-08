# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ReactionNotificationSettings,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetReactionNotificationSettings(BaseObject):
    """
    Changes notification settings for reactions

    :param notification_settings: The new notification settings for reactions
    :type notification_settings: :class:`ReactionNotificationSettings`
    """

    ID: typing.Literal["setReactionNotificationSettings"] = field(
        default="setReactionNotificationSettings", metadata={"alias": "@type"}
    )
    notification_settings: ReactionNotificationSettings
