import re
# 메타문자

# A|B 는 A 또는 B라는 의미
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m) # Crow


