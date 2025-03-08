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
class RequestAuthenticationPasswordRecovery(BaseObject):
    """
    Requests to send a 2-step verification password recovery code to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword
    """

    ID: typing.Literal["requestAuthenticationPasswordRecovery"] = field(
        default="requestAuthenticationPasswordRecovery", metadata={"alias": "@type"}
    )
