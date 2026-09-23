time_in_seconds = int(input())
seconds = time_in_seconds % 60
minutes = time_in_seconds // 60
hours = minutes // 60
minutes = minutes % 60
print(f"{hours}:{minutes}:{seconds}")