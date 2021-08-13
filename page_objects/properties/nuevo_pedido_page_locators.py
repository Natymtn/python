from selenium.webdriver.common.by import By


class NuevoPedidoPageLocators:
    INP_PATENTE = (By.XPATH, "//input[@formcontrolname = 'patente']")
    BTN_BUSCAR = (By.XPATH, "//label[contains(text(), 'Ingrese la patente')]/following-sibling::div//button")
    TBL_SINIESTROS = (By.XPATH, "//table[@role='grid']")
    LBL_NO_HAY_SINIESTROS = (By.XPATH, "//p[text()='No se encontraron siniestros para la patente buscada']")
