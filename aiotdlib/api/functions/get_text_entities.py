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
class GetTextEntities(BaseObject):
    """
    Returns all entities (mentions, hashtags, cashtags, bot commands, bank card numbers, URLs, and email addresses) found in the text. Can be called synchronously

    :param text: The text in which to look for entities
    :type text: :class:`String`
    """

    ID: typing.Literal["getTextEntities"] = field(default="getTextEntities", metadata={"alias": "@type"})
    text: String
