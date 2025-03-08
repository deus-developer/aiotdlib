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
class GetMe(BaseObject):
    """
    Returns the current user
    """

    ID: typing.Literal["getMe"] = field(default="getMe", metadata={"alias": "@type"})
