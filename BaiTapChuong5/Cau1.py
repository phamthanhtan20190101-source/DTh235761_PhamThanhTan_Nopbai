
while True:
    chuoi = input("Nhập vào một chuỗi: ")
    if chuoi == chuoi[::-1]:
        print("Chuỗi này là đối xứng.")
    else:
        print("Chuỗi này không phải là đối xứng.")
    
    tiep_tuc = input("Bạn có muốn tiếp tục không? (c/k): ")
    if tiep_tuc.lower() != 'c':
        print("Cảm ơn bạn đã sử dụng phần mềm!")
        break

