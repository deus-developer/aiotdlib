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
class GetLogStream(BaseObject):
    """
    Returns information about currently used log stream for internal logging of TDLib. Can be called synchronously
    """

    ID: typing.Literal["getLogStream"] = field(default="getLogStream", metadata={"alias": "@type"})
