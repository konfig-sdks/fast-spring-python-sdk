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


class UserPrincipal(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            email = schemas.StrSchema
            siteId = schemas.StrSchema
        
            @staticmethod
            def siteIds() -> typing.Type['UserPrincipalSiteIds']:
                return UserPrincipalSiteIds
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            companyName = schemas.StrSchema
            siteName = schemas.StrSchema
            loginToken = schemas.StrSchema
        
            @staticmethod
            def roles() -> typing.Type['UserPrincipalRoles']:
                return UserPrincipalRoles
            apiAccess = schemas.BoolSchema
            userId = schemas.StrSchema
            
            
            class entitlements(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Entitlement']:
                        return Entitlement
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Entitlement'], typing.List['Entitlement']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'entitlements':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Entitlement':
                    return super().__getitem__(i)
            clientCredentials = schemas.BoolSchema
            
            
            class authProviderType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def COGNITO(cls):
                    return cls("COGNITO")
                
                @schemas.classproperty
                def COMMERCE(cls):
                    return cls("COMMERCE")
                
                @schemas.classproperty
                def SOCIAL_GOOGLE(cls):
                    return cls("SOCIAL_GOOGLE")
            accessToken = schemas.StrSchema
            tokenExpires = schemas.Int64Schema
            __annotations__ = {
                "email": email,
                "siteId": siteId,
                "siteIds": siteIds,
                "firstName": firstName,
                "lastName": lastName,
                "companyName": companyName,
                "siteName": siteName,
                "loginToken": loginToken,
                "roles": roles,
                "apiAccess": apiAccess,
                "userId": userId,
                "entitlements": entitlements,
                "clientCredentials": clientCredentials,
                "authProviderType": authProviderType,
                "accessToken": accessToken,
                "tokenExpires": tokenExpires,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["siteId"]) -> MetaOapg.properties.siteId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["siteIds"]) -> 'UserPrincipalSiteIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyName"]) -> MetaOapg.properties.companyName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["siteName"]) -> MetaOapg.properties.siteName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loginToken"]) -> MetaOapg.properties.loginToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roles"]) -> 'UserPrincipalRoles': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiAccess"]) -> MetaOapg.properties.apiAccess: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entitlements"]) -> MetaOapg.properties.entitlements: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientCredentials"]) -> MetaOapg.properties.clientCredentials: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authProviderType"]) -> MetaOapg.properties.authProviderType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accessToken"]) -> MetaOapg.properties.accessToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tokenExpires"]) -> MetaOapg.properties.tokenExpires: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["email", "siteId", "siteIds", "firstName", "lastName", "companyName", "siteName", "loginToken", "roles", "apiAccess", "userId", "entitlements", "clientCredentials", "authProviderType", "accessToken", "tokenExpires", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["siteId"]) -> typing.Union[MetaOapg.properties.siteId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["siteIds"]) -> typing.Union['UserPrincipalSiteIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> typing.Union[MetaOapg.properties.firstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyName"]) -> typing.Union[MetaOapg.properties.companyName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["siteName"]) -> typing.Union[MetaOapg.properties.siteName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loginToken"]) -> typing.Union[MetaOapg.properties.loginToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roles"]) -> typing.Union['UserPrincipalRoles', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiAccess"]) -> typing.Union[MetaOapg.properties.apiAccess, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> typing.Union[MetaOapg.properties.userId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entitlements"]) -> typing.Union[MetaOapg.properties.entitlements, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientCredentials"]) -> typing.Union[MetaOapg.properties.clientCredentials, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authProviderType"]) -> typing.Union[MetaOapg.properties.authProviderType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accessToken"]) -> typing.Union[MetaOapg.properties.accessToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tokenExpires"]) -> typing.Union[MetaOapg.properties.tokenExpires, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email", "siteId", "siteIds", "firstName", "lastName", "companyName", "siteName", "loginToken", "roles", "apiAccess", "userId", "entitlements", "clientCredentials", "authProviderType", "accessToken", "tokenExpires", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        siteId: typing.Union[MetaOapg.properties.siteId, str, schemas.Unset] = schemas.unset,
        siteIds: typing.Union['UserPrincipalSiteIds', schemas.Unset] = schemas.unset,
        firstName: typing.Union[MetaOapg.properties.firstName, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        companyName: typing.Union[MetaOapg.properties.companyName, str, schemas.Unset] = schemas.unset,
        siteName: typing.Union[MetaOapg.properties.siteName, str, schemas.Unset] = schemas.unset,
        loginToken: typing.Union[MetaOapg.properties.loginToken, str, schemas.Unset] = schemas.unset,
        roles: typing.Union['UserPrincipalRoles', schemas.Unset] = schemas.unset,
        apiAccess: typing.Union[MetaOapg.properties.apiAccess, bool, schemas.Unset] = schemas.unset,
        userId: typing.Union[MetaOapg.properties.userId, str, schemas.Unset] = schemas.unset,
        entitlements: typing.Union[MetaOapg.properties.entitlements, list, tuple, schemas.Unset] = schemas.unset,
        clientCredentials: typing.Union[MetaOapg.properties.clientCredentials, bool, schemas.Unset] = schemas.unset,
        authProviderType: typing.Union[MetaOapg.properties.authProviderType, str, schemas.Unset] = schemas.unset,
        accessToken: typing.Union[MetaOapg.properties.accessToken, str, schemas.Unset] = schemas.unset,
        tokenExpires: typing.Union[MetaOapg.properties.tokenExpires, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserPrincipal':
        return super().__new__(
            cls,
            *args,
            email=email,
            siteId=siteId,
            siteIds=siteIds,
            firstName=firstName,
            lastName=lastName,
            companyName=companyName,
            siteName=siteName,
            loginToken=loginToken,
            roles=roles,
            apiAccess=apiAccess,
            userId=userId,
            entitlements=entitlements,
            clientCredentials=clientCredentials,
            authProviderType=authProviderType,
            accessToken=accessToken,
            tokenExpires=tokenExpires,
            _configuration=_configuration,
            **kwargs,
        )

from fast_spring_python_sdk.model.entitlement import Entitlement
from fast_spring_python_sdk.model.user_principal_roles import UserPrincipalRoles
from fast_spring_python_sdk.model.user_principal_site_ids import UserPrincipalSiteIds
