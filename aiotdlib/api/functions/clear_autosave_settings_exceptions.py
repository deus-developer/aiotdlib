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
class ClearAutosaveSettingsExceptions(BaseObject):
    """
    Clears the list of all autosave settings exceptions. The method is guaranteed to work only after at least one call to getAutosaveSettings
    """

    ID: typing.Literal["clearAutosaveSettingsExceptions"] = field(
        default="clearAutosaveSettingsExceptions", metadata={"alias": "@type"}
    )
