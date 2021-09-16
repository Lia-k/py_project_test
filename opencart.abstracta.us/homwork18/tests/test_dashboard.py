def test_check_found_iphone_via_search_field(dashboard, product_list):
    dashboard.find_item_with_search_field("iPhone")
    product_list.check_searched_element_is_displayed("iPhone")


def test_check_imac_product_category_choosing(dashboard, product_list):
    dashboard.choose_category("1")
    dashboard.choose_sub_category("2")
    product_list.check_searched_element_is_displayed("iMac")
