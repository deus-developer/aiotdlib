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
class ToggleSupergroupCanHaveSponsoredMessages(BaseObject):
    """
    Toggles whether sponsored messages are shown in the channel chat; requires owner privileges in the channel. The chat must have at least chatBoostFeatures.min_sponsored_message_disable_boost_level boost level to disable sponsored messages

    :param supergroup_id: The identifier of the channel
    :type supergroup_id: :class:`Int53`
    :param can_have_sponsored_messages: The new value of can_have_sponsored_messages
    :type can_have_sponsored_messages: :class:`Bool`
    """

    ID: typing.Literal["toggleSupergroupCanHaveSponsoredMessages"] = field(
        default="toggleSupergroupCanHaveSponsoredMessages", metadata={"alias": "@type"}
    )
    supergroup_id: Int53
    can_have_sponsored_messages: Bool
