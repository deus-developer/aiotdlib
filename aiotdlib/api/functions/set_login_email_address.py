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
class SetLoginEmailAddress(BaseObject):
    """
    Changes the login email address of the user. The email address can be changed only if the current user already has login email and passwordState.login_email_address_pattern is non-empty. The change will not be applied until the new login email address is confirmed with checkLoginEmailAddressCode. To use Apple ID/Google ID instead of an email address, call checkLoginEmailAddressCode directly

    :param new_login_email_address: New login email address
    :type new_login_email_address: :class:`String`
    """

    ID: typing.Literal["setLoginEmailAddress"] = field(default="setLoginEmailAddress", metadata={"alias": "@type"})
    new_login_email_address: String
