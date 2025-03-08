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
class GetRecoveryEmailAddress(BaseObject):
    """
    Returns a 2-step verification recovery email address that was previously set up. This method can be used to verify a password provided by the user

    :param password: The 2-step verification password for the current user
    :type password: :class:`String`
    """

    ID: typing.Literal["getRecoveryEmailAddress"] = field(
        default="getRecoveryEmailAddress", metadata={"alias": "@type"}
    )
    password: String
