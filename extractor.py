import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import xlwt
from xlwt import Workbook
from time import sleep

parsed_uri = None


def url_maker(u):  # where u is given raw url
    global parsed_uri
    parsed_uri = urlparse(u)
    if parsed_uri.scheme == "":
        u = 'http://' + u
        parsed_uri = urlparse(u)
        u = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        return u
    else:
        parsed_uri = urlparse(u)
        u = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        return u


def url_extractor(u, c):  # where c is content of given url
    global parsed_uri
    soup = BeautifulSoup(c, features="lxml")
    tags = soup.find_all('a', href=True)
    urls = {u}
    for a in tags:
        parsed_uri = urlparse(a['href'])
        if parsed_uri.scheme != '' and (parsed_uri.netloc == '' or parsed_uri.netloc != '') and re.match(r'^/.+', parsed_uri.path):
            urls.add('{uri.scheme}://{uri.netloc}{uri.path}'.format(uri=parsed_uri))
        elif parsed_uri.scheme == '' and (parsed_uri.netloc == '' or parsed_uri.netloc != '') and (re.match(r'^/.+', parsed_uri.path) or re.match(r'^(\w)[\w/.]+', parsed_uri.path)):
            urls.add(u+'{uri.path}'.format(uri=parsed_uri))
    return urls


def html_stripper(html):
    text = re.sub('<[^<]+?>', '', html)
    return text


def mail_extractor(u, c):
    ma = re.findall(r"[a-zA-Z0-9-_.+]+@[a-zA-Z0-9-]+\.[0-9a-zA-Z.]+", c)
    for m in ma:
        extracted_mails.add(m)
        extracted_mails_urls.add(m+" : "+u)


print('Make sure that the executed python file and text file which contains urls should be in the same folder.\n')
sleep(1)
input_text_file = str(input('Input the file name which contains website links, (extension = .txt): '))
output_xl_name = str(input('Enter the desire name for excel file, (extension = .xls): '))

f = open(input_text_file, "r")
count = 0

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 11')
style = xlwt.easyxf('font: bold 1; borders: left thin, right thin, top thin, bottom thin;')
sheet1.write(0, 0, 'S.No', style)
sheet1.write(0, 1, 'Base URL', style)
sheet1.write(0, 2, 'E-mail IDs', style)
sheet1.write(0, 3, 'E-Mail IDs : Internal Links', style)
sheet1.write(0, 4, 'Internal Links', style)
sheet1.write(0, 5, 'External Links', style)
for x in f:
    count = count + 1
    url = x.rstrip('\n')
    print(url)
    res = None
    status_code = None
    try:
        res = requests.get(url_maker(url))
        status_code = res.status_code
    except Exception as ex:
        print(ex)

    if status_code == 200:
        site_url = res.url                                  # site_url
        extracted_mails = set()                             # mails
        extracted_mails_urls = set()                         # mail ids : url
        site_links = set()                                  # site_links
        other_links = set()                                 # other_links

        extracted_urls = url_extractor(res.url, res.text)   # site_n_other_links
        for url in extracted_urls:
            parsed_uri = urlparse(url)
            if site_url == '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri):
                site_links.add(url)
                r = requests.get(url)
                # stripped_html = html_stripper(r.text)
                mail_extractor(url, r.text)
            else:
                other_links.add(url)
        print(extracted_mails)
        # writing_to_xl(output_xl_name, site_url, extracted_mails, site_links, other_links)
        style2 = xlwt.easyxf('borders: left thin, right thin, top thin, bottom thin')
        sheet1.write(count, 0, count, xlwt.easyxf('align: horiz center; borders: left thin, right thin, top thin, bottom thin;'))
        sheet1.write(count, 1, site_url, style2)
        sheet1.write(count, 2, '\n'.join(extracted_mails), style2)
        sheet1.write(count, 3, '\n'.join(extracted_mails_urls), style2)
        sheet1.write(count, 4, '\n'.join(site_links), style2)
        sheet1.write(count, 5, '\n'.join(other_links), style2)

wb.save(output_xl_name)
