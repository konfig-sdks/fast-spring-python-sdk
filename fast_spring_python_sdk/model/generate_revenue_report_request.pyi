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


class GenerateRevenueReportRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def filter() -> typing.Type['FilterRevenueReportRequest']:
                return FilterRevenueReportRequest
        
            @staticmethod
            def reportColumns() -> typing.Type['GenerateRevenueReportRequestReportColumns']:
                return GenerateRevenueReportRequestReportColumns
        
            @staticmethod
            def groupBy() -> typing.Type['GenerateRevenueReportRequestGroupBy']:
                return GenerateRevenueReportRequestGroupBy
            
            
            class pageCount(
                schemas.Int32Schema
            ):
                pass
            
            
            class pageNumber(
                schemas.Int32Schema
            ):
                pass
            _async = schemas.BoolSchema
        
            @staticmethod
            def notificationEmails() -> typing.Type['GenerateRevenueReportRequestNotificationEmails']:
                return GenerateRevenueReportRequestNotificationEmails
            __annotations__ = {
                "filter": filter,
                "reportColumns": reportColumns,
                "groupBy": groupBy,
                "pageCount": pageCount,
                "pageNumber": pageNumber,
                "async": _async,
                "notificationEmails": notificationEmails,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filter"]) -> 'FilterRevenueReportRequest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reportColumns"]) -> 'GenerateRevenueReportRequestReportColumns': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupBy"]) -> 'GenerateRevenueReportRequestGroupBy': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageCount"]) -> MetaOapg.properties.pageCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageNumber"]) -> MetaOapg.properties.pageNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["async"]) -> MetaOapg.properties._async: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notificationEmails"]) -> 'GenerateRevenueReportRequestNotificationEmails': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["filter", "reportColumns", "groupBy", "pageCount", "pageNumber", "async", "notificationEmails", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filter"]) -> typing.Union['FilterRevenueReportRequest', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reportColumns"]) -> typing.Union['GenerateRevenueReportRequestReportColumns', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupBy"]) -> typing.Union['GenerateRevenueReportRequestGroupBy', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageCount"]) -> typing.Union[MetaOapg.properties.pageCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageNumber"]) -> typing.Union[MetaOapg.properties.pageNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["async"]) -> typing.Union[MetaOapg.properties._async, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notificationEmails"]) -> typing.Union['GenerateRevenueReportRequestNotificationEmails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["filter", "reportColumns", "groupBy", "pageCount", "pageNumber", "async", "notificationEmails", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        filter: typing.Union['FilterRevenueReportRequest', schemas.Unset] = schemas.unset,
        reportColumns: typing.Union['GenerateRevenueReportRequestReportColumns', schemas.Unset] = schemas.unset,
        groupBy: typing.Union['GenerateRevenueReportRequestGroupBy', schemas.Unset] = schemas.unset,
        pageCount: typing.Union[MetaOapg.properties.pageCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pageNumber: typing.Union[MetaOapg.properties.pageNumber, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        notificationEmails: typing.Union['GenerateRevenueReportRequestNotificationEmails', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GenerateRevenueReportRequest':
        return super().__new__(
            cls,
            *args,
            filter=filter,
            reportColumns=reportColumns,
            groupBy=groupBy,
            pageCount=pageCount,
            pageNumber=pageNumber,
            notificationEmails=notificationEmails,
            _configuration=_configuration,
            **kwargs,
        )

from fast_spring_python_sdk.model.filter_revenue_report_request import FilterRevenueReportRequest
from fast_spring_python_sdk.model.generate_revenue_report_request_group_by import GenerateRevenueReportRequestGroupBy
from fast_spring_python_sdk.model.generate_revenue_report_request_notification_emails import GenerateRevenueReportRequestNotificationEmails
from fast_spring_python_sdk.model.generate_revenue_report_request_report_columns import GenerateRevenueReportRequestReportColumns
