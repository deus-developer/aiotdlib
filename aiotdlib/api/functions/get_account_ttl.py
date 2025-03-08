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
class GetAccountTtl(BaseObject):
    """
    Returns the period of inactivity after which the account of the current user will automatically be deleted
    """

    ID: typing.Literal["getAccountTtl"] = field(default="getAccountTtl", metadata={"alias": "@type"})
