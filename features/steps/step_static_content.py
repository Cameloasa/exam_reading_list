from behave import given,then

@given(u'användaren är på startsidan')
def step_given_start_page(context):
    context.reading_list.navigate_to(context.base_url)

@then(u'texten "Läslistan" ska visas')
def step_then_title_visible(context):
    context.reading_list.check_main_heading_visible()


@then(u'texten "Välkommen!" ska visas')
def step_then_subtitle_visible(context):
    context.reading_list.check_welcome_message_visible()

@then(u'texten "Sidan för dig som gillar att läsa. Välj dina favoriter." ska visas')
def step_then_text_visible(context):
    context.reading_list.check_content_message_visible()








