# coding: utf-8

"""
    FastSpring API

    The FastSpring API and its supported requests, data, endpoints, and rate limits.  The FastSpring API is a backend service you can use to communicate with your FastSpring Store programmatically. It requires basic understanding of HTTP communication methods. The primary API communication methods include: - **GET** - request data from your store - **POST** - send data to your store, such as creating a new product record - **DELETE** - remove data from your store  The structure of the JSON data sent and received using the API is very similar to Webhooks. However, using the FastSpring API, you initiate all communication with your FastSpring Store.  If you prefer a client-side method of communicating with your FastSpring Store and generating dynamic webpage content, check out the [Store Builder Library](https://fastspring.com/docs/get-started-with-store-builder-library/).  ## Access the API  #### API Credentials and Authentication  FastSpring API credentials consist of a single username and password for your entire Store. The username and password are used for [Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) when making requests to the API.  #### Obtain Your API Credentials  1. Log on to the FastSpring App and navigate to [Integrations](https://fastspring.com/docs/integrations) > **API Credentials**. Initially, the only option on this page is the **Create** command.  2. Click **Create** to generate your API **Username** and **Password**. The page automatically refreshes, and then your credentials are displayed.  3. Make a note of the credentials and store them securely.  The API credentials allow complete access and control over your FastSpring Store. You will not be able to view the password in the FastSpring App after this session. If you forget your API credentials, you can reset them, however any of your stored procedures that rely on API access must be updated immediately with the new credentials. Otherwise, the API requests will fail.  ## API Requests  **Make all requests to https://api.fastspring.com**  When you make your requests, consider the following: - Ensure that the HTTP methods for all calls use uppercase letters (“GET,” “POST,” “DELETE”) Lowercase letters may result in a 404 error response. - FastSpring requires TLS 1.2 (or later) encryption for all calls to the FastSpring API.  - The API requires a **User-Agent** header in all requests. If your request does not include it, you may receive an 401 error message when attempting to make API requests. - The API uses basic authentication and does not support URL-encoded authentication. Use **Base64** to encode your username and password in the header. 

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from fast_spring_python_sdk import schemas  # noqa: F401


class UpdateQuoteRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "expirationDateDays",
            "name",
            "recipient",
            "currency",
            "recipientAddress",
            "items",
            "fulfillmentTerm",
        }
        
        class properties:
            
            
            class currency(
                schemas.StrSchema
            ):
                pass
            
            
            class expirationDateDays(
                schemas.Int32Schema
            ):
                pass
            fulfillmentTerm = schemas.StrSchema
            
            
            class items(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ItemRequest']:
                        return ItemRequest
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ItemRequest'], typing.List['ItemRequest']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'items':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ItemRequest':
                    return super().__getitem__(i)
            name = schemas.StrSchema
        
            @staticmethod
            def recipientAddress() -> typing.Type['AddressRequest']:
                return AddressRequest
        
            @staticmethod
            def recipient() -> typing.Type['ContactRequest']:
                return ContactRequest
            
            
            class tags(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TagRequest']:
                        return TagRequest
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TagRequest'], typing.List['TagRequest']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tags':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TagRequest':
                    return super().__getitem__(i)
            
            
            class coupon(
                schemas.StrSchema
            ):
                pass
            
            
            class notes(
                schemas.StrSchema
            ):
                pass
            netTermsDays = schemas.Int32Schema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def OPEN(cls):
                    return cls("OPEN")
                
                @schemas.classproperty
                def CANCELED(cls):
                    return cls("CANCELED")
                
                @schemas.classproperty
                def AWAITING_PAYMENT(cls):
                    return cls("AWAITING_PAYMENT")
                
                @schemas.classproperty
                def COMPLETED(cls):
                    return cls("COMPLETED")
                
                @schemas.classproperty
                def EXPIRED(cls):
                    return cls("EXPIRED")
            
            
            class taxId(
                schemas.StrSchema
            ):
                pass
            
            
            class source(
                schemas.StrSchema
            ):
                pass
            
            
            class sourceIP(
                schemas.StrSchema
            ):
                pass
            
            
            class invoiceId(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "currency": currency,
                "expirationDateDays": expirationDateDays,
                "fulfillmentTerm": fulfillmentTerm,
                "items": items,
                "name": name,
                "recipientAddress": recipientAddress,
                "recipient": recipient,
                "tags": tags,
                "coupon": coupon,
                "notes": notes,
                "netTermsDays": netTermsDays,
                "status": status,
                "taxId": taxId,
                "source": source,
                "sourceIP": sourceIP,
                "invoiceId": invoiceId,
            }
    
    expirationDateDays: MetaOapg.properties.expirationDateDays
    name: MetaOapg.properties.name
    recipient: 'ContactRequest'
    currency: MetaOapg.properties.currency
    recipientAddress: 'AddressRequest'
    items: MetaOapg.properties.items
    fulfillmentTerm: MetaOapg.properties.fulfillmentTerm
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expirationDateDays"]) -> MetaOapg.properties.expirationDateDays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fulfillmentTerm"]) -> MetaOapg.properties.fulfillmentTerm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items"]) -> MetaOapg.properties.items: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipientAddress"]) -> 'AddressRequest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipient"]) -> 'ContactRequest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> MetaOapg.properties.tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coupon"]) -> MetaOapg.properties.coupon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["netTermsDays"]) -> MetaOapg.properties.netTermsDays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxId"]) -> MetaOapg.properties.taxId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sourceIP"]) -> MetaOapg.properties.sourceIP: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invoiceId"]) -> MetaOapg.properties.invoiceId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["currency", "expirationDateDays", "fulfillmentTerm", "items", "name", "recipientAddress", "recipient", "tags", "coupon", "notes", "netTermsDays", "status", "taxId", "source", "sourceIP", "invoiceId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expirationDateDays"]) -> MetaOapg.properties.expirationDateDays: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fulfillmentTerm"]) -> MetaOapg.properties.fulfillmentTerm: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items"]) -> MetaOapg.properties.items: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipientAddress"]) -> 'AddressRequest': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipient"]) -> 'ContactRequest': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union[MetaOapg.properties.tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coupon"]) -> typing.Union[MetaOapg.properties.coupon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["netTermsDays"]) -> typing.Union[MetaOapg.properties.netTermsDays, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxId"]) -> typing.Union[MetaOapg.properties.taxId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sourceIP"]) -> typing.Union[MetaOapg.properties.sourceIP, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invoiceId"]) -> typing.Union[MetaOapg.properties.invoiceId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["currency", "expirationDateDays", "fulfillmentTerm", "items", "name", "recipientAddress", "recipient", "tags", "coupon", "notes", "netTermsDays", "status", "taxId", "source", "sourceIP", "invoiceId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        expirationDateDays: typing.Union[MetaOapg.properties.expirationDateDays, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        recipient: 'ContactRequest',
        currency: typing.Union[MetaOapg.properties.currency, str, ],
        recipientAddress: 'AddressRequest',
        items: typing.Union[MetaOapg.properties.items, list, tuple, ],
        fulfillmentTerm: typing.Union[MetaOapg.properties.fulfillmentTerm, str, ],
        tags: typing.Union[MetaOapg.properties.tags, list, tuple, schemas.Unset] = schemas.unset,
        coupon: typing.Union[MetaOapg.properties.coupon, str, schemas.Unset] = schemas.unset,
        notes: typing.Union[MetaOapg.properties.notes, str, schemas.Unset] = schemas.unset,
        netTermsDays: typing.Union[MetaOapg.properties.netTermsDays, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        taxId: typing.Union[MetaOapg.properties.taxId, str, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, str, schemas.Unset] = schemas.unset,
        sourceIP: typing.Union[MetaOapg.properties.sourceIP, str, schemas.Unset] = schemas.unset,
        invoiceId: typing.Union[MetaOapg.properties.invoiceId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateQuoteRequest':
        return super().__new__(
            cls,
            *args,
            expirationDateDays=expirationDateDays,
            name=name,
            recipient=recipient,
            currency=currency,
            recipientAddress=recipientAddress,
            items=items,
            fulfillmentTerm=fulfillmentTerm,
            tags=tags,
            coupon=coupon,
            notes=notes,
            netTermsDays=netTermsDays,
            status=status,
            taxId=taxId,
            source=source,
            sourceIP=sourceIP,
            invoiceId=invoiceId,
            _configuration=_configuration,
            **kwargs,
        )

from fast_spring_python_sdk.model.address_request import AddressRequest
from fast_spring_python_sdk.model.contact_request import ContactRequest
from fast_spring_python_sdk.model.item_request import ItemRequest
from fast_spring_python_sdk.model.tag_request import TagRequest
