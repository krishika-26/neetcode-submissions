class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_count = 0
        fleet_value = 0
        for pos,spd in sorted(list(zip(position, speed)), reverse = True):
            time = (target - pos)/spd
            if time > fleet_value:
                fleet_count+=1
                fleet_value = time
        return fleet_count
                


        
        