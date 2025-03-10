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
class SetSupergroupUnrestrictBoostCount(BaseObject):
    """
    Changes the number of times the supergroup must be boosted by a user to ignore slow mode and chat permission restrictions; requires can_restrict_members administrator right

    :param supergroup_id: Identifier of the supergroup
    :type supergroup_id: :class:`Int53`
    :param unrestrict_boost_count: New value of the unrestrict_boost_count supergroup setting; 0-8. Use 0 to remove the setting
    :type unrestrict_boost_count: :class:`Int32`
    """

    ID: typing.Literal["setSupergroupUnrestrictBoostCount"] = field(
        default="setSupergroupUnrestrictBoostCount", metadata={"alias": "@type"}
    )
    supergroup_id: Int53
    unrestrict_boost_count: Int32
