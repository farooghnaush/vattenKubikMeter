class waterCubic:
    def __init__(self, value):
        self.value = value

    def measure_water(self):
        """Räkna hur mycket vatten en terrängen kan förvara."""
        
        if not self.value:
            return 0
     
        n = len(self.value)
    
        #fylla på två listor med 0
        left_height_max = [0] * n
        right_height_max = [0] * n

        #fylla på ett list med högsta värde från rätt sidan
        for i in range(n):
            left_height_max[i] = max(left_height_max[i-1], self.value[i])
            
        #fylla på andra list med högsta värde från andra sidan
        for i in range(n - 2, -2, -1):
            right_height_max[i] = max(right_height_max[i+1], self.value[i])
    
        #jämföra med original list
        water = 0
        for i in range(n):
            water += min(left_height_max[i], right_height_max[i]) - self.value[i]

        return water