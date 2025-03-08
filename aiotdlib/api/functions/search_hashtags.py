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
class SearchHashtags(BaseObject):
    """
    Searches for recently used hashtags by their prefix

    :param prefix: Hashtag prefix to search for
    :type prefix: :class:`String`
    :param limit: The maximum number of hashtags to be returned
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["searchHashtags"] = field(default="searchHashtags", metadata={"alias": "@type"})
    prefix: String
    limit: Int32
