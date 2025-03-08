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
class RemoveRecentHashtag(BaseObject):
    """
    Removes a hashtag from the list of recently used hashtags

    :param hashtag: Hashtag to delete
    :type hashtag: :class:`String`
    """

    ID: typing.Literal["removeRecentHashtag"] = field(default="removeRecentHashtag", metadata={"alias": "@type"})
    hashtag: String
