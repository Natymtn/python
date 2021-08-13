from page_objects.properties.login_page_locators import LoginPageLocators


class LoginPage(LoginPageLocators):
    def __init__(self, driver):
        self.driver = driver

    def login(self, usuario, contrasenia):
        self.driver.find_element(*LoginPageLocators.INP_USUARIO).send_keys(usuario)
        self.driver.find_element(*LoginPageLocators.INP_CONTRASENIA).send_keys(contrasenia)
        self.driver.find_element(*LoginPageLocators.BTN_INGRESAR).click()
