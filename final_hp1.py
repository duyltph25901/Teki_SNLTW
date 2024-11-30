# Chào mừng khách hàng
print('''
    Xin chào quý khách, vậy là Tết 2025 đã sắp đến, cùng tới ngay cửa hàng trực tuyến Demo_Name, để mua sắm đồ mới thôi.
    Quý khách vui lòng thực hiện theo những yêu cầu của bảng thông tin hiển thị:
      
    1. Sau khi hiển thị ra menu cửa hàng, quý khách vui lòng nhập mã sản phẩm và số lượng quý khách cần.
    2. Nếu quý khách muốn mua thêm mặt hàng khác vui lòng bấm phím Y, còn không bấm phím N.
    3. Sau khi hệ thống xuất hóa đơn, quý khách vui lòng nhập thông tin liên hệ và địa chỉ giao hàng.
''')

# Mảng chứa thông tin sản phẩm
productNameArr = []
productQuantityArr = []
productPriceArr = []
productIdArr = []

while True:
    # Hiển thị menu cửa hàng với căn chỉnh đẹp
    print('''
        ------------------------ Menu ------------------------
        Mã sản phẩm  |  Tên sản phẩm        |  Giá thành     
        --------------|---------------------|-----------------
        1.            |  Pháo hoa           |  60.000 VND / 1 hộp
        2.            |  Lồng đèn           |  50.000 VND / 1 chiếc
        3.            |  Lì xì              |  10.000 VND / 1 tá
        4.            |  Đèn Led            |  20.000 VND / 1 dây (5m)
        5.            |  Hoa đào            |  200.000 VND / 1 cây
    ''')

    # Nhập mã sản phẩm và số lượng muốn mua
    idProductBought = int(input("Mời bạn nhập mã hàng muốn mua: "))
    quantityProductBought = int(input("Nhập số lượng bạn muốn mua: "))

    # Khai báo các biến lưu tên và giá của sản phẩm
    productName = ''
    productPrice = 0

    # Kiểm tra mã sản phẩm và gán giá trị cho tên sản phẩm và giá thành
    if idProductBought == 1:
        productPrice = 60000
        productName = "Pháo hoa"
    elif idProductBought == 2:
        productPrice = 50000
        productName = "Lồng đèn"
    elif idProductBought == 3:
        productPrice = 10000
        productName = "Lì xì"
    elif idProductBought == 4:
        productPrice = 20000
        productName = "Đèn Led"
    elif idProductBought == 5:
        productName = "Hoa đào"
        productPrice = 200000

    # Thêm sản phẩm vào danh sách
    productNameArr.append(productName)
    productQuantityArr.append(quantityProductBought)
    productPriceArr.append(productPrice)
    productIdArr.append(idProductBought)

    # Hiển thị hóa đơn
    print('''
        ------------------------ Hóa đơn hiện tại ------------------------
        Mã sản phẩm  |  Tên sản phẩm        |  Số lượng  |  Thành tiền  
        -------------|----------------------|------------|--------------
    ''')

    for i in range(len(productIdArr)):
        # Căn chỉnh và in các phần tử trong hóa đơn
        print(f'''
        {productIdArr[i]} | {productNameArr[i]} | x{productQuantityArr[i]} | {productQuantityArr[i] * productPriceArr[i]} VND
        ''')

    # Hỏi người dùng có muốn mua thêm sản phẩm không
    continueShopping = input("\nBạn có muốn mua thêm mặt hàng khác không? (Y/N): ").strip().lower()
    if continueShopping != 'y':
        break

# Sau khi mua xong, tính tổng tiền và xuất hóa đơn cuối cùng
totalAmount = sum([productQuantityArr[i] * productPriceArr[i] for i in range(len(productIdArr))])
print(f"\n----------------------- Tổng tiền hóa đơn -----------------------")
print(f"Tổng tiền thanh toán: {totalAmount} VND")