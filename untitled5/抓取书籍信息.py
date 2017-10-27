import re
import requests

res = requests.get(r"http://opac.ncu.edu.cn/opac/item.php?marc_no=0000935942")

book_author_ = re.findall(r'<dt>题名/责任者:</dt><dd><a.*?>(.*)<\/a><span.*?>(.*)<\/span><\/li>', str(res.text))
publisher_date_ = re.findall(r'<dt>出版发行项:</dt><dd>(.*)</dd></dl>', str(res.text))
for title_author in book_author_:
    with open('information.txt', 'a+', encoding="utf-8") as f1:
        book_author = book_author + '\n'
        f1.write(book_author)

for publisher_date in publisher_date_:
    with open('information.txt', 'a+', encoding="utf-8") as f2:
        publisher_date = publisher_date + '\n'
        f2.write(publisher_date)
