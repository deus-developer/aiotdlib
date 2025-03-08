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
class GetConnectedWebsites(BaseObject):
    """
    Returns all website where the current user used Telegram to log in
    """

    ID: typing.Literal["getConnectedWebsites"] = field(default="getConnectedWebsites", metadata={"alias": "@type"})
