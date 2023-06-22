import tinhtoan

def main():
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    print(f"The area is {tinhtoan.area(width, length)}")
    print(f"The perimeter is {tinhtoan.perimeter(width, length)}")
    
if __name__ == '__main__':
    main()