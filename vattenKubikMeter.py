class vattenKubikMeter:
    def __init__(self, value):
        self.value = value

    def beräkna_vatten(self):
        """Räkna hur mycket vatten en terrängen kan förvara."""
        
        if not self.value:
            return 0
     
        n = len(self.value)
    
        #fylla på två listor med 0
        vänster_höjd_max = [0] * n
        höger_höjd_max = [0] * n

        #fylla på ett list med högsta värde från ett sidan
        for i in range(n):
            vänster_höjd_max[i] = max(vänster_höjd_max[i-1], self.value[i])
            
        #fylla på andra list med högsta värde från andra sidan
        for i in range(n - 2, -2, -1):
            höger_höjd_max[i] = max(höger_höjd_max[i+1], self.value[i])
    
        #jämföra med original list, beräkna vatten i 
        #terrängen om värde i original list är mindre 
        vatten = 0
        for i in range(n):
            vatten += min(vänster_höjd_max[i], höger_höjd_max[i]) - self.value[i]

        return vatten

if __name__ == "__main__":
    print("Ange siffror med mellanslag:")
    a = [int(x) for x in input().split()]
    b = vattenKubikMeter(a)
    w = b.beräkna_vatten()
    print(f"{w} m³")