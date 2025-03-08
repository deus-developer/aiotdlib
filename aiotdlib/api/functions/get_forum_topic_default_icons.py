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
class GetForumTopicDefaultIcons(BaseObject):
    """
    Returns the list of custom emoji, which can be used as forum topic icon by all users
    """

    ID: typing.Literal["getForumTopicDefaultIcons"] = field(
        default="getForumTopicDefaultIcons", metadata={"alias": "@type"}
    )
