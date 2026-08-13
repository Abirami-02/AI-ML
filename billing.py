import csv
CRATE_SIZE = 4
FREE_DELIVERY_THRESHOLD = 500

def process_orders(orders_from_csv):
    results = []
    for order in orders_from_csv:
        unit_price = float(order.get("unit_price", 0))
        quantity = int(order.get("quantity", 0))
        total_cost = unit_price * quantity
        crates = quantity // CRATE_SIZE
        leftover = quantity % CRATE_SIZE
        free_delivery = total_cost >= FREE_DELIVERY_THRESHOLD
        results.append({
            "order_id": order.get("order_id"),
            "total_cost": total_cost,
            "crates": crates,
            "leftover": leftover,
            "free_delivery": free_delivery
        })
    return results

def loaded_orders_csv(filepath):
    orders=[]
    with open(filepath,mode="r",newline="",encoding="utf-8") as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            orders.append(row)
        return orders
if __name__ == "__main__":
    orders_from_csv =loaded_orders_csv("orders.csv")
    results=process_orders(orders_from_csv)
    for r in results[:100]:
        print(r)
        print()
    print("Total orders processed:",len(results))