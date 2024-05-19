price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}


def total_cost_shopping():
    totalcost=0
    for key in quantity_list.keys():
         if key in price_list.keys():
             #totalcost=quantity_list[key]*price_list[key]
             a=quantity_list[key]                                 #  first initialize the keys and then do the operation
             b=price_list[key]
             totalcost=a*b
    print('the total cost is ', totalcost)
    

def cost_of_fruits(fruit, quantity):
    cost=0
    if fruit in price_list and fruit in quantity_list:
            cost=cost+(quantity*price_list[fruit])
    print("cost of", quantity , fruit, '=', cost)
    return cost


def main():
    cost_of_fruits('apple', 10)
    total_cost_shopping()


if __name__ == "__main__":
    main()