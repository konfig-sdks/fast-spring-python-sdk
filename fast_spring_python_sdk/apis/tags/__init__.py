# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from fast_spring_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    PRODUCTS = "Products"
    SUBSCRIPTIONS = "Subscriptions"
    ORDERS = "Orders"
    QUOTES = "Quotes"
    DATA = "Data"
    ACCOUNTS = "Accounts"
    COUPONS = "Coupons"
    EVENTS = "Events"
    RETURNS = "Returns"
    SESSIONS = "Sessions"
    WEBHOOKS = "Webhooks"
