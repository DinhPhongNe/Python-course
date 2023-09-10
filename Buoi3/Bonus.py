# Nhập các tỉ giá chuyển đổi
rate = {'USD': 30500, 'EUR': 31500, 'JPY': 225,
        'GBP': 42000, 'AUD': 22400, 'CAD': 23000, 
        'CHF': 28500, 'CNY': 4600, 'HKD': 3950,
        'IDR': 2150, 'INR': 410, 'KRW': 27, 
        'MYR': 7150, 'PHP': 610, 'SGD': 22250,
        'THB': 875, 'VND': 1, 'RUB': 500, 
        'MXN': 650, 'BRL': 5350}

# Hàm chuyển đổi
def currency_convert(amount, from_currency, to_currency):
  
    # Lấy tỉ giá chuyển đổi từ tiền tệ này sang tiền tệ khác
    from_rate = rate[from_currency]  
    to_rate = rate[to_currency]  

    # Thực hiện chuyển đổi
    converted_amount = amount * to_rate / from_rate

    # Trả về kết quả chuyển đổi
    return converted_amount

# Nhập số tiền cần chuyển đổi
amount = float(input("Nhập số tiền: "))

# Nhập tiền tệ ban đầu
from_currency = input("Từ loại tiền: ") 

# Nhập tiền tệ cần đổi
to_currency = input("Sang loại tiền: ")

# Gọi hàm chuyển đổi
converted_amount = currency_convert(amount, from_currency, to_currency)

# In kết quả ra màn hình
print(amount, from_currency, "=", converted_amount, to_currency)