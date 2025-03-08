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
class GetBusinessConnectedBot(BaseObject):
    """
    Returns the business bot that is connected to the current user account. Returns a 404 error if there is no connected bot
    """

    ID: typing.Literal["getBusinessConnectedBot"] = field(
        default="getBusinessConnectedBot", metadata={"alias": "@type"}
    )
