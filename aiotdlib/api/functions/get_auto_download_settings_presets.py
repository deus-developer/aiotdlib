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
class GetAutoDownloadSettingsPresets(BaseObject):
    """
    Returns auto-download settings presets for the current user
    """

    ID: typing.Literal["getAutoDownloadSettingsPresets"] = field(
        default="getAutoDownloadSettingsPresets", metadata={"alias": "@type"}
    )
