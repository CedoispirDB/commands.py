import hashlib

x = [".png", ".jpeg", ".mp4", ".rtf", ".pdf", ".txt"]
for n in x:
    ex = hashlib.sha1(n.encode()).hexdigest()
    print(n + ": " + ex)
