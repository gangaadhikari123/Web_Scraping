# Web Scraping Project - Pokhara Properties

This project extracts property listings from an HTML file and filters them to show only properties located in Pokhara, Nepal.

## Project Overview

The project consists of a Python script that:
1. Parses an HTML file containing property listings
2. Extracts relevant information from each property listing
3. Filters properties to only include those in Pokhara
4. Saves the filtered data to a JSON file

## Files Description

- **`extract_pokhara.py`**: Main Python script that performs the web scraping
- **`scrap.html`**: HTML file containing the property listings to be scraped
- **`pokhara_data.json`**: Output file containing the filtered Pokhara properties

## How the Code Works

### 1. HTML Parsing
```python
from bs4 import BeautifulSoup
import json

# Open and parse the HTML file
with open('scrap.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')
```
- Uses BeautifulSoup library to parse the HTML file
- Opens the file with UTF-8 encoding to handle special characters

### 2. Finding Property Listings
```python
# Find all property listings (each listing is in a div with class 'item-listing-wrap')
listings = soup.find_all('div', class_='item-listing-wrap')
```
- Searches for all div elements with class 'item-listing-wrap'
- Each div represents a single property listing

### 3. Data Extraction Process
For each property listing, the script extracts:

#### Title
```python
title_tag = listing.find('h2', class_='item-title')
title = title_tag.get_text(strip=True) if title_tag else None
```
- Finds the h2 element with class 'item-title'
- Extracts the text content and removes extra whitespace

#### Price
```python
price_tag = listing.find('span', class_='price')
price = price_tag.get_text(strip=True) if price_tag else None
```
- Locates the span element with class 'price'
- Extracts the price information

#### Address
```python
address_tag = listing.find('address', class_='item-address')
address = address_tag.get_text(strip=True) if address_tag else None
```
- Finds the address element with class 'item-address'
- Extracts the property location

#### Property Type
```python
type_tag = listing.find('ul', class_='item-amenities')
property_type = None
if type_tag:
    type_li = type_tag.find('li', class_='h-type')
    if type_li:
        property_type = type_li.get_text(strip=True)
```
- Looks for the amenities list
- Finds the specific list item with class 'h-type' that contains property type

#### Author
```python
author_tag = listing.find('div', class_='item-author')
author = None
if author_tag:
    author_link = author_tag.find('a')
    author = author_link.get_text(strip=True) if author_link else None
```
- Locates the author div
- Extracts the author name from the link within it

#### Date
```python
date_tag = listing.find('div', class_='item-date')
date = date_tag.get_text(strip=True) if date_tag else None
```
- Finds the date div and extracts the listing date

### 4. Filtering Logic
```python
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
```
- Checks if the address field exists and contains the word 'Pokhara'
- Only includes properties that meet this criteria
- Creates a dictionary with all extracted information

### 5. Data Export
```python
# Save to JSON file
with open('pokhara_data.json', 'w', encoding='utf-8') as f:
    json.dump(pokhara_properties, f, ensure_ascii=False, indent=2)
```
- Saves the filtered data to a JSON file
- Uses UTF-8 encoding to preserve special characters
- Formats the JSON with proper indentation for readability

## Working Steps

### Step 1: Setup
1. Ensure you have the required Python libraries installed:
   ```bash
   pip install beautifulsoup4
   ```
2. Make sure you have the `scrap.html` file in the same directory as the script

### Step 2: Run the Script
```bash
python extract_pokhara.py
```

### Step 3: Check Output
- The script will create a `pokhara_data.json` file
- This file contains only the properties located in Pokhara
- Each property entry includes: title, price, address, property type, author, and date

## Output Format

The generated JSON file contains an array of property objects, each with the following structure:
```json
{
  "title": "Property Title",
  "price": "Price Information",
  "address": "Property Address in Pokhara",
  "property_type": "Type of Property",
  "author": "Author/Agent Name",
  "date": "Listing Date"
}
```

## Error Handling

The script includes basic error handling:
- Uses conditional checks (`if title_tag else None`) to handle missing elements
- Gracefully handles cases where certain information might not be available
- Continues processing even if individual listings have missing data

## Dependencies

- **BeautifulSoup4**: HTML parsing library
- **json**: Built-in Python library for JSON handling

## Notes

- The script is specifically designed for the HTML structure found in `scrap.html`
- It filters properties based on the presence of 'Pokhara' in the address field
- The output is saved in UTF-8 encoding to properly handle Nepali characters
- The script processes all listings but only saves those matching the Pokhara criteria 