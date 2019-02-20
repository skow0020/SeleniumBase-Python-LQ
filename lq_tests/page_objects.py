class Page(object):
    html = "www.literaryquicksand.com"


class Header(Page):
    header = '.menu_post_header'
    categories = '=CATEGORIES'


class HomePage(Page):
    href = "/"
    page_header = '[alt="Literary Quicksand"]'
    email = 'input[name="EMAIL"]'
    sign_up = 'input[value="Sign me up!"]'


class CategoryBookLists(Page):
    href = '/category/book-lists'
    book_lists_header = '.title_category'


class ContributorsPage(Page):
    href = '/contributors'
    page_header = '.page-content h1'
    contributor_Joli = '=Joli'


class WriteForUsPage(Page):
    href = '/contact/write-for-us'
    page_header = ".page-content h2"
    name_input = "[name=your-name]"
    email_input = "[name=your-email]"
    send_button = "[value=send]"
