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
class GetSavedOrderInfo(BaseObject):
    """
    Returns saved order information. Returns a 404 error if there is no saved order information
    """

    ID: typing.Literal["getSavedOrderInfo"] = field(default="getSavedOrderInfo", metadata={"alias": "@type"})
