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
class GetProxies(BaseObject):
    """
    Returns the list of proxies that are currently set up. Can be called before authorization
    """

    ID: typing.Literal["getProxies"] = field(default="getProxies", metadata={"alias": "@type"})
