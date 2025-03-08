# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import MISSING, dataclass, field

from ..types.base import *


@dataclass(slots=True, kw_only=True)
class RegisterUser(BaseObject):
    """
    Finishes user registration. Works only when the current authorization state is authorizationStateWaitRegistration

    :param first_name: The first name of the user; 1-64 characters
    :type first_name: :class:`String`
    :param last_name: The last name of the user; 0-64 characters
    :type last_name: :class:`String`
    :param disable_notification: Pass true to disable notification about the current user joining Telegram for other users that added them to contact list
    :type disable_notification: :class:`Bool`
    """

    ID: typing.Literal["registerUser"] = field(default="registerUser", metadata={"alias": "@type"})
    first_name: String = field(default=MISSING, metadata={"min_length": 1, "max_length": 64})
    last_name: String = field(default="", metadata={"max_length": 64})
    disable_notification: Bool = field(default=False)
