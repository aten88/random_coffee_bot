from asgiref.sync import sync_to_async
from aiogram.types.user import User

from admin_panel.telegram.models import TgUser


@sync_to_async
def create_tg_user(user: User, email: str, enter_full_name: str):
    tg_user = TgUser.objects.create(
        id=user.id,
        email=email,
        enter_full_name=enter_full_name,
        username=user.username,
        full_name=user.full_name
    )
    return tg_user


@sync_to_async
def get_tg_user(user_id):
    return TgUser.objects.filter(id=user_id).first()


@sync_to_async
def search_tg_user(email: str):
    return TgUser.objects.filter(email=email).first()


@sync_to_async
def user_id_block_unblock(user_id):
    user_model = TgUser.objects.filter(id=user_id).first()
    if not user_model.is_unblocked:
        user_model.is_unblocked = True
        user_model.save()
    else:
        user_model.is_unblocked = False
        user_model.save()
