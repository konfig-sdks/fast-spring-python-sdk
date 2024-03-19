import typing_extensions

from fast_spring_python_sdk.apis.tags import TagValues
from fast_spring_python_sdk.apis.tags.products_api import ProductsApi
from fast_spring_python_sdk.apis.tags.subscriptions_api import SubscriptionsApi
from fast_spring_python_sdk.apis.tags.orders_api import OrdersApi
from fast_spring_python_sdk.apis.tags.quotes_api import QuotesApi
from fast_spring_python_sdk.apis.tags.data_api import DataApi
from fast_spring_python_sdk.apis.tags.accounts_api import AccountsApi
from fast_spring_python_sdk.apis.tags.coupons_api import CouponsApi
from fast_spring_python_sdk.apis.tags.events_api import EventsApi
from fast_spring_python_sdk.apis.tags.returns_api import ReturnsApi
from fast_spring_python_sdk.apis.tags.sessions_api import SessionsApi
from fast_spring_python_sdk.apis.tags.webhooks_api import WebhooksApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PRODUCTS: ProductsApi,
        TagValues.SUBSCRIPTIONS: SubscriptionsApi,
        TagValues.ORDERS: OrdersApi,
        TagValues.QUOTES: QuotesApi,
        TagValues.DATA: DataApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.COUPONS: CouponsApi,
        TagValues.EVENTS: EventsApi,
        TagValues.RETURNS: ReturnsApi,
        TagValues.SESSIONS: SessionsApi,
        TagValues.WEBHOOKS: WebhooksApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PRODUCTS: ProductsApi,
        TagValues.SUBSCRIPTIONS: SubscriptionsApi,
        TagValues.ORDERS: OrdersApi,
        TagValues.QUOTES: QuotesApi,
        TagValues.DATA: DataApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.COUPONS: CouponsApi,
        TagValues.EVENTS: EventsApi,
        TagValues.RETURNS: ReturnsApi,
        TagValues.SESSIONS: SessionsApi,
        TagValues.WEBHOOKS: WebhooksApi,
    }
)
