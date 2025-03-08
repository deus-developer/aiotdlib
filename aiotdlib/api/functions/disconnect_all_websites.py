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
class DisconnectAllWebsites(BaseObject):
    """
    Disconnects all websites from the current user's Telegram account
    """

    ID: typing.Literal["disconnectAllWebsites"] = field(default="disconnectAllWebsites", metadata={"alias": "@type"})
