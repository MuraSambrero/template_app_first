from pydantic import BaseModel, validator
from typing import Optional, Literal, Set
import re

class FormField(BaseModel):
    name: str
    value: str
    type: Optional[Literal["email", "phone", "date", "text"]] = None

    @validator("type", pre=True, always=True)
    def set_type(cls, v, values):
        if v is not None:
            return v
        phone_regex = r"\+7\d{10}$"
        date_regex = r"\d{2}.\d{2}.\d{4}$|\d{4}-\d{2}-\d{2}$"
        email_regex = r"^\S+@\S+\.\S+$"

        value = values.get("value")
        if re.match(date_regex, value):
            return "date"
        elif re.match(phone_regex, value):
            return "phone"
        elif re.match(email_regex, value):
            return "email"
        return "text"

    def __eq__(self, other):
        return self.name == other.name and \
            self.type == other.type

    def __hash__(self):
        return hash(self.name)


class Form(BaseModel):
    fields: Set[FormField, ]