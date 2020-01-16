#!/usr/bin/env python3

import schedule
import time

from websites import cnn
from websites import guardian
from database import manager
from telegram import request as tel_req


def run_program():
    """
    Business logic, e.g. time and order management, happens here.
    """

    # CNN news
    schedule.every().day.at("08:00").do(run_cnn)
    schedule.every().day.at("23:00").do(run_guardian)

    schedule.every(2).seconds.do(run_guardian)

    while True:
        schedule.run_pending()
        time.sleep(1)


def run_cnn():
    article_model = cnn.parse_article()
    manager.save(article_model)
    tel_req.send_message(article_model)


def run_guardian():
    article_model = guardian.parse_article()
    manager.save(article_model)
    tel_req.send_message(article_model)


if __name__ == "__main__":
    run_program()
