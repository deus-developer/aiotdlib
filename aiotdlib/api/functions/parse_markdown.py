# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing
from dataclasses import dataclass, field

from ..types.all import (
    FormattedText,
)
from ..types.base import *


@dataclass(slots=True, kw_only=True)
class ParseMarkdown(BaseObject):
    """
    Parses Markdown entities in a human-friendly format, ignoring markup errors. Can be called synchronously

    :param text: The text to parse. For example, "__italic__ ~~strikethrough~~ ||spoiler|| **bold** `code` ```pre``` __[italic__ text_url](telegram.org) __italic**bold italic__bold**"
    :type text: :class:`FormattedText`
    """

    ID: typing.Literal["parseMarkdown"] = field(default="parseMarkdown", metadata={"alias": "@type"})
    text: FormattedText
