from .generic_indicator import GenericIndicator
from pyti.commodity_channel_index import commodity_channel_index as cci


# params: period
# https://github.com/kylejusticemagnuson/pyti/blob/master/pyti/commodity_channel_index.py
class PytiCommodityChannelIndex(GenericIndicator):

    def __init__(self, market, interval, periods, params=None):
        super().__init__(market, interval, periods, None, None, params)

    def next_calculation(self, candle):
        if self.get_datawindow() is not None:
            self.value = cci(
                self.get_close(),
                self.get_high(),
                self.get_low(),
                self.params['period']
            )[-1]
