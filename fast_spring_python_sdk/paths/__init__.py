# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from fast_spring_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ACCOUNTS_ACCOUNT_ID = "/accounts/{account_id}"
    ACCOUNTS_ACCOUNT_ID_AUTHENTICATE = "/accounts/{account_id}/authenticate"
    ACCOUNTS = "/accounts"
    COUPONS = "/coupons"
    COUPONS_COUPON_ID = "/coupons/{coupon_id}"
    COUPONS_COUPON_ID_CODES = "/coupons/{coupon_id}/codes"
    EVENTS_PROCESSED = "/events/processed"
    EVENTS_UNPROCESSED = "/events/unprocessed"
    EVENTS_EVENT_ID = "/events/{event_id}"
    ORDERS_ORDER_ID = "/orders/{order_id}"
    ORDERSPRODUCTSPRODUCT_PATHLIMITLIMITPAGEPAGE = "/orders?products&#x3D;{product_path}&amp;limit&#x3D;{limit}&amp;page&#x3D;{page}"
    ORDERSBEGINBEGIN_DATEENDEND_DATELIMITLIMITPAGEPAGE = "/orders?begin&#x3D;{begin_date}&amp;end&#x3D;{end_date}&amp;limit&#x3D;{limit}&amp;page&#x3D;{page}"
    ORDERSPRODUCTSPRODUCT_PATHBEGINBEGIN_DATEENDEND_DATE = "/orders?products&#x3D;{product_path}&amp;begin&#x3D;{begin_date}&amp;end&#x3D;{end_date}"
    ORDERSENDEND_DATE = "/orders?end&#x3D;{end_date}"
    ORDERSBEGINBEGIN_DATEENDEND_DATERETURNSRETURN = "/orders?begin&#x3D;{begin_date}&amp;end&#x3D;{end_date}&amp;returns&#x3D;{return}"
    ORDERS = "/orders"
    PRODUCTS_PRODUCT_PATH = "/products/{product_path}"
    PRODUCTS = "/products"
    PRODUCTS_OFFERS_PRODUCT_PATH = "/products/offers/{product_path}"
    PRODUCTS_PRICE = "/products/price"
    PRODUCTS_PRICE_ID = "/products/price/{id}"
    PRODUCTS_PRICECOUNTRYCOUNTRY = "/products/price?country&#x3D;{country}"
    PRODUCTS_PRICECOUNTRYCOUNTRYCURRENCYCURRENCY = "/products/price?country&#x3D;{country}&amp;currency&#x3D;{currency}"
    PRODUCTS_PRICE_IDCOUNTRYCOUNTRYCURRENCYCURRENCY = "/products/price/{id}?country&#x3D;{country}&amp;currency&#x3D;{currency}"
    PRODUCTS_PRICE_IDCOUNTRYCOUNTRY = "/products/price/{id}?country&#x3D;{country}"
    PRODUCTS_ID = "/products/{id}"
    RETURNS_ID = "/returns/{id}"
    RETURNS = "/returns"
    SESSIONS = "/sessions"
    SUBSCRIPTIONS = "/subscriptions"
    SUBSCRIPTIONS_ESTIMATE = "/subscriptions/estimate"
    SUBSCRIPTIONS_SUBSCRIPTION_ID = "/subscriptions/{subscription_id}"
    SUBSCRIPTIONS_SUBSCRIPTION_ID_ENTRIES = "/subscriptions/{subscription_id}/entries"
    SUBSCRIPTIONS_CHARGE = "/subscriptions/charge"
    SUBSCRIPTIONS_SUBSCRIPTION_ID_PAUSE = "/subscriptions/{subscription_id}/pause"
    SUBSCRIPTIONS_SUBSCRIPTION_ID_RESUME = "/subscriptions/{subscription_id}/resume"
    SUBSCRIPTIONS_SUBSCRIPTION_ID_CONVERT = "/subscriptions/{subscription_id}/convert"
    SUBSCRIPTIONS_SUBSCRIPTION_ID_HISTORY = "/subscriptions/{subscription_id}/history"
    QUOTES_ID = "/quotes/{id}"
    QUOTES_ID_CANCEL = "/quotes/{id}/cancel"
    QUOTES = "/quotes"
    WEBHOOKS_KEYS = "/webhooks/keys"
    DATA_V1_SUBSCRIPTION = "/data/v1/subscription"
    DATA_V1_REVENUE = "/data/v1/revenue"
    DATA_V1_JOBS_ID = "/data/v1/jobs/{id}"
    DATA_V1_JOBS = "/data/v1/jobs"
    DATA_V1_UTIL_CACHE = "/data/v1/util/cache"
    DATA_V1_DOWNLOADS_ID = "/data/v1/downloads/{id}"