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
class GetRecentlyVisitedTMeUrls(BaseObject):
    """
    Returns t.me URLs recently visited by a newly registered user

    :param referrer: Google Play referrer to identify the user
    :type referrer: :class:`String`
    """

    ID: typing.Literal["getRecentlyVisitedTMeUrls"] = field(
        default="getRecentlyVisitedTMeUrls", metadata={"alias": "@type"}
    )
    referrer: String
