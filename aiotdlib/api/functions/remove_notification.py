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
class RemoveNotification(BaseObject):
    """
    Removes an active notification from notification list. Needs to be called only if the notification is removed by the current user

    :param notification_group_id: Identifier of notification group to which the notification belongs
    :type notification_group_id: :class:`Int32`
    :param notification_id: Identifier of removed notification
    :type notification_id: :class:`Int32`
    """

    ID: typing.Literal["removeNotification"] = field(default="removeNotification", metadata={"alias": "@type"})
    notification_group_id: Int32
    notification_id: Int32
