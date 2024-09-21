import re
from playwright.sync_api import Page, expect, Route
import json


def test_request_replace(page: Page):
    new_header = 'яблокофон 16 про'

    def change_response_header_name(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = new_header
        new_body = json.dumps(body)
        route.fulfill(
            response=response,
            body=new_body
        )

    page.route(re.compile('library/step0_iphone/digitalmat'), change_response_header_name)
    page.goto('https://www.apple.com/shop/buy-iphone')
    btn_iphone = page.get_by_role("heading", name="iPhone 16 Pro & iPhone 16 Pro")
    btn_iphone.click()
    header = page.get_by_role("heading", name=new_header)
    expect(header).to_have_text(new_header)
