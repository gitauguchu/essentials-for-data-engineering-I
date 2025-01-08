def calculate_discounted_price(price, discount):
    """
    This functions takes the price and calculates the discount based on the discount percentage specified
    Returns: float
    """

    return price * (1-discount / 100)

help(calculate_discounted_price)