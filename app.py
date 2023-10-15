
# import instaloader
# from datetime import datetime
# from itertools import dropwhile, takewhile
# import csv
# import pandas as pd




# class GetInstagramProfile():
#     def __init__(self) -> None:
#         self.L = instaloader.Instaloader()

#     def download_users_profile_picture(self,username):
#         self.L.download_profile(username, profile_pic_only=True)


#     def get_post_info_csv(self, username):
#         with open(username + '.csv', 'w', newline='', encoding='utf-8') as file:
#             writer = csv.writer(file)
#             posts = instaloader.Profile.from_username(self.L.context, username).get_posts()
#             for post in posts:
#                 caption = post.caption if post.caption is not None else "No caption available"
#                 writer.writerow(["post", caption])
                


# if __name__=="__main__":
#     username=input("Enter the username : ")
#     cls = GetInstagramProfile()
#     cls.get_post_info_csv(username)




# #   second


# # import instaloader
# # profile_name = input("Enter Insta Profile name: ")
# # print ("Downloading Media...")
# # instaloader.Instaloader().download_profile(profile_name, profile_pic_only=False)
# # print ("Download Completed!")
import instaloader
import csv
import pandas as pd

class GetInstagramProfile():
    def __init__(self):
        self.L = instaloader.Instaloader()

    def download_users_profile_picture(self, username):
        self.L.download_profile(username, profile_pic_only=True)

    def get_post_info_csv(self, username):
        captions = []  # List to store captions
        posts = instaloader.Profile.from_username(self.L.context, username).get_posts()
        
        with open(username + '.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for i, post in enumerate(posts, start=1):
                caption = post.caption if post.caption is not None else "No caption available"
                captions.append(caption)
                writer.writerow(["post " + str(i), caption]) 
        
        # Create a DataFrame from the list of captions
        data = {'Captions': captions}
        df = pd.DataFrame(data)
        print(df)
        
        # Save the DataFrame to a CSV file
        # df.to_csv(username + '_captions.csv', index=False)

if __name__ == "__main__":
    username = input("Enter the username: ")
    cls = GetInstagramProfile()
    cls.get_post_info_csv(username)
