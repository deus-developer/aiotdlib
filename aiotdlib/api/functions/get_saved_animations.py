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
class GetSavedAnimations(BaseObject):
    """
    Returns saved animations
    """

    ID: typing.Literal["getSavedAnimations"] = field(default="getSavedAnimations", metadata={"alias": "@type"})
