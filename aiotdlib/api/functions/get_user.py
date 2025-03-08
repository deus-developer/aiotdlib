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
class GetUser(BaseObject):
    """
    Returns information about a user by their identifier. This is an offline request if the current user is not a bot

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["getUser"] = field(default="getUser", metadata={"alias": "@type"})
    user_id: Int53
