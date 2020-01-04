#Read in file and Format Data
file1 = open("list_of_ALL_movies_seen.txt","r+")
vocab = file1.readlines()

for i in range(0,len(vocab)):
    vocab[i] = vocab[i].splitlines()
