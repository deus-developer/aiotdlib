# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    AffiliateType,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetConnectedAffiliateProgram(BaseObject):
    """
    Returns an affiliate program that were connected to the given affiliate by identifier of the bot that created the program

    :param affiliate: The affiliate to which the affiliate program will be connected
    :type affiliate: :class:`AffiliateType`
    :param bot_user_id: Identifier of the bot that created the program
    :type bot_user_id: :class:`Int53`
    """

    ID: typing.Literal["getConnectedAffiliateProgram"] = field(
        default="getConnectedAffiliateProgram", metadata={"alias": "@type"}
    )
    affiliate: AffiliateType
    bot_user_id: Int53
