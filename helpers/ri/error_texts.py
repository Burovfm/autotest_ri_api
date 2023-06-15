def error_create_application_already_exist(application_name):
    return f'ERROR: Application name [{application_name}] already exist (SQLSTATE AO026)'


def error_method_empty_body(param_name) -> str:
    return f'invalid {param_name}: value length must be 36 runes'


def error_method_empty_param(param_name) -> str:
    return f'invalid {param_name}: value length must be 36 runes'


def error_value_length_must_between_1_or_36(param_name) -> str:
    return f'invalid {param_name}: value length must be 36 runes'


def error_invalid_uuid_format(param_type, value) -> str:
    return f'invalid value for {param_type} type: {value}'



