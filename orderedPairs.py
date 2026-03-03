class OrderedPairs:
    def __iter__(self):
        self.n = 0
        self.i = 1
        self.j = 1
        return self

    def __next__(self):
        while self.i < self.n:
            if self.j <= self.n:
                if self.i < self.j:
                    result = (self.i, self.j)
                    self.j += 1
                    return result
                self.j += 1
            else:
                self.i += 1
                self.j = self.i + 1
        raise StopIteration
    
    def set_n(self, n):
        self.n = n
        self.i = 1
        self.j = 1
    
    def pairs(self, n):
        self.n = n
        count=0
        print(f"Generating ordered pairs for n={self.n}")
        for i in range(1, self.n + 1):
            for j in range(i, self.n + 1):
                i_val = j - i  # Define i_val before using
                # Yield pairs (i_val, j) where i_val = n - j and i_val > 0
                if i_val > 0:
                    count += 1
                    print(f"Yielding valid ordered pair (i={i}, j={j}) where i_val > 0 - Total count: {count}")
                    yield (i, j)
    
    def ordpair_count(self, n):
        count = 0
        for i in range(1, n + 1):
            b = i
            a = n - b
            if a > 0:
                count += 1
        return count
# Example usage:
if __name__ == "__main__":
    ordered_pairs = OrderedPairs()
    ordered_pairs.set_n(3)
    for pair in ordered_pairs:
        print(pair)  # Output the ordered pairs (i, j) where 1 <= i < j <= n
    ordpair = ordered_pairs.ordpair_count(6)
    print(f"Total ordered pairs (i, j) where 1 <= i < j <= 3: {ordpair}")