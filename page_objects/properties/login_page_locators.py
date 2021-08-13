from selenium.webdriver.common.by import By


class LoginPageLocators:
    INP_USUARIO = (By.NAME, "usuario")
    INP_CONTRASENIA = (By.NAME, "contrasenia")
    BTN_INGRESAR = (By.ID, "btn-ingresar")

