from playwright.sync_api import Page, expect

hompage_url = "https://automationexercise.com/"


def test_register_user(page: Page):
    # Navigate to the registration page
    page.goto(hompage_url)
    expect(page).to_have_title("Automation Exercise")

    page.locator("a[href='/login']").click()
    expect(page).to_have_url("https://automationexercise.com/login")
    expect(
        page.get_by_role(
            "heading",
            name="New User Signup!"
        )
    )

    page.locator("input[data-qa='signup-name']").fill("Jay Casamorin")
    page.locator("input[data-qa='signup-email']").fill("jay.casamorin@gmail.com")
    page.locator("button[data-qa='signup-button']").click()

    expect(page.get_by_role("heading", name="Enter Account Information")).to_be_visible()

    page.get_by_role("radio", name="Mr.").check()
    page.locator("input[data-qa='password']").fill("jaycasamorin")

    page.locator("select[data-qa='days']").select_option("17")
    page.locator("select[data-qa='months']").select_option("12")
    page.locator("select[data-qa='years']").select_option("1999")

    page.get_by_role("checkbox", name="Sign up for our newsletter!").check()
    page.get_by_role("checkbox", name="Receive special offers from our partners!").check()

    page.locator("input[data-qa='first_name']").fill("Jay")
    page.locator("input[data-qa='last_name']").fill("Casamorin")
    page.locator("input[data-qa='company']").fill("Example Company")
    page.locator("input[data-qa='address']").fill("123 Main St")
    page.locator("input[data-qa='address2']").fill("Apt 4B")

    page.get_by_role("combobox", name="Country").select_option("Canada")
    page.locator("input[data-qa='state']").fill("Ontario")
    page.locator("input[data-qa='city']").fill("Toronto")
    page.locator("input[data-qa='zipcode']").fill("M5H 2N2")
    page.locator("input[data-qa='mobile_number']").fill("+1 416-555-1234")
    page.locator("button[data-qa='create-account']").click()

    expect(page.get_by_role("heading", name="Account Created!")).to_be_visible()
    page.locator("a[data-qa='continue-button']").click()

    expect(page.get_by_role("listitem").filter(has_text="Logged in as Jay Casamorin")).to_be_visible()
    page.locator("a[href='/delete_account']").click()

    expect(page.get_by_role("heading", name="Account Deleted!")).to_be_visible()
    page.locator("a[data-qa='continue-button']").click()