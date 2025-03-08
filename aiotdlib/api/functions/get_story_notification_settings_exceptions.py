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
class GetStoryNotificationSettingsExceptions(BaseObject):
    """
    Returns the list of chats with non-default notification settings for stories
    """

    ID: typing.Literal["getStoryNotificationSettingsExceptions"] = field(
        default="getStoryNotificationSettingsExceptions", metadata={"alias": "@type"}
    )
