import parse

line = "hello my name is Karan, I live in Bangalore"

parse_format = "hello my name is {}, I live in {}"

result = parse.parse(parse_format, line)

if result:
    name = result[0]
    place = result[1]

    print(name, place)
else:
    print("no match")