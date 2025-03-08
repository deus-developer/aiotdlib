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
class GetAttachmentMenuBot(BaseObject):
    """
    Returns information about a bot that can be added to attachment or side menu

    :param bot_user_id: Bot's user identifier
    :type bot_user_id: :class:`Int53`
    """

    ID: typing.Literal["getAttachmentMenuBot"] = field(default="getAttachmentMenuBot", metadata={"alias": "@type"})
    bot_user_id: Int53
