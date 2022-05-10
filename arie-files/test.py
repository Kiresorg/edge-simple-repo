import unittest


class TestAddProductsToCart(unittest.TestCase):
    """
        Add to cart unit test
    """

    def test_add_products_to_cart(self):
        product_list = [
                "2% milk, 1 gallon",
                "salted butter, 1 lb",
                "iceberg lettuce, 1 head"            
            ]

        actual_cart = add_products_to_cart(product_list)

        expected_cart = {
            "your_cart": [
                "2% milk, 1 gallon",
                "salted butter, 1 lb",
                "iceberg lettuce, 1 head"            
            ]
        }

        self.assertEqual(actual_cart, expected_cart)

    def test_add_too_many_products_to_cart(self):

        product_list = ["candy bar"] * 25

        with self.assertRaises(ValueError) as exception_context:
            add_products_to_cart(product_list)

        self.assertEqual(
            str(exception_context.exception),
            "You may not add more than 10 products at a time to your cart."
        )

    
class SortCartTest(unittest.TestCase):
    """
        Sort cart unit test
    """
    def test_sort_cart(self):

        unsorted_cart = {
            "your_cart": [
                "greenbeans",
                "potatoes",
                "tomatoes",
                "apples"
            ]
        }

        expected_cart = {
            "your_cart": [
                "apples",
                "greenbeans",
                "potatoes",
                "tomatoes"
            ]
        }

        sort_cart(unsorted_cart)

        self.assertEqual(unsorted_cart, expected_cart)


def add_products_to_cart(product_list):
    if len(product_list) > 10:
        raise ValueError("You may not add more than 10 products at a time to your cart.")
    return {"your_cart": product_list}

def sort_cart(cart):
    sorted_list = sorted(cart['your_cart'])
    cart['your_cart'] = sorted_list

if __name__ == "__main__":
    addProducts = add_products_to_cart(["tomatoes", "oranges", "apples", "milk"])
    print(addProducts)
    sort_cart(addProducts)
    print(addProducts)