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
class ReorderActiveUsernames(BaseObject):
    """
    Changes order of active usernames of the current user

    :param usernames: The new order of active usernames. All currently active usernames must be specified
    :type usernames: :class:`Vector[String]`
    """

    ID: typing.Literal["reorderActiveUsernames"] = field(default="reorderActiveUsernames", metadata={"alias": "@type"})
    usernames: Vector[String]
