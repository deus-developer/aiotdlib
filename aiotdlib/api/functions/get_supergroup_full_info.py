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
class GetSupergroupFullInfo(BaseObject):
    """
    Returns full information about a supergroup or a channel by its identifier, cached for up to 1 minute

    :param supergroup_id: Supergroup or channel identifier
    :type supergroup_id: :class:`Int53`
    """

    ID: typing.Literal["getSupergroupFullInfo"] = field(default="getSupergroupFullInfo", metadata={"alias": "@type"})
    supergroup_id: Int53
