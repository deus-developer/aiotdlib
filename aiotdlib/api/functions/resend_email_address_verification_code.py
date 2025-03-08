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
class ResendEmailAddressVerificationCode(BaseObject):
    """
    Resends the code to verify an email address to be added to a user's Telegram Passport
    """

    ID: typing.Literal["resendEmailAddressVerificationCode"] = field(
        default="resendEmailAddressVerificationCode", metadata={"alias": "@type"}
    )
