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
class CheckAuthenticationPassword(BaseObject):
    """
    Checks the 2-step verification password for correctness. Works only when the current authorization state is authorizationStateWaitPassword

    :param password: The 2-step verification password to check
    :type password: :class:`String`
    """

    ID: typing.Literal["checkAuthenticationPassword"] = field(
        default="checkAuthenticationPassword", metadata={"alias": "@type"}
    )
    password: String
