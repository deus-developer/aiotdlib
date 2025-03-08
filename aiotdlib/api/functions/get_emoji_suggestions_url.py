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
class GetEmojiSuggestionsUrl(BaseObject):
    """
    Returns an HTTP URL which can be used to automatically log in to the translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation

    :param language_code: Language code for which the emoji replacements will be suggested
    :type language_code: :class:`String`
    """

    ID: typing.Literal["getEmojiSuggestionsUrl"] = field(default="getEmojiSuggestionsUrl", metadata={"alias": "@type"})
    language_code: String
