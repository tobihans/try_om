from datetime import date
from typing import Optional
from redis_om import HashModel

class Language(HashModel):
    author: str
    creation_date: date
    nb_ob_keywords: Optional[int]

python = Language(author="Guido van Rossum", creation_date="1991", nb_of_keywords = 38)
rust = Language(author="Graydon Hoare", creation_date="2010")
typescript = Language(author="Anders Hejlsberg", creation_date="2012")
nim = Language(author="Andreas Rumpf", creation_date="2008")

print(nim.pk)
print(nim.creation_date, type(nim.creation_date))
