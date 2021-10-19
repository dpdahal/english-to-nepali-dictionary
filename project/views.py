from django.shortcuts import render

from bs4 import BeautifulSoup as Bs

import requests


def index(request):
    if request.method == 'POST':
        data = request.POST
        criteria = data['search']
        q = {"q": criteria}
        res = requests.get('https://www.englishnepalidictionary.com/', params=q).text
        dp = Bs(res, 'html5lib')
        meaning = dp.find('div', class_="search-result").h3.text
        content = {
            'meaning': meaning
        }
        return render(request, 'index.html', content)
    return render(request, 'index.html')
