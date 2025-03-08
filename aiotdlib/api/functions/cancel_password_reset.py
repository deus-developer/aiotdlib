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
class CancelPasswordReset(BaseObject):
    """
    Cancels reset of 2-step verification password. The method can be called if passwordState.pending_reset_date > 0
    """

    ID: typing.Literal["cancelPasswordReset"] = field(default="cancelPasswordReset", metadata={"alias": "@type"})
