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
class CheckAuthenticationBotToken(BaseObject):
    """
    Checks the authentication token of a bot; to log in as a bot. Works only when the current authorization state is authorizationStateWaitPhoneNumber. Can be used instead of setAuthenticationPhoneNumber and checkAuthenticationCode to log in

    :param token: The bot token
    :type token: :class:`String`
    """

    ID: typing.Literal["checkAuthenticationBotToken"] = field(
        default="checkAuthenticationBotToken", metadata={"alias": "@type"}
    )
    token: String
