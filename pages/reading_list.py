from playwright.sync_api import Page, expect

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

    BOOK_LIST = {

    }

    """Initializes the ReadingListPage with a Playwright Page instance."""
    def __init__(self, page : Page):
        self.page = page

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
        """Checks that all form fields identified by label are visible and submit button is disabled."""
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
        """Fills the input field for the specified label with the provided value."""

        test_id = self.FORM_INPUT_TO_TEST_ID.get(field_label)
        if not test_id:
            raise ValueError(f"Label unknown: {field_label}")

        input_field = self.page.get_by_test_id(test_id)
        expect(input_field).to_be_visible(timeout=5000)
        input_field.fill(value)
