from playwright.sync_api import Page
from time import sleep


def test_fill_the_practice_form(page: Page):
    page.goto("https://demoqa.com/automation-practice-form", wait_until="domcontentloaded")

    page.get_by_placeholder('First Name').fill('Egor')

    page.get_by_placeholder('Last Name').fill('Kovalenko')

    page.locator('#userEmail').fill('boogywoogy@mail.com')

    page.locator('//*[@for="gender-radio-1"]').click()

    page.locator('#userNumber').fill('+7923798323')

    page.locator('#dateOfBirthInput').click()

    page.locator('.react-datepicker__month-select').select_option('March')

    page.locator('.react-datepicker__year-select').select_option('1988')

    page.get_by_label('Choose Tuesday, March 22nd, 1988').click()

    subject_field = page.locator('#subjectsInput')
    subject_field.click()
    subject_field.fill('Bio')
    subject_field.press('Enter')

    page.locator('//*[@for="hobbies-checkbox-2"]').check()
    page.get_by_placeholder('Current Address').fill('asbasbjdhjshdjshdsahdsajdhsa')

    state_el = page.locator('#react-select-3-input')
    state_el.fill('N')
    state_el.press('Enter')

    city_el = page.locator('#react-select-4-input')
    city_el.fill('D')
    city_el.press('Enter')

    page.get_by_role('button', name='Submit').click()


def test_get_by_role(page: Page):
    page.goto('https://the-internet.herokuapp.com/', wait_until='domcontentloaded')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('eg')
    page.get_by_role('textbox', name='password').fill('kxea45ss_')
    page.get_by_role('button').click()
