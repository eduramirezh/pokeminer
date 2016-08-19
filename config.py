# coding: utf-8
from datetime import datetime

DB_ENGINE = 'sqlite:///db.sqlite'
ENCRYPT_PATH = './libencrypt.so'

AREA_NAME = u'Santiago'
LANGUAGE = 'EN'  # ISO 639-1 codes EN, DE, FR, and ZH currently supported.
MAP_START = (-33.3558958, -70.8161943)
MAP_END = (-33.6218522, -70.4972985)
MAP_PROVIDER_URL = '//{s}.tile.osm.org/{z}/{x}/{y}.png'
MAP_PROVIDER_ATTRIBUTION = '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
GRID = (1, 1)  # row, column
DISABLE_WORKERS = []
CYCLES_PER_WORKER = 3
SCAN_DELAY = 10  # seconds
PROXIES = None  # Insert dictionary with 'http' and 'https' keys to enable

SCAN_RADIUS = 70  # metres

ACCOUNTS = [
    ('contactodjango', '123123123', 'ptc')
]

TRASH_IDS = []
#STAGE2 = [3, 6, 9, 12, 15, 18, 31, 34, 45, 62, 65, 68, 71, 76, 94, 139, 141, 149, 149]

REPORT_SINCE = datetime(2016, 8, 18)
GOOGLE_MAPS_KEY = 'AIzaSyBSIwr4LxaDsyAOBgsUW1ufLQ_teYkqBrg'
