import pytube

# Ask the user for the YouTube video link
link = input("Enter the YouTube video link: ")

# Ask the user for the desired resolution
resolution = input("Enter the desired resolution (e.g. 1080p): ")

# Create a YouTube object using the link
yt = pytube.YouTube(link)

# Get all available streams for the video
streams = yt.streams.filter(resolution=resolution).all()

# Print the available streams
print("Available streams:")
for i, stream in enumerate(streams):
    print(f"{i}: {stream}")

# Ask the user to select a stream
index = int(input("Enter the index of the stream to download: "))

# Download the selected stream
streams[index].download()

print("Video downloaded!")
