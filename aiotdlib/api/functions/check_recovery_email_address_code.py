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
class CheckRecoveryEmailAddressCode(BaseObject):
    """
    Checks the 2-step verification recovery email address verification code

    :param code: Verification code to check
    :type code: :class:`String`
    """

    ID: typing.Literal["checkRecoveryEmailAddressCode"] = field(
        default="checkRecoveryEmailAddressCode", metadata={"alias": "@type"}
    )
    code: String
