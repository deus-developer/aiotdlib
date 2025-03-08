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
class SearchUserByPhoneNumber(BaseObject):
    """
    Searches a user by their phone number. Returns a 404 error if the user can't be found

    :param phone_number: Phone number to search for
    :type phone_number: :class:`String`
    :param only_local: Pass true to get only locally available information without sending network requests
    :type only_local: :class:`Bool`
    """

    ID: typing.Literal["searchUserByPhoneNumber"] = field(
        default="searchUserByPhoneNumber", metadata={"alias": "@type"}
    )
    phone_number: String
    only_local: Bool = field(default=False)
