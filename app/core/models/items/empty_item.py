from app.core.models.items.base import BaseItem


class EmptyItem(BaseItem):

    def __init__(self):
        super(EmptyItem, self).__init__("Empty")

    @staticmethod
    def get_param_name(): return "None"

    def get_filter_params(self):
        return {}

    def __get__(self, instance=None, owner=None) -> dict:
        return {}

    def __getitem__(self, item):
        return {}

    def __setitem__(self, key, value):
        pass

    def get_price(self):
        return 0

    def create_from_dict(self, data: dict):
        pass
