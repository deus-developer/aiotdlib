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
class GetStarWithdrawalUrl(BaseObject):
    """
    Returns a URL for Telegram Star withdrawal

    :param owner_id: Identifier of the owner of the Telegram Stars; can be identifier of an owned bot, or identifier of an owned channel chat
    :type owner_id: :class:`MessageSender`
    :param star_count: The number of Telegram Stars to withdraw. Must be at least getOption("star_withdrawal_count_min")
    :type star_count: :class:`Int53`
    :param password: The 2-step verification password of the current user
    :type password: :class:`String`
    """

    ID: typing.Literal["getStarWithdrawalUrl"] = field(default="getStarWithdrawalUrl", metadata={"alias": "@type"})
    owner_id: MessageSender
    star_count: Int53
    password: String
