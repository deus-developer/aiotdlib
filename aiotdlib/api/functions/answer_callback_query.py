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
class AnswerCallbackQuery(BaseObject):
    """
    Sets the result of a callback query; for bots only

    :param callback_query_id: Identifier of the callback query
    :type callback_query_id: :class:`Int64`
    :param text: Text of the answer
    :type text: :class:`String`
    :param url: URL to be opened
    :type url: :class:`String`
    :param cache_time: Time during which the result of the query can be cached, in seconds
    :type cache_time: :class:`Int32`
    :param show_alert: Pass true to show an alert to the user instead of a toast notification
    :type show_alert: :class:`Bool`
    """

    ID: typing.Literal["answerCallbackQuery"] = field(default="answerCallbackQuery", metadata={"alias": "@type"})
    callback_query_id: Int64
    text: String
    url: String
    cache_time: Int32
    show_alert: Bool = field(default=False)
