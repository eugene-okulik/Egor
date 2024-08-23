from playwright.sync_api import Page, expect, BrowserContext, Dialog


def test_ok(page: Page):
    def accept_alert(alert: Dialog):
        alert.accept()

    page.on('dialog', accept_alert)
    page.goto('https://www.qa-practice.com/elements/alert/confirm', wait_until='domcontentloaded')
    page.get_by_role('link', name='Click').click()

    expect(page.locator('#result-text')).to_have_text('Ok')


def test_button_enabled(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button', wait_until="domcontentloaded")

    click_button = page.get_by_role('link', name='Click')
    with context.expect_page() as new_page_event:
        click_button.click()

    new_page = new_page_event.value
    result = new_page.locator('#result-text')

    expect(result).to_have_text('I am a new page in a new tab')
    new_page.close()

    expect(page.get_by_role('link', name='Click')).to_be_enabled()


def test_color_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties', wait_until='domcontentloaded')

    locator = page.locator('#colorChange')
    expect(locator).to_have_css("color", "rgb(255, 255, 255)", timeout=100)
    locator.click()
