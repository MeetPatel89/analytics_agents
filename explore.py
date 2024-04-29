d = {
    "language":"python",
    "description":"return numbers from 1 to 10 according to Zen of Python"
}

for key, value in d.items():
    print(key, value)
    
from operator import itemgetter

transform = {
    "language": itemgetter("language"),
    # other transformations...
}

data = {
    "language": "Python",
    # other data...
}

print(transform["language"](data))