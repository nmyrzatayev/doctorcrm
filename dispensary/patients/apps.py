# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PatientsConfig(AppConfig):
    name = 'dispensary.patients'
    verbose_name = _(u'Пациенты')


default_app_config = '{module}.{app}'.format(
    module=__name__,
    app=PatientsConfig.__name__
)
