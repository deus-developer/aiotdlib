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
class EditUserStarSubscription(BaseObject):
    """
    Cancels or re-enables Telegram Star subscription for a user; for bots only

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param telegram_payment_charge_id: Telegram payment identifier of the subscription
    :type telegram_payment_charge_id: :class:`String`
    :param is_canceled: Pass true to cancel the subscription; pass false to allow the user to enable it
    :type is_canceled: :class:`Bool`
    """

    ID: typing.Literal["editUserStarSubscription"] = field(
        default="editUserStarSubscription", metadata={"alias": "@type"}
    )
    user_id: Int53
    telegram_payment_charge_id: String
    is_canceled: Bool = field(default=False)
