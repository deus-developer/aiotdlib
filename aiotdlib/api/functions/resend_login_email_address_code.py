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
class ResendLoginEmailAddressCode(BaseObject):
    """
    Resends the login email address verification code
    """

    ID: typing.Literal["resendLoginEmailAddressCode"] = field(
        default="resendLoginEmailAddressCode", metadata={"alias": "@type"}
    )
