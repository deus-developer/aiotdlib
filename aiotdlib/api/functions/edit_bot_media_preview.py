# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    InputStoryContent,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class EditBotMediaPreview(BaseObject):
    """
    Replaces media preview in the list of media previews of a bot. Returns the new preview after edit is completed server-side

    :param bot_user_id: Identifier of the target bot. The bot must be owned and must have the main Web App
    :type bot_user_id: :class:`Int53`
    :param language_code: Language code of the media preview to edit
    :type language_code: :class:`String`
    :param file_id: File identifier of the media to replace
    :type file_id: :class:`Int32`
    :param content: Content of the new preview
    :type content: :class:`InputStoryContent`
    """

    ID: typing.Literal["editBotMediaPreview"] = field(default="editBotMediaPreview", metadata={"alias": "@type"})
    bot_user_id: Int53
    language_code: String
    file_id: Int32
    content: InputStoryContent
