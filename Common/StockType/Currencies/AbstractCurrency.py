from abc import *
from Common.StockType.AbstractStock import AbstractStock


class AbstractCurrency(AbstractStock):
    _info_labels: list = list()
    _info_list: list = list()
    _name: str = 'NA'

    def __init__(self, c_name: str):
        self.__class = 'Currency'

    def __str__(self):
        return self.__class

    @property
    def InfoList(self):
        return self._info_list

    @property
    def InfoLabels(self):
        return self._info_labels

    @property
    def Name(self):
        return self._name
