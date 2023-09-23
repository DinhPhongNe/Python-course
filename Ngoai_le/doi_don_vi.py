print("---------------------===đổi đơn vị===---------------------")
# Dictionary chức năng chuyển đổi 
unit_convert = {'m-km': 1000, 
                'km-m': 0.001,
                'kg-g': 1000,
                'g-kg': 0.001,
                's-min': 60,
                'min-s': 1/60}

# Hàm chuyển đổi
def convert(value, from_unit, to_unit):
   conversion = unit_convert[from_unit+'-'+to_unit]
   return value * conversion
   
# Main
print('Chương trình chuyển đổi đơn vị')

while True:
   value = float(input('Nhập giá trị: '))
   from_unit = input('Đơn vị ban đầu: ')
   to_unit = input('Đơn vị cần chuyển: ')
   
   result = convert(value, from_unit, to_unit)
   
   print(f'{value} {from_unit} = {result} {to_unit}')
   
   ans = input('Tiếp tục? (Y/N): ')
   if ans == 'N':
      break