from __future__ import annotations

import re

from typing import Optional

from commitizen import defaults

from .base import BaseFormat


class AsciiDoc(BaseFormat):
    extension = "adoc"

    RE_TITLE = re.compile(r"^(?P<level>=+) (?P<title>.*)$")

    def parse_version_from_title(self, line: str) -> Optional[str]:
        m = self.RE_TITLE.match(line)
        if not m:
            return None
        # Capture last match as AsciiDoc use postfixed URL labels
        matches = list(re.finditer(defaults.version_parser, m.group("title")))
        if not matches:
            return None
        return matches[-1].group("version")

    def parse_title_level(self, line: str) -> Optional[int]:
        m = self.RE_TITLE.match(line)
        if not m:
            return None
        return len(m.group("level"))
