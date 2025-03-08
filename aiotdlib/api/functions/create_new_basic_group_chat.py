# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import MISSING, dataclass, field

from ..types.base import *


@dataclass(slots=True, kw_only=True)
class CreateNewBasicGroupChat(BaseObject):
    """
    Creates a new basic group and sends a corresponding messageBasicGroupChatCreate. Returns information about the newly created chat

    :param title: Title of the new basic group; 1-128 characters
    :type title: :class:`String`
    :param user_ids: Identifiers of users to be added to the basic group; may be empty to create a basic group without other members, defaults to list()
    :type user_ids: :class:`Vector[Int53]`
    :param message_auto_delete_time: Message auto-delete time value, in seconds; must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically
    :type message_auto_delete_time: :class:`Int32`
    """

    ID: typing.Literal["createNewBasicGroupChat"] = field(
        default="createNewBasicGroupChat", metadata={"alias": "@type"}
    )
    title: String = field(default=MISSING, metadata={"min_length": 1, "max_length": 128})
    user_ids: Vector[Int53] = field(default_factory=list)
    message_auto_delete_time: Int32 = field(default=0)
