# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    StoryPrivacySettings,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetStoryPrivacySettings(BaseObject):
    """
    Changes privacy settings of a story. The method can be called only for stories posted on behalf of the current user and if story.can_be_edited == true

    :param story_id: Identifier of the story
    :type story_id: :class:`Int32`
    :param privacy_settings: The new privacy settings for the story
    :type privacy_settings: :class:`StoryPrivacySettings`
    """

    ID: typing.Literal["setStoryPrivacySettings"] = field(
        default="setStoryPrivacySettings", metadata={"alias": "@type"}
    )
    story_id: Int32
    privacy_settings: StoryPrivacySettings
