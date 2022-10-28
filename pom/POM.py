# https://symonstorozhenko.wixsite.com/website-1/contact

class ContactPage:
    def __init__(self, page):
        self.page = page
        # self.search_term_input = page.locator('[aria-label="Enter your search term"]')

    def navigate(self):
        self.page.goto("https://symonstorozhenko.wixsite.com/website-1/contact")

    def submit_form(self, name, address, email, phone, subject, message):
        self.page.get_by_placeholder("Enter your name").click()
        self.page.get_by_placeholder("Enter your name").fill(name)
        self.page.get_by_placeholder("Enter your address").fill(address)
        self.page.get_by_placeholder("Enter your email").fill(email)
        self.page.get_by_placeholder("Enter your phone number").fill(phone)
        self.page.get_by_placeholder("Type the subject").click()
        self.page.get_by_placeholder("Type the subject").fill(subject)
        self.page.get_by_placeholder("Type your message here...").fill(message)


