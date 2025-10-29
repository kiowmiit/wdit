filename = "sample01.txt"
chunk_size = 1024 #1 KB

with open(filename, "rb") as file:
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        print(f"Chunk: {len(chunk)} bytes")