# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    LanguagePackString,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetCustomLanguagePackString(BaseObject):
    """
    Adds, edits or deletes a string in a custom local language pack. Can be called before authorization

    :param language_pack_id: Identifier of a previously added custom local language pack in the current localization target
    :type language_pack_id: :class:`String`
    :param new_string: New language pack string
    :type new_string: :class:`LanguagePackString`
    """

    ID: typing.Literal["setCustomLanguagePackString"] = field(
        default="setCustomLanguagePackString", metadata={"alias": "@type"}
    )
    language_pack_id: String
    new_string: LanguagePackString
