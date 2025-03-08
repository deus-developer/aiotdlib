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
class GetGrossingWebAppBots(BaseObject):
    """
    Returns the most grossing Web App bots

    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of bots to be returned; up to 100
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getGrossingWebAppBots"] = field(default="getGrossingWebAppBots", metadata={"alias": "@type"})
    offset: String
    limit: Int32
