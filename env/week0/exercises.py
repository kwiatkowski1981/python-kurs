
# download time converter

s = 1
m = s * 60
g = s * 3600

toDownload = 12.82
speed = 1  # 1 000 000 Bit/s = 8 000 000 Byte/s

# 12 gb = 12 000 000 000 Byte

second = float(input('podaj szybkosc łącza internetu w Mega-Bitach'))
print(f'twoja szybkosc to {speed} Mega-Bitów/s')
fileSize = float(input('podaj wielkosc pliku do sciągnięcia w Mega-Bajtach'))
print(f'Twoj plik ma {toDownload} Mega-Bajtów wielkości')

result = fileSize / second
timeLeftInMinutes = result / m
timeLeftInHours = result / g
downloadTime = 'na sciagniecie pliku potrzeba'
print(f'{downloadTime} {result}')
print(f'{downloadTime} {timeLeftInMinutes:.2f} minuty')
print(f'{downloadTime} {timeLeftInHours:.2f}  godziny')

