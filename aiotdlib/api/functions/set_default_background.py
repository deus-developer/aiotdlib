# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    BackgroundType,
    InputBackground,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetDefaultBackground(BaseObject):
    """
    Sets default background for chats; adds the background to the list of installed backgrounds

    :param for_dark_theme: Pass true if the background is set for a dark theme
    :type for_dark_theme: :class:`Bool`
    :param background: The input background to use; pass null to create a new filled background, defaults to None
    :type background: :class:`InputBackground`, optional
    :param type_: Background type; pass null to use the default type of the remote background; backgroundTypeChatTheme isn't supported, defaults to None
    :type type_: :class:`BackgroundType`, optional
    """

    ID: typing.Literal["setDefaultBackground"] = field(default="setDefaultBackground", metadata={"alias": "@type"})
    for_dark_theme: Bool = field(default=False)
    background: typing.Optional[InputBackground] = field(default=None)
    type_: typing.Optional[BackgroundType] = field(default=None, metadata={"alias": "type"})
