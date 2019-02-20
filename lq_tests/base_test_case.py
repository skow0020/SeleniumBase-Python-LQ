from seleniumbase import BaseCase


class BaseTestCase(BaseCase):

    def setUp(self):
        super(BaseTestCase, self).setUp()
        # Add custom setUp code for your tests AFTER the super().setUp()

    def tearDown(self):
        # Add custom tearDown code for your tests BEFORE the super().tearDown()
        super(BaseTestCase, self).tearDown()
