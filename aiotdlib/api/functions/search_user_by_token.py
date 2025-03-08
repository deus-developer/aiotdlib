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
class SearchUserByToken(BaseObject):
    """
    Searches a user by a token from the user's link

    :param token: Token to search for
    :type token: :class:`String`
    """

    ID: typing.Literal["searchUserByToken"] = field(default="searchUserByToken", metadata={"alias": "@type"})
    token: String
