import re

from jsonschema import validate


def assert_json_schema(response, schema):
    validate(response, schema)


def get_body_error_msg(msg, param_name=''):
    if msg.find(':') >= 0:
        list_msg = msg.split(';')
        errors = list()
        for i in list_msg:
            result = re.search(f'{param_name}: ([^\n]+)', i)
            try:
                errors.append(result.group(0))
            except AttributeError:
                raise Exception(f"{param_name} not found")
        return sorted(list(set(errors)))
    else:
        return msg

