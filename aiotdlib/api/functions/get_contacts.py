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
class GetContacts(BaseObject):
    """
    Returns all contacts of the user
    """

    ID: typing.Literal["getContacts"] = field(default="getContacts", metadata={"alias": "@type"})
