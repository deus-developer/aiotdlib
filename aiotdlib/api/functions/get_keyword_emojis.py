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
class GetKeywordEmojis(BaseObject):
    """
    Return emojis matching the keyword. Supported only if the file database is enabled. Order of results is unspecified

    :param text: Text to search for
    :type text: :class:`String`
    :param input_language_codes: List of possible IETF language tags of the user's input language; may be empty if unknown, defaults to list()
    :type input_language_codes: :class:`Vector[String]`
    """

    ID: typing.Literal["getKeywordEmojis"] = field(default="getKeywordEmojis", metadata={"alias": "@type"})
    text: String
    input_language_codes: Vector[String] = field(default_factory=list)
