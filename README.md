<div align="left">

[![Visit Fastspring](./header.png)](https://fastspring.com&#x2F;)

# Fastspring<a id="fastspring"></a>

The FastSpring API and its supported requests, data, endpoints, and rate limits.

The FastSpring API is a backend service you can use to communicate with your FastSpring Store programmatically. It requires basic understanding of HTTP communication methods. The primary API communication methods include:
- **GET** - request data from your store
- **POST** - send data to your store, such as creating a new product record
- **DELETE** - remove data from your store

The structure of the JSON data sent and received using the API is very similar to Webhooks. However, using the FastSpring API, you initiate all communication with your FastSpring Store.

If you prefer a client-side method of communicating with your FastSpring Store and generating dynamic webpage content, check out the [Store Builder Library](https://fastspring.com/docs/get-started-with-store-builder-library/).

## Access the API<a id="access-the-api"></a>

#### API Credentials and Authentication<a id="api-credentials-and-authentication"></a>

FastSpring API credentials consist of a single username and password for your entire Store. The username and password are used for [Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) when making requests to the API.

#### Obtain Your API Credentials<a id="obtain-your-api-credentials"></a>

1. Log on to the FastSpring App and navigate to [Integrations](https://fastspring.com/docs/integrations) > **API Credentials**. Initially, the only option on this page is the **Create** command.

2. Click **Create** to generate your API **Username** and **Password**. The page automatically refreshes, and then your credentials are displayed.

3. Make a note of the credentials and store them securely.

The API credentials allow complete access and control over your FastSpring Store. You will not be able to view the password in the FastSpring App after this session. If you forget your API credentials, you can reset them, however any of your stored procedures that rely on API access must be updated immediately with the new credentials. Otherwise, the API requests will fail.

## API Requests<a id="api-requests"></a>

**Make all requests to https://api.fastspring.com**

When you make your requests, consider the following:
- Ensure that the HTTP methods for all calls use uppercase letters (“GET,” “POST,” “DELETE”) Lowercase letters may result in a 404 error response.
- FastSpring requires TLS 1.2 (or later) encryption for all calls to the FastSpring API. 
- The API requires a **User-Agent** header in all requests. If your request does not include it, you may receive an 401 error message when attempting to make API requests.
- The API uses basic authentication and does not support URL-encoded authentication. Use **Base64** to encode your username and password in the header.



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`fastspring.accounts.create_new_account`](#fastspringaccountscreate_new_account)
  * [`fastspring.accounts.get_account_by_id`](#fastspringaccountsget_account_by_id)
  * [`fastspring.accounts.get_authenticated_management_url`](#fastspringaccountsget_authenticated_management_url)
  * [`fastspring.accounts.get_by_parameter`](#fastspringaccountsget_by_parameter)
  * [`fastspring.accounts.update_account_by_id`](#fastspringaccountsupdate_account_by_id)
  * [`fastspring.coupons.assign_codes_to_coupon`](#fastspringcouponsassign_codes_to_coupon)
  * [`fastspring.coupons.create_new_coupon`](#fastspringcouponscreate_new_coupon)
  * [`fastspring.coupons.delete_associated_codes`](#fastspringcouponsdelete_associated_codes)
  * [`fastspring.coupons.get_codes_assigned_to_coupon`](#fastspringcouponsget_codes_assigned_to_coupon)
  * [`fastspring.coupons.get_details`](#fastspringcouponsget_details)
  * [`fastspring.data.download_report_by_id`](#fastspringdatadownload_report_by_id)
  * [`fastspring.data.generate_revenue_report`](#fastspringdatagenerate_revenue_report)
  * [`fastspring.data.generate_subscription_report`](#fastspringdatagenerate_subscription_report)
  * [`fastspring.data.get_job_information`](#fastspringdataget_job_information)
  * [`fastspring.data.get_job_information_0`](#fastspringdataget_job_information_0)
  * [`fastspring.data.reset_cache_for_service_end_points`](#fastspringdatareset_cache_for_service_end_points)
  * [`fastspring.events.get_processed_events`](#fastspringeventsget_processed_events)
  * [`fastspring.events.get_unprocessed_events`](#fastspringeventsget_unprocessed_events)
  * [`fastspring.events.update_event_by_id`](#fastspringeventsupdate_event_by_id)
  * [`fastspring.orders.get_by_date_range`](#fastspringordersget_by_date_range)
  * [`fastspring.orders.get_by_end_date`](#fastspringordersget_by_end_date)
  * [`fastspring.orders.get_by_id`](#fastspringordersget_by_id)
  * [`fastspring.orders.get_by_product_path`](#fastspringordersget_by_product_path)
  * [`fastspring.orders.get_by_product_path_and_date_range`](#fastspringordersget_by_product_path_and_date_range)
  * [`fastspring.orders.get_orders_with_returns`](#fastspringordersget_orders_with_returns)
  * [`fastspring.orders.update_tags_and_attributes`](#fastspringordersupdate_tags_and_attributes)
  * [`fastspring.products.create_and_update`](#fastspringproductscreate_and_update)
  * [`fastspring.products.create_or_update_offers`](#fastspringproductscreate_or_update_offers)
  * [`fastspring.products.delete_product_by_id`](#fastspringproductsdelete_product_by_id)
  * [`fastspring.products.get_all_offers_by_type`](#fastspringproductsget_all_offers_by_type)
  * [`fastspring.products.get_all_product_ids`](#fastspringproductsget_all_product_ids)
  * [`fastspring.products.get_all_product_prices`](#fastspringproductsget_all_product_prices)
  * [`fastspring.products.get_all_product_prices_by_country`](#fastspringproductsget_all_product_prices_by_country)
  * [`fastspring.products.get_all_product_prices_by_country_and_currency`](#fastspringproductsget_all_product_prices_by_country_and_currency)
  * [`fastspring.products.get_by_product_path`](#fastspringproductsget_by_product_path)
  * [`fastspring.products.get_price_by_id`](#fastspringproductsget_price_by_id)
  * [`fastspring.products.get_product_price_by_country`](#fastspringproductsget_product_price_by_country)
  * [`fastspring.products.get_product_price_by_country_and_currency`](#fastspringproductsget_product_price_by_country_and_currency)
  * [`fastspring.quotes.cancel_quote_by_id`](#fastspringquotescancel_quote_by_id)
  * [`fastspring.quotes.create_new_quote`](#fastspringquotescreate_new_quote)
  * [`fastspring.quotes.delete_quote_by_id`](#fastspringquotesdelete_quote_by_id)
  * [`fastspring.quotes.get_all_quotes`](#fastspringquotesget_all_quotes)
  * [`fastspring.quotes.get_by_id`](#fastspringquotesget_by_id)
  * [`fastspring.quotes.update_quote_by_id`](#fastspringquotesupdate_quote_by_id)
  * [`fastspring.returns.create_new_return`](#fastspringreturnscreate_new_return)
  * [`fastspring.returns.get_by_id`](#fastspringreturnsget_by_id)
  * [`fastspring.sessions.create_new_session`](#fastspringsessionscreate_new_session)
  * [`fastspring.subscriptions.cancel_subscription_by_id`](#fastspringsubscriptionscancel_subscription_by_id)
  * [`fastspring.subscriptions.convert_expired_trial_without_payment_method`](#fastspringsubscriptionsconvert_expired_trial_without_payment_method)
  * [`fastspring.subscriptions.get_all_subscriptions`](#fastspringsubscriptionsget_all_subscriptions)
  * [`fastspring.subscriptions.get_by_id`](#fastspringsubscriptionsget_by_id)
  * [`fastspring.subscriptions.get_entries`](#fastspringsubscriptionsget_entries)
  * [`fastspring.subscriptions.get_plan_change_history`](#fastspringsubscriptionsget_plan_change_history)
  * [`fastspring.subscriptions.pause_subscription`](#fastspringsubscriptionspause_subscription)
  * [`fastspring.subscriptions.preview_plan_change`](#fastspringsubscriptionspreview_plan_change)
  * [`fastspring.subscriptions.rebill_managed_subscription`](#fastspringsubscriptionsrebill_managed_subscription)
  * [`fastspring.subscriptions.remove_scheduled_pause`](#fastspringsubscriptionsremove_scheduled_pause)
  * [`fastspring.subscriptions.resume_subscription`](#fastspringsubscriptionsresume_subscription)
  * [`fastspring.subscriptions.update_subscription`](#fastspringsubscriptionsupdate_subscription)
  * [`fastspring.webhooks.update_webhook_key_secret`](#fastspringwebhooksupdate_webhook_key_secret)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=FastSpring&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from fast_spring_python_sdk import FastSpring, ApiException

fastspring = FastSpring(username="YOUR_USERNAME", password="YOUR_PASSWORD")

try:
    # Create an account
    create_new_account_response = fastspring.accounts.create_new_account(
        contact={
            "company": "ABC Company",
            "email": "ne1@all.com",
            "first": "Leeroy",
            "last": "Jenkins",
            "phone": "+1254789654",
        },
    )
except ApiException as e:
    print("Exception when calling AccountsApi.create_new_account: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from fast_spring_python_sdk import FastSpring, ApiException

fastspring = FastSpring(username="YOUR_USERNAME", password="YOUR_PASSWORD")


async def main():
    try:
        # Create an account
        create_new_account_response = await fastspring.accounts.acreate_new_account(
            contact={
                "company": "ABC Company",
                "email": "ne1@all.com",
                "first": "Leeroy",
                "last": "Jenkins",
                "phone": "+1254789654",
            },
        )
    except ApiException as e:
        print("Exception when calling AccountsApi.create_new_account: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from fast_spring_python_sdk import FastSpring, ApiException

fastspring = FastSpring(username="YOUR_USERNAME", password="YOUR_PASSWORD")

try:
    # Create an account
    create_new_account_response = fastspring.accounts.raw.create_new_account(
        contact={
            "company": "ABC Company",
            "email": "ne1@all.com",
            "first": "Leeroy",
            "last": "Jenkins",
            "phone": "+1254789654",
        },
    )
    pprint(create_new_account_response.headers)
    pprint(create_new_account_response.status)
    pprint(create_new_account_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccountsApi.create_new_account: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `fastspring.accounts.create_new_account`<a id="fastspringaccountscreate_new_account"></a>

Create an account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_account_response = fastspring.accounts.create_new_account(
    contact={
        "company": "ABC Company",
        "email": "ne1@all.com",
        "first": "Leeroy",
        "last": "Jenkins",
        "phone": "+1254789654",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### contact: `ContactRequest`<a id="contact-contactrequest"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateOneAccount`](./fast_spring_python_sdk/type/create_one_account.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.accounts.get_account_by_id`<a id="fastspringaccountsget_account_by_id"></a>

Get an account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_account_by_id_response = fastspring.accounts.get_account_by_id(
    account_id="account_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

Account Id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{account_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.accounts.get_authenticated_management_url`<a id="fastspringaccountsget_authenticated_management_url"></a>

Get authenticated account management URL

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_authenticated_management_url_response = (
    fastspring.accounts.get_authenticated_management_url(
        account_id="account_id_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

Account Id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{account_id}/authenticate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.accounts.get_by_parameter`<a id="fastspringaccountsget_by_parameter"></a>

If no parameters are sent, the operation will return a list of accountIDs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_parameter_response = fastspring.accounts.get_by_parameter(
    email="string_example",
    custom="string_example",
    _global="string_example",
    order_id="string_example",
    order_reference="string_example",
    subscription_id="string_example",
    products="string_example",
    subscriptions="string_example",
    refunds="string_example",
    limit=3.14,
    page=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

Account email

##### custom: `str`<a id="custom-str"></a>

Account custom key

##### _global: `str`<a id="_global-str"></a>

Account global key

##### order_id: `str`<a id="order_id-str"></a>

Order id

##### order_reference: `str`<a id="order_reference-str"></a>

Order Reference

##### subscription_id: `str`<a id="subscription_id-str"></a>

Subscription ID

##### products: `str`<a id="products-str"></a>

Product ID

##### subscriptions: `str`<a id="subscriptions-str"></a>

\"active\", \"ended\", \"canceled\", \"started\" will return accounts with subscriptions in the corresponding state

##### refunds: `str`<a id="refunds-str"></a>

true

##### limit: `Union[int, float]`<a id="limit-unionint-float"></a>

integer value indicating the maximum number of records to be returned Or, when used together with page, the maximum number of records to be returned per page

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

Integer value that must be used in conjunction with limit to specify which page of results should be returned

#### 🔄 Return<a id="🔄-return"></a>

[`AccountsGetByParameterResponse`](./fast_spring_python_sdk/pydantic/accounts_get_by_parameter_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.accounts.update_account_by_id`<a id="fastspringaccountsupdate_account_by_id"></a>

Update account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_account_by_id_response = fastspring.accounts.update_account_by_id(
    account_id="account_id_example",
    contact={
        "company": "ABC Company",
        "email": "ne1@all.com",
        "first": "Leeroy",
        "last": "Jenkins",
        "phone": "+1254789654",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

Account Id

##### contact: `ContactRequest`<a id="contact-contactrequest"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateOneAccount`](./fast_spring_python_sdk/type/create_one_account.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{account_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.coupons.assign_codes_to_coupon`<a id="fastspringcouponsassign_codes_to_coupon"></a>

Assign codes to a coupon

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
fastspring.coupons.assign_codes_to_coupon(
    codes=["string_example"],
    coupon_id="coupon_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### codes: [`AddcouponcodestoacouponRequestCodes`](./fast_spring_python_sdk/type/addcouponcodestoacoupon_request_codes.py)<a id="codes-addcouponcodestoacouponrequestcodesfast_spring_python_sdktypeaddcouponcodestoacoupon_request_codespy"></a>

##### coupon_id: `str`<a id="coupon_id-str"></a>

Coupon Id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddcouponcodestoacouponRequest`](./fast_spring_python_sdk/type/addcouponcodestoacoupon_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/coupons/{coupon_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.coupons.create_new_coupon`<a id="fastspringcouponscreate_new_coupon"></a>

Create a coupon

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
fastspring.coupons.create_new_coupon(
    body=None,
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/coupons` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.coupons.delete_associated_codes`<a id="fastspringcouponsdelete_associated_codes"></a>

Delete all codes associated with a coupon

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
fastspring.coupons.delete_associated_codes(
    coupon_id="coupon_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### coupon_id: `str`<a id="coupon_id-str"></a>

Coupon Id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/coupons/{coupon_id}/codes` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.coupons.get_codes_assigned_to_coupon`<a id="fastspringcouponsget_codes_assigned_to_coupon"></a>

Get coupon codes assigned to a coupon

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_codes_assigned_to_coupon_response = fastspring.coupons.get_codes_assigned_to_coupon(
    body=None,
    coupon_id="coupon_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### coupon_id: `str`<a id="coupon_id-str"></a>

Coupon Id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/coupons/{coupon_id}/codes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.coupons.get_details`<a id="fastspringcouponsget_details"></a>

Retrieve coupon details

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = fastspring.coupons.get_details(
    coupon_id="coupon_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### coupon_id: `str`<a id="coupon_id-str"></a>

Coupon Id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/coupons/{coupon_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.data.download_report_by_id`<a id="fastspringdatadownload_report_by_id"></a>

Download a report based on job ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
download_report_by_id_response = fastspring.data.download_report_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data/v1/downloads/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.data.generate_revenue_report`<a id="fastspringdatagenerate_revenue_report"></a>

Generates a revenue report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_revenue_report_response = fastspring.data.generate_revenue_report(
    filter={
        "start_date": "YYYY-MM-DD",
        "end_date": "YYYY-MM-DD",
        "sync_date": "YYYY-MM-DD",
    },
    report_columns=["string_example"],
    group_by=["string_example"],
    page_count=30,
    page_number=0,
    _async=False,
    notification_emails=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filter: [`FilterRevenueReportRequest`](./fast_spring_python_sdk/type/filter_revenue_report_request.py)<a id="filter-filterrevenuereportrequestfast_spring_python_sdktypefilter_revenue_report_requestpy"></a>


##### report_columns: [`GenerateRevenueReportRequestReportColumns`](./fast_spring_python_sdk/type/generate_revenue_report_request_report_columns.py)<a id="report_columns-generaterevenuereportrequestreportcolumnsfast_spring_python_sdktypegenerate_revenue_report_request_report_columnspy"></a>

##### group_by: [`GenerateRevenueReportRequestGroupBy`](./fast_spring_python_sdk/type/generate_revenue_report_request_group_by.py)<a id="group_by-generaterevenuereportrequestgroupbyfast_spring_python_sdktypegenerate_revenue_report_request_group_bypy"></a>

##### page_count: `int`<a id="page_count-int"></a>

##### page_number: `int`<a id="page_number-int"></a>

##### _async: `bool`<a id="_async-bool"></a>

##### notification_emails: [`GenerateRevenueReportRequestNotificationEmails`](./fast_spring_python_sdk/type/generate_revenue_report_request_notification_emails.py)<a id="notification_emails-generaterevenuereportrequestnotificationemailsfast_spring_python_sdktypegenerate_revenue_report_request_notification_emailspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GenerateRevenueReportRequest`](./fast_spring_python_sdk/type/generate_revenue_report_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DataGenerateRevenueReportResponse`](./fast_spring_python_sdk/pydantic/data_generate_revenue_report_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data/v1/revenue` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.data.generate_subscription_report`<a id="fastspringdatagenerate_subscription_report"></a>

Generates a subscription report

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_subscription_report_response = fastspring.data.generate_subscription_report(
    filter={
        "start_date": "YYYY-MM-DD",
        "end_date": "YYYY-MM-DD",
        "sync_date": "YYYY-MM-DD",
    },
    report_columns=["string_example"],
    group_by=["string_example"],
    page_count=30,
    page_number=0,
    _async=False,
    notification_emails=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filter: [`FilterSubscriptionReportRequest`](./fast_spring_python_sdk/type/filter_subscription_report_request.py)<a id="filter-filtersubscriptionreportrequestfast_spring_python_sdktypefilter_subscription_report_requestpy"></a>


##### report_columns: [`GenerateSubscriptionReportRequestReportColumns`](./fast_spring_python_sdk/type/generate_subscription_report_request_report_columns.py)<a id="report_columns-generatesubscriptionreportrequestreportcolumnsfast_spring_python_sdktypegenerate_subscription_report_request_report_columnspy"></a>

##### group_by: [`GenerateSubscriptionReportRequestGroupBy`](./fast_spring_python_sdk/type/generate_subscription_report_request_group_by.py)<a id="group_by-generatesubscriptionreportrequestgroupbyfast_spring_python_sdktypegenerate_subscription_report_request_group_bypy"></a>

##### page_count: `int`<a id="page_count-int"></a>

##### page_number: `int`<a id="page_number-int"></a>

##### _async: `bool`<a id="_async-bool"></a>

##### notification_emails: [`GenerateSubscriptionReportRequestNotificationEmails`](./fast_spring_python_sdk/type/generate_subscription_report_request_notification_emails.py)<a id="notification_emails-generatesubscriptionreportrequestnotificationemailsfast_spring_python_sdktypegenerate_subscription_report_request_notification_emailspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GenerateSubscriptionReportRequest`](./fast_spring_python_sdk/type/generate_subscription_report_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DataGenerateSubscriptionReportResponse`](./fast_spring_python_sdk/pydantic/data_generate_subscription_report_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data/v1/subscription` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.data.get_job_information`<a id="fastspringdataget_job_information"></a>

Get job information based on a job ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_information_response = fastspring.data.get_job_information(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data/v1/jobs/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.data.get_job_information_0`<a id="fastspringdataget_job_information_0"></a>

Get information from a job listing.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_information_0_response = fastspring.data.get_job_information_0()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data/v1/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.data.reset_cache_for_service_end_points`<a id="fastspringdatareset_cache_for_service_end_points"></a>

Reset cache for data service end points.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
reset_cache_for_service_end_points_response = (
    fastspring.data.reset_cache_for_service_end_points()
)
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data/v1/util/cache` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.events.get_processed_events`<a id="fastspringeventsget_processed_events"></a>

Get processed events

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_processed_events_response = fastspring.events.get_processed_events(
    days=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### days: `int`<a id="days-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events/processed` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.events.get_unprocessed_events`<a id="fastspringeventsget_unprocessed_events"></a>

Get unprocessed events

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_unprocessed_events_response = fastspring.events.get_unprocessed_events(
    begin=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### begin: `int`<a id="begin-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events/unprocessed` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.events.update_event_by_id`<a id="fastspringeventsupdate_event_by_id"></a>

Update an event

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
fastspring.events.update_event_by_id(
    processed=True,
    event_id="event_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### processed: `bool`<a id="processed-bool"></a>

##### event_id: `str`<a id="event_id-str"></a>

Event Id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateasingleeventRequest`](./fast_spring_python_sdk/type/updateasingleevent_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/events/{event_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.orders.get_by_date_range`<a id="fastspringordersget_by_date_range"></a>

Get orders by date range

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_date_range_response = fastspring.orders.get_by_date_range(
    begin_date="begin_date_example",
    end_date="end_date_example",
    limit=3.14,
    page=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### begin_date: `str`<a id="begin_date-str"></a>

filters results to include transactions after the specified begin date (must be at least one day before the specified end date), the format must be MM/DD/YY

##### end_date: `str`<a id="end_date-str"></a>

filters results to include transactions before the specified end date, the format must be MM/DD/YY

##### limit: `Union[int, float]`<a id="limit-unionint-float"></a>

integer limits the number of order records returned per page (default is 50 records)

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

specifies page number of results to be returned; used together with limit to control pagination

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/orders?begin&#x3D;{begin_date}&amp;end&#x3D;{end_date}&amp;limit&#x3D;{limit}&amp;page&#x3D;{page}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.orders.get_by_end_date`<a id="fastspringordersget_by_end_date"></a>

Get orders by end date

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_end_date_response = fastspring.orders.get_by_end_date(
    end_date="end_date_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### end_date: `str`<a id="end_date-str"></a>

filters results to include transactions before the specified end date, the format must be MM/DD/YY

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/orders?end&#x3D;{end_date}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.orders.get_by_id`<a id="fastspringordersget_by_id"></a>

Get orders by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = fastspring.orders.get_by_id(
    order_id="order_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### order_id: `str`<a id="order_id-str"></a>

Order Id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/orders/{order_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.orders.get_by_product_path`<a id="fastspringordersget_by_product_path"></a>

Get orders by product path

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_product_path_response = fastspring.orders.get_by_product_path(
    product_path="product_path_example",
    limit=3.14,
    page=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### product_path: `str`<a id="product_path-str"></a>

Product path

##### limit: `Union[int, float]`<a id="limit-unionint-float"></a>

integer limits the number of order records returned per page (default is 50 records)

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

specifies page number of results to be returned; used together with limit to control pagination

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/orders?products&#x3D;{product_path}&amp;limit&#x3D;{limit}&amp;page&#x3D;{page}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.orders.get_by_product_path_and_date_range`<a id="fastspringordersget_by_product_path_and_date_range"></a>

Get orders by product path AND date range

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_product_path_and_date_range_response = (
    fastspring.orders.get_by_product_path_and_date_range(
        product_path="product_path_example",
        begin_date="begin_date_example",
        end_date="end_date_example",
        limit=3.14,
        page=3.14,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### product_path: `str`<a id="product_path-str"></a>

Product path

##### begin_date: `str`<a id="begin_date-str"></a>

filters results to include transactions after the specified begin date (must be at least one day before the specified end date), the format must be yyyy-mm-dd

##### end_date: `str`<a id="end_date-str"></a>

filters results to include transactions before the specified end date, the format must be yyyy-mm-dd

##### limit: `Union[int, float]`<a id="limit-unionint-float"></a>

integer limits the number of order records returned per page (default is 50 records)

##### page: `Union[int, float]`<a id="page-unionint-float"></a>

specifies page number of results to be returned; used together with limit to control pagination

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/orders?products&#x3D;{product_path}&amp;begin&#x3D;{begin_date}&amp;end&#x3D;{end_date}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.orders.get_orders_with_returns`<a id="fastspringordersget_orders_with_returns"></a>

Get orders with returns only

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_orders_with_returns_response = fastspring.orders.get_orders_with_returns(
    begin_date="begin_date_example",
    end_date="end_date_example",
    _return=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### begin_date: `str`<a id="begin_date-str"></a>

filters results to include transactions after the specified begin date (must be at least one day before the specified end date), the format must be MM/DD/YY

##### end_date: `str`<a id="end_date-str"></a>

filters results to include transactions before the specified end date, the format must be MM/DD/YY

##### _return: `bool`<a id="_return-bool"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/orders?begin&#x3D;{begin_date}&amp;end&#x3D;{end_date}&amp;returns&#x3D;{return}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.orders.update_tags_and_attributes`<a id="fastspringordersupdate_tags_and_attributes"></a>

Update order tags and attributes

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_tags_and_attributes_response = fastspring.orders.update_tags_and_attributes(
    body=None,
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🔄 Return<a id="🔄-return"></a>

[`OrdersUpdateTagsAndAttributesResponse`](./fast_spring_python_sdk/pydantic/orders_update_tags_and_attributes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/orders` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.products.create_and_update`<a id="fastspringproductscreate_and_update"></a>

Create and update products

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_and_update_response = fastspring.products.create_and_update(
    products=[
        {
            "description": {
                "summary": {
                    "en": "String",
                },
                "action": {
                    "en": "String",
                },
                "full": {
                    "en": "String",
                },
            },
            "product": "{product_path}",
            "display": {
                "en": "String",
            },
            "fulfillment": {
                "instructions": {
                    "en": "String",
                    "es": "String",
                },
            },
            "image": "https://d8y8nchqlnmka.cloudfront.net/NVaGM-nhSpQ/-FooqIP-R84/photio-imac-hero.png",
            "format": "digital",
            "sku": "string",
            "attributes": {
                "key1": "value1",
                "key2": "value2",
            },
            "pricing": {
                "trial": 2,
                "interval": "month",
                "interval_length": 1,
                "quantity_behavior": "allow",
                "quantity_default": 1,
                "price": {
                    "usd": 14.95,
                    "eur": 10.99,
                },
                "quantity_discounts": {
                    "key": 3.14,
                },
                "discount_reason": {
                    "en": "The Reason",
                },
                "discount_duration": 1,
            },
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### products: List[`Product`]<a id="products-listproduct"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateoneormorenewproductsRequest`](./fast_spring_python_sdk/type/createoneormorenewproducts_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ProductsCreateAndUpdateResponse`](./fast_spring_python_sdk/pydantic/products_create_and_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.products.create_or_update_offers`<a id="fastspringproductscreate_or_update_offers"></a>

Create or Update Product offers

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_or_update_offers_response = fastspring.products.create_or_update_offers(
    body=None,
    product_path="product_path_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### product_path: `str`<a id="product_path-str"></a>

Product path

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🔄 Return<a id="🔄-return"></a>

[`ProductsCreateOrUpdateOffersResponse`](./fast_spring_python_sdk/pydantic/products_create_or_update_offers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products/offers/{product_path}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.products.delete_product_by_id`<a id="fastspringproductsdelete_product_by_id"></a>

Delete products

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_product_by_id_response = fastspring.products.delete_product_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Product Id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.products.get_all_offers_by_type`<a id="fastspringproductsget_all_offers_by_type"></a>

Get all offers for a product by offer type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_offers_by_type_response = fastspring.products.get_all_offers_by_type(
    product_path="product_path_example",
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### product_path: `str`<a id="product_path-str"></a>

Product path

##### type: `str`<a id="type-str"></a>

Offer Type

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products/offers/{product_path}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.products.get_all_product_ids`<a id="fastspringproductsget_all_product_ids"></a>

Get all product IDs

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_product_ids_response = fastspring.products.get_all_product_ids()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.products.get_all_product_prices`<a id="fastspringproductsget_all_product_prices"></a>

Get all product prices

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_product_prices_response = fastspring.products.get_all_product_prices()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products/price` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.products.get_all_product_prices_by_country`<a id="fastspringproductsget_all_product_prices_by_country"></a>

Get all product prices in specified country

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_product_prices_by_country_response = (
    fastspring.products.get_all_product_prices_by_country(
        country="country_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

Country code

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products/price?country&#x3D;{country}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.products.get_all_product_prices_by_country_and_currency`<a id="fastspringproductsget_all_product_prices_by_country_and_currency"></a>

Get all product prices in specified country and currency

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_product_prices_by_country_and_currency_response = (
    fastspring.products.get_all_product_prices_by_country_and_currency(
        country="country_example",
        currency="currency_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

Country code

##### currency: `str`<a id="currency-str"></a>

Currency code

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products/price?country&#x3D;{country}&amp;currency&#x3D;{currency}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.products.get_by_product_path`<a id="fastspringproductsget_by_product_path"></a>

Get products by path

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_product_path_response = fastspring.products.get_by_product_path(
    product_path="product_path_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### product_path: `str`<a id="product_path-str"></a>

Product path

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products/{product_path}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.products.get_price_by_id`<a id="fastspringproductsget_price_by_id"></a>

Get a product price

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_price_by_id_response = fastspring.products.get_price_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Product Id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products/price/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.products.get_product_price_by_country`<a id="fastspringproductsget_product_price_by_country"></a>

Get a product price in a specified country

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_product_price_by_country_response = (
    fastspring.products.get_product_price_by_country(
        id="id_example",
        country="country_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Product Id

##### country: `str`<a id="country-str"></a>

country code

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products/price/{id}?country&#x3D;{country}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.products.get_product_price_by_country_and_currency`<a id="fastspringproductsget_product_price_by_country_and_currency"></a>

Get a product price in a specified country and currency

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_product_price_by_country_and_currency_response = (
    fastspring.products.get_product_price_by_country_and_currency(
        id="id_example",
        country="country_example",
        currency="currency_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Product Id

##### country: `str`<a id="country-str"></a>

Country code

##### currency: `str`<a id="currency-str"></a>

currency code

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products/price/{id}?country&#x3D;{country}&amp;currency&#x3D;{currency}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.quotes.cancel_quote_by_id`<a id="fastspringquotescancel_quote_by_id"></a>

Cancel a quote

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
cancel_quote_by_id_response = fastspring.quotes.cancel_quote_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

A unique identifier for the quote

#### 🔄 Return<a id="🔄-return"></a>

[`QuoteResponse`](./fast_spring_python_sdk/pydantic/quote_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes/{id}/cancel` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.quotes.create_new_quote`<a id="fastspringquotescreate_new_quote"></a>

Create a quote

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_quote_response = fastspring.quotes.create_new_quote(
    items=[
        {
            "product": "product_example",
        }
    ],
    name="Quote for ABC Company",
    recipient_address={
        "address_line1": "801 Garden St",
        "address_line2": "Suite 201",
        "city": "Santa Barbara",
        "country": "US",
        "postal_code": "93101",
        "region": "California",
    },
    recipient={
        "company": "ABC Company",
        "email": "ne1@all.com",
        "first": "Leeroy",
        "last": "Jenkins",
        "phone": "+1254789654",
    },
    tags=[
        {
            "key": "tag-key",
            "value": "Tag Value",
        }
    ],
    coupon="TENOFF",
    currency="USD",
    expiration_date_days=30,
    fulfillment_term="string_example",
    notes="This is a Note",
    net_terms_days=1,
    tax_id="BE09999999XX",
    source="MANAGER",
    source_ip="181.55.25.101",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### items: List[`ItemRequest`]<a id="items-listitemrequest"></a>

##### name: `str`<a id="name-str"></a>

##### recipient_address: [`AddressRequest`](./fast_spring_python_sdk/type/address_request.py)<a id="recipient_address-addressrequestfast_spring_python_sdktypeaddress_requestpy"></a>


##### recipient: [`ContactRequest`](./fast_spring_python_sdk/type/contact_request.py)<a id="recipient-contactrequestfast_spring_python_sdktypecontact_requestpy"></a>


##### tags: List[`TagRequest`]<a id="tags-listtagrequest"></a>

##### coupon: `str`<a id="coupon-str"></a>

##### currency: `str`<a id="currency-str"></a>

##### expiration_date_days: `int`<a id="expiration_date_days-int"></a>

##### fulfillment_term: `str`<a id="fulfillment_term-str"></a>

##### notes: `str`<a id="notes-str"></a>

##### net_terms_days: `int`<a id="net_terms_days-int"></a>

##### tax_id: `str`<a id="tax_id-str"></a>

##### source: `str`<a id="source-str"></a>

##### source_ip: `str`<a id="source_ip-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateQuoteRequest`](./fast_spring_python_sdk/type/create_quote_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`QuoteResponse`](./fast_spring_python_sdk/pydantic/quote_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.quotes.delete_quote_by_id`<a id="fastspringquotesdelete_quote_by_id"></a>

Delete a quote

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_quote_by_id_response = fastspring.quotes.delete_quote_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

A unique identifier for the quote

#### 🔄 Return<a id="🔄-return"></a>

[`QuoteResponse`](./fast_spring_python_sdk/pydantic/quote_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.quotes.get_all_quotes`<a id="fastspringquotesget_all_quotes"></a>

Get all quotes

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_quotes_response = fastspring.quotes.get_all_quotes(
    created_begin="1970-01-01T00:00:00.00Z",
    created_end="1970-01-01T00:00:00.00Z",
    created_email="string_example",
    expires_begin="1970-01-01T00:00:00.00Z",
    expires_end="1970-01-01T00:00:00.00Z",
    search_param="string_example",
    expired_before="1970-01-01T00:00:00.00Z",
    only_quote_id=True,
    statuses=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### created_begin: `datetime`<a id="created_begin-datetime"></a>

The format must be YYYY-MM-DD

##### created_end: `datetime`<a id="created_end-datetime"></a>

The format must be YYYY-MM-DD

##### created_email: `str`<a id="created_email-str"></a>

##### expires_begin: `datetime`<a id="expires_begin-datetime"></a>

The format must be YYYY-MM-DD

##### expires_end: `datetime`<a id="expires_end-datetime"></a>

The format must be YYYY-MM-DD

##### search_param: `str`<a id="search_param-str"></a>

##### expired_before: `datetime`<a id="expired_before-datetime"></a>

The format must be YYYY-MM-DD

##### only_quote_id: `bool`<a id="only_quote_id-bool"></a>

##### statuses: List[`str`]<a id="statuses-liststr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`CollectionModelQuoteResponse`](./fast_spring_python_sdk/pydantic/collection_model_quote_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.quotes.get_by_id`<a id="fastspringquotesget_by_id"></a>

Get a quote

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = fastspring.quotes.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`QuoteResponse`](./fast_spring_python_sdk/pydantic/quote_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.quotes.update_quote_by_id`<a id="fastspringquotesupdate_quote_by_id"></a>

Update a quote

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_quote_by_id_response = fastspring.quotes.update_quote_by_id(
    id="id_example",
    update_quote_request={
        "coupon": "TENOFF",
        "currency": "USD",
        "expiration_date_days": 30,
        "fulfillment_term": "fulfillment_term_example",
        "items": [
            {
                "product": "product_example",
            }
        ],
        "name": "Quote for ABC Company",
        "notes": "This is a Note",
        "recipient_address": {
            "address_line1": "801 Garden St",
            "address_line2": "Suite 201",
            "city": "Santa Barbara",
            "country": "US",
            "postal_code": "93101",
            "region": "California",
        },
        "recipient": {
            "company": "ABC Company",
            "email": "ne1@all.com",
            "first": "Leeroy",
            "last": "Jenkins",
            "phone": "+1254789654",
        },
        "status": "OPEN",
        "tax_id": "BE09999999XX",
        "source": "MANAGER",
        "source_ip": "181.55.25.101",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

A unique identifier for the quote

##### update_quote_request: [`UpdateQuoteRequest`](./fast_spring_python_sdk/type/update_quote_request.py)<a id="update_quote_request-updatequoterequestfast_spring_python_sdktypeupdate_quote_requestpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`QuotesUpdateQuoteByIdRequest`](./fast_spring_python_sdk/type/quotes_update_quote_by_id_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`QuoteResponse`](./fast_spring_python_sdk/pydantic/quote_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/quotes/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.returns.create_new_return`<a id="fastspringreturnscreate_new_return"></a>

Create returns

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_return_response = fastspring.returns.create_new_return(
    body=None,
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/returns` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.returns.get_by_id`<a id="fastspringreturnsget_by_id"></a>

Get returns

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = fastspring.returns.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/returns/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.sessions.create_new_session`<a id="fastspringsessionscreate_new_session"></a>

Create a session

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_session_response = fastspring.sessions.create_new_session(
    account="uKj7izONRfanVwBL9eiG_A",
    items=[
        {
            "product": "{product_path}",
            "quantity": 1,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account: `str`<a id="account-str"></a>

##### items: List[`Item2`]<a id="items-listitem2"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateasessionwithoutoverridinganydefaultvaluesRequest`](./fast_spring_python_sdk/type/createasessionwithoutoverridinganydefaultvalues_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sessions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.subscriptions.cancel_subscription_by_id`<a id="fastspringsubscriptionscancel_subscription_by_id"></a>

Cancel a subscription

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
cancel_subscription_by_id_response = fastspring.subscriptions.cancel_subscription_by_id(
    subscription_id="subscription_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscription_id: `str`<a id="subscription_id-str"></a>

Subscription Id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/subscriptions/{subscription_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.subscriptions.convert_expired_trial_without_payment_method`<a id="fastspringsubscriptionsconvert_expired_trial_without_payment_method"></a>

Convert an Expired Trial Subscription without a Payment Method

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
convert_expired_trial_without_payment_method_response = (
    fastspring.subscriptions.convert_expired_trial_without_payment_method(
        subscription_id="subscription_id_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscription_id: `str`<a id="subscription_id-str"></a>

Subscription Id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/subscriptions/{subscription_id}/convert` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.subscriptions.get_all_subscriptions`<a id="fastspringsubscriptionsget_all_subscriptions"></a>

Get all subscriptions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_subscriptions_response = fastspring.subscriptions.get_all_subscriptions()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/subscriptions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.subscriptions.get_by_id`<a id="fastspringsubscriptionsget_by_id"></a>

Get a subscription

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = fastspring.subscriptions.get_by_id(
    subscription_id="subscription_id_example",
    account_id="string_example",
    begin="string_example",
    end="string_example",
    event="string_example",
    products="string_example",
    scope="string_example",
    status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscription_id: `str`<a id="subscription_id-str"></a>

Subscription Id

##### account_id: `str`<a id="account_id-str"></a>

specify a specific customer account whose subscriptions you want to retrieve

##### begin: `str`<a id="begin-str"></a>

specify the beginning of a date range in yyyy-mm-dd-format

##### end: `str`<a id="end-str"></a>

specify the end of a date range in yyyy-mm-dd format

##### event: `str`<a id="event-str"></a>

In each event, use begin and end to retrieve the corresponding subscriptions

##### products: `str`<a id="products-str"></a>

enter one or more product ids to filter the response to include only subscriptions for the specified products; use commas to separate multiple values

##### scope: `str`<a id="scope-str"></a>

##### status: `str`<a id="status-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/subscriptions/{subscription_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.subscriptions.get_entries`<a id="fastspringsubscriptionsget_entries"></a>

Get subscription entries

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
fastspring.subscriptions.get_entries(
    subscription_id="subscription_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscription_id: `str`<a id="subscription_id-str"></a>

Subscription Id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/subscriptions/{subscription_id}/entries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.subscriptions.get_plan_change_history`<a id="fastspringsubscriptionsget_plan_change_history"></a>

Get subscription plan change history

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
fastspring.subscriptions.get_plan_change_history(
    subscription_id="subscription_id_example",
    scope="base_plan",
    order="increasing",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscription_id: `str`<a id="subscription_id-str"></a>

Subscription Id

##### scope: `str`<a id="scope-str"></a>

Type of items to return

##### order: `str`<a id="order-str"></a>

Sort Order for the results

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/subscriptions/{subscription_id}/history` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.subscriptions.pause_subscription`<a id="fastspringsubscriptionspause_subscription"></a>

Pause a subscription

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
pause_subscription_response = fastspring.subscriptions.pause_subscription(
    body=None,
    subscription_id="subscription_id_example",
    pause_period_count=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscription_id: `str`<a id="subscription_id-str"></a>

Subscription Id

##### pause_period_count: `int`<a id="pause_period_count-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PauseSubscriptionRequest`](./fast_spring_python_sdk/type/pause_subscription_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/subscriptions/{subscription_id}/pause` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.subscriptions.preview_plan_change`<a id="fastspringsubscriptionspreview_plan_change"></a>

Preview a proposed prorated plan change

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
preview_plan_change_response = fastspring.subscriptions.preview_plan_change(
    subscription="string_example",
    product="string_example",
    quantity=1,
    pricing={
        "usd": 14.95,
        "eur": 10.99,
    },
    addons=[{}],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscription: `str`<a id="subscription-str"></a>

##### product: `str`<a id="product-str"></a>

##### quantity: `int`<a id="quantity-int"></a>

##### pricing: `Price`<a id="pricing-price"></a>

##### addons: List[`SubscriptionAddon`]<a id="addons-listsubscriptionaddon"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EstimateSubscriptionRequest`](./fast_spring_python_sdk/type/estimate_subscription_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/subscriptions/estimate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.subscriptions.rebill_managed_subscription`<a id="fastspringsubscriptionsrebill_managed_subscription"></a>

Rebill a managed subscription

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rebill_managed_subscription_response = (
    fastspring.subscriptions.rebill_managed_subscription(
        body=None,
    )
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Union[bool, date, datetime, dict, float, int, list, str, None]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/subscriptions/charge` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.subscriptions.remove_scheduled_pause`<a id="fastspringsubscriptionsremove_scheduled_pause"></a>

Remove a scheduled pause

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_scheduled_pause_response = fastspring.subscriptions.remove_scheduled_pause(
    subscription_id="subscription_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscription_id: `str`<a id="subscription_id-str"></a>

Subscription Id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/subscriptions/{subscription_id}/resume` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.subscriptions.resume_subscription`<a id="fastspringsubscriptionsresume_subscription"></a>

Resume a canceled subscription

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
fastspring.subscriptions.resume_subscription(
    subscriptions=[
        {
            "subscription": "{subscription_id}",
            "deactivation": "deactivation_example",
        }
    ],
    subscription_id="subscription_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscriptions: List[`Subscription6`]<a id="subscriptions-listsubscription6"></a>

##### subscription_id: `str`<a id="subscription_id-str"></a>

Subscription Id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UncancelasubscriptionpriortodeactivationRequest`](./fast_spring_python_sdk/type/uncancelasubscriptionpriortodeactivation_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/subscriptions/{subscription_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.subscriptions.update_subscription`<a id="fastspringsubscriptionsupdate_subscription"></a>

Update a subscription

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_subscription_response = fastspring.subscriptions.update_subscription(
    subscriptions=[
        {
            "subscription": "{subscription_id}",
            "product": "{subscription_product_path}",
            "quantity": 1,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subscriptions: List[`Subscription`]<a id="subscriptions-listsubscription"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChangetheproductforanactivesubscriptionRequest`](./fast_spring_python_sdk/type/changetheproductforanactivesubscription_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/subscriptions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `fastspring.webhooks.update_webhook_key_secret`<a id="fastspringwebhooksupdate_webhook_key_secret"></a>

Update a webhook key secret

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_webhook_key_secret_response = fastspring.webhooks.update_webhook_key_secret(
    url="string_example",
    hmac_secret="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

The URL associated with the webhook.

##### hmac_secret: `str`<a id="hmac_secret-str"></a>

The new HMAC Secret key.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksUpdateWebhookKeySecretRequest`](./fast_spring_python_sdk/type/webhooks_update_webhook_key_secret_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebhooksUpdateWebhookKeySecretResponse`](./fast_spring_python_sdk/pydantic/webhooks_update_webhook_key_secret_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/keys` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
