
from rest_framework.exceptions import Throttled


class ContactThrottled(

    Throttled

):

    default_detail = (

        "Too many messages have been sent. "

        "Please wait a moment before trying again."

    )
