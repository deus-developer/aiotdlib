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
class DeleteSavedCredentials(BaseObject):
    """
    Deletes saved credentials for all payment provider bots
    """

    ID: typing.Literal["deleteSavedCredentials"] = field(default="deleteSavedCredentials", metadata={"alias": "@type"})
