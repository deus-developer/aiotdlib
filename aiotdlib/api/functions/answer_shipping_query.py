# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    ShippingOption,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class AnswerShippingQuery(BaseObject):
    """
    Sets the result of a shipping query; for bots only

    :param shipping_query_id: Identifier of the shipping query
    :type shipping_query_id: :class:`Int64`
    :param shipping_options: Available shipping options
    :type shipping_options: :class:`Vector[ShippingOption]`
    :param error_message: An error message, empty on success
    :type error_message: :class:`String`
    """

    ID: typing.Literal["answerShippingQuery"] = field(default="answerShippingQuery", metadata={"alias": "@type"})
    shipping_query_id: Int64
    shipping_options: Vector[ShippingOption]
    error_message: String
