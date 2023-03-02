from dataclasses import dataclass, asdict
from typing import Literal

@dataclass
class Registration:   
    cpf: int
    name: str 
    birth_date: str
    type_customer: Literal['LP', 'AA'] = 'ALL'

    def as_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return Registration(**data)