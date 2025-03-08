# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    BusinessAwayMessageSettings,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetBusinessAwayMessageSettings(BaseObject):
    """
    Changes the business away message settings of the current user. Requires Telegram Business subscription

    :param away_message_settings: The new settings for the away message of the business; pass null to disable the away message, defaults to None
    :type away_message_settings: :class:`BusinessAwayMessageSettings`, optional
    """

    ID: typing.Literal["setBusinessAwayMessageSettings"] = field(
        default="setBusinessAwayMessageSettings", metadata={"alias": "@type"}
    )
    away_message_settings: typing.Optional[BusinessAwayMessageSettings] = field(default=None)
