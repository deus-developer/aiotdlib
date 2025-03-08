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
class GetSavedNotificationSound(BaseObject):
    """
    Returns saved notification sound by its identifier. Returns a 404 error if there is no saved notification sound with the specified identifier

    :param notification_sound_id: Identifier of the notification sound
    :type notification_sound_id: :class:`Int64`
    """

    ID: typing.Literal["getSavedNotificationSound"] = field(
        default="getSavedNotificationSound", metadata={"alias": "@type"}
    )
    notification_sound_id: Int64
