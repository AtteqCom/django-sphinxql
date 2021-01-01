import shutil
import os
from subprocess import DEVNULL
from time import sleep
from django.conf import settings
from django.test import TransactionTestCase
from sphinxql import configuration


class Searchd:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Searchd, cls).__new__(cls)
            cls._instance.running = False
            cls.setUpBool = True

        return cls._instance

    def start(self):
        if self.running:
            return

        # Django does not support apps using its connections on loading, see
        # https://docs.djangoproject.com/en/1.7/ref/applications/#django.apps.AppConfig.ready
        # Doing so picks the wrong database for tests.
        # We reconfigure after loading to get the right test database.
        configuration.indexes_configurator.configure(True, True)
        configuration.indexes_configurator.output()

        self._clean_sphinx_index()

        configuration.index()
        configuration.start(DEVNULL)
        # Give searchd some time to start up
        # This is cumbersome, reading the information about start from pipe would be much nicer!
        sleep(1)
        self.running = True

    def stop(self):
        if self.running:
            configuration.stop(silent_fail=False)
            shutil.rmtree(settings.INDEXES['path'], ignore_errors=True)
            self.running = False

    def index(self):
        return configuration.index()

    def reindex(self):
        return configuration.reindex()

    def _clean_sphinx_index(self):
        if os.path.exists(settings.INDEXES['path']):
            try:
                self.stop()
            except:
                pass

            try:
                shutil.rmtree(settings.INDEXES['path'])
            except:
                sleep(5)  # Wait until the server stops and releases all the locks
                shutil.rmtree(settings.INDEXES['path'])
        os.makedirs(settings.INDEXES['path'], exist_ok=True)


class SphinxQLTestCaseMixin:
    running = False

    def setUp(self):
        super(SphinxQLTestCaseMixin, self).setUp()
        Searchd().start()

    def index(self):
        """
        Used to reindex the sphinx index.
        """
        return Searchd().reindex()

    def tearDown(cls):
        Searchd().stop()
        super(SphinxQLTestCaseMixin, cls).tearDown()


class SphinxQLTestCase(SphinxQLTestCaseMixin, TransactionTestCase):
    pass
