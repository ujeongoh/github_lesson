def dec_to_hex(decimal_num):
    """Converts a decimal number to a hexadecimal string.

    Args:
        decimal_num (int): The decimal number to convert.

    Returns:
        str: The hexadecimal string representation of the decimal number.
    """
    hex_chars = '0123456789ABCDEF'
    hex_str = ''
    while decimal_num > 0:
        remainder = decimal_num % 16
        hex_str = hex_chars[remainder] + hex_str
        decimal_num //= 16
    return hex_str or '0'
