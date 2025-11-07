import requests
r = requests.get('https://www.kenya-airways.com/en-in/book-manage/manage-booking/change-booking/')

print(r.headers)
