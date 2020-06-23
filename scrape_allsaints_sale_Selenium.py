from selenium import webdriver

# Specifying incognito mode when launching browser
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# Create an instance of Chrome in incognito mode
browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=option)

# Navigate to allsaints.com --> clothing retail website --> looking at coats and jackets 
browser.get("https://www.allsaints.com/men/sale/coats-and-jackets/style,any/colour,any/size,any/")


# Generate a selenium object the description of the jacket --> <span class="product-item__name__text">Cleaver Blazer</span>
description_element = browser.find_elements_by_xpath("//span[@class='product-item__name__text']")

# List Comprehension to get the actual description and not the selenium objects.
description = [x.text for x in description_element]

# print response in terminal
print('Descriptions:')
print(description, '\n')

# Similar to above but to get the pre-sale price --> <span class="product-item__price-old">
old_price_element = browser.find_elements_by_xpath("//span[@class='product-item__price-old']")
old_price = [x.text for x in old_price_element] # same concept as for-loop/ list-comprehension above.

# print response in terminal
print("Old Prices:")
print(old_price, '\n')

# Similar to above but to get the sale price --> <span class="product-item__price-new">
new_price_element = browser.find_elements_by_xpath("//span[@class='product-item__price-new']")
new_price = [x.text for x in new_price_element] # same concept as for-loop/ list-comprehension above.

# print response in terminal
print("New Prices:")
print(new_price, '\n')

browser.quit()


# Pair each description with the old and new prices and print to terminal
for description, old_price, new_price in zip(description, old_price, new_price):
     print("Description: " + description)
     print("Old Price: " + old_price)
     print("Sale Price: " + new_price, '\n')
