import time

from behave import *

from page_objects import nuevo_pedido_page
from page_objects.helpers import Helpers


@given("que el analista está en nuevo pedido")
def step_impl(context):
    helper = Helpers
    time.sleep(2)  # HAY QUE BORRAR ESTO
    context.driver.get(helper.obtener_parametro('url') + "#/pedidoInspeccion")


@when("busca una {patente}")
def step_impl(context, patente):
    context.page = nuevo_pedido_page.NuevoPedidoPage(context.driver)
    helper = Helpers
    if patente == "patente valida":
        context.page.ingresar_patente(helper.obtener_parametro('patenteValida'))
    else:
        context.page.ingresar_patente(helper.obtener_parametro('patenteInvalida'))


@then("visualiza el resultado de la busqueda de patente {resultado}")
def step_impl(context, resultado):
    if resultado == "encuentra siniestro":
        assert context.page.encuentra_siniestros()
    else:
        assert context.page.encuentra_siniestros() is False
        assert context.page.mensaje_no_hay_siniestros()

