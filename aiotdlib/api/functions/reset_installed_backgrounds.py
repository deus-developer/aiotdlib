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
class ResetInstalledBackgrounds(BaseObject):
    """
    Resets list of installed backgrounds to its default value
    """

    ID: typing.Literal["resetInstalledBackgrounds"] = field(
        default="resetInstalledBackgrounds", metadata={"alias": "@type"}
    )
