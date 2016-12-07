#!/usr/bin/env python
# -*- coding: utf-8 -*-

import arrow

import requests
from requests.auth import HTTPBasicAuth
import json


url = 'https://lb.api-sandbox.openprocurement.org/api/2.3/tenders/81d3064cc3d643daa536cfe035b89baa'
auth = HTTPBasicAuth('l.velychko.prozorro.gov.ua', '864b2d40120d4df89a924a364d7eba8d')


def request_get_tender():
    return requests.get(
        url,
        auth=auth
    )


def get_tender_data():
    get_response = request_get_tender()
    tender_json_response = json.loads(get_response.text)
    return tender_json_response

tender_json = get_tender_data()

# Інформація про тендер

tender_uaid = tender_json['data']['tenderID']
tender_title = tender_json['data']['title']
tender_title_eng = tender_json['data']['title_en']

# Інформація про замовника

procuring_entity_name = tender_json['data']['procuringEntity']['name']
procuring_entity_country_name = tender_json['data']['procuringEntity']['address']['countryName']
procuring_entity_street_address = tender_json['data']['procuringEntity']['address']['streetAddress']
procuring_entity_region = tender_json['data']['procuringEntity']['address']['region']
procuring_entity_locality = tender_json['data']['procuringEntity']['address']['locality']
procuring_entity_postal_code = tender_json['data']['procuringEntity']['address']['postalCode']

contact_point_name = tender_json['data']['procuringEntity']['contactPoint']['name']
contact_point_url = tender_json['data']['procuringEntity']['contactPoint']['url']
contact_point_email = tender_json['data']['procuringEntity']['contactPoint']['email']
procuring_entity_identifier = tender_json['data']['procuringEntity']['identifier']['id']
procuring_entity_legal_name = tender_json['data']['procuringEntity']['identifier']['legalName']

# Інформація про процедуру

enquiry_period_st = tender_json['data']['enquiryPeriod']['startDate']
enquiry_period_start = arrow.get((''.join(enquiry_period_st.split(".")[0])), 'YYYY-MM-DDTHH:mm:ss').to('local')

enquiry_period_e = tender_json['data']['enquiryPeriod']['endDate']
enquiry_period_end = arrow.get((''.join(enquiry_period_e.split(".")[0])), 'YYYY-MM-DDTHH:mm:ss').to('local')

tender_period_e = tender_json['data']['tenderPeriod']['endDate']
tender_period_end = arrow.get(''.join(tender_period_e.split(".")[0]), 'YYYY-MM-DDTHH:mm:ss').to('local')

complaint_period_e = tender_json['data']['complaintPeriod']['endDate']
complaint_period_end = arrow.get(''.join(complaint_period_e.split(".")[0]), 'YYYY-MM-DDTHH:mm:ss').to('local')

value_amount = tender_json['data']['value']['amount']
value_currency = tender_json['data']['value']['currency']
value_tax = tender_json['data']['value']['valueAddedTaxIncluded']

minimal_step_amount = tender_json['data']['minimalStep']['amount']

# Інформація про предмет закупівлі

tender_description = tender_json['data']['description']
items_description = tender_json['data']['items'][0]['description']
items_quantity = tender_json['data']['items'][0]['quantity']

items_classification_scheme = tender_json['data']['items'][0]['classification']['scheme']
items_classification_description = tender_json['data']['items'][0]['classification']['description']
items_classification_id = tender_json['data']['items'][0]['classification']['id']

# Тендерна документація

documents_date_publ = tender_json['data']['documents'][0]['datePublished']
documents_date_published = arrow.get(''.join(documents_date_publ.split(".")[0]), 'YYYY-MM-DDTHH:mm').to('local')

documents_title = tender_json['data']['documents'][0]['title']

# Інформація про відміну

cancellations_reason = tender_json['data']['cancellations'][0]['reason']

cancellations_date_data = tender_json['data']['cancellations'][0]['date']
cancellations_date = arrow.get(''.join(cancellations_date_data.split(".")[0]), 'YYYY-MM-DDTHH:mm').to('local')

cancellations_doc_title = tender_json['data']['cancellations'][0]['documents'][1]['title']

cancellations_doc_date_publ = tender_json['data']['cancellations'][0]['documents'][1]['datePublished']
cancellations_doc_date_published = arrow.get(''.join(cancellations_doc_date_publ.split(".")[0]), 'YYYY-MM-DDTHH:mm').to('local')
