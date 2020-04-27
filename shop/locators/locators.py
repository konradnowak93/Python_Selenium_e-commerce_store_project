class MainPageLocators:

    information_banner_class = "woocommerce-store-notice__dismiss-link"
    my_wish_list_xpath = "//*[@id='noo-site']/header/div[1]/div/ul[2]/li[1]/a"
    my_account_css = "#noo-site > header > div.noo-topbar > div > ul.pull-right.noo-topbar-right > li:nth-child(2) > a"
    checkout_xpath = "//*[@id='noo-site']/header/div[1]/div/ul[2]/li[3]/a"
    search_field_class = "icon_search"
    search_field_input_class = "form-control"
    shopping_cart_xpath = "//*[@id='nav-menu-item-cart']/a/span/span[2]"
    main_logo_class = "custom-logo"
    page_title_class = "page-title"

class MyAccountLocators:

    register_username_id = "reg_username"
    register_mail_id = "reg_email"
    register_password_id = "reg_password"
    register_button_name = "register"
    go_back_to_shop_button_xpath = "//p[@id='backtoblog']//a"
    login_username_or_email_id = "username"
    login_password_id = "password"
    login_button_name = "login"
    back_to_blog_button_xpath = "//*[@id='backtoblog']/a"
    logout_button_xpath = "//*[@id='post-8']/div/div/nav/ul/li[6]/a"

class ProductsListLocators:
    products_list_xpath = "//div[contains(@class, 'noo-product-inner')]//h3"

class ProductPageLocators:
    product_colour_id = "pa_color"
    product_size_id = "pa_size"
    add_to_wishlist_xpath = "//*[@id='product-1162']/div[1]/div[2]/div[1]/div/a"
    add_to_cart_first_product_xpath = "//*[@id='product-1162']/div[1]/div[2]/form/div/div[2]/button"
    add_to_cart_second_product_xpath = "//*[@id='product-1485']/div[1]/div[2]/form/div/div[2]/button"
    product_added_to_cart_class = "woocommerce-message"
    view_cart_xpath = "//*[@id='noo-site']/div[2]/div/div/div[1]/div/a"

class WishlistLocators:
    remove_from_wishlist_button_xpath = "//*[@id='yith-wcwl-row-1162']/td[1]/div/a"
    select_options_xpath = "//*[@id='yith-wcwl-row-1162']/td[6]/a"
    successfully_removed_xpath = "//*[@id='yith-wcwl-form']/div[1]"
    successfully_removed_class = "woocommerce-message"

class ShoppingCartLocators:
    remove_from_cart_xpath = "//*[@id='post-6']/div/div/form/table/tbody/tr[1]/td[6]/a"
    clear_cart_class = "empty-cart"
    update_cart_name = "update_cart"
    continue_shopping_class = "continue"
    increase_qty_class = "qty-increase"
    decrease_qty_class = "qty-qty-decrease"
    proceed_to_checkout_xpath = "//*[@id='post-6']/div/div/div[2]/div[2]/div/a"
    successfully_removed_class = "woocommerce-message"
    successfully_emptied_xpath = "//*[@id='post-6']/div/div/p[1]"
    successfully_updated_xpath = "//*[@id='post-6']/div/div/div[1]"

class CheckoutLocators:
    order_review_heading_id = "order_review_heading"
    billing_first_name_id = "billing_first_name"
    billing_last_name_id = "billing_last_name"
    billing_company_id = "billing_company"
    countries_list_xpath = "//*[@id='billing_country']"
    house_and_street_id = "billing_address_1"
    apartment_id = "billing_address_2"
    billing_postcode_id = "billing_postcode"
    billing_city_id = "billing_city"
    billing_phone_id = "billing_phone"
    billing_email_id = "billing_email"
    terms_conditions_xpath = "//*[@id='terms']"
    place_order_id = "place_order"
    order_received_class = "woocommerce-thankyou-order-received"