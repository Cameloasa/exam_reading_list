from behave import given
from pages.reading_list import ReadingListPage

@given(u'användaren är på startsidan')
def step_given_start_page(context,base_url):
    context.reading_list.navigate_to(context.base_url)

