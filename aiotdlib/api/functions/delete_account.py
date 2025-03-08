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
class DeleteAccount(BaseObject):
    """
    Deletes the account of the current user, deleting all information associated with the user from the server. The phone number of the account can be used to create a new account. Can be called before authorization when the current authorization state is authorizationStateWaitPassword

    :param reason: The reason why the account was deleted; optional
    :type reason: :class:`String`
    :param password: The 2-step verification password of the current user. If the current user isn't authorized, then an empty string can be passed and account deletion can be canceled within one week
    :type password: :class:`String`
    """

    ID: typing.Literal["deleteAccount"] = field(default="deleteAccount", metadata={"alias": "@type"})
    reason: String
    password: String
