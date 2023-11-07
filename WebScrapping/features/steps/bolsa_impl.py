from behave import *

@given('that the user access bolsa.es')
def step_impl(context):
    pass

@given('the following fields are displayed')
def check_fields(context):
    fields = context.tester.get_fields_name()
    for f in context.table:
        assert f["Field Name"] in fields

@then('get fields values')
def print_fields_values(context):
    context.tester.display_fields_values()
