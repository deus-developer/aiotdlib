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
class SendPhoneNumberFirebaseSms(BaseObject):
    """
    Sends Firebase Authentication SMS to the specified phone number. Works only when received a code of the type authenticationCodeTypeFirebaseAndroid or authenticationCodeTypeFirebaseIos

    :param token: Play Integrity API or SafetyNet Attestation API token for the Android application, or secret from push notification for the iOS application
    :type token: :class:`String`
    """

    ID: typing.Literal["sendPhoneNumberFirebaseSms"] = field(
        default="sendPhoneNumberFirebaseSms", metadata={"alias": "@type"}
    )
    token: String
