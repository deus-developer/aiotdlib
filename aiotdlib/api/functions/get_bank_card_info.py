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
class GetBankCardInfo(BaseObject):
    """
    Returns information about a bank card

    :param bank_card_number: The bank card number
    :type bank_card_number: :class:`String`
    """

    ID: typing.Literal["getBankCardInfo"] = field(default="getBankCardInfo", metadata={"alias": "@type"})
    bank_card_number: String
