# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import MISSING, dataclass, field

from ..types.all import (
    PhoneNumberAuthenticationSettings,
    PhoneNumberCodeType,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SendPhoneNumberCode(BaseObject):
    """
    Sends a code to the specified phone number. Aborts previous phone number verification if there was one. On success, returns information about the sent code

    :param phone_number: The phone number, in international format
    :type phone_number: :class:`String`
    :param type_: Type of the request for which the code is sent
    :type type_: :class:`PhoneNumberCodeType`
    :param settings: Settings for the authentication of the user's phone number; pass null to use default settings, defaults to None
    :type settings: :class:`PhoneNumberAuthenticationSettings`, optional
    """

    ID: typing.Literal["sendPhoneNumberCode"] = field(default="sendPhoneNumberCode", metadata={"alias": "@type"})
    phone_number: String
    type_: PhoneNumberCodeType = field(default=MISSING, metadata={"alias": "type"})
    settings: typing.Optional[PhoneNumberAuthenticationSettings] = field(default=None)
