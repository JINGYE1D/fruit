MAX_WEIGHT = 1000.0  # 1kg
PACKING_FEE = 1.0  # €


def process(type, store):
    weight = 0.0
    price = PACKING_FEE
    pack = []
    i = 0

    while i < len(store):
        if weight + store[i][1] <= MAX_WEIGHT:
            pack.append(store[i][0])
            price += type[store[i][0]] * store[i][1] / 1000.0
            weight += store[i][1]
            i += 1
        else:
            if len(pack) == 0:
                return
            print(f"\tBox: {pack}")
            print(f"\tPrice: {price:.2f}, Weight: {weight:.0f}")
            # new pack
            weight = 0.0
            price = PACKING_FEE
            pack = []
    if len(pack) == 0:
        return
    print(f"\tBox: {pack}")
    print(f"\tPrice: {price:.2f}, Weight: {weight:.0f}")


def main():
    print("Example 1:")
    type = {"apple": 4.0}
    store = [("apple", 250)]
    process(type, store)

    print("Example 2:")
    type = {"apple": 1.0, "avocado": 10.0}
    store = [("apple", 300), ("avocado", 300), ("apple", 300), ("apple", 300), ("avocado", 300)]
    process(type, store)

    print("Example 3:")
    type = {"apple": 1.0, "avocado": 10.0}
    store = []
    process(type, store)

    print("Example 4:")
    type = {"apple": 1.0, "avocado": 10.0}
    store = [("apple", 0), ("avocado", 300), ("apple", 3000), ("apple", 300), ("avocado", 300)]
    process(type, store)


main()
