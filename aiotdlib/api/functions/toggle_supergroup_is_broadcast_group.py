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
class ToggleSupergroupIsBroadcastGroup(BaseObject):
    """
    Upgrades supergroup to a broadcast group; requires owner privileges in the supergroup

    :param supergroup_id: Identifier of the supergroup
    :type supergroup_id: :class:`Int53`
    """

    ID: typing.Literal["toggleSupergroupIsBroadcastGroup"] = field(
        default="toggleSupergroupIsBroadcastGroup", metadata={"alias": "@type"}
    )
    supergroup_id: Int53
