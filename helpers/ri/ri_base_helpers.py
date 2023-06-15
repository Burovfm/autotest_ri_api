import testit


@testit.step("Создание нового application_uuid для существующего customer_id")
def help_create(ri, application_uuid=None, customer_id=None, application_name=None, description=None):
    body = {
        "application_uuid": application_uuid,
        "customer_id": customer_id,
        "application_name": application_name,
        "description": description
    }
    return ri.create(json_data=body)


@testit.step("Проверить данные приложения для существующего customer_id")
def help_get_application(ri, customer_id, application_uuid):
    body = {
        "customer_id": customer_id,
        "application_uuid": application_uuid

    }
    return ri.get_application(json_data=body)
