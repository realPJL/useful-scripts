import os

def clear_json_xz_files(directory):
    for f in os.listdir(directory):
        if f.endswith(".txt"):
            os.remove(os.path.join(directory, f))

# Example usage:
clear_json_xz_files('downloaded_reels')

