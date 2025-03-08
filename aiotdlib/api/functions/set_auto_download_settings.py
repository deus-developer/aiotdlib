# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import MISSING, dataclass, field

from ..types.all import (
    AutoDownloadSettings,
    NetworkType,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetAutoDownloadSettings(BaseObject):
    """
    Sets auto-download settings

    :param settings: New user auto-download settings
    :type settings: :class:`AutoDownloadSettings`
    :param type_: Type of the network for which the new settings are relevant
    :type type_: :class:`NetworkType`
    """

    ID: typing.Literal["setAutoDownloadSettings"] = field(
        default="setAutoDownloadSettings", metadata={"alias": "@type"}
    )
    settings: AutoDownloadSettings
    type_: NetworkType = field(default=MISSING, metadata={"alias": "type"})
