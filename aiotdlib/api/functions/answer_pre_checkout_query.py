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
class AnswerPreCheckoutQuery(BaseObject):
    """
    Sets the result of a pre-checkout query; for bots only

    :param pre_checkout_query_id: Identifier of the pre-checkout query
    :type pre_checkout_query_id: :class:`Int64`
    :param error_message: An error message, empty on success
    :type error_message: :class:`String`
    """

    ID: typing.Literal["answerPreCheckoutQuery"] = field(default="answerPreCheckoutQuery", metadata={"alias": "@type"})
    pre_checkout_query_id: Int64
    error_message: String
