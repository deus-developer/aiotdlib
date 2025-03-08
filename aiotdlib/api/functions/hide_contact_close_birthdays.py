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
class HideContactCloseBirthdays(BaseObject):
    """
    Hides the list of contacts that have close birthdays for 24 hours
    """

    ID: typing.Literal["hideContactCloseBirthdays"] = field(
        default="hideContactCloseBirthdays", metadata={"alias": "@type"}
    )
