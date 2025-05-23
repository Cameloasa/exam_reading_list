from playwright.sync_api import sync_playwright
from pages.reading_list import ReadingListPage


def before_all(context):
    # Starta Playwright
    playwright  = sync_playwright().start()
    browser = playwright.chromium.launch(headless= True)
    context.playwright  = playwright
    context.browser = browser

def before_scenario(context, scenario):
    # Öppna en ny webbsida före varje scenario
    context.page = context.browser.new_page()
    context.base_url = "https://tap-ht24-testverktyg.github.io/exam-template/"
    context.reading_list = ReadingListPage(context.page)

def after_scenario(context, scenario):
    # Stäng webbsidan efter varje scenario
    context.page.close()

def after_all(context):
    # Stäng browsern och stoppa Playwright när alla tester är klara
    context.browser.close()
    context.playwright.stop()
