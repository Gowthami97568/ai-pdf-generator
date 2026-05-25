import os
from generator import generate_report, generate_notes, generate_resume
from pdf import create_pdf

print("1. Report")
print("2. Notes")
print("3. Resume")

choice = input("Enter choice: ")
topic = input("Enter topic: ")

if choice == "1":
    content = generate_report(topic)
elif choice == "2":
    content = generate_notes(topic)
elif choice == "3":
    content = generate_resume(topic)
else:
    print("Invalid choice")
    exit()

filename = topic.replace(" ", "_") + ".pdf"

create_pdf(content, filename)

os.startfile(filename)

print("PDF created successfully!")