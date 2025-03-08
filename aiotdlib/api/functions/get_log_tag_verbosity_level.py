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
class GetLogTagVerbosityLevel(BaseObject):
    """
    Returns current verbosity level for a specified TDLib internal log tag. Can be called synchronously

    :param tag: Logging tag to change verbosity level
    :type tag: :class:`String`
    """

    ID: typing.Literal["getLogTagVerbosityLevel"] = field(
        default="getLogTagVerbosityLevel", metadata={"alias": "@type"}
    )
    tag: String
