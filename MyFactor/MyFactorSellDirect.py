#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- encoding:utf-8 -*-
from abupy import AbuFactorBuyTD, BuyCallMixin

class AbuTwoDayBuy(AbuFactorBuyTD, BuyCallMixin):
    """示例AbuLeastPolyWrap，混入BuyCallMixin，即向上突破触发买入event"""

    def _init_self(self, **kwargs):

        pass

    def fit_day(self, today):
        """
        针对每一个交易日拟合买入交易策略，今天涨，昨天涨就买
        :param today: 当前驱动的交易日金融时间序列数据
        :return:
        """
        # 今天的涨幅
        td_change = today.p_change
        # 昨天的涨幅
        yd_change = self.yesterday.p_change

        if td_change > 0 and 0 < yd_change < td_change:
            # 连续涨两天, 且今天的涨幅比昨天还高 －>买入, 用到了今天的涨幅，只能明天买
            return self.buy_tomorrow()
        return None
