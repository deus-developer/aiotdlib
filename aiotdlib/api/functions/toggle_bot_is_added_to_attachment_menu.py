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
class ToggleBotIsAddedToAttachmentMenu(BaseObject):
    """
    Adds or removes a bot to attachment and side menu. Bot can be added to the menu, only if userTypeBot.can_be_added_to_attachment_menu == true

    :param bot_user_id: Bot's user identifier
    :type bot_user_id: :class:`Int53`
    :param is_added: Pass true to add the bot to attachment menu; pass false to remove the bot from attachment menu
    :type is_added: :class:`Bool`
    :param allow_write_access: Pass true if the current user allowed the bot to send them messages. Ignored if is_added is false
    :type allow_write_access: :class:`Bool`
    """

    ID: typing.Literal["toggleBotIsAddedToAttachmentMenu"] = field(
        default="toggleBotIsAddedToAttachmentMenu", metadata={"alias": "@type"}
    )
    bot_user_id: Int53
    is_added: Bool = field(default=False)
    allow_write_access: Bool = field(default=False)
