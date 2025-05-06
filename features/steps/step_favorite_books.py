from behave import when, then
#TODO
@when(u'användaren favoritmarkerar boken "{title}"')
def step_when_click_on_books(context,title):
    context.reading_list.mark_book_as_favorite(title)

@then(u'boken "{title}" av "{author}" visas i Mina böcker')
def step_book_visible_in_favorites(context, title, author):
    assert context.reading_list.is_book_in_favorites(title), f'Book "{title}" by {author} was not found in favorites'
