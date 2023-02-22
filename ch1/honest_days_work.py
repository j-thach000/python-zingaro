# todo
# [x] take input
# [] process input (P, paint / B, badges / D, badge price / remaining paint???)
# [] print input

paint_total = int(input()) # how much total paint do we have
badge_paint_req = int(input()) # how much paint does it take for a badge to be finished
badge_cost = int(input()) # how much do we sell the badge for

badges_total = paint_total // badge_paint_req # // opposed to / produces the closest integer 

paint_remainder = paint_total % badge_paint_req

profit = (badges_total * badge_cost) + paint_remainder
print(profit)



