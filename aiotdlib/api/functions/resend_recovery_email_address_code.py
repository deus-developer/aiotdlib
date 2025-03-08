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
class ResendRecoveryEmailAddressCode(BaseObject):
    """
    Resends the 2-step verification recovery email address verification code
    """

    ID: typing.Literal["resendRecoveryEmailAddressCode"] = field(
        default="resendRecoveryEmailAddressCode", metadata={"alias": "@type"}
    )
