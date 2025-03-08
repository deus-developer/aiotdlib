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
class SetSupergroupUsername(BaseObject):
    """
    Changes the editable username of a supergroup or channel, requires owner privileges in the supergroup or channel

    :param supergroup_id: Identifier of the supergroup or channel
    :type supergroup_id: :class:`Int53`
    :param username: New value of the username. Use an empty string to remove the username. The username can't be completely removed if there is another active or disabled username
    :type username: :class:`String`
    """

    ID: typing.Literal["setSupergroupUsername"] = field(default="setSupergroupUsername", metadata={"alias": "@type"})
    supergroup_id: Int53
    username: String
