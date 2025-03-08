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
class CheckPasswordRecoveryCode(BaseObject):
    """
    Checks whether a 2-step verification password recovery code sent to an email address is valid

    :param recovery_code: Recovery code to check
    :type recovery_code: :class:`String`
    """

    ID: typing.Literal["checkPasswordRecoveryCode"] = field(
        default="checkPasswordRecoveryCode", metadata={"alias": "@type"}
    )
    recovery_code: String
