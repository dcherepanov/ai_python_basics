t = int(input('Time (sec): '))
hours = t // 3600
minutes = (t - 3600 * hours) // 60
seconds = (t - 3600 * hours - 60 * minutes) % 60
print(f'{hours}:{minutes}:{seconds}')
