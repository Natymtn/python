from behave.model import Scenario
from behave import *
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from page_objects import login_page

import json

from page_objects.helpers import Helpers


def before_all(context):
    helper = Helpers

    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome("drivers/chromedriver.exe", options=options)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    Scenario.continue_after_failed_step = False
    context.driver.get(helper.obtener_parametro('url') + "#/login")
    context.page = login_page.LoginPage(context.driver)
    context.page.login(helper.obtener_parametro('usuario'), helper.obtener_parametro('contrasenia'))


def after_all(context):
    context.driver.close()
    context.driver.quit()
