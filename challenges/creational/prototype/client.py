from product import Product

def main():
    complex_product_a = Product('Product A',['us','ca'])
    print(f"The address memory of product A is->{id(complex_product_a)}")

    """
    Create a new complex product by cloning the previous one.
    """
    complex_product_b = Product('Product B',['mx'])
    print(f"The address memory of product B is->{id(complex_product_b)}")

if __name__ == '__main__':
    main()