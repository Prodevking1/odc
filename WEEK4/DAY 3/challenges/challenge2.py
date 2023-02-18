items_purchase = {
  "Water": "$75",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$100"

prices = {item: float(price.strip("$").replace(",", "")) for item, price in items_purchase.items()}
affordable_items = sorted([item for item, price in prices.items() if price <= float(wallet.strip("$").replace(",", ""))])

if affordable_items:
    print(affordable_items)
else:
    print("Nothing")
