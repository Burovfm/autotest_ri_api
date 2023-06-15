import pytest
import testit

from hamcrest import assert_that, equal_to, contains_string
from helpers.ri.error_texts import (error_create_application_already_exist,
                                    error_invalid_uuid_format, error_value_length_must_between_1_or_36,
                                    error_method_empty_body, error_method_empty_param)
from helpers.ri.schema_methods import (schema_response_error)
from helpers.base_helpers import assert_json_schema, get_body_error_msg
from helpers.ri.ri_base_helpers import help_get_application
from helpers.exceptions import StatusCode4XX
from helpers.generate_data import generate_text, generate_uuid


class Test200:
    @pytest.mark.Smoke
    @testit.workItemIds(39184)
    @testit.displayName('Создание нового application_uuid для существующего customer_id')
    @testit.externalId('Создание нового application_uuid для существующего customer_id')
    @testit.title('Создание нового application_uuid для существующего customer_id')
    def test_create_application(self, ri):
        application_uuid = generate_uuid()
        application_name = generate_text(min_chars=10, max_chars=36)
        description = generate_text(min_chars=10, max_chars=36)
        customer_id = 94359
        with testit.step('Вызвать метод Create - создать новое приложение с корректными параметрами'):
            body = {
                "application_uuid": application_uuid,
                "customer_id": customer_id,
                "application_name": application_name,
                "description": description
            }
            response = ri.create(json_data=body).json()
        with testit.step('Проверить значение параметра success'):
            assert_that(
                actual_or_assertion=response.get('success'),
                matcher=equal_to(True)
            )
        application_data = help_get_application(ri, customer_id, application_uuid).json()
        with testit.step('dfjhsgdhs'):
            assert_that(
                actual_or_assertion=application_data.get('application_name'),
                matcher=equal_to(application_name)
            )

            assert_that(
                actual_or_assertion=application_data.get('application_uuid'),
                matcher=equal_to(application_uuid)
            )

            assert_that(
                actual_or_assertion=application_data.get('description'),
                matcher=equal_to(description)
            )


class Test400:
    @pytest.mark.Smoke
    @testit.workItemIds(39034)
    @pytest.mark.xfail(raises=StatusCode4XX)
    @testit.displayName('Повторное создание существующего application_uuid')
    @testit.externalId('Повторное создание существующего application_uuid')
    def test_create_an_applications_with_the_same_app_uuid(self, ri):
        application_uuid = generate_uuid()
        application_name = generate_text(min_chars=10, max_chars=36)
        description = generate_text(min_chars=10, max_chars=36)
        customer_id = 94359
        with testit.step('Вызвать метод Create - создать новое приложение с корректными параметрами'):
            body = {
                "application_uuid": application_uuid,
                "customer_id": customer_id,
                "application_name": application_name,
                "description": description
            }
            response = ri.create(json_data=body).json()
        with testit.step('Проверить значение параметра success'):
            assert_that(
                actual_or_assertion=response.get('success'),
                matcher=equal_to(True)
            )
            app_name_used = application_name
        with testit.step('Вызвать метод Create - создать второе приложение c application_uuid из первого приложения'):
            body = {
                "application_uuid": application_uuid,
                "customer_id": customer_id,
                "application_name": app_name_used,
                "description": description
            }
            response = ri.create(json_data=body).json()
            error_msg = response.get('error')
        with testit.step('Проверить схему ответа метода'):
            assert_json_schema(response, schema_response_error)
        with testit.step('Проверить вывод ошибки'):
            assert_that(
                actual_or_assertion=get_body_error_msg(msg=error_msg, param_name="ERROR"),
                matcher=equal_to([error_create_application_already_exist(application_name=app_name_used)])
            )

    @pytest.mark.Regress
    @testit.workItemIds(65387)
    @testit.displayName('Создание нового приложение (пустое тело запроса)')
    @testit.externalId('Создание нового приложение (пустое тело запроса)')
    def test_create_application_without_parameters(self, ri):
        with testit.step('Создание нового приложение (пустое тело запроса)'):
            response = ri.create(json_data={}).json()
        with testit.step('Проверить сообщение об ошибке'):
            error_msg = response.get('error')
            assert_that(
                actual_or_assertion=error_msg,
                matcher=contains_string(error_method_empty_body("CreateRequest.ApplicationUuid"))
            )

    @pytest.mark.Regress
    @testit.workItemIds(39036)
    @testit.displayName('Валидация  поля application_uuid  в методе Create')
    @testit.externalId('Валидация  поля application_uuid  в методе Create')
    @pytest.mark.parametrize("application_uuid, error_text", [
        ("q" * 37, error_value_length_must_between_1_or_36("CreateRequest.ApplicationUuid")),
        (" ", error_method_empty_param("CreateRequest.ApplicationUuid")),
        ([], error_invalid_uuid_format("string", "["))
    ])
    def test_validate_application_name(self, ri, application_uuid, error_text):
        with testit.step('Вызвать метод CreateApplication с невалидным application_uuid'):
            body = {
                "application_uuid": application_uuid
            }
            response = ri.create(json_data=body).json()
        with testit.step('Проверить сообщение об ошибке'):
            assert_that(
                actual_or_assertion=response.get("error"),
                matcher=contains_string(error_text)
            )
