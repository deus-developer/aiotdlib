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
class CancelRecoveryEmailAddressVerification(BaseObject):
    """
    Cancels verification of the 2-step verification recovery email address
    """

    ID: typing.Literal["cancelRecoveryEmailAddressVerification"] = field(
        default="cancelRecoveryEmailAddressVerification", metadata={"alias": "@type"}
    )
