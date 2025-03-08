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
class CheckEmailAddressVerificationCode(BaseObject):
    """
    Checks the email address verification code for Telegram Passport

    :param code: Verification code to check
    :type code: :class:`String`
    """

    ID: typing.Literal["checkEmailAddressVerificationCode"] = field(
        default="checkEmailAddressVerificationCode", metadata={"alias": "@type"}
    )
    code: String
