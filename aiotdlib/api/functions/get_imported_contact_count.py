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
class GetImportedContactCount(BaseObject):
    """
    Returns the total number of imported contacts
    """

    ID: typing.Literal["getImportedContactCount"] = field(
        default="getImportedContactCount", metadata={"alias": "@type"}
    )
