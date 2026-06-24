class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack_fleet = []
        cars = sorted(list(zip(position, speed)), reverse= True)
        for pos, spd in cars:
            time_taken = (target - pos)/spd
            if len(stack_fleet) == 0:
                stack_fleet.append(time_taken)
            elif time_taken <= stack_fleet[-1]:
                continue
            else:
                stack_fleet.append(time_taken)
        return len(stack_fleet)

        
        