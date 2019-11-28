#from django.shortcuts import render

import requests
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from bs4 import BeautifulSoup

class Home(View):
    def get(self, request):

        blog_url = request.GET.get('url')
        data = self.fetch_data_from_url(blog_url)
        return JsonResponse(data)

    def post(self, request):
        return HttpResponse("post method")

    def fetch_data_from_url(self, url):
        page = requests.get(url)
        html_content = BeautifulSoup(page.content, "html.parser")

        data = {}

        data['title'] = html_content.\
            find_all('h1', class_="entry-header-title")[0].\
            get_text().strip()
        data['featured_image'] = html_content.\
            find_all('img', class_="attachment-bayleaf-large")[0].\
            attrs['data-lazy-src']
        data['content'] = html_content.\
            find_all('div', class_="entry-content")[0].\
            get_text()
        data['published_date'] = html_content.\
            find_all('time', class_="entry-date")[0].\
            attrs['datetime']
        data['author_name'] = html_content.\
            find_all('span', class_="meta-author")[0].\
            get_text().strip()
        data['author_image'] = html_content.\
            find_all('img', class_="avatar")[0].attrs['data-lazy-src']
        data['author_bio'] = html_content.\
            find_all('div', class_="entry-author-bio")[0].get_text()

        return data
