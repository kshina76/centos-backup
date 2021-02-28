
period = 10*12
interest_rate = 1.010 # 月利
reserve = 30000 # 毎月の積み立て
funding = 0
profit_month = 0
profit_year = 0
for i in range(1, period + 1):
    funding += reserve  # 積み立て
    profit_month = funding * (interest_rate - 1)  # 月利
    profit_year += profit_month # 税金処理のための変数
    funding *= interest_rate # 月利を加えた資金
    if i % 12 == 0:
        zeikin = profit_year * 0.20315
        profit_year = 0
        funding -= zeikin
    print(i, funding)
