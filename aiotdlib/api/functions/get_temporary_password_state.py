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
class GetTemporaryPasswordState(BaseObject):
    """
    Returns information about the current temporary password
    """

    ID: typing.Literal["getTemporaryPasswordState"] = field(
        default="getTemporaryPasswordState", metadata={"alias": "@type"}
    )
