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
class GetCountries(BaseObject):
    """
    Returns information about existing countries. Can be called before authorization
    """

    ID: typing.Literal["getCountries"] = field(default="getCountries", metadata={"alias": "@type"})
