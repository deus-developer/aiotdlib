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
class ShareUsersWithBot(BaseObject):
    """
    Shares users after pressing a keyboardButtonTypeRequestUsers button with the bot

    :param chat_id: Identifier of the chat with the bot
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message with the button
    :type message_id: :class:`Int53`
    :param button_id: Identifier of the button
    :type button_id: :class:`Int32`
    :param shared_user_ids: Identifiers of the shared users
    :type shared_user_ids: :class:`Vector[Int53]`
    :param only_check: Pass true to check that the users can be shared by the button instead of actually sharing them
    :type only_check: :class:`Bool`
    """

    ID: typing.Literal["shareUsersWithBot"] = field(default="shareUsersWithBot", metadata={"alias": "@type"})
    chat_id: Int53
    message_id: Int53
    button_id: Int32
    shared_user_ids: Vector[Int53]
    only_check: Bool = field(default=False)
