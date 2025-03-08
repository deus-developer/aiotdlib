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
class ToggleSupergroupIsAllHistoryAvailable(BaseObject):
    """
    Toggles whether the message history of a supergroup is available to new members; requires can_change_info member right

    :param supergroup_id: The identifier of the supergroup
    :type supergroup_id: :class:`Int53`
    :param is_all_history_available: The new value of is_all_history_available
    :type is_all_history_available: :class:`Bool`
    """

    ID: typing.Literal["toggleSupergroupIsAllHistoryAvailable"] = field(
        default="toggleSupergroupIsAllHistoryAvailable", metadata={"alias": "@type"}
    )
    supergroup_id: Int53
    is_all_history_available: Bool
