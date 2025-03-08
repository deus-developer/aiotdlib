# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    PhoneNumberAuthenticationSettings,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetAuthenticationPhoneNumber(BaseObject):
    """
    Sets the phone number of the user and sends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitPhoneNumber, or if there is no pending authentication query and the current authorization state is authorizationStateWaitEmailAddress, authorizationStateWaitEmailCode, authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword

    :param phone_number: The phone number of the user, in international format
    :type phone_number: :class:`String`
    :param settings: Settings for the authentication of the user's phone number; pass null to use default settings, defaults to None
    :type settings: :class:`PhoneNumberAuthenticationSettings`, optional
    """

    ID: typing.Literal["setAuthenticationPhoneNumber"] = field(
        default="setAuthenticationPhoneNumber", metadata={"alias": "@type"}
    )
    phone_number: String
    settings: typing.Optional[PhoneNumberAuthenticationSettings] = field(default=None)
