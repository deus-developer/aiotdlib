# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ReadDatePrivacySettings,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetReadDatePrivacySettings(BaseObject):
    """
    Changes privacy settings for message read date

    :param settings: New settings
    :type settings: :class:`ReadDatePrivacySettings`
    """

    ID: typing.Literal["setReadDatePrivacySettings"] = field(
        default="setReadDatePrivacySettings", metadata={"alias": "@type"}
    )
    settings: ReadDatePrivacySettings
