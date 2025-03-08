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
class GetNewChatPrivacySettings(BaseObject):
    """
    Returns privacy settings for new chat creation
    """

    ID: typing.Literal["getNewChatPrivacySettings"] = field(
        default="getNewChatPrivacySettings", metadata={"alias": "@type"}
    )
