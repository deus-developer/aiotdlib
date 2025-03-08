# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    InputInlineQueryResult,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class AnswerWebAppQuery(BaseObject):
    """
    Sets the result of interaction with a Web App and sends corresponding message on behalf of the user to the chat from which the query originated; for bots only

    :param web_app_query_id: Identifier of the Web App query
    :type web_app_query_id: :class:`String`
    :param result: The result of the query
    :type result: :class:`InputInlineQueryResult`
    """

    ID: typing.Literal["answerWebAppQuery"] = field(default="answerWebAppQuery", metadata={"alias": "@type"})
    web_app_query_id: String
    result: InputInlineQueryResult
