import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    SecureGiveEventStickerItem,
    SecureLevel,
    SecureSmsNotification,
    SecureTokenChecked,
    SecureTransaction,
)


class CheckTokenResponse(BaseResponse):
    response: SecureTokenChecked


class GetAppBalanceResponse(BaseResponse):
    response: int


class GetSMSHistoryResponse(BaseResponse):
    response: typing.List["SecureSmsNotification"]


class GetTransactionsHistoryResponse(BaseResponse):
    response: typing.List["SecureTransaction"]


class GetUserLevelResponse(BaseResponse):
    response: typing.List["SecureLevel"]


class GiveEventStickerResponse(BaseResponse):
    response: typing.List["SecureGiveEventStickerItem"]


class SendNotificationResponse(BaseResponse):
    response: typing.List[int]


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
