# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    LanguagePackInfo,
    LanguagePackString,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetCustomLanguagePack(BaseObject):
    """
    Adds or changes a custom local language pack to the current localization target

    :param info: Information about the language pack. Language pack identifier must start with 'X', consist only of English letters, digits and hyphens, and must not exceed 64 characters. Can be called before authorization
    :type info: :class:`LanguagePackInfo`
    :param strings: Strings of the new language pack
    :type strings: :class:`Vector[LanguagePackString]`
    """

    ID: typing.Literal["setCustomLanguagePack"] = field(default="setCustomLanguagePack", metadata={"alias": "@type"})
    info: LanguagePackInfo
    strings: Vector[LanguagePackString]
