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
class GetUserLink(BaseObject):
    """
    Returns an HTTPS link, which can be used to get information about the current user
    """

    ID: typing.Literal["getUserLink"] = field(default="getUserLink", metadata={"alias": "@type"})
