MAX_WEIGHT = 1000.0 # 1kg
PACKING_FEE = 1.0 # €

class FruitType:
    def __init__(self, items):
        self.map = {}
        for item in items:
            self.map[item[0]] = item[1]

    def getPrice(self, key):
        return self.map[key] / 1000.0

class FruitStorage:
    def __init__(self, items):
        self.list = []
        self.list = items
        self.index = 0

    def getCurrentFruit(self):
        return self.list[self.index]

    def fetch(self, amount):
        (_, left) = self.list[self.index]
        if (left > amount):
            self.list[self.index][1] -= amount
        else:
            self.index += 1

    def empty(self):
        if (self.index >= len(self.list)):
            return True
        else:
            return False

class FruitPackage:
    def __init__(self, fruitType, fruitStorage):
        self.quota = FruitType(fruitType)
        self.storage = FruitStorage(fruitStorage)
        self.response = []
        self.package = []
        self.total_price = PACKING_FEE
        self.total_weight = 0.0

    def packingFruit(self, fruit, weight):
        self.package.append((fruit, weight))
        self.total_price += self.quota.getPrice(fruit) * weight
        self.total_weight += weight
        self.storage.fetch(weight)

    def packingFinish(self):
        if (len(self.package) != 0):
            self.response.append({"Price": self.total_price,
                                "Weight": self.total_weight,
                                "Package": self.package})
            # new package
            self.package = []
            self.total_price = PACKING_FEE
            self.total_weight = 0.0
            return True
        else:
            return False

    def process(self):
        while (not self.storage.empty()):
            (fruit, weight) = self.storage.getCurrentFruit()
            if (self.total_weight + weight <= MAX_WEIGHT):
                self.packingFruit(fruit, weight)
            else:
                if (not self.packingFinish()):
                    break

        # last package
        self.packingFinish()

    def print(self):
        print("Example:")
        for i in range(len(self.response)):
            price = self.response[i]["Price"]
            weight = self.response[i]["Weight"]
            package = self.response[i]["Package"]

            print(f"    box {i + 1}: ", end = "")
            for j in range(len(package) - 1):
                (fruit, _) = package[j]
                print(f"{fruit}", end = ", ")
            (fruit, _) = package[-1]
            print(f"{fruit}", end = " - ")
            print(f"{weight:.0f}g - {price:.2f}€".replace(".", ","))


def main():
    # Example 1
    ex1 = FruitPackage([("apple", 4.0)],
                         [("apple", 250)])
    ex1.process()
    ex1.print()

    # Example 2
    ex2 = FruitPackage([("apple", 1.0), ("avocado", 10.0)],
                         [("apple", 300), ("avocado", 300), ("apple", 300), ("apple", 300), ("avocado", 300)])
    ex2.process()
    ex2.print()

    # Extra testcases
    ex3 = FruitPackage([("apple", 1.0), ("avocado", 10.0)],
                       [])
    ex3.process()
    ex3.print()

    #
    ex4 = FruitPackage([("apple", 1.0), ("avocado", 10.0)],
                       [("apple", 0), ("avocado", 300), ("apple", 3000), ("apple", 300), ("avocado", 300)])
    ex4.process()
    ex4.print()

if __name__ == '__main__':
    main()
