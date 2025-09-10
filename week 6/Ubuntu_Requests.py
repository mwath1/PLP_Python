import requests
import os
from urllib.parse import urlparse

#Prompts the user for a URL containing an image
def main():
    urls = input("Enter the URLs of the images (comma-separated): ").split(',')
    urls = [url.strip() for url in urls if url.strip()]  # Clean up whitespace and remove empty strings

    #Creates a directory called "Fetched_Images" if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)
    for url in urls:
        try:
            #Fetches the image from the URL
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raises an error for bad responses


            #Extracts the filename from the URL
            parsed_url = urlparse(url)
            image_name = os.path.basename(parsed_url.path)
            
    #prevent duplicate downloads
            if image_name in os.listdir("Fetched_Images"):
                print(f"✗ Skipped {url}: Already downloaded.")
                continue

            if not image_name:
                image_name = "image.jpg"  # Default name if URL doesn't end with a filename
            #Checks if the content is an image
            if not response.headers.get('Content-Type', '').startswith('image/'):
                print(f"✗ Skipped {url}: Not an image.")
                continue
            
            #checks http headers
            print("content-type:", response.headers.get('Content-Type'))
            print("content-length:", response.headers.get('Content-Length'))

            #save the image to the "Fetched_Images" directory
            image_path = os.path.join("Fetched_Images", image_name)
            with open(image_path, "wb") as f:
                f.write(response.content)
            print(f"Successfully saved {image_name} to Fetched_Images directory.")
            print(f"Image URL: {url}")
            print("\nConnection strengthened. Community enriched.")
            

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error: {e}")
        except Exception as e:
            print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()