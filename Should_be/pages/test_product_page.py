from Product_page import ProductPage

def test_guest_can_add_product_to_cart(browser):
    link = "http://10.11.18.78/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()

