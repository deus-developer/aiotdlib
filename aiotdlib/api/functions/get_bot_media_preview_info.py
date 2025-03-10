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
class GetBotMediaPreviewInfo(BaseObject):
    """
    Returns the list of media previews for the given language and the list of languages for which the bot has dedicated previews

    :param bot_user_id: Identifier of the target bot. The bot must be owned and must have the main Web App
    :type bot_user_id: :class:`Int53`
    :param language_code: A two-letter ISO 639-1 language code for which to get previews. If empty, then default previews are returned
    :type language_code: :class:`String`
    """

    ID: typing.Literal["getBotMediaPreviewInfo"] = field(default="getBotMediaPreviewInfo", metadata={"alias": "@type"})
    bot_user_id: Int53
    language_code: String = field(default="")
