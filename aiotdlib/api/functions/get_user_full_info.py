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
class GetUserFullInfo(BaseObject):
    """
    Returns full information about a user by their identifier

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["getUserFullInfo"] = field(default="getUserFullInfo", metadata={"alias": "@type"})
    user_id: Int53
