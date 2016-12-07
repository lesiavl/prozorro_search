#!/usr/bin/env python
# -*- coding: utf-8 -*-

tender_id_gl = 'UA-2016-12-06-000286-1'

tender_number_filter = u'//button[text()="№ закупівлі"]'
tender_search_field = '//*[@id="blocks"]/div/input'
go_to_tender_link = '//a[@href="/tender/{}/"]'.format(tender_id_gl)

prozorro_tender_uaid = '//div[@class="tender--head--inf"]'

prozorro_tender_title = '//div[@class="tender--head--title col-sm-9"]'
prozorro_tender_title_eng = '//div[@class="tender--head--title col-sm-9"]/child::b'

# Інформація про замовника

prozorro_procuring_entity_name = u'//strong[text()="Найменування замовника:"]/../following-sibling::td[1]'
prozorro_procuring_entity_address = u'//strong[text()="Місцезнаходження замовника:"]/../following-sibling::td[1]'

prozorro_contact_point_name = '//*[@id="sticky-wrapper"]/div/div/p[2]'
prozorro_contact_point_url = u'//strong[text()="Вебсайт замовника:"]/../following-sibling::td[1]'
prozorro_contact_point_email = '//*[@id="sticky-wrapper"]/div/div/small/a'
prozorro_procuring_entity_identifier = u'//strong[text()="Код ЄДРПОУ:"]/../following-sibling::td[1]'
prozorro_procuring_entity_legal_name = u'//strong[text()="Найменування замовника:"]/../following-sibling::td[1]'

# Інформація про процедуру

prozorro_enquiry_period_start = u'//strong[text()="Publication date:"]/../following-sibling::td[1]'
prozorro_enquiry_period_end = u'//strong[text()="Звернення за роз’ясненнями:"]/../following-sibling::td[1]'
prozorro_tender_period_end = u'//strong[text()="Кінцевий строк подання тендерних пропозицій:"]/../following-sibling::td[1]'
prozorro_complaint_period_end = u'//strong[text()="Оскарження умов закупівлі:"]/../following-sibling::td[1]'

prozorro_value_complex = u'//strong[text()="Очікувана вартість:"]/../following-sibling::td[1]'
prozorro_minimal_step_amount = u'//strong[text()="Розмір мінімального кроку пониження ціни:"]/../following-sibling::td[1]'


# Інформація про предмет закупівлі

prozorro_tender_description = '//div[@class="tender--description--text description open"][1]'

prozorro_items_description = '//div[@class="tender--description--text description padding-side"][1]'
prozorro_items_quantity = '//div[@class="padding margin-bottom"][1]'
prozorro_items_classification = '//div[@class="tender-date padding-left-more"][3]'

prozorro_items_classification_descript = '//div[@class="tender-date padding-left-more"][1]'

# Тендерна документація

prozorro_documents_date_published = '//td[@class="col-sm-2 date"]'
prozorro_documents_title = '(//td[@class="col-sm-6"]/a)[4]'

# Інформація про відміну

prozorro_cancellations_reason = '(//div[@class="col-md-12 margin-bottom"][2])/div'
prozorro_cancellations_date = u'//strong[text()="Дата скасування"]/following-sibling::div'
prozorro_cancellations_doc_date_publ = '//td[@class="col-sm-2"][1]'
prozorro_cancellations_doc_title = '(//td[@class="col-sm-6"]/a)[6]'

