text = "X-DSPAM-Confidence:    0.8475"

index = text.find(":")
fdigit = float(text[index + 1:].strip())

print(fdigit + 100)
