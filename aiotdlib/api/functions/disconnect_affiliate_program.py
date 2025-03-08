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
class DisconnectAffiliateProgram(BaseObject):
    """
    Disconnects an affiliate program from the given affiliate and immediately deactivates its referral link. Returns updated information about the disconnected affiliate program

    :param affiliate: The affiliate to which the affiliate program is connected
    :type affiliate: :class:`AffiliateType`
    :param url: The referral link of the affiliate program
    :type url: :class:`String`
    """

    ID: typing.Literal["disconnectAffiliateProgram"] = field(
        default="disconnectAffiliateProgram", metadata={"alias": "@type"}
    )
    affiliate: AffiliateType
    url: String
