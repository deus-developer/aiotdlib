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
class SetBotUpdatesStatus(BaseObject):
    """
    Informs the server about the number of pending bot updates if they haven't been processed for a long time; for bots only

    :param pending_update_count: The number of pending updates
    :type pending_update_count: :class:`Int32`
    :param error_message: The last error message
    :type error_message: :class:`String`
    """

    ID: typing.Literal["setBotUpdatesStatus"] = field(default="setBotUpdatesStatus", metadata={"alias": "@type"})
    pending_update_count: Int32
    error_message: String
