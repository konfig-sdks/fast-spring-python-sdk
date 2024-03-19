import typing_extensions

from fast_spring_python_sdk.paths import PathValues
from fast_spring_python_sdk.apis.paths.accounts_account_id import AccountsAccountId
from fast_spring_python_sdk.apis.paths.accounts_account_id_authenticate import AccountsAccountIdAuthenticate
from fast_spring_python_sdk.apis.paths.accounts import Accounts
from fast_spring_python_sdk.apis.paths.coupons import Coupons
from fast_spring_python_sdk.apis.paths.coupons_coupon_id import CouponsCouponId
from fast_spring_python_sdk.apis.paths.coupons_coupon_id_codes import CouponsCouponIdCodes
from fast_spring_python_sdk.apis.paths.events_processed import EventsProcessed
from fast_spring_python_sdk.apis.paths.events_unprocessed import EventsUnprocessed
from fast_spring_python_sdk.apis.paths.events_event_id import EventsEventId
from fast_spring_python_sdk.apis.paths.orders_order_id import OrdersOrderId
from fast_spring_python_sdk.apis.paths.ordersproductsproduct_pathlimitlimitpagepage import OrdersproductsproductPathlimitlimitpagepage
from fast_spring_python_sdk.apis.paths.ordersbeginbegin_dateendend_datelimitlimitpagepage import OrdersbeginbeginDateendendDatelimitlimitpagepage
from fast_spring_python_sdk.apis.paths.ordersproductsproduct_pathbeginbegin_dateendend_date import OrdersproductsproductPathbeginbeginDateendendDate
from fast_spring_python_sdk.apis.paths.ordersendend_date import OrdersendendDate
from fast_spring_python_sdk.apis.paths.ordersbeginbegin_dateendend_datereturnsreturn import OrdersbeginbeginDateendendDatereturnsreturn
from fast_spring_python_sdk.apis.paths.orders import Orders
from fast_spring_python_sdk.apis.paths.products_product_path import ProductsProductPath
from fast_spring_python_sdk.apis.paths.products import Products
from fast_spring_python_sdk.apis.paths.products_offers_product_path import ProductsOffersProductPath
from fast_spring_python_sdk.apis.paths.products_price import ProductsPrice
from fast_spring_python_sdk.apis.paths.products_price_id import ProductsPriceId
from fast_spring_python_sdk.apis.paths.products_pricecountrycountry import ProductsPricecountrycountry
from fast_spring_python_sdk.apis.paths.products_pricecountrycountrycurrencycurrency import ProductsPricecountrycountrycurrencycurrency
from fast_spring_python_sdk.apis.paths.products_price_idcountrycountrycurrencycurrency import ProductsPriceIdcountrycountrycurrencycurrency
from fast_spring_python_sdk.apis.paths.products_price_idcountrycountry import ProductsPriceIdcountrycountry
from fast_spring_python_sdk.apis.paths.products_id import ProductsId
from fast_spring_python_sdk.apis.paths.returns_id import ReturnsId
from fast_spring_python_sdk.apis.paths.returns import Returns
from fast_spring_python_sdk.apis.paths.sessions import Sessions
from fast_spring_python_sdk.apis.paths.subscriptions import Subscriptions
from fast_spring_python_sdk.apis.paths.subscriptions_estimate import SubscriptionsEstimate
from fast_spring_python_sdk.apis.paths.subscriptions_subscription_id import SubscriptionsSubscriptionId
from fast_spring_python_sdk.apis.paths.subscriptions_subscription_id_entries import SubscriptionsSubscriptionIdEntries
from fast_spring_python_sdk.apis.paths.subscriptions_charge import SubscriptionsCharge
from fast_spring_python_sdk.apis.paths.subscriptions_subscription_id_pause import SubscriptionsSubscriptionIdPause
from fast_spring_python_sdk.apis.paths.subscriptions_subscription_id_resume import SubscriptionsSubscriptionIdResume
from fast_spring_python_sdk.apis.paths.subscriptions_subscription_id_convert import SubscriptionsSubscriptionIdConvert
from fast_spring_python_sdk.apis.paths.subscriptions_subscription_id_history import SubscriptionsSubscriptionIdHistory
from fast_spring_python_sdk.apis.paths.quotes_id import QuotesId
from fast_spring_python_sdk.apis.paths.quotes_id_cancel import QuotesIdCancel
from fast_spring_python_sdk.apis.paths.quotes import Quotes
from fast_spring_python_sdk.apis.paths.webhooks_keys import WebhooksKeys
from fast_spring_python_sdk.apis.paths.data_v1_subscription import DataV1Subscription
from fast_spring_python_sdk.apis.paths.data_v1_revenue import DataV1Revenue
from fast_spring_python_sdk.apis.paths.data_v1_jobs_id import DataV1JobsId
from fast_spring_python_sdk.apis.paths.data_v1_jobs import DataV1Jobs
from fast_spring_python_sdk.apis.paths.data_v1_util_cache import DataV1UtilCache
from fast_spring_python_sdk.apis.paths.data_v1_downloads_id import DataV1DownloadsId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACCOUNTS_ACCOUNT_ID: AccountsAccountId,
        PathValues.ACCOUNTS_ACCOUNT_ID_AUTHENTICATE: AccountsAccountIdAuthenticate,
        PathValues.ACCOUNTS: Accounts,
        PathValues.COUPONS: Coupons,
        PathValues.COUPONS_COUPON_ID: CouponsCouponId,
        PathValues.COUPONS_COUPON_ID_CODES: CouponsCouponIdCodes,
        PathValues.EVENTS_PROCESSED: EventsProcessed,
        PathValues.EVENTS_UNPROCESSED: EventsUnprocessed,
        PathValues.EVENTS_EVENT_ID: EventsEventId,
        PathValues.ORDERS_ORDER_ID: OrdersOrderId,
        PathValues.ORDERSPRODUCTSPRODUCT_PATHLIMITLIMITPAGEPAGE: OrdersproductsproductPathlimitlimitpagepage,
        PathValues.ORDERSBEGINBEGIN_DATEENDEND_DATELIMITLIMITPAGEPAGE: OrdersbeginbeginDateendendDatelimitlimitpagepage,
        PathValues.ORDERSPRODUCTSPRODUCT_PATHBEGINBEGIN_DATEENDEND_DATE: OrdersproductsproductPathbeginbeginDateendendDate,
        PathValues.ORDERSENDEND_DATE: OrdersendendDate,
        PathValues.ORDERSBEGINBEGIN_DATEENDEND_DATERETURNSRETURN: OrdersbeginbeginDateendendDatereturnsreturn,
        PathValues.ORDERS: Orders,
        PathValues.PRODUCTS_PRODUCT_PATH: ProductsProductPath,
        PathValues.PRODUCTS: Products,
        PathValues.PRODUCTS_OFFERS_PRODUCT_PATH: ProductsOffersProductPath,
        PathValues.PRODUCTS_PRICE: ProductsPrice,
        PathValues.PRODUCTS_PRICE_ID: ProductsPriceId,
        PathValues.PRODUCTS_PRICECOUNTRYCOUNTRY: ProductsPricecountrycountry,
        PathValues.PRODUCTS_PRICECOUNTRYCOUNTRYCURRENCYCURRENCY: ProductsPricecountrycountrycurrencycurrency,
        PathValues.PRODUCTS_PRICE_IDCOUNTRYCOUNTRYCURRENCYCURRENCY: ProductsPriceIdcountrycountrycurrencycurrency,
        PathValues.PRODUCTS_PRICE_IDCOUNTRYCOUNTRY: ProductsPriceIdcountrycountry,
        PathValues.PRODUCTS_ID: ProductsId,
        PathValues.RETURNS_ID: ReturnsId,
        PathValues.RETURNS: Returns,
        PathValues.SESSIONS: Sessions,
        PathValues.SUBSCRIPTIONS: Subscriptions,
        PathValues.SUBSCRIPTIONS_ESTIMATE: SubscriptionsEstimate,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID: SubscriptionsSubscriptionId,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_ENTRIES: SubscriptionsSubscriptionIdEntries,
        PathValues.SUBSCRIPTIONS_CHARGE: SubscriptionsCharge,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_PAUSE: SubscriptionsSubscriptionIdPause,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_RESUME: SubscriptionsSubscriptionIdResume,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_CONVERT: SubscriptionsSubscriptionIdConvert,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_HISTORY: SubscriptionsSubscriptionIdHistory,
        PathValues.QUOTES_ID: QuotesId,
        PathValues.QUOTES_ID_CANCEL: QuotesIdCancel,
        PathValues.QUOTES: Quotes,
        PathValues.WEBHOOKS_KEYS: WebhooksKeys,
        PathValues.DATA_V1_SUBSCRIPTION: DataV1Subscription,
        PathValues.DATA_V1_REVENUE: DataV1Revenue,
        PathValues.DATA_V1_JOBS_ID: DataV1JobsId,
        PathValues.DATA_V1_JOBS: DataV1Jobs,
        PathValues.DATA_V1_UTIL_CACHE: DataV1UtilCache,
        PathValues.DATA_V1_DOWNLOADS_ID: DataV1DownloadsId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACCOUNTS_ACCOUNT_ID: AccountsAccountId,
        PathValues.ACCOUNTS_ACCOUNT_ID_AUTHENTICATE: AccountsAccountIdAuthenticate,
        PathValues.ACCOUNTS: Accounts,
        PathValues.COUPONS: Coupons,
        PathValues.COUPONS_COUPON_ID: CouponsCouponId,
        PathValues.COUPONS_COUPON_ID_CODES: CouponsCouponIdCodes,
        PathValues.EVENTS_PROCESSED: EventsProcessed,
        PathValues.EVENTS_UNPROCESSED: EventsUnprocessed,
        PathValues.EVENTS_EVENT_ID: EventsEventId,
        PathValues.ORDERS_ORDER_ID: OrdersOrderId,
        PathValues.ORDERSPRODUCTSPRODUCT_PATHLIMITLIMITPAGEPAGE: OrdersproductsproductPathlimitlimitpagepage,
        PathValues.ORDERSBEGINBEGIN_DATEENDEND_DATELIMITLIMITPAGEPAGE: OrdersbeginbeginDateendendDatelimitlimitpagepage,
        PathValues.ORDERSPRODUCTSPRODUCT_PATHBEGINBEGIN_DATEENDEND_DATE: OrdersproductsproductPathbeginbeginDateendendDate,
        PathValues.ORDERSENDEND_DATE: OrdersendendDate,
        PathValues.ORDERSBEGINBEGIN_DATEENDEND_DATERETURNSRETURN: OrdersbeginbeginDateendendDatereturnsreturn,
        PathValues.ORDERS: Orders,
        PathValues.PRODUCTS_PRODUCT_PATH: ProductsProductPath,
        PathValues.PRODUCTS: Products,
        PathValues.PRODUCTS_OFFERS_PRODUCT_PATH: ProductsOffersProductPath,
        PathValues.PRODUCTS_PRICE: ProductsPrice,
        PathValues.PRODUCTS_PRICE_ID: ProductsPriceId,
        PathValues.PRODUCTS_PRICECOUNTRYCOUNTRY: ProductsPricecountrycountry,
        PathValues.PRODUCTS_PRICECOUNTRYCOUNTRYCURRENCYCURRENCY: ProductsPricecountrycountrycurrencycurrency,
        PathValues.PRODUCTS_PRICE_IDCOUNTRYCOUNTRYCURRENCYCURRENCY: ProductsPriceIdcountrycountrycurrencycurrency,
        PathValues.PRODUCTS_PRICE_IDCOUNTRYCOUNTRY: ProductsPriceIdcountrycountry,
        PathValues.PRODUCTS_ID: ProductsId,
        PathValues.RETURNS_ID: ReturnsId,
        PathValues.RETURNS: Returns,
        PathValues.SESSIONS: Sessions,
        PathValues.SUBSCRIPTIONS: Subscriptions,
        PathValues.SUBSCRIPTIONS_ESTIMATE: SubscriptionsEstimate,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID: SubscriptionsSubscriptionId,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_ENTRIES: SubscriptionsSubscriptionIdEntries,
        PathValues.SUBSCRIPTIONS_CHARGE: SubscriptionsCharge,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_PAUSE: SubscriptionsSubscriptionIdPause,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_RESUME: SubscriptionsSubscriptionIdResume,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_CONVERT: SubscriptionsSubscriptionIdConvert,
        PathValues.SUBSCRIPTIONS_SUBSCRIPTION_ID_HISTORY: SubscriptionsSubscriptionIdHistory,
        PathValues.QUOTES_ID: QuotesId,
        PathValues.QUOTES_ID_CANCEL: QuotesIdCancel,
        PathValues.QUOTES: Quotes,
        PathValues.WEBHOOKS_KEYS: WebhooksKeys,
        PathValues.DATA_V1_SUBSCRIPTION: DataV1Subscription,
        PathValues.DATA_V1_REVENUE: DataV1Revenue,
        PathValues.DATA_V1_JOBS_ID: DataV1JobsId,
        PathValues.DATA_V1_JOBS: DataV1Jobs,
        PathValues.DATA_V1_UTIL_CACHE: DataV1UtilCache,
        PathValues.DATA_V1_DOWNLOADS_ID: DataV1DownloadsId,
    }
)
