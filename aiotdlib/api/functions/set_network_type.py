# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    NetworkType,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetNetworkType(BaseObject):
    """
    Sets the current network type. Can be called before authorization. Calling this method forces all network connections to reopen, mitigating the delay in switching between different networks, so it must be called whenever the network is changed, even if the network type remains the same. Network type is used to check whether the library can use the network at all and also for collecting detailed network data usage statistics

    :param type_: The new network type; pass null to set network type to networkTypeOther, defaults to None
    :type type_: :class:`NetworkType`, optional
    """

    ID: typing.Literal["setNetworkType"] = field(default="setNetworkType", metadata={"alias": "@type"})
    type_: typing.Optional[NetworkType] = field(default=None, metadata={"alias": "type"})
