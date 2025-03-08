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
class GetLanguagePackInfo(BaseObject):
    """
    Returns information about a language pack. Returned language pack identifier may be different from a provided one. Can be called before authorization

    :param language_pack_id: Language pack identifier
    :type language_pack_id: :class:`String`
    """

    ID: typing.Literal["getLanguagePackInfo"] = field(default="getLanguagePackInfo", metadata={"alias": "@type"})
    language_pack_id: String
