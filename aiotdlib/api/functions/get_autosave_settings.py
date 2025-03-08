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
class GetAutosaveSettings(BaseObject):
    """
    Returns autosave settings for the current user
    """

    ID: typing.Literal["getAutosaveSettings"] = field(default="getAutosaveSettings", metadata={"alias": "@type"})
