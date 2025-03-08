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
class TestGetDifference(BaseObject):
    """
    Forces an updates.getDifference call to the Telegram servers; for testing only
    """

    ID: typing.Literal["testGetDifference"] = field(default="testGetDifference", metadata={"alias": "@type"})
