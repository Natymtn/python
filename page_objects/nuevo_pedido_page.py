import time

from selenium.webdriver.support.wait import WebDriverWait

from page_objects.properties.nuevo_pedido_page_locators import NuevoPedidoPageLocators
from selenium.webdriver.support import expected_conditions as ec


class NuevoPedidoPage(NuevoPedidoPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def ingresar_patente(self, patente):
        self.wait.until(ec.visibility_of_element_located(NuevoPedidoPageLocators.INP_PATENTE))
        self.driver.find_element(*NuevoPedidoPageLocators.INP_PATENTE).send_keys(patente)
        self.driver.find_element(*NuevoPedidoPageLocators.BTN_BUSCAR).click()

    def encuentra_siniestros(self):
        try:
            self.wait.until(ec.presence_of_element_located(NuevoPedidoPageLocators.TBL_SINIESTROS))
            encuentra_siniestro = True
        except:
            encuentra_siniestro = False
        return encuentra_siniestro

    def mensaje_no_hay_siniestros(self):
        try:
            self.wait.until(ec.presence_of_element_located(NuevoPedidoPageLocators.LBL_NO_HAY_SINIESTROS))
            encuentra_mensaje = True
        except:
            encuentra_mensaje = False
        return encuentra_mensaje
