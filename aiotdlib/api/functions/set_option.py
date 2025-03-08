# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    OptionValue,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class SetOption(BaseObject):
    """
    Sets the value of an option. (Check the list of available options on https://core.telegram.org/tdlib/options.) Only writable options can be set. Can be called before authorization

    :param name: The name of the option
    :type name: :class:`String`
    :param value: The new value of the option; pass null to reset option value to a default value, defaults to None
    :type value: :class:`OptionValue`, optional
    """

    ID: typing.Literal["setOption"] = field(default="setOption", metadata={"alias": "@type"})
    name: String
    value: typing.Optional[OptionValue] = field(default=None)
