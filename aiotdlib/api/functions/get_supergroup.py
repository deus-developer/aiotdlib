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
class GetSupergroup(BaseObject):
    """
    Returns information about a supergroup or a channel by its identifier. This is an offline request if the current user is not a bot

    :param supergroup_id: Supergroup or channel identifier
    :type supergroup_id: :class:`Int53`
    """

    ID: typing.Literal["getSupergroup"] = field(default="getSupergroup", metadata={"alias": "@type"})
    supergroup_id: Int53
