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
class GetGroupsInCommon(BaseObject):
    """
    Returns a list of common group chats with a given user. Chats are sorted by their type and creation date

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param limit: The maximum number of chats to be returned; up to 100
    :type limit: :class:`Int32`
    :param offset_chat_id: Chat identifier starting from which to return chats; use 0 for the first request
    :type offset_chat_id: :class:`Int53`
    """

    ID: typing.Literal["getGroupsInCommon"] = field(default="getGroupsInCommon", metadata={"alias": "@type"})
    user_id: Int53
    limit: Int32
    offset_chat_id: Int53 = field(default=0)
