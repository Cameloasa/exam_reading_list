from behave import then

@then('fältet "{field}" ska vara synligt')
def step_field_should_be_visible(context, field):
    context.reading_list.are_fields_visible([field])

@then(u'knappen "Lägg till ny bok" ska vara inaktiverad')
def step_then_submit_button_disabled(context):
    context.reading_list.is_submit_button_disabled()


