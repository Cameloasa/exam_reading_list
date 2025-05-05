from behave import then, when

@then(u'ska navigeringsknappen "{section}" vara synlig')
def step_then_navigation_buttons_visible(context, section):
    context.reading_list.check_navigation_button_visible(section)

@when(u'användaren klickar på navigeringsknappen "{section}"')
def step_when_click_on_navigation_buttons(context, section):
    context.reading_list.click_on_navigation_button(section)

@then('ska navigeringsknappen "{section}" vara inaktiverad')
def step_check_button_disabled(context, section):
    assert context.reading_list.is_navigation_button_disabled(section), \
        f'Knappen "{section}" borde vara inaktiverad men är aktiverad.'

@then('ska navigeringsknapparna "{sections}" vara aktiverade')
def step_check_buttons_enabled(context, sections):
    section_list = [l.strip() for l in sections.split(",")]
    assert context.reading_list.are_navigation_buttons_enabled(section_list), \
        f'Någon av knapparna {section_list} är inte aktiverad som förväntat.'



