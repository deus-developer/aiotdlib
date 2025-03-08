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
class SendEmailAddressVerificationCode(BaseObject):
    """
    Sends a code to verify an email address to be added to a user's Telegram Passport

    :param email_address: Email address
    :type email_address: :class:`String`
    """

    ID: typing.Literal["sendEmailAddressVerificationCode"] = field(
        default="sendEmailAddressVerificationCode", metadata={"alias": "@type"}
    )
    email_address: String
