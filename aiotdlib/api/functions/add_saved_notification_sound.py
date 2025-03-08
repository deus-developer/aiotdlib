# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    InputFile,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class AddSavedNotificationSound(BaseObject):
    """
    Adds a new notification sound to the list of saved notification sounds. The new notification sound is added to the top of the list. If it is already in the list, its position isn't changed

    :param sound: Notification sound file to add
    :type sound: :class:`InputFile`
    """

    ID: typing.Literal["addSavedNotificationSound"] = field(
        default="addSavedNotificationSound", metadata={"alias": "@type"}
    )
    sound: InputFile
