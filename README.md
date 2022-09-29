# Brock Class Availability Scraper

This is a WORK IN PROGRESS project to scrape class spot availability numbers from the course planning page.

## Installation

To install, optionally create a python virtual environment (`python -m venv venv`), then install the dependencies (`pip install -r requirements.txt`).

Rename `sekrets.py.changeme` to contain your login brock login information. This project assumes you have 2-factor authentication enabled on your account. Place the 2fa generator key in `TOTP_GEN`.

## Usage

Simply run `main.py`.