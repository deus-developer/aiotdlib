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
class SharePhoneNumber(BaseObject):
    """
    Shares the phone number of the current user with a mutual contact. Supposed to be called when the user clicks on chatActionBarSharePhoneNumber

    :param user_id: Identifier of the user with whom to share the phone number. The user must be a mutual contact
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["sharePhoneNumber"] = field(default="sharePhoneNumber", metadata={"alias": "@type"})
    user_id: Int53
