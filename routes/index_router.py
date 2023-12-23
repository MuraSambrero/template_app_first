from fastapi import APIRouter, Request
from models.form_model import Form, FormField
from controllers.add_form_controller import find_template, field_and_type_form

index_router = APIRouter()

@index_router.post("/get_form")
def get_form(request: Request):
    form_data = request.query_params.items()
    form_fields = [FormField(name=elem[0], value=elem[1]) for elem in form_data]
    new_form = Form(fields=set(form_fields))
    template_name = find_template(new_form)
    if template_name is None:
        return field_and_type_form(new_form.fields)
    return template_name
