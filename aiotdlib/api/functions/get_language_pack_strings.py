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
class GetLanguagePackStrings(BaseObject):
    """
    Returns strings from a language pack in the current localization target by their keys. Can be called before authorization

    :param language_pack_id: Language pack identifier of the strings to be returned
    :type language_pack_id: :class:`String`
    :param keys: Language pack keys of the strings to be returned; leave empty to request all available strings
    :type keys: :class:`Vector[String]`
    """

    ID: typing.Literal["getLanguagePackStrings"] = field(default="getLanguagePackStrings", metadata={"alias": "@type"})
    language_pack_id: String
    keys: Vector[String]
