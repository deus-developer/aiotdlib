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
class SearchChats(BaseObject):
    """
    Searches for the specified query in the title and username of already known chats; this is an offline request. Returns chats in the order seen in the main chat list

    :param query: Query to search for. If the query is empty, returns up to 50 recently found chats
    :type query: :class:`String`
    :param limit: The maximum number of chats to be returned
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["searchChats"] = field(default="searchChats", metadata={"alias": "@type"})
    query: String
    limit: Int32
