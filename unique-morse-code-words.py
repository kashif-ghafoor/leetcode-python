code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
        "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
words = ["gin", "zen", "gig", "msg"]

output = []
for word in words:
    transformation = ''
    for char in word:
        transformation += code[ord(char) - 97]
    output.append(transformation)

print(len(set(output)))
