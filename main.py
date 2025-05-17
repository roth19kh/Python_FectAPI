import requests
from tabulate import tabulate

def stringLimit(show_char: int, word: str) -> str:
    res = ""
    if len(word) > show_char:
        for index in range(show_char):
            res += str(word[index])
        res +="..."
    else:
        res = word
    return res
# kdmv = "Samsung 49-Inch CHG90 144Hz Curved Gaming Monitor (LC49HG90DMNXZA) – Super Ultrawide Screen QLED "
# print(stringLimit(10, kdmv)+"...")

try:
    res = requests.get('https://fakestoreapi.com/products')
    if res.status_code == 200:
        data = res.json()
        table = []
        for item in data:
            table.append(
                [
                    item["id"],
                    item["title"],
                    f"${item['price']:.2f}",
                    item["category"],
                    stringLimit(30, item["description"])
                ]
            )
        print(tabulate
              (table,
                       ["ID", "Title", "Price","Category", "Description"],
                       tablefmt="heavy_outline"
                       )
              )


        is_filter  = input("Do you want to filter products? (y/n): ")
        while is_filter.lower() not in ["y"or"n"]:
            is_filter = input("Do you want to filter products? (y/n): ")
        if is_filter.lower() == "y":
            filter_option = int(input("Filter by 1.ID or 2.Category 3.Title: "))
            while filter_option not in [1, 2, 3]:
                filter_option = int(input("Filter by 1.ID or 2.Category 3.Title: "))
                #filter
            if filter_option == 1:
                filter_string = input("Enter product ID:")
            elif filter_option == 2:
                filter_string = input("Enter product Category:")
            else:
                filter_string = input("Enter product Title:")

            filter_result = []
            filter_result_row = []
            for item in data:
                if filter_option == 1:
                     #filter id
                    if int(item['id']) == int(filter_string):
                        # filter_result.append(item)
                        filter_result_row.append([
                            item["id"],
                            stringLimit(20, item["title"]),
                            f"${item['price']:.2f}",
                            item["category"],
                            stringLimit(30, item["description"])
                        ])
                elif filter_option == 2:
                    #fl category
                    if item['category'] == filter_string:
                        # filter_result.append(item)
                        filter_result_row.append([
                            item["id"],
                            stringLimit(20, item["title"]),
                            f"${item['price']:.2f}",
                            item["category"],
                            stringLimit(30, item["description"])
                        ])
                else:
                    #fl title
                    if item['title'] == filter_string:
                        # filter_result.append(item)
                        filter_result_row.append([
                            item["id"],
                            stringLimit(20, item["title"]),
                            f"${item['price']:.2f}",
                            item["category"],
                            stringLimit(30, item["description"])
                        ])
            print (tabulate(filter_result_row,["ID", "Title", "Price","Category", "Description"], tablefmt="grid"))
                # print(filter_result)
            see_product_options = input("Do you want to see product details? (y/n): ")
            while see_product_options  not in ["y", "n"]:
                see_product_options  = input("Do you want to see product details? (y/n): ")
            if see_product_options  == "y":
                see_product_details = input("Enter product ID:")
                for item in filter_result_row:
                    if int(item[0]) == int(see_product_details):
                        for detail_data in data:
                            if detail_data["id"] == int(see_product_details):
                                print("-----------------------------------------------")
                                print("Product Details:")
                                print(f"ID: {detail_data['id']}")
                                print(f"Title: {detail_data['title']}")
                                print(f"Price: ${detail_data['price']:.2f}")
                                print(f"Category: {detail_data['category']}")
                                print(f"Description: {detail_data['description']}")
                                print("Image",detail_data['image'])
                                break
            else:
                pass
        else:
            pass

except Exception as e:
    print(e)