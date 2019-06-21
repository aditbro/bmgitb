'''test pasien creators'''

from django.test import TestCase
from django.forms.models import model_to_dict
from main.models import Client
from main.tests.factories import generate_pasien