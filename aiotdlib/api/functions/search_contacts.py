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
class SearchContacts(BaseObject):
    """
    Searches for the specified query in the first names, last names and usernames of the known user contacts

    :param limit: The maximum number of users to be returned
    :type limit: :class:`Int32`
    :param query: Query to search for; may be empty to return all contacts
    :type query: :class:`String`
    """

    ID: typing.Literal["searchContacts"] = field(default="searchContacts", metadata={"alias": "@type"})
    limit: Int32
    query: String = field(default="")
