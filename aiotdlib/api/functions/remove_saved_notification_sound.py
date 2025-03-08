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
class RemoveSavedNotificationSound(BaseObject):
    """
    Removes a notification sound from the list of saved notification sounds

    :param notification_sound_id: Identifier of the notification sound
    :type notification_sound_id: :class:`Int64`
    """

    ID: typing.Literal["removeSavedNotificationSound"] = field(
        default="removeSavedNotificationSound", metadata={"alias": "@type"}
    )
    notification_sound_id: Int64
