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
class GetLogVerbosityLevel(BaseObject):
    """
    Returns current verbosity level of the internal logging of TDLib. Can be called synchronously
    """

    ID: typing.Literal["getLogVerbosityLevel"] = field(default="getLogVerbosityLevel", metadata={"alias": "@type"})
