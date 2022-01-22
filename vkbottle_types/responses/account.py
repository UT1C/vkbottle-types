import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    AccountAccountCounters,
    AccountInfo,
    AccountNameRequest,
    AccountOffer,
    AccountPushSettings,
    AccountUserSettings,
    BaseBoolInt,
    GroupsGroup,
    UsersUserFull,
)


class ChangePasswordResponse(BaseResponse):
    response: "ChangePasswordResponseModel"


class GetActiveOffersResponse(BaseResponse):
    response: "GetActiveOffersResponseModel"


class GetAppPermissionsResponse(BaseResponse):
    response: int


class GetBannedResponse(BaseResponse):
    response: "GetBannedResponseModel"


class GetCountersResponse(BaseResponse):
    response: AccountAccountCounters


class GetInfoResponse(BaseResponse):
    response: AccountInfo


class GetProfileInfoResponse(BaseResponse):
    response: AccountUserSettings


class GetPushSettingsResponse(BaseResponse):
    response: AccountPushSettings


class SaveProfileInfoResponse(BaseResponse):
    response: "SaveProfileInfoResponseModel"


class ChangePasswordResponseModel(BaseResponse):
    token: typing.Optional[str] = None
    secret: typing.Optional[str] = None


class GetActiveOffersResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AccountOffer"]] = None


class GetBannedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[int]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroup"]] = None


class SaveProfileInfoResponseModel(BaseResponse):
    changed: typing.Optional["BaseBoolInt"] = None
    name_request: typing.Optional["AccountNameRequest"] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
