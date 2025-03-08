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
class SetGroupCallParticipantIsSpeaking(BaseObject):
    """
    Informs TDLib that speaking state of a participant of an active group has changed

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    :param audio_source: Group call participant's synchronization audio source identifier, or 0 for the current user
    :type audio_source: :class:`Int32`
    :param is_speaking: Pass true if the user is speaking
    :type is_speaking: :class:`Bool`
    """

    ID: typing.Literal["setGroupCallParticipantIsSpeaking"] = field(
        default="setGroupCallParticipantIsSpeaking", metadata={"alias": "@type"}
    )
    group_call_id: Int32
    audio_source: Int32 = field(default=0)
    is_speaking: Bool = field(default=False)
