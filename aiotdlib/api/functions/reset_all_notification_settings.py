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
class ResetAllNotificationSettings(BaseObject):
    """
    Resets all chat and scope notification settings to their default values. By default, all chats are unmuted and message previews are shown
    """

    ID: typing.Literal["resetAllNotificationSettings"] = field(
        default="resetAllNotificationSettings", metadata={"alias": "@type"}
    )
