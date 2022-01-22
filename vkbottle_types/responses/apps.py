import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    AppsApp,
    AppsCatalogList,
    AppsLeaderboard,
    AppsScope,
    UsersUserFull,
    UsersUserMin,
)


class GetCatalogResponse(BaseResponse):
    response: AppsCatalogList


class GetFriendsListResponse(BaseResponse):
    response: "GetFriendsListResponseModel"


class GetLeaderboardExtendedResponse(BaseResponse):
    response: "GetLeaderboardExtendedResponseModel"


class GetLeaderboardResponse(BaseResponse):
    response: "GetLeaderboardResponseModel"


class GetMiniAppPoliciesResponse(BaseResponse):
    response: "GetMiniAppPoliciesResponseModel"


class GetScopesResponse(BaseResponse):
    response: "GetScopesResponseModel"


class GetScoreResponse(BaseResponse):
    response: int


class GetResponse(BaseResponse):
    response: "GetResponseModel"


class ImageUploadResponse(BaseResponse):
    response: "ImageUploadResponseModel"


class SendRequestResponse(BaseResponse):
    response: int


class GetFriendsListResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UsersUserFull"]] = None


class GetLeaderboardExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AppsLeaderboard"]] = None
    profiles: typing.Optional[typing.List["UsersUserMin"]] = None


class GetLeaderboardResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AppsLeaderboard"]] = None


class GetMiniAppPoliciesResponseModel(BaseResponse):
    privacy_policy: typing.Optional[str] = None
    terms: typing.Optional[str] = None


class GetScopesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AppsScope"]] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AppsApp"]] = None


class ImageUploadResponseModel(BaseResponse):
    hash: typing.Optional[str] = None
    image: typing.Optional[str] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
