from bs4 import BeautifulSoup
import json

# Open and parse the HTML file
with open('scrap.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find all property listings (each listing is in a div with class 'item-listing-wrap')
listings = soup.find_all('div', class_='item-listing-wrap')

pokhara_properties = []

for listing in listings:
    # Extract title
    title_tag = listing.find('h2', class_='item-title')
    title = title_tag.get_text(strip=True) if title_tag else None

    # Extract price
    price_tag = listing.find('span', class_='price')
    price = price_tag.get_text(strip=True) if price_tag else None

    # Extract address
    address_tag = listing.find('address', class_='item-address')
    address = address_tag.get_text(strip=True) if address_tag else None

    # Extract property type
    type_tag = listing.find('ul', class_='item-amenities')
    property_type = None
    if type_tag:
        type_li = type_tag.find('li', class_='h-type')
        if type_li:
            property_type = type_li.get_text(strip=True)

    # Extract author
    author_tag = listing.find('div', class_='item-author')
    author = None
    if author_tag:
        author_link = author_tag.find('a')
        author = author_link.get_text(strip=True) if author_link else None

    # Extract date
    date_tag = listing.find('div', class_='item-date')
    date = date_tag.get_text(strip=True) if date_tag else None

    # Only add if address contains 'Pokhara'
    if address and 'Pokhara' in address:
        pokhara_properties.append({
            'title': title,
            'price': price,
            'address': address,
            'property_type': property_type,
            'author': author,
            'date': date
        })

# Save to JSON file
with open('pokhara_data.json', 'w', encoding='utf-8') as f:
    json.dump(pokhara_properties, f, ensure_ascii=False, indent=2)

print("Pokhara data saved to pokhara_data.json")