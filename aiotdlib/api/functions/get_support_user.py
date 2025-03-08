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
class GetSupportUser(BaseObject):
    """
    Returns a user that can be contacted to get support
    """

    ID: typing.Literal["getSupportUser"] = field(default="getSupportUser", metadata={"alias": "@type"})
