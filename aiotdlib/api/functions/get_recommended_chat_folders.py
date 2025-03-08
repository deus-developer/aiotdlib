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
class GetRecommendedChatFolders(BaseObject):
    """
    Returns recommended chat folders for the current user
    """

    ID: typing.Literal["getRecommendedChatFolders"] = field(
        default="getRecommendedChatFolders", metadata={"alias": "@type"}
    )
