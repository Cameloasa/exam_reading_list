from behave import then, when

@then(u'ska navigeringsknappen "{section}" vara synlig')
def step_impl(context, section):
    context.reading_list.check_navigation_button_visible(section)

@when(u'användaren klickar på "Katalog"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When användaren klickar på "Katalog"')

