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
class GetPaymentReceipt(BaseObject):
    """
    Returns information about a successful payment

    :param chat_id: Chat identifier of the messagePaymentSuccessful message
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["getPaymentReceipt"] = field(default="getPaymentReceipt", metadata={"alias": "@type"})
    chat_id: Int53
    message_id: Int53
