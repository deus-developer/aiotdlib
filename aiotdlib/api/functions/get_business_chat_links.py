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
class GetBusinessChatLinks(BaseObject):
    """
    Returns business chat links created for the current account
    """

    ID: typing.Literal["getBusinessChatLinks"] = field(default="getBusinessChatLinks", metadata={"alias": "@type"})
