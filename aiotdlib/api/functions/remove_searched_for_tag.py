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
class RemoveSearchedForTag(BaseObject):
    """
    Removes a hashtag or a cashtag from the list of recently searched for hashtags or cashtags

    :param tag: Hashtag or cashtag to delete
    :type tag: :class:`String`
    """

    ID: typing.Literal["removeSearchedForTag"] = field(default="removeSearchedForTag", metadata={"alias": "@type"})
    tag: String
