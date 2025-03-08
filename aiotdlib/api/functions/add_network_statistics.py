# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    NetworkStatisticsEntry,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class AddNetworkStatistics(BaseObject):
    """
    Adds the specified data to data usage statistics. Can be called before authorization

    :param entry: The network statistics entry with the data to be added to statistics
    :type entry: :class:`NetworkStatisticsEntry`
    """

    ID: typing.Literal["addNetworkStatistics"] = field(default="addNetworkStatistics", metadata={"alias": "@type"})
    entry: NetworkStatisticsEntry
