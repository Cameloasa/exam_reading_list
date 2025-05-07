from behave import when, then

@when(u'användaren favoritmarkerar boken "{title}"')
def step_when_mark_as_favorit(context,title):
    context.reading_list.toggle_book_as_favorite(title)

@then(u'boken "{title}" av "{author}" visas i Mina böcker')
def step_book_visible_in_favorites(context, title, author):
    assert context.reading_list.is_book_in_favorites(title), f'Book "{title}" by {author} was not found in favorites'

@when(u'användaren favoritmarkerar boken "{title}" igen')
def step_when_mark_as_favorit(context, title):
    context.reading_list.toggle_book_as_favorite(title)

@then(u'boken "{title}" av "{author}" visas inte i Mina böcker')
def step_then_book_not_visible_in_favorites(context, title, author):
    assert not context.reading_list.is_book_in_favorites(title), f'Book "{title}" by {author} was found in favorites'





