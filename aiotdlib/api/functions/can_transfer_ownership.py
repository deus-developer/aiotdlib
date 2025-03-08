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
class CanTransferOwnership(BaseObject):
    """
    Checks whether the current session can be used to transfer a chat ownership to another user
    """

    ID: typing.Literal["canTransferOwnership"] = field(default="canTransferOwnership", metadata={"alias": "@type"})
