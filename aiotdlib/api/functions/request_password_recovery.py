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
class RequestPasswordRecovery(BaseObject):
    """
    Requests to send a 2-step verification password recovery code to an email address that was previously set up
    """

    ID: typing.Literal["requestPasswordRecovery"] = field(
        default="requestPasswordRecovery", metadata={"alias": "@type"}
    )
