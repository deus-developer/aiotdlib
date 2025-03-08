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
class RemoveNotificationGroup(BaseObject):
    """
    Removes a group of active notifications. Needs to be called only if the notification group is removed by the current user

    :param notification_group_id: Notification group identifier
    :type notification_group_id: :class:`Int32`
    :param max_notification_id: The maximum identifier of removed notifications
    :type max_notification_id: :class:`Int32`
    """

    ID: typing.Literal["removeNotificationGroup"] = field(
        default="removeNotificationGroup", metadata={"alias": "@type"}
    )
    notification_group_id: Int32
    max_notification_id: Int32
