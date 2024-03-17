price_ranges = [1, 24, float('inf')]

price_values = [
    [20_000, 14_000, 12_000], 
    [20_000, 15_500, 12_500]
]

def calculate_rate(km, carType):
    if (km < 0):
        raise ValueError('Invalid distance')
    if (carType != 1 and carType != 2):
        raise ValueError('Invalid car type')
    
    value = 0
    for i in range(len(price_ranges)):
        if (km <= 0): 
            break
        value = value + price_values[carType - 1][i] * min(km, price_ranges[i])
        km -= price_ranges[i]

    return value
        
def main():
    carType = int(input('Car types available: \n1 - VF5 Plus\n2 - VF e34\nChoose: '))
    distance = int(input('Distance travelled: '))
    try :
        print('{:,}'.format(calculate_rate(distance, carType)))
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()