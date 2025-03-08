# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    BusinessGreetingMessageSettings,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetBusinessGreetingMessageSettings(BaseObject):
    """
    Changes the business greeting message settings of the current user. Requires Telegram Business subscription

    :param greeting_message_settings: The new settings for the greeting message of the business; pass null to disable the greeting message, defaults to None
    :type greeting_message_settings: :class:`BusinessGreetingMessageSettings`, optional
    """

    ID: typing.Literal["setBusinessGreetingMessageSettings"] = field(
        default="setBusinessGreetingMessageSettings", metadata={"alias": "@type"}
    )
    greeting_message_settings: typing.Optional[BusinessGreetingMessageSettings] = field(default=None)
