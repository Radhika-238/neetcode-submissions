class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack =  []
        time = []

        for i in range(len(position)):
            stack.append((position[i], speed[i]))
        stack.sort(reverse = True)

        for p, s  in stack:
            time_taken = (target - p)/s
            if not time or  time_taken > time[-1]:
                time.append(time_taken)
        
        return len(time)
            