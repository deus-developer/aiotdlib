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
class RecoverAuthenticationPassword(BaseObject):
    """
    Recovers the 2-step verification password with a password recovery code sent to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword

    :param recovery_code: Recovery code to check
    :type recovery_code: :class:`String`
    :param new_password: New 2-step verification password of the user; may be empty to remove the password
    :type new_password: :class:`String`
    :param new_hint: New password hint; may be empty
    :type new_hint: :class:`String`
    """

    ID: typing.Literal["recoverAuthenticationPassword"] = field(
        default="recoverAuthenticationPassword", metadata={"alias": "@type"}
    )
    recovery_code: String
    new_password: String = field(default="")
    new_hint: String = field(default="")
