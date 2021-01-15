from django.apps import AppConfig
from deep.model import DeepModel


class BusinessRegisterConfig(AppConfig):
    name = 'BusinessRegister'
    model = DeepModel()




