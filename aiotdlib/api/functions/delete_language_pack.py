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
class DeleteLanguagePack(BaseObject):
    """
    Deletes all information about a language pack in the current localization target. The language pack which is currently in use (including base language pack) or is being synchronized can't be deleted. Can be called before authorization

    :param language_pack_id: Identifier of the language pack to delete
    :type language_pack_id: :class:`String`
    """

    ID: typing.Literal["deleteLanguagePack"] = field(default="deleteLanguagePack", metadata={"alias": "@type"})
    language_pack_id: String
