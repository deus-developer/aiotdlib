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
class GetReadDatePrivacySettings(BaseObject):
    """
    Returns privacy settings for message read date
    """

    ID: typing.Literal["getReadDatePrivacySettings"] = field(
        default="getReadDatePrivacySettings", metadata={"alias": "@type"}
    )
