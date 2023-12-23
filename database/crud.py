from models.template_model import Template, TemplateField
from config import Config


def get_valid_templates(client) -> list[Template]:
    templates = [
        Template(
            name=elem['name'],
            fields=[
                TemplateField(
                    name=key, type=value
                )
                for key, value in elem.items() if key != 'name'
            ]
        )
        for elem in get_templates(client)
    ]
    return templates


def get_templates(client) -> list[dict]:
    db = client[Config.mongo_init_db_name]
    collection = db[Config.collection_name]
    templates = [
        {
            name: type for name, type in template.items() if name != '_id'
        }
        for template in collection.find()
    ]
    return templates

# for elem in fake_db: # Для добавления fake_db в бд MongoDB
#     append_template(client, elem)
