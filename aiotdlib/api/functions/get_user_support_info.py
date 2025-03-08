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
class GetUserSupportInfo(BaseObject):
    """
    Returns support information for the given user; for Telegram support only

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["getUserSupportInfo"] = field(default="getUserSupportInfo", metadata={"alias": "@type"})
    user_id: Int53
