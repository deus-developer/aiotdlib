# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    InputPassportElement,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetPassportElement(BaseObject):
    """
    Adds an element to the user's Telegram Passport. May return an error with a message "PHONE_VERIFICATION_NEEDED" or "EMAIL_VERIFICATION_NEEDED" if the chosen phone number or the chosen email address must be verified first

    :param element: Input Telegram Passport element
    :type element: :class:`InputPassportElement`
    :param password: The 2-step verification password of the current user
    :type password: :class:`String`
    """

    ID: typing.Literal["setPassportElement"] = field(default="setPassportElement", metadata={"alias": "@type"})
    element: InputPassportElement
    password: String
