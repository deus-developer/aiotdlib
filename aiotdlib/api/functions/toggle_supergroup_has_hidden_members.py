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
class ToggleSupergroupHasHiddenMembers(BaseObject):
    """
    Toggles whether non-administrators can receive only administrators and bots using getSupergroupMembers or searchChatMembers. Can be called only if supergroupFullInfo.can_hide_members == true

    :param supergroup_id: Identifier of the supergroup
    :type supergroup_id: :class:`Int53`
    :param has_hidden_members: New value of has_hidden_members
    :type has_hidden_members: :class:`Bool`
    """

    ID: typing.Literal["toggleSupergroupHasHiddenMembers"] = field(
        default="toggleSupergroupHasHiddenMembers", metadata={"alias": "@type"}
    )
    supergroup_id: Int53
    has_hidden_members: Bool
