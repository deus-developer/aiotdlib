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
class GetPreferredCountryLanguage(BaseObject):
    """
    Returns an IETF language tag of the language preferred in the country, which must be used to fill native fields in Telegram Passport personal details. Returns a 404 error if unknown

    :param country_code: A two-letter ISO 3166-1 alpha-2 country code
    :type country_code: :class:`String`
    """

    ID: typing.Literal["getPreferredCountryLanguage"] = field(
        default="getPreferredCountryLanguage", metadata={"alias": "@type"}
    )
    country_code: String
