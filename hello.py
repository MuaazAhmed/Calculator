mobiles = {
    100: {"Name": "samsung_galaxy_s23", "price": 120000},
    101: {"Name": "nokia N8        ", "price":  80000},
    102: {"Name": "appple_iphone-14", "price":  16000}
}

cloths = {
    200: {"Name": "jeans     ", "price": 1500},
    201: {"Name": "T-shirt    ", "price": 600},
    202: {"Name": "suit      ", "price":  25000}
}

your_kart = []



def smartphone():
    while True:
        try:
            print("------------Mobiles Category----------------")
            for key, value in mobiles.items():
                print("code.", key, ':', value,)
            print("****************\n")
            print("****************")
            buy = int(input("Enter the mobile code."))
            if buy in mobiles:
                print("your item add to your kart")
                your_kart.append(
                    {"Name": mobiles[buy]["Name"], "price": mobiles[buy]["price"]})

                break
            elif buy not in  mobiles:
                print("it's iteam is not in list")
                continue
            else:
                print("Enter a valid number")
            break
        except ValueError:
            continue


def Cloths():
    while True:
        try:
            print("-------Cloth Category----------\n")
            for key, value in cloths.items():
                print("code.", key, ':', value,)
            print("****************\n")
            print("****************")
            buy = int(input("Enter the cloth code."))
            if buy in cloths:
                print("your item add to your kart")
                your_kart.append(
                    {"Name": cloths[buy]["Name"], "price": cloths[buy]["price"]})
                break
            else:
                    print("it's iteam is not in list")
        except ValueError:
            continue

def bill():
    Money=0
    print('\n\t============== YOUR_BILL ==============\n')
    print('SNo.\tProduct\t\t\tPrice\n----------------------------------------------')
    j=1
    for item in your_kart:
        print('{}\t{}\t\t{}\t\t\t'.format(j,item["Name"], item["price"]))
        Money+=item['price']
        j+=1
    print('----------------------------------------------')
    print('Total Amount:\t\t\t\t',Money)
    print('----------------------------------------------')
    password=input("Enter your ATM code\t\t\t")
    print('----------------------transaction is successful------------------------')
    print('\n$$$$ Thank You. Visit Again $$$$')
    exit()



def main():
    while True:
        print('\n\n--------------------WELCOM TO STORE-98--------------------')
        print('\n')
        c = input('\n\t\t1.FOR SMART-PHONE.\n\t\t2.FOR CLOTHES.\n\t\t4.Bill.\n\t\t5.Exit.\n\nEnter choice :')

        if c == '1':
            smartphone()

        elif c == '2':
            Cloths()

        elif c=='4':
            bill()

        elif c=='4':
            print("thanks for visting us")
            print(count)
            exit()
        else:
            print("enter a valid number")

if __name__ == '__main__':
    main()