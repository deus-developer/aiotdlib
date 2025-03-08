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
class TestCallEmpty(BaseObject):
    """
    Does nothing; for testing only. This is an offline method. Can be called before authorization
    """

    ID: typing.Literal["testCallEmpty"] = field(default="testCallEmpty", metadata={"alias": "@type"})
