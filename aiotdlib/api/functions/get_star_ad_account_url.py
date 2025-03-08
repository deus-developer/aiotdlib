# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    MessageSender,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetStarAdAccountUrl(BaseObject):
    """
    Returns a URL for a Telegram Ad platform account that can be used to set up advertisements for the chat paid in the owned Telegram Stars

    :param owner_id: Identifier of the owner of the Telegram Stars; can be identifier of an owned bot, or identifier of an owned channel chat
    :type owner_id: :class:`MessageSender`
    """

    ID: typing.Literal["getStarAdAccountUrl"] = field(default="getStarAdAccountUrl", metadata={"alias": "@type"})
    owner_id: MessageSender
