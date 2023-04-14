from product import Product

def main():
    productWithAlias = Product(1,'a','Product A','',100,[],'Alias A')
    print(f"Product with alias->{productWithAlias.__dict__}")

    productWithoutAlias = Product(2,'b','Product B','',100,[],'')
    print(f"Product without Alias->{productWithoutAlias.__dict__}")

    productWithCountries = Product(3,'c','Product C','',100,['mx','usr','ca'],'')
    print(f"Product with countries{productWithCountries.__dict__}")

    productWithDescription = Product(4,'a','Product D','Description ABC',100,['mx','usr','ca'],'')
    print(f"Product with description->{productWithDescription.__dict__}")

if __name__ == '__main__':
    main()