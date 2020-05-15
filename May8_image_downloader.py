import requests
from bs4 import BeautifulSoup as bs
import os.path

TOTAL_NUM = 10
TOTAL_DOWNLOAD_SIZE = [0]


def get_image_url(link):
    html_data = requests.get(link).content
    soup = bs(html_data)

    image_div = soup.find("div", {"id":"comic"})
    image_url = image_div.find("img").get("src")
    final_link = "https:" + image_url

    return final_link


def get_filesize(file_name):
    download_size = os.path.getsize(file_name)
    return download_size
    
    

def download_image(image_url):
    response = requests.get(image_url)
    if response.status_code != 200:
        print("Link Broken!")
        return 1
    else:
        image_data = requests.get(image_url).content
        file_name = image_url.split("/")[-1]
        if os.path.exists(file_name):
            print("File already exists!")
        else:
            file = open(file_name, "wb")
            file.write(image_data)
            file.close()
            TOTAL_DOWNLOAD_SIZE[0] += get_filesize(file_name)
            

    return 0

def get_percent(current, total):
    
    percent = (current / total) * 100    
    return percent


def main():
    total_size = 0
    for joke_num in range(1, TOTAL_NUM + 1):
        link = f"https://xkcd.com/{joke_num}/"
        
        image_url = get_image_url(link)
        print(f"Downloading {image_url}")
        
        download_image(image_url)
        
        percent = get_percent(joke_num, TOTAL_NUM)
        print(f"Downloaded {percent}%")
        
    print(f"Total size of files downloaded: {TOTAL_DOWNLOAD_SIZE[0] / 1024} kB")
        

link = f"https://xkcd.com/1/"

print(get_image_url(link))

# if __name__ == "__main__":
#     try:
#         main()
#     except requests.exceptions.ConnectionError:
#         print("No Internet Connection!")