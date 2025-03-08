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
class CheckLoginEmailAddressCode(BaseObject):
    """
    Checks the login email address authentication

    :param code: Email address authentication to check
    :type code: :class:`EmailAddressAuthentication`
    """

    ID: typing.Literal["checkLoginEmailAddressCode"] = field(
        default="checkLoginEmailAddressCode", metadata={"alias": "@type"}
    )
    code: EmailAddressAuthentication
