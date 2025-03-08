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
class GetPasswordState(BaseObject):
    """
    Returns the current state of 2-step verification
    """

    ID: typing.Literal["getPasswordState"] = field(default="getPasswordState", metadata={"alias": "@type"})
