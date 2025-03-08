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
class GetStorageStatisticsFast(BaseObject):
    """
    Quickly returns approximate storage usage statistics. Can be called before authorization
    """

    ID: typing.Literal["getStorageStatisticsFast"] = field(
        default="getStorageStatisticsFast", metadata={"alias": "@type"}
    )
