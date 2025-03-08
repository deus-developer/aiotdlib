# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    EmojiCategoryType,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetEmojiCategories(BaseObject):
    """
    Returns available emoji categories

    :param type_: Type of emoji categories to return; pass null to get default emoji categories, defaults to None
    :type type_: :class:`EmojiCategoryType`, optional
    """

    ID: typing.Literal["getEmojiCategories"] = field(default="getEmojiCategories", metadata={"alias": "@type"})
    type_: typing.Optional[EmojiCategoryType] = field(default=None, metadata={"alias": "type"})
