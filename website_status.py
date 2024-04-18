# don't just run this script - it uses a console argument
# python3 website_status.py https://example.com

# pip install requests
import sys
import requests

# Function to check if a website is up or down
def check_website(website):
    try:
        response = requests.get(website)
        if response.status_code == 200:
            print(f"Website {website} is UP")
        else:
            print(f"Website {website} is DOWN")
    except requests.ConnectionError:
        print(f"Could not connect to website {website}")

# Usage information
def usage():
    print("Usage: {} <website>".format(sys.argv[0]))
    print("Example: {} https://example.com".format(sys.argv[0]))

# Main function
def main():
    # Check if website argument is provided
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    website = sys.argv[1]
    check_website(website)

# Call the main function
if __name__ == "__main__":
    main()
