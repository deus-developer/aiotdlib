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
class AddCustomServerLanguagePack(BaseObject):
    """
    Adds a custom server language pack to the list of installed language packs in current localization target. Can be called before authorization

    :param language_pack_id: Identifier of a language pack to be added
    :type language_pack_id: :class:`String`
    """

    ID: typing.Literal["addCustomServerLanguagePack"] = field(
        default="addCustomServerLanguagePack", metadata={"alias": "@type"}
    )
    language_pack_id: String
