def traffic_count(array):
    hours = ["4:00pm", "5:00pm", "6:00pm", "7:00pm", "8:00pm"]
    maxCars = []
    for m in range(len(hours)-1):
        maxCars.append(max(array[6*m: 6*(m+1)]))
    return list(zip(hours, maxCars))