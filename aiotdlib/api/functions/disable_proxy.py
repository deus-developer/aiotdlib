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
class DisableProxy(BaseObject):
    """
    Disables the currently enabled proxy. Can be called before authorization
    """

    ID: typing.Literal["disableProxy"] = field(default="disableProxy", metadata={"alias": "@type"})
