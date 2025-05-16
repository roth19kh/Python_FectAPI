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
                    stringLimit(20, item["title"]),
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
        if is_filter.lower() == "y":
            filter_option = int(input("Filter by 1.ID or 2.Category: "))
            while filter_option not in [1, 2]:
                filter_option = int(input("Filter by 1.ID or 2.Category: "))
                #filter
            if filter_option == 1:
                filter_string = input("Enter product ID:")
            else:
                filter_string = input("Enter product Category:")

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
                else:
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
            print (tabulate(filter_result_row,["ID", "Title", "Price","Category", "Description"], tablefmt="grid"))
                # print(filter_result)
        else:
            pass

except Exception as e:
    print(e)