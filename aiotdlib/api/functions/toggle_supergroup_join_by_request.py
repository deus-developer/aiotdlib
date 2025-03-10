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
class ToggleSupergroupJoinByRequest(BaseObject):
    """
    Toggles whether all users directly joining the supergroup need to be approved by supergroup administrators; requires can_restrict_members administrator right

    :param supergroup_id: Identifier of the supergroup that isn't a broadcast group
    :type supergroup_id: :class:`Int53`
    :param join_by_request: New value of join_by_request
    :type join_by_request: :class:`Bool`
    """

    ID: typing.Literal["toggleSupergroupJoinByRequest"] = field(
        default="toggleSupergroupJoinByRequest", metadata={"alias": "@type"}
    )
    supergroup_id: Int53
    join_by_request: Bool
