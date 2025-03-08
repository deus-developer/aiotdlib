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
class GetApplicationConfig(BaseObject):
    """
    Returns application config, provided by the server. Can be called before authorization
    """

    ID: typing.Literal["getApplicationConfig"] = field(default="getApplicationConfig", metadata={"alias": "@type"})
