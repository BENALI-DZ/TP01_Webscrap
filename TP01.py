import requests
from bs4 import BeautifulSoup
import pandas as pd

# رابط الموقع
url = 'http://books.toscrape.com/'

# طلب الصفحة
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# استخراج كل الكتب
books = soup.find_all('article', class_='product_pod')

# قائمة لتخزين النتائج
data = []

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    stock = book.find('p', class_='instock availability').text.strip()
    data.append([title, price, stock])

# إنشاء DataFrame
df = pd.DataFrame(data, columns=['Title', 'Price', 'Availability'])

# عرض النتائج
print(df)

# حفظ في ملف CSV
df.to_csv("books.csv", index=False, encoding="utf-8-sig")
