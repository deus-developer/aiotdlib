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
class DisableAllSupergroupUsernames(BaseObject):
    """
    Disables all active non-editable usernames of a supergroup or channel, requires owner privileges in the supergroup or channel

    :param supergroup_id: Identifier of the supergroup or channel
    :type supergroup_id: :class:`Int53`
    """

    ID: typing.Literal["disableAllSupergroupUsernames"] = field(
        default="disableAllSupergroupUsernames", metadata={"alias": "@type"}
    )
    supergroup_id: Int53
