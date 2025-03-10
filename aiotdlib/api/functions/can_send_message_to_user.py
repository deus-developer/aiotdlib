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
class CanSendMessageToUser(BaseObject):
    """
    Check whether the current user can message another user or try to create a chat with them

    :param user_id: Identifier of the other user
    :type user_id: :class:`Int53`
    :param only_local: Pass true to get only locally available information without sending network requests
    :type only_local: :class:`Bool`
    """

    ID: typing.Literal["canSendMessageToUser"] = field(default="canSendMessageToUser", metadata={"alias": "@type"})
    user_id: Int53
    only_local: Bool = field(default=False)
