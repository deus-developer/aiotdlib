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
class CheckPhoneNumberCode(BaseObject):
    """
    Check the authentication code and completes the request for which the code was sent if appropriate

    :param code: Authentication code to check
    :type code: :class:`String`
    """

    ID: typing.Literal["checkPhoneNumberCode"] = field(default="checkPhoneNumberCode", metadata={"alias": "@type"})
    code: String
