operation_parameter_map = {
    '/accounts-POST': {
        'parameters': [
            {
                'name': 'contact'
            },
        ]
    },
    '/accounts/{account_id}-GET': {
        'parameters': [
            {
                'name': 'account_id'
            },
        ]
    },
    '/accounts/{account_id}/authenticate-GET': {
        'parameters': [
            {
                'name': 'account_id'
            },
        ]
    },
    '/accounts-GET': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'custom'
            },
            {
                'name': 'global'
            },
            {
                'name': 'orderID'
            },
            {
                'name': 'orderReference'
            },
            {
                'name': 'subscriptionId'
            },
            {
                'name': 'products'
            },
            {
                'name': 'subscriptions'
            },
            {
                'name': 'refunds'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/accounts/{account_id}-POST': {
        'parameters': [
            {
                'name': 'account_id'
            },
            {
                'name': 'contact'
            },
        ]
    },
    '/coupons/{coupon_id}-POST': {
        'parameters': [
            {
                'name': 'codes'
            },
            {
                'name': 'coupon_id'
            },
        ]
    },
    '/coupons-POST': {
        'parameters': [
        ]
    },
    '/coupons/{coupon_id}/codes-DELETE': {
        'parameters': [
            {
                'name': 'coupon_id'
            },
        ]
    },
    '/coupons/{coupon_id}/codes-GET': {
        'parameters': [
            {
                'name': 'coupon_id'
            },
        ]
    },
    '/coupons/{coupon_id}-GET': {
        'parameters': [
            {
                'name': 'coupon_id'
            },
        ]
    },
    '/data/v1/downloads/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/data/v1/revenue-POST': {
        'parameters': [
            {
                'name': 'filter'
            },
            {
                'name': 'reportColumns'
            },
            {
                'name': 'groupBy'
            },
            {
                'name': 'pageCount'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'async'
            },
            {
                'name': 'notificationEmails'
            },
        ]
    },
    '/data/v1/subscription-POST': {
        'parameters': [
            {
                'name': 'filter'
            },
            {
                'name': 'reportColumns'
            },
            {
                'name': 'groupBy'
            },
            {
                'name': 'pageCount'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'async'
            },
            {
                'name': 'notificationEmails'
            },
        ]
    },
    '/data/v1/jobs/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/data/v1/jobs-GET': {
        'parameters': [
        ]
    },
    '/data/v1/util/cache-GET': {
        'parameters': [
        ]
    },
    '/events/processed-GET': {
        'parameters': [
            {
                'name': 'days'
            },
        ]
    },
    '/events/unprocessed-GET': {
        'parameters': [
            {
                'name': 'begin'
            },
        ]
    },
    '/events/{event_id}-POST': {
        'parameters': [
            {
                'name': 'processed'
            },
            {
                'name': 'event_id'
            },
        ]
    },
    '/orders?begin={begin_date}&end={end_date}&limit={limit}&page={page}-GET': {
        'parameters': [
            {
                'name': 'begin_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/orders?end={end_date}-GET': {
        'parameters': [
            {
                'name': 'end_date'
            },
        ]
    },
    '/orders/{order_id}-GET': {
        'parameters': [
            {
                'name': 'order_id'
            },
        ]
    },
    '/orders?products={product_path}&limit={limit}&page={page}-GET': {
        'parameters': [
            {
                'name': 'product_path'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/orders?products={product_path}&begin={begin_date}&end={end_date}-GET': {
        'parameters': [
            {
                'name': 'product_path'
            },
            {
                'name': 'begin_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/orders?begin={begin_date}&end={end_date}&returns={return}-GET': {
        'parameters': [
            {
                'name': 'begin_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'return'
            },
        ]
    },
    '/orders-POST': {
        'parameters': [
        ]
    },
    '/products-POST': {
        'parameters': [
            {
                'name': 'products'
            },
        ]
    },
    '/products/offers/{product_path}-POST': {
        'parameters': [
            {
                'name': 'product_path'
            },
        ]
    },
    '/products/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/products/offers/{product_path}-GET': {
        'parameters': [
            {
                'name': 'product_path'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/products-GET': {
        'parameters': [
        ]
    },
    '/products/price-GET': {
        'parameters': [
        ]
    },
    '/products/price?country={country}-GET': {
        'parameters': [
            {
                'name': 'country'
            },
        ]
    },
    '/products/price?country={country}&currency={currency}-GET': {
        'parameters': [
            {
                'name': 'country'
            },
            {
                'name': 'currency'
            },
        ]
    },
    '/products/{product_path}-GET': {
        'parameters': [
            {
                'name': 'product_path'
            },
        ]
    },
    '/products/price/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/products/price/{id}?country={country}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'country'
            },
        ]
    },
    '/products/price/{id}?country={country}&currency={currency}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'country'
            },
            {
                'name': 'currency'
            },
        ]
    },
    '/quotes/{id}/cancel-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/quotes-POST': {
        'parameters': [
            {
                'name': 'items'
            },
            {
                'name': 'name'
            },
            {
                'name': 'recipientAddress'
            },
            {
                'name': 'recipient'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'coupon'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'expirationDateDays'
            },
            {
                'name': 'fulfillmentTerm'
            },
            {
                'name': 'notes'
            },
            {
                'name': 'netTermsDays'
            },
            {
                'name': 'taxId'
            },
            {
                'name': 'source'
            },
            {
                'name': 'sourceIP'
            },
        ]
    },
    '/quotes/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/quotes-GET': {
        'parameters': [
            {
                'name': 'createdBegin'
            },
            {
                'name': 'createdEnd'
            },
            {
                'name': 'createdEmail'
            },
            {
                'name': 'expiresBegin'
            },
            {
                'name': 'expiresEnd'
            },
            {
                'name': 'searchParam'
            },
            {
                'name': 'expiredBefore'
            },
            {
                'name': 'onlyQuoteId'
            },
            {
                'name': 'statuses'
            },
        ]
    },
    '/quotes/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/quotes/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'updateQuoteRequest'
            },
        ]
    },
    '/returns-POST': {
        'parameters': [
        ]
    },
    '/returns/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/sessions-POST': {
        'parameters': [
            {
                'name': 'account'
            },
            {
                'name': 'items'
            },
        ]
    },
    '/subscriptions/{subscription_id}-DELETE': {
        'parameters': [
            {
                'name': 'subscription_id'
            },
        ]
    },
    '/subscriptions/{subscription_id}/convert-POST': {
        'parameters': [
            {
                'name': 'subscription_id'
            },
        ]
    },
    '/subscriptions-GET': {
        'parameters': [
        ]
    },
    '/subscriptions/{subscription_id}-GET': {
        'parameters': [
            {
                'name': 'subscription_id'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'begin'
            },
            {
                'name': 'end'
            },
            {
                'name': 'event'
            },
            {
                'name': 'products'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/subscriptions/{subscription_id}/entries-GET': {
        'parameters': [
            {
                'name': 'subscription_id'
            },
        ]
    },
    '/subscriptions/{subscription_id}/history-GET': {
        'parameters': [
            {
                'name': 'subscription_id'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'order'
            },
        ]
    },
    '/subscriptions/{subscription_id}/pause-POST': {
        'parameters': [
            {
                'name': 'subscription_id'
            },
            {
                'name': 'pausePeriodCount'
            },
        ]
    },
    '/subscriptions/estimate-POST': {
        'parameters': [
            {
                'name': 'subscription'
            },
            {
                'name': 'product'
            },
            {
                'name': 'quantity'
            },
            {
                'name': 'pricing'
            },
            {
                'name': 'addons'
            },
        ]
    },
    '/subscriptions/charge-POST': {
        'parameters': [
        ]
    },
    '/subscriptions/{subscription_id}/resume-POST': {
        'parameters': [
            {
                'name': 'subscription_id'
            },
        ]
    },
    '/subscriptions/{subscription_id}-POST': {
        'parameters': [
            {
                'name': 'subscriptions'
            },
            {
                'name': 'subscription_id'
            },
        ]
    },
    '/subscriptions-POST': {
        'parameters': [
            {
                'name': 'subscriptions'
            },
        ]
    },
    '/webhooks/keys-POST': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'hmacSecret'
            },
        ]
    },
};