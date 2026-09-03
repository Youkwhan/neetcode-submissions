class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = list(zip(position, speed))
        pos_speed.sort(reverse=True)

        #farthest in the front 
        #we want to see if cars behind can catch up.
        fleets = []

        for position,speed in pos_speed:
            eta = (target-position)/speed
            fleets.append(eta)
            #fleets so earlier car is in first
            #if the later car -1 is faster (lower time) merge
            while len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        return len(fleets)

            

