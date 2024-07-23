import i18n


def get_message(group: str, message_id: str) -> str:
    return i18n.t(group + "." + message_id)
