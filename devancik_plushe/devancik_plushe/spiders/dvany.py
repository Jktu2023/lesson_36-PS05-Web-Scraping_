# Попробуй написать spider для нахождения всех источников освещения с сайта divan.ru
# Нужно взять название источника освещения, цену и ссылку
# *Можно попробовать сделать это на другом сайте с продажей источников освещения
# В поле для ответа загрузи ссылку на Git.



import scrapy

class DvanySpider(scrapy.Spider):
    name = "dvany"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        dict1 = {}  # создаем словарь
        lites = response.css('div.lsooF') # выбираем нужные блоки

        for idx, lite in enumerate(lites): # перебираем вместе с индексом
            # сохраняем каждую запись в словарь с уникальным ключом
            dict1[idx] = {
                'name': lite.css('span::text').get(),
                'price': lite.css('meta::attr(content)').get(),
                'link': lite.css('link::attr(href)').get()
            }

        # Обрабатываем текущую страницу 1
        yield {'page_data': dict1}

        # Ищем ссылку на следующую страницу
        next_page = response.css('a.next::attr(href)').get()  # предполагается, что есть такая ссылка
        if next_page:
            yield response.follow(next_page, callback=self.parse)





# import scrapy
#
# class DvanySpider(scrapy.Spider):
#     name = "dvany"
#     allowed_domains = ["divan.ru"]
#     start_urls = ["https://www.divan.ru/category/svet"]
#
#     def parse(self, response):
#         dict1 = {}  # создаем словарь
#         lites = response.css('div.lsooF')  # выбираем нужные блоки
#
#         for idx, lite in enumerate(lites):
#             # сохраняем каждую запись в словарь с уникальным ключом
#             dict1[idx] = {
#                 'name': lite.css('span::text').get(),
#                 'price': lite.css('meta::attr(content)').get(),
#                 'link': lite.css('link::attr(href)').get()
#             }
#         # возвращаем или используем dict1 дальше
#         return dict1


# import scrapy
#
#
# class DvanySpider(scrapy.Spider):
#     name = "dvany"
#     allowed_domains = ["divan.ru"]
#     start_urls = ["https://www.divan.ru/category/svet"]
#
#     def parse(self, response):
#         lites = response.css('div.lsooF') # lsooF
#
#         for lite in lites:
#             yield {
#                 'name': lite.css('span::text').get(),
#                 'price': lite.css('meta::attr(content)').get(),
#                 'link': lite.css('link::attr(href)').get()
#             }


# в терминале scrapy_shell
#  fetch("https://divan.ru")
# qq = lites[0].css('meta::attr(content)').get()
# print(qq)

# в терминале classic
# python -m scrapy crawl divany.py # запуск файла в терминале, передэтим переходим в нужную папку командой cd



 # ['<div class="lsooF"><a tabindex="0" class="ui-GPFV8 qUioe ProductName ActiveProduct" href="/product/podvesnoj-svetilnik-ferum-orange"><span itemprop="name">Подвесной светильник Ферум Orange<
# /span></a><link itemprop="url" href="https://www.divan.ru/product/podvesnoj-svetilnik-ferum-orange"><meta itemprop="price" content="4990"><meta itemprop="priceCurrency" content="RUB"><link itemprop="a
# vailability" href="http://schema.org/InStock"><div class="pY3d2"><div class="q5Uds fxA6s"><span class="ui-LD-ZU KIkOH" data-testid="price">4990<span class="ui-i5wwi ui-VDyJR ui-VWOa-">руб.</span></spa
# n><span class="ui-LD-ZU ui-SVNym bSEDs" data-testid="price">5990<span class="ui-i5wwi ui-VDyJR ui-VWOa-">руб.</span></span><div class="ui-FIExl dW3QK"><div class="ui-G4iQB ui-5kIyv ui-WATUm ui-PzkuZ">
# <svg class="ui-A4pWG" width="60" height="33" viewbox="0 0 60 33" xmlns="http://www.w3.org/2000/svg"><path vector-effect="non-scaling-stroke" d="M0.906839 13.7782L8.56459 1.94703C9.45127 0.754977 10.86
# 19 0.0397351 12.3935 0H55.2845C57.8639 0 60 2.06623 60 6.64901V28.3511C60 30.8941 57.9042 33.0001 55.2845 33.0001H12.3935C10.8619 33.0001 9.45127 32.2849 8.56459 31.0928L0.906839 19.2617C-0.30228 17.6
# 325 -0.30228 15.4074 0.906839 13.7782ZM8.5 19.0001C9.88071 19.0001 11 17.8808 11 16.5001C11 15.1194 9.88071 14.0001 8.5 14.0001C7.11929 14.0001 6 15.1194 6 16.5001C6 17.8808 7.11929 19.0001 8.5 19.000
# 1Z"></path></svg><div class="ui-OQy8X">16</div></div></div></div></div><div class=""></div></div>']
