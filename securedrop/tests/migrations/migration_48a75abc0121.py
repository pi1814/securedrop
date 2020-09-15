# -*- coding: utf-8 -*-

import random
import string
import uuid

from sqlalchemy import text
from sqlalchemy.exc import NoSuchColumnError

from db import db
from journalist_app import create_app
from .helpers import (random_bool, random_bytes, random_chars, random_datetime,
                      random_username, bool_or_none)

random.seed('ᕕ( ᐛ )ᕗ')


class UpgradeTester:
  """
  This migration verifies that the seen_files, seen_messages, and seen_replies association tables
  now exist, and that the data migration completes successfully.
  """

    JOURNO_NUM = 20
    SOURCE_NUM = 20

    def __init__(self, config):
        self.config = config
        self.app = create_app(config)

    def load_data(self):
        with self.app.app_context():
            for _ in range(self.SOURCE_NUM):
                self.add_source()

            for _ in range(self.JOURNO_NUM):
                self.add_journalist()

            for i in range(self.JOURNO_NUM):
                self.add_reply(i)  # add one reply from each journalist to

            for i in range(self.SOURCE_NUM):
                self.add_message(i)  # add one message from each source

            for i in range(self.SOURCE_NUM):
                self.add_file(i)  # add one file from each source

    def check_upgrade(self):
      pass

    @staticmethod
    def add_source():
      pass

    @staticmethod
    def add_journalist():
      pass

    @staticmethod
    def add_reply(journalist_id):
      pass

    @staticmethod
    def add_message(source_id):
      pass

    @staticmethod
    def add_file(source_id):
      pass


class DowngradeTester:
  """
  This migration verifies that the seen_files, seen_messages, and seen_replies association tables
  are removed.
  """

    JOURNO_NUM = 20
    SOURCE_NUM = 20

    def __init__(self, config):
        self.config = config
        self.app = create_app(config)

    def load_data(self):
        with self.app.app_context():
            for _ in range(self.SOURCE_NUM):
                self.add_source()

            for _ in range(self.JOURNO_NUM):
                self.add_journalist()

            for i in range(self.JOURNO_NUM):
                self.add_reply(i)  # add one reply from each journalist to

            for i in range(self.SOURCE_NUM):
                self.add_message(i)  # add one message from each source

            for i in range(self.SOURCE_NUM):
                self.add_file(i)  # add one file from each source

    def check_downgrade(self):
        pass

    @staticmethod
    def add_source():
      pass

    @staticmethod
    def add_journalist():
      pass

    @staticmethod
    def add_reply(journalist_id):
      pass

    @staticmethod
    def add_message(source_id):
      pass

    @staticmethod
    def add_file(source_id):
      pass