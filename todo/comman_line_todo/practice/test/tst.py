contents = ["Percent button is used to find the percentage of a number. Enter the percentage amount, ",
            "click the % button, then enter the number you want the", 
            "aldkfjalskdfjlasjdflaskjdf alsfdj asdfj" ]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"{filename}", 'w')
    file.write(content)


