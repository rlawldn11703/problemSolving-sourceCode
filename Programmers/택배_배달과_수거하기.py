def check_farpoint(house):
    while house and house[-1] == 0:
        house.pop()
    n = len(house)
    return n

def move_truck(house,cap):
    truck = cap
    dist = check_farpoint(house)
    while house:
        parcel = house.pop()
        if truck >= parcel:
            truck -= parcel
        else:
            parcel -= truck
            house.append(parcel)
            break
    return dist
        
def solution(cap, n, deliveries, pickups):
    ans = 0
    while deliveries or pickups:
        d_deliver = move_truck(deliveries,cap)
        d_pickup = move_truck(pickups,cap)
        ans += max(d_deliver,d_pickup) * 2
    return ans