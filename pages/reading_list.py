
from playwright.sync_api import Page, expect
import re

class ReadingListPage:

    """Page object for the reading list Sections"""
    SECTION_TO_TEST_ID = {
        "Katalog": "catalog",
        "Lägg till bok": "add-book",
        "Mina böcker": "favorites"
    }

    """Page object for the Add Book Form Section"""
    FORM_INPUT_TO_TEST_ID = {
        "Titel": "add-input-title",
        "Författare": "add-input-author"
    }


    """Initializes the ReadingListPage with a Playwright Page instance."""
    def __init__(self, page : Page):
        self.page = page
        self.last_book = {}

    def navigate_to(self, base_url: str):
        """Navigates to the application's base URL."""
        self.page.goto(base_url, timeout=10000)

    def check_main_heading_visible(self):
        """Checks that the main <h1> heading with 'Läslistan' is visible."""
        locator_h1 = self.page.get_by_text("Läslistan")
        expect(locator_h1).to_be_visible()

    def check_welcome_message_visible(self):
        """Checks that the <h2> heading with 'Välkommen!' is visible."""
        locator_h2 = self.page.get_by_text("Välkommen!")
        expect(locator_h2).to_be_visible()

    def check_content_message_visible(self):
        """Checks that the paragraph contains the expected welcome text."""
        locator_p = self.page.get_by_text("Sidan för dig som gillar att läsa. Välj dina favoriter.")
        expect(locator_p).to_be_visible()


    """Navigation buttons"""
    def check_navigation_button_visible(self, section: str):
        """Click navigation button visibility."""

        test_id = self.SECTION_TO_TEST_ID.get(section)
        if not test_id:
            raise ValueError(f"Unknown section: {section}")
        button = self.page.get_by_test_id(test_id)
        expect(button).to_be_visible()

    def click_on_navigation_button(self, section: str):
        """Click navigation button."""

        test_id = self.SECTION_TO_TEST_ID.get(section)
        if not test_id:
            raise ValueError(f"Unknown button label: {section}")

        button = self.page.get_by_test_id(test_id)
        expect(button).to_be_visible(timeout= 5000)

        if button.is_enabled():
            button.click()
        else:
            print(f'Button "{section}" is currently disabled. Skipping click.')

    def is_navigation_button_disabled(self, section: str) -> bool:
        """Returns True if the given navigation button is disabled."""

        test_id = self.SECTION_TO_TEST_ID.get(section)
        if not test_id:
            raise ValueError(f"Unknown button label: {section}")

        button = self.page.get_by_test_id(test_id)
        return not button.is_enabled()

    def are_navigation_buttons_enabled(self, sections: list[str]) -> bool:
        """Returns True if all specified navigation buttons are enabled."""

        for section in sections:
            test_id = self.SECTION_TO_TEST_ID.get(section)
            if not test_id:
                raise ValueError(f"Unknown button label: {section}")
            button = self.page.get_by_test_id(test_id)
            if not button.is_enabled():
                return False
        return True

    """Add book form """
    def are_fields_visible(self, fields: list[str]):
        """Checks that all form fields identified by label are visible."""
        for label in fields:
            test_id = self.FORM_INPUT_TO_TEST_ID.get(label.strip())
            if not test_id:
                raise ValueError(f"Unknown form field label: {label}")

            element = self.page.get_by_test_id(test_id)
            expect(element).to_be_visible(timeout=5000)

    def is_submit_button_disabled(self):
        """Checks submit button is disabled"""
        submit_button = self.page.get_by_test_id("add-submit")
        expect(submit_button).not_to_be_enabled(), "Submit button should be disabled initially"

    def is_submit_button_enabled(self) -> bool:
        """Form button state, enabled, disabled Lägg till ny bok."""
        return self.page.get_by_test_id("add-submit").is_enabled()

    def fill_form_field_by_label(self, field_label: str, value: str):
        """Fills a single input field identified by label."""

        test_id = self.FORM_INPUT_TO_TEST_ID.get(field_label.strip())
        if not test_id:
            raise ValueError(f"Label unknown: {field_label}")

        input_field = self.page.get_by_test_id(test_id)

        expect(input_field).to_be_visible(timeout=5000)

        input_field.fill(value.strip())

    def fill_add_book_form(self, title: str, author: str):
        """Fills out the form with title and author and stores data for later validation."""
        self.fill_form_field_by_label("Titel", title)
        self.fill_form_field_by_label("Författare", author)

        self.last_book = {"title": title, "author": author}

    def submit_new_book(self):
        """Submits the add book form."""
        submit_button = self.page.get_by_test_id("add-submit")
        expect(submit_button).to_be_enabled(timeout=3000)
        submit_button.click()


    """Catalog"""
    def check_book_in_catalog(self, title: str, author: str) -> bool:
        """Checks if a specific book with title and author is present and visible in the catalog."""

        pattern = rf'"\s*{re.escape(title)}\s*"\s*,\s*{re.escape(author)}\s*'
        regex = re.compile(pattern)

        books = self.page.locator(".book")
        count = books.count()

        for i in range(count):
            book_element = books.nth(i)
            text = book_element.inner_text().strip()
            if regex.search(text):
                expect(book_element).to_be_visible(), f'Book "{title}" by {author} is not visible'
                return True
        return False


    """Favorites"""
    def toggle_book_as_favorite(self, title: str) -> None:
        """Toggles the heart icon (star) for a specific book title in the catalog to either mark or unmark it as a favorite."""

        # Locate button on test ID- star
        star_button = self.page.get_by_test_id(f'star-{title}')

        # Check that button is visible
        expect(star_button).to_be_visible(timeout=3000)

        # Click button to change the state (mark/unmark)
        star_button.click()

        # Check if the button was marked as favorit (has the clas 'selected')
        if 'selected' in star_button.get_attribute('class'):
            expect(star_button).to_have_class(
                re.compile(r'\bselected\b')), f'The heart icon for "{title}" should be marked as favorite.'
        else:
            expect(star_button).not_to_have_class(
                re.compile(r'\bselected\b')), f'The heart icon for "{title}" should not be marked as favorite.'


    def is_book_in_favorites(self, title: str) -> bool:
        """Checks if a book with the given title is present in the 'Mina böcker' (favorites) section."""
        favorite_book = self.page.get_by_test_id(f"fav-{title}")
        try:
            expect(favorite_book).to_be_visible(timeout=3000)
            return True
        except Exception:
            return False




