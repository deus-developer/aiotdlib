# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import MISSING, dataclass, field

from ..types.all import (
    CollectibleItemType,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetCollectibleItemInfo(BaseObject):
    """
    Returns information about a given collectible item that was purchased at https://fragment.com

    :param type_: Type of the collectible item. The item must be used by a user and must be visible to the current user
    :type type_: :class:`CollectibleItemType`
    """

    ID: typing.Literal["getCollectibleItemInfo"] = field(default="getCollectibleItemInfo", metadata={"alias": "@type"})
    type_: CollectibleItemType = field(default=MISSING, metadata={"alias": "type"})
