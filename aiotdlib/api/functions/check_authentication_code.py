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
class CheckAuthenticationCode(BaseObject):
    """
    Checks the authentication code. Works only when the current authorization state is authorizationStateWaitCode

    :param code: Authentication code to check
    :type code: :class:`String`
    """

    ID: typing.Literal["checkAuthenticationCode"] = field(
        default="checkAuthenticationCode", metadata={"alias": "@type"}
    )
    code: String
