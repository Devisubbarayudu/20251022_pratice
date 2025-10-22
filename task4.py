monthly_rainfall = (120, 150, 120, 180, 120, 90, 110, 130, 100, 140, 120, 160)
total=sum(monthly_rainfall)
print(total)

average= sum(monthly_rainfall) / len(monthly_rainfall)
print(average)

count=monthly_rainfall.count(120)
print(count)

highest = max(monthly_rainfall)  
print(highest)
lowest = min(monthly_rainfall)   
print(lowest)
