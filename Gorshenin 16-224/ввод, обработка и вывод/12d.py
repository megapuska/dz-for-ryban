buy = 40
all_buy = 40 * 2000
broker_buy = all_buy * 0.03

sell = 42.75
all_sell = 42.75 * 2000
broker_sell = all_sell * 0.03

sum_all = (all_sell - broker_sell) - (all_buy - broker_buy)
print(all_buy,broker_buy,all_sell,broker_sell,sum_all)
