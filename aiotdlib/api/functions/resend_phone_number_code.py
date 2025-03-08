# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ResendCodeReason,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class ResendPhoneNumberCode(BaseObject):
    """
    Resends the authentication code sent to a phone number. Works only if the previously received authenticationCodeInfo next_code_type was not null and the server-specified timeout has passed

    :param reason: Reason of code resending; pass null if unknown, defaults to None
    :type reason: :class:`ResendCodeReason`, optional
    """

    ID: typing.Literal["resendPhoneNumberCode"] = field(default="resendPhoneNumberCode", metadata={"alias": "@type"})
    reason: typing.Optional[ResendCodeReason] = field(default=None)
