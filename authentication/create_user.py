from helpers import get_users, hash_password


def create_user():
    user_list = get_users()
    x = hash_password("xxxx")
    user_list["Denis"] = x
    return user_list


