sensor_temperaturas = [28, 31, 27, 35, 29]


for i in range(len(sensor_temperaturas)):
    if sensor_temperaturas[i] > 30:
        print(f"Sensor {i+1} acima do limite")
