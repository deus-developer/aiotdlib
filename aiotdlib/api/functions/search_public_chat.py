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
class SearchPublicChat(BaseObject):
    """
    Searches a public chat by its username. Currently, only private chats, supergroups and channels can be public. Returns the chat if found; otherwise, an error is returned

    :param username: Username to be resolved
    :type username: :class:`String`
    """

    ID: typing.Literal["searchPublicChat"] = field(default="searchPublicChat", metadata={"alias": "@type"})
    username: String
