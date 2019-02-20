from .base_test_case import BaseTestCase
from .page_objects import HomePage


class MyTestClass(BaseTestCase):

    def test_email_signup(self):
        self.open('http://www.literaryquicksand.com')
        self.click(HomePage.email)
        self.update_text(HomePage.email, 'skow0020@gmail.com')
        self.click(HomePage.sign_up)
