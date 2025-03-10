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
class ReportSupergroupAntiSpamFalsePositive(BaseObject):
    """
    Reports a false deletion of a message by aggressive anti-spam checks; requires administrator rights in the supergroup. Can be called only for messages from chatEventMessageDeleted with can_report_anti_spam_false_positive == true

    :param supergroup_id: Supergroup identifier
    :type supergroup_id: :class:`Int53`
    :param message_id: Identifier of the erroneously deleted message from chatEventMessageDeleted
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["reportSupergroupAntiSpamFalsePositive"] = field(
        default="reportSupergroupAntiSpamFalsePositive", metadata={"alias": "@type"}
    )
    supergroup_id: Int53
    message_id: Int53
