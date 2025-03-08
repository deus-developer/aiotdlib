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
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class EditCustomLanguagePackInfo(BaseObject):
    """
    Edits information about a custom local language pack in the current localization target. Can be called before authorization

    :param info: New information about the custom local language pack
    :type info: :class:`LanguagePackInfo`
    """

    ID: typing.Literal["editCustomLanguagePackInfo"] = field(
        default="editCustomLanguagePackInfo", metadata={"alias": "@type"}
    )
    info: LanguagePackInfo
