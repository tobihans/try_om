from datetime import date
from typing import Optional

from redis_om import HashModel


class Language(HashModel):
    name: str
    author: str
    creation_date: date
    nb_of_keywords: Optional[int]

    def __str__(self) -> str:
        if self.nb_of_keywords:
            return f"{self.name}({self.nb_of_keywords} keywords) was created by {self.author} in {self.creation_date.year}."

        return f"{self.name} was created by {self.author} in {self.creation_date.year}."


python = Language(
    name="Python", author="Guido van Rossum", creation_date="1991", nb_of_keywords=38
)
rust = Language(
    name="Rust", author="Graydon Hoare", creation_date="2010", nb_of_keywords=53
)
typescript = Language(
    name="TypeScript", author="Anders Hejlsberg", creation_date="2012"
)
nim = Language(
    name="Nim", author="Andreas Rumpf", creation_date="2008", nb_of_keywords=70
)

python.save()
rust.save()
typescript.save()
nim.save()

print(Language.get(rust.pk))
