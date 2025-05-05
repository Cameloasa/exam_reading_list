from playwright.sync_api import Page, expect

class ReadingListPage:
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
        section_to_test_id = {
            "Katalog": "catalog",
            "Lägg till bok": "add-book",
            "Mina böcker": "favorites"
        }
        test_id = section_to_test_id.get(section)
        if not test_id:
            raise ValueError(f"Unknown section: {section}")
        button = self.page.get_by_test_id(test_id)
        expect(button).to_be_visible()

    def click_on_navigation_button(self, section: str):
        """Click navigation button."""
        section_to_test_id = {
            "Katalog": "catalog",
            "Lägg till bok": "add-book",
            "Mina böcker": "favorites"
        }
        test_id = section_to_test_id.get(section)
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
        section_to_test_id = {
            "Katalog": "catalog",
            "Lägg till bok": "add-book",
            "Mina böcker": "favorites"
        }
        test_id = section_to_test_id.get(section)
        if not test_id:
            raise ValueError(f"Unknown button label: {section}")

        button = self.page.get_by_test_id(test_id)
        return not button.is_enabled()

    def are_navigation_buttons_enabled(self, sections: list[str]) -> bool:
        """Returns True if all specified navigation buttons are enabled."""
        section_to_test_id = {
            "Katalog": "catalog",
            "Lägg till bok": "add-book",
            "Mina böcker": "favorites"
        }

        for section in sections:
            test_id = section_to_test_id.get(section)
            if not test_id:
                raise ValueError(f"Unknown button label: {section}")
            button = self.page.get_by_test_id(test_id)
            if not button.is_enabled():
                return False
        return True

