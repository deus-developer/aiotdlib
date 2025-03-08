# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    EmailAddressAuthentication,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class CheckAuthenticationEmailCode(BaseObject):
    """
    Checks the authentication of an email address. Works only when the current authorization state is authorizationStateWaitEmailCode

    :param code: Email address authentication to check
    :type code: :class:`EmailAddressAuthentication`
    """

    ID: typing.Literal["checkAuthenticationEmailCode"] = field(
        default="checkAuthenticationEmailCode", metadata={"alias": "@type"}
    )
    code: EmailAddressAuthentication
