from bs4 import BeautifulSoup

f= open('hello.html')
html= f.read()
soup= BeautifulSoup(html, 'html.parser')

# print(soup.prettify()) #prints to consule our html file we loaded (it's a string)

# searching by tag
all_list_items = soup.find_all('li')
all_divs = soup.find_all('div')

# searching by class
all_goodbye_elements = soup.find_all(class_='goodbye') #notice class_
hi= soup.find_all('li', class_='goodbye')

# searching by tag AND class
all_french_list_items = soup.find_all('li', class_='french')

# searching by id
all_hello_elements = soup.find_all(id='hello-list')

#Number 2
print('List elements within the gooodbye list')
goodbye_list_items = all_goodbye_elements[0].find_all('li')
for c in goodbye_list_items:
    print(c.string)
# print (goodbye_list_items)
print('------')

img_tag = soup.find('img')
print('The img width:')
print(img_tag['width'])
print('------')

a_tag= soup.find_all('p')
for c in a_tag:
    x= soup.find('a')
print('The URL is:')
print(x)


# print('list items:', all_list_items)
# print('------')
# print('divs:', all_divs)
# print('------')
# print('goodbye elements:', all_goodbye_elements)
# print('------')
# print('french stuff:', all_french_list_items)
# print('------')
# print('hello id elements:', all_hello_elements)
# print('------')


# print(type(all_list_items[0])) #returns: <class 'bs4.element.Tag'>
# print('------')


# for c in all_list_items:
#   print(c.string)
# print('------')

# print('Children of hello-list:')
# for c in all_hello_elements[0].children:
#   print(c.string)
# print('------')

# print('List items within the hello tag')
# hello_list_items = all_hello_elements[0].find_all('li')
# print (hello_list_items)
# print('------')


# all_hello_elements = soup.find_all(id='hello-list')
# print(all_hello_elements[0])
# print('------')
#above and below DO THE SAME THING!
#‘find( )’ always just returns the first matching element
#so only use it when you know there’s only one (or you know you only want the first one).
# the_hello_element = soup.find(id='hello-list')
# print(the_hello_element)
# print('------')

# img_tag = soup.find('img')
# print('The img source:')
# print(img_tag['src'])
# print('------')
