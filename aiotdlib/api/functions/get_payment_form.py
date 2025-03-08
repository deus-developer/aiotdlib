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
    ThemeParameters,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class GetPaymentForm(BaseObject):
    """
    Returns an invoice payment form. This method must be called when the user presses inline button of the type inlineKeyboardButtonTypeBuy, or wants to buy access to media in a messagePaidMedia message

    :param input_invoice: The invoice
    :type input_invoice: :class:`InputInvoice`
    :param theme: Preferred payment form theme; pass null to use the default theme, defaults to None
    :type theme: :class:`ThemeParameters`, optional
    """

    ID: typing.Literal["getPaymentForm"] = field(default="getPaymentForm", metadata={"alias": "@type"})
    input_invoice: InputInvoice
    theme: typing.Optional[ThemeParameters] = field(default=None)
