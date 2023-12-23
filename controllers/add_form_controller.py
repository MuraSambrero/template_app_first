from database.crud import get_valid_templates
from database.database import client
from models.form_model import Form


def find_template(new_form: Form) -> str | None:
    templates = get_valid_templates(client)
    for template in templates:
        is_valid_template_field_and_type = template.fields.issubset(new_form.fields)
        if is_valid_template_field_and_type is False:
            continue
        print(new_form.fields)
        return template.name
    return None


def field_and_type_form(form_fields) -> dict:
    form = dict()
    for elem in form_fields:
        form[elem.name] = elem.type
    return form
