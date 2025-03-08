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
class GetSavedNotificationSounds(BaseObject):
    """
    Returns the list of saved notification sounds. If a sound isn't in the list, then default sound needs to be used
    """

    ID: typing.Literal["getSavedNotificationSounds"] = field(
        default="getSavedNotificationSounds", metadata={"alias": "@type"}
    )
