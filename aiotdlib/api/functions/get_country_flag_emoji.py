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
class GetCountryFlagEmoji(BaseObject):
    """
    Returns an emoji for the given country. Returns an empty string on failure. Can be called synchronously

    :param country_code: A two-letter ISO 3166-1 alpha-2 country code as received from getCountries
    :type country_code: :class:`String`
    """

    ID: typing.Literal["getCountryFlagEmoji"] = field(default="getCountryFlagEmoji", metadata={"alias": "@type"})
    country_code: String
