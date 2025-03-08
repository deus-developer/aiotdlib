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
class TestNetwork(BaseObject):
    """
    Sends a simple network request to the Telegram servers; for testing only. Can be called before authorization
    """

    ID: typing.Literal["testNetwork"] = field(default="testNetwork", metadata={"alias": "@type"})
