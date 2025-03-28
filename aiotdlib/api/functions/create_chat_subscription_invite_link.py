# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    StarSubscriptionPricing,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class CreateChatSubscriptionInviteLink(BaseObject):
    """
    Creates a new subscription invite link for a channel chat. Requires can_invite_users right in the chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param name: Invite link name; 0-32 characters
    :type name: :class:`String`
    :param subscription_pricing: Information about subscription plan that will be applied to the users joining the chat via the link. Subscription period must be 2592000 in production environment, and 60 or 300 if Telegram test environment is used
    :type subscription_pricing: :class:`StarSubscriptionPricing`
    """

    ID: typing.Literal["createChatSubscriptionInviteLink"] = field(
        default="createChatSubscriptionInviteLink", metadata={"alias": "@type"}
    )
    chat_id: Int53
    name: String = field(default="", metadata={"max_length": 32})
    subscription_pricing: StarSubscriptionPricing = field(default=0)
