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
class GetCloseFriends(BaseObject):
    """
    Returns all close friends of the current user
    """

    ID: typing.Literal["getCloseFriends"] = field(default="getCloseFriends", metadata={"alias": "@type"})
