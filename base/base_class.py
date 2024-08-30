class Base:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        print(f"Current URL - {self.driver.current_url}")

    @staticmethod
    def check_title(title, check_title):
        assert title.text == check_title
        print(f'Title "{check_title}" successfully verified')

    def check_url(self, check_url):
        assert self.driver.current_url == check_url
        print(f'URL "{check_url}" successfully verified')
