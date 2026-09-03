class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        fleet = []
        for position, speed in cars:
            hours = (target-position)/speed 
            fleet.append(hours)
            if len(fleet) >=2 and fleet[-1] <= fleet[-2]:
                fleet.pop()
        return len(fleet)
