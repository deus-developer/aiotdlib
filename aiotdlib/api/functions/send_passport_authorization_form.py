# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    PassportElementType,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SendPassportAuthorizationForm(BaseObject):
    """
    Sends a Telegram Passport authorization form, effectively sharing data with the service. This method must be called after getPassportAuthorizationFormAvailableElements if some previously available elements are going to be reused

    :param authorization_form_id: Authorization form identifier
    :type authorization_form_id: :class:`Int32`
    :param types: Types of Telegram Passport elements chosen by user to complete the authorization form
    :type types: :class:`Vector[PassportElementType]`
    """

    ID: typing.Literal["sendPassportAuthorizationForm"] = field(
        default="sendPassportAuthorizationForm", metadata={"alias": "@type"}
    )
    authorization_form_id: Int32
    types: Vector[PassportElementType]
