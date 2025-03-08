# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    InputInvoice,
    OrderInfo,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class ValidateOrderInfo(BaseObject):
    """
    Validates the order information provided by a user and returns the available shipping options for a flexible invoice

    :param input_invoice: The invoice
    :type input_invoice: :class:`InputInvoice`
    :param allow_save: Pass true to save the order information
    :type allow_save: :class:`Bool`
    :param order_info: The order information, provided by the user; pass null if empty, defaults to None
    :type order_info: :class:`OrderInfo`, optional
    """

    ID: typing.Literal["validateOrderInfo"] = field(default="validateOrderInfo", metadata={"alias": "@type"})
    input_invoice: InputInvoice
    allow_save: Bool = field(default=False)
    order_info: typing.Optional[OrderInfo] = field(default=None)
