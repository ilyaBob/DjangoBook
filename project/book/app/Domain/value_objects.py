from dataclasses import dataclass

from slugify import slugify


class Slug:

    @classmethod
    def format_str(self, value: str) -> str:
        return slugify(value)
