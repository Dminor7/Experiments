from request_ab import AppBrain
import os
url_list = ["https://www.appbrain.com/app/cartoon-photo-effect-cartoon-art-filter/com.photobyte.cartooneffect"]


if __name__ == '__main__':
    app_brain = AppBrain()
    app_brain.scrape(url_list, 100)
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # folder = os.path.join(BASE_DIR,"outgoing")
   
  
