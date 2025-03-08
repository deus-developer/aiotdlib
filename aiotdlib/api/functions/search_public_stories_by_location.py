# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    LocationAddress,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SearchPublicStoriesByLocation(BaseObject):
    """
    Searches for public stories by the given address location. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit

    :param address: Address of the location
    :type address: :class:`LocationAddress`
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of stories to be returned; up to 100. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["searchPublicStoriesByLocation"] = field(
        default="searchPublicStoriesByLocation", metadata={"alias": "@type"}
    )
    address: LocationAddress
    offset: String
    limit: Int32
