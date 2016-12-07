#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import prozorro_locators

prozorro_url = 'https://qa23.prozorro.gov.ua/tender/search/'


def datetime_iso_portal(str_date):
    import arrow
    return arrow.get(str_date, 'DD.MM.YYYY HH:mm').to('local')


def wait_before_click(driver, element):
    return ui.WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, element)))


def wait_until_visible(driver, element):
    return ui.WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, element)))


def wait_for_presence(driver, element):
    return ui.WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, element)))


def wait_for_text_presence(driver, element, text):
    return ui.WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.XPATH, element), text))


class FindTender:

    def __init__(self, driver):
        self.driver = driver

    def find_tender_on_prozorro(self):
        self.driver.set_window_size(1200, 1000)
        self.driver.get(prozorro_url)

        wait_for_presence(self.driver, prozorro_locators.tender_number_filter)
        self.driver.find_element_by_xpath(prozorro_locators.tender_number_filter).click()
        wait_for_presence(self.driver, prozorro_locators.tender_search_field)
        self.driver.find_element_by_xpath(prozorro_locators.tender_search_field).send_keys(prozorro_locators.tender_id_gl)
        wait_until_visible(self.driver, prozorro_locators.go_to_tender_link)
        self.driver.find_element_by_xpath(prozorro_locators.go_to_tender_link).click()

        self.driver.execute_script("window.scrollTo(0, 159);")
        self.driver.implicitly_wait(10)

    def find_elements(self):
        wait_for_presence(self.driver, prozorro_locators.prozorro_tender_uaid)
        tender_id = self.driver.find_element_by_xpath(prozorro_locators.prozorro_tender_uaid).text
        tender_id_element = tender_id.strip(" ").split(' ')[0]

# Інформація про тендер

        tender_title = self.driver.find_element_by_xpath(prozorro_locators.prozorro_tender_title).text
        tender_title_element = tender_title.split("\n")[0]
        tender_title_eng_element = tender_title.split("\n")[1]

# Інформація про замовника

        procuring_entity_name_element = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_procuring_entity_name).text

        procuring_entity_address_element = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_procuring_entity_address).text

        procuring_entity_postal_code_element = procuring_entity_address_element.split(', ')[0]
        procuring_entity_country_name_element = procuring_entity_address_element.split(', ')[1]
        procuring_entity_region = ''.join(procuring_entity_address_element.split(', ')[2])
        procuring_entity_region_element = ' '.join(procuring_entity_region.split(' ')[:-1])
        procuring_entity_locality_element = procuring_entity_address_element.split(', ')[3]
        procuring_entity_street_address_element = procuring_entity_address_element.split(', ')[4]

        contact_point_name_element = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_contact_point_name).text
        contact_point_email_element = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_contact_point_email).text

        contact_point_url = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_contact_point_url).text
        contact_point_url_element = ''.join(contact_point_url)

        procuring_entity_identifier_element = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_procuring_entity_identifier).text
        procuring_entity_legal_name_element = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_procuring_entity_legal_name).text

# Інформація про процедуру

        self.driver.execute_script("window.scrollTo(0, 1084);")

        wait_for_presence(self.driver, prozorro_locators.prozorro_enquiry_period_start)
        enquiry_period_start = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_enquiry_period_start).text
        enquiry_period_start_element = datetime_iso_portal(enquiry_period_start)

        enquiry_period_end = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_enquiry_period_end).text
        enquiry_period_end_element = datetime_iso_portal(' '.join(enquiry_period_end.split()[1:]))

        tender_period_end = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_tender_period_end).text
        tender_period_end_element = datetime_iso_portal(tender_period_end)

        complaint_period_end = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_complaint_period_end).text
        complaint_period_end_element = datetime_iso_portal(' '.join(complaint_period_end.split()[1:]))

        value_amount = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_value_complex).text
        value_amount_el = value_amount.split(' ')[0:2]
        value_amount_element = float(''.join(value_amount_el))
        value_currency_element = value_amount.split(' ')[-3]
        value_tax = value_amount.split(' ')[3:]
        value_tax_element = bool([u'з ПДВ' in value_tax])

        minimal_step = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_minimal_step_amount).text
        minimal_step_amount_el = minimal_step.split(' ')[0]
        minimal_step_amount_element = float(''.join(minimal_step_amount_el))

# Інформація про предмет закупівлі

        self.driver.execute_script("window.scrollTo(0, 1985);")

        wait_for_presence(self.driver, prozorro_locators.prozorro_tender_description)
        tender_description_element = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_tender_description).text

        items_description_element = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_items_description).text

        items_quantity_el = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_items_quantity).text
        items_quantity_element = int(items_quantity_el.split(' ')[0])

        items_classif_el = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_items_classification).text
        items_classif_scheme_element = items_classif_el.split(': ')[0]

        items_classif_id_element = items_classif_el.split(': ')[1]

        items_classif_description_el = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_items_classification_descript).text
        items_classif_description_element = items_classif_description_el.split(u' — ')[-1]

# Тендерна документація

        documents_date_publ_el = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_documents_date_published).text
        documents_date_publ_element = datetime_iso_portal(documents_date_publ_el)

        documents_title_element = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_documents_title).text

# Інформація про відміну

        self.driver.execute_script("window.scrollTo(0, 2462);")

        wait_for_presence(self.driver, prozorro_locators.prozorro_cancellations_reason)
        cancellations_reason_element = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_cancellations_reason).text

        cancellations_date_el = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_cancellations_date).text
        cancellations_date_element = datetime_iso_portal(cancellations_date_el)

        cancellations_doc_title_element = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_cancellations_doc_title).text

        cancellations_doc_date_published_el = self.driver.find_element_by_xpath(
            prozorro_locators.prozorro_cancellations_doc_date_publ).text
        cancellations_doc_date_published_element = datetime_iso_portal(cancellations_doc_date_published_el)

        return [tender_id_element,
                tender_title_element,
                tender_title_eng_element,
                procuring_entity_name_element,
                procuring_entity_postal_code_element,
                procuring_entity_country_name_element,
                procuring_entity_region_element,
                procuring_entity_locality_element,
                procuring_entity_street_address_element,
                contact_point_name_element,
                contact_point_email_element,
                contact_point_url_element,
                procuring_entity_identifier_element,
                procuring_entity_legal_name_element,
                enquiry_period_start_element,
                enquiry_period_end_element,
                tender_period_end_element,
                complaint_period_end_element,
                value_amount_element,
                value_currency_element,
                value_tax_element,
                minimal_step_amount_element,
                tender_description_element,
                items_description_element,
                items_quantity_element,
                items_classif_scheme_element,
                items_classif_description_element,
                items_classif_id_element,
                documents_date_publ_element,
                documents_title_element,
                cancellations_reason_element,
                cancellations_date_element,
                cancellations_doc_title_element,
                cancellations_doc_date_published_element
                ]




