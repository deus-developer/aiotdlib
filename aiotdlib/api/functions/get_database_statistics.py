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
class GetDatabaseStatistics(BaseObject):
    """
    Returns database statistics
    """

    ID: typing.Literal["getDatabaseStatistics"] = field(default="getDatabaseStatistics", metadata={"alias": "@type"})
