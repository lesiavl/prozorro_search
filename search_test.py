#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest

from objects import *
from data_fields import *


class TestProzorroPortal(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_get_tender(self):
        get_response = request_get_tender()
        self.assertEqual(get_response.status_code, 200)

    def test_find_tender_prozorro(self):
        find_tender = FindTender(self.driver)
        find_tender.find_tender_on_prozorro()

        tender_values = find_tender.find_elements()

        tender_id_element = tender_values[0]
        tender_title_element = tender_values[1]
        tender_title_eng_element = tender_values[2]

        procuring_entity_name_element = tender_values[3]
        procuring_entity_postal_code_element = tender_values[4]
        procuring_entity_country_name_element = tender_values[5]
        procuring_entity_region_element = tender_values[6]
        procuring_entity_locality_element = tender_values[7]
        procuring_entity_street_address_element = tender_values[8]

        contact_point_name_element = tender_values[9]
        contact_point_email_element = tender_values[10]
        contact_point_url_element = tender_values[11]
        procuring_entity_identifier_element = tender_values[12]
        procuring_entity_legal_name_element = tender_values[13]

        enquiry_period_start_element = tender_values[14]
        enquiry_period_end_element = tender_values[15]
        tender_period_end_element = tender_values[16]
        complaint_period_end_element = tender_values[17]
        value_amount_element = tender_values[18]
        value_currency_element = tender_values[19]
        value_tax_element = tender_values[20]
        minimal_step_amount_element = tender_values[21]

        tender_description_element = tender_values[22]
        items_description_element = tender_values[23]
        items_quantity_element = tender_values[24]
        items_classif_scheme_element = tender_values[25]
        items_classif_description_element = tender_values[26]
        items_classif_id_element = tender_values[27]
        documents_date_publ_element = tender_values[28]
        documents_title_element = tender_values[29]

        cancellations_reason_element = tender_values[30]
        cancellations_date_element = tender_values[31]
        cancellations_doc_title_element = tender_values[32]
        cancellations_doc_date_published_element = tender_values[33]

# Інформація про тендер

        self.assertEquals(tender_uaid, tender_id_element)
        self.assertEquals(tender_title, tender_title_element)
        self.assertEquals(tender_title_eng, tender_title_eng_element)

# Інформація про замовника

        self.assertEquals(procuring_entity_name, procuring_entity_name_element)
        self.assertEquals(procuring_entity_street_address, procuring_entity_street_address_element)
        self.assertEquals(procuring_entity_country_name,  procuring_entity_country_name_element)
        self.assertEquals(procuring_entity_postal_code, procuring_entity_postal_code_element)
        self.assertEquals(procuring_entity_locality, procuring_entity_locality_element)
        self.assertEquals(procuring_entity_region, procuring_entity_region_element)
        self.assertEquals(contact_point_name_element, contact_point_name_element)
        self.assertEquals(contact_point_email, contact_point_email_element)
        self.assertEquals(contact_point_url, contact_point_url_element)
        self.assertEquals(procuring_entity_identifier, procuring_entity_identifier_element)
        self.assertEquals(procuring_entity_legal_name, procuring_entity_legal_name_element)

# Інформація про процедуру

        self.assertEquals(enquiry_period_start, enquiry_period_start_element)
        self.assertEquals(enquiry_period_end, enquiry_period_end_element)
        self.assertEquals(tender_period_end, tender_period_end_element)
        self.assertEquals(complaint_period_end, complaint_period_end_element)

        self.assertEquals(value_amount, value_amount_element)
        self.assertEquals(value_currency, value_currency_element)
        self.assertEquals(value_tax, value_tax_element)
        self.assertEquals(minimal_step_amount, minimal_step_amount_element)

# Інформація про предмет закупівлі

        self.assertEquals(tender_description, tender_description_element)
        self.assertEquals(items_description, items_description_element)
        self.assertEquals(items_quantity, items_quantity_element)
        self.assertEquals(items_classification_scheme, items_classif_scheme_element)
        self.assertEquals(items_classification_description, items_classif_description_element)
        self.assertEquals(items_classification_id, items_classif_id_element)

# Тендерна документація

        self.assertEquals(documents_date_published, documents_date_publ_element)
        self.assertEquals(documents_title, documents_title_element)

# Інформація про відміну

        self.assertEquals(cancellations_reason, cancellations_reason_element)
        self.assertEquals(cancellations_date, cancellations_date_element)
        self.assertEquals(cancellations_doc_title, cancellations_doc_title_element)
        self.assertEquals(cancellations_doc_date_published, cancellations_doc_date_published_element)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

