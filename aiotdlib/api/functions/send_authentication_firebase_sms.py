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
class SendAuthenticationFirebaseSms(BaseObject):
    """
    Sends Firebase Authentication SMS to the phone number of the user. Works only when the current authorization state is authorizationStateWaitCode and the server returned code of the type authenticationCodeTypeFirebaseAndroid or authenticationCodeTypeFirebaseIos

    :param token: Play Integrity API or SafetyNet Attestation API token for the Android application, or secret from push notification for the iOS application
    :type token: :class:`String`
    """

    ID: typing.Literal["sendAuthenticationFirebaseSms"] = field(
        default="sendAuthenticationFirebaseSms", metadata={"alias": "@type"}
    )
    token: String
