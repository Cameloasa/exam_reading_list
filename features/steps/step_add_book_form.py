from behave import then,when

@then('fältet "{field}" ska vara synligt')
def step_field_should_be_visible(context, field):
    context.reading_list.are_fields_visible([field])

@then(u'knappen "Lägg till ny bok" ska vara inaktiverad')
def step_then_submit_button_disabled(context):
    context.reading_list.is_submit_button_disabled()

@when(u'användaren fyller i "{field}" med "{value}"')
def step_when_fill_add_book_form(context, field, value):
    context.reading_list.fill_form_field_by_label(field, value)

@then(u'knappen "Lägg till ny bok" ska vara aktiverad')
def step_then_submit_button_enabled(context):
    context.reading_list.is_submit_button_enabled()




