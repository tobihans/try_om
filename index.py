from datetime import date
from typing import Optional
from redis_om import HashModel

class Language(HashModel):
    author: str
    creation_date: date
    nb_ob_keywords: Optional[int]

python = Language(author="Guido van Rossum", creation_date=date(year=1991, month=1, day=1), nb_of_keywords = 38)
rust = Language(author="Graydon Hoare", creation_date=date(year=2010, month=1, day=1))
typescript = Language(author="Anders Hejlsberg", creation_date=date(year=2012, month=1, day=1))
nim = Language(author="Andreas Rumpf", creation_date=date(year=2008, month=1, day=1))
