from pydantic import BaseModel
from typing import Literal, Set, Optional

class TemplateField(BaseModel):
    name: str
    type: Optional[Literal["email", "phone", "date", "text"]] = None

    def __eq__(self, other):
        return self.name == other

    def __hash__(self):
        return hash(self.name)

class Template(BaseModel):
    name: str
    fields: Set[TemplateField]






# '''Валидация для каждого поля в отдельности'''
# class EmailCheck(BaseModel):
#     email: EmailStr
#
# def is_email(some_email):
#     try:
#         EmailCheck(email=some_email)
#         return 'email'
#     except ValueError as error:
#         return False
#
# # mail = 'neonesyandex.ru'
# # my_mail = is_email(mail)
# # print(my_mail)
#
# class PhoneCheck(BaseModel):
#     phone: str
#
#     @field_validator('phone')
#     def check_phone(cls, v):
#         regex = r'\+7[0-9]{10}$'
#         phone_field = v
#         if phone_field and not re.match(regex, phone_field):
#             raise ValueError("Phone Number Invalid.")
#         return True
#
# def is_phone(some_phone):
#     try:
#         PhoneCheck(phone=some_phone)
#         return 'phone'
#     except ValueError as error:
#         return False
#
# phone = '+79248200008'
# my_phone = is_phone(phone)
# print(my_phone)



