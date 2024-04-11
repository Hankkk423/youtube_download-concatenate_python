# Open the temp.txt file for reading
with open("temp_description.txt", "r", encoding="utf-8") as temp_file:
    lines = temp_file.readlines()

# Open the youtube_urls.txt file for writing
with open("youtube_urls.txt", "w") as youtube_urls_file:
    for line in lines:
        if line.strip().startswith("- Watch:"):
            # Extract the URL from the line
            url = line.strip().split("- Watch: ")[1]
            # Write the URL to youtube_urls.txt
            youtube_urls_file.write(url + "\n")
