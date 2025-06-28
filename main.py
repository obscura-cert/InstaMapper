from instaloader import Instaloader, Profile
from colorama import Fore, Style, init
from statistics import mean

init(autoreset=True)

class InstaMapper:
    def __init__(self):
        self.loader = Instaloader()

    def fetch_profile(self, username):
        try:
            profile = Profile.from_username(self.loader.context, username)

            print(f"{Fore.GREEN}[✔] Profile Found: {username}\n")

            # BASIC INFO
            print(f"{Fore.CYAN}🧑‍💼 BASIC PROFILE INFO")
            print(f"{Fore.WHITE}Username              : {profile.username}")
            print(f"Full Name             : {profile.full_name}")
            print(f"Biography             : {profile.biography}")
            print(f"External URL          : {profile.external_url}")
            print(f"Profile Pic (HD)      : {profile.profile_pic_url}")
            print(f"User ID               : {profile.userid}")
            print(f"Is Private            : {profile.is_private}")
            print(f"Is Verified           : {profile.is_verified}")
            print(f"Business Category     : {profile.business_category_name}")

            # STATS
            print(f"{Fore.CYAN}📊 STATS")
            print(f"Posts                 : {profile.mediacount}")
            print(f"Followers             : {profile.followers}")
            print(f"Following             : {profile.followees}")

            posts = list(profile.get_posts())[:10]  # Sample 10 posts
            likes = [post.likes for post in posts if post.likes is not None]
            comments = [post.comments for post in posts if post.comments is not None]
            engagement = ((mean(likes) + mean(comments)) / profile.followers * 100) if profile.followers and likes else 0

            print(f"Average Likes         : {mean(likes):.2f}" if likes else "Average Likes         : N/A")
            print(f"Average Comments      : {mean(comments):.2f}" if comments else "Average Comments      : N/A")
            print(f"Engagement Rate       : {engagement:.2f}%\n")

            # ACCOUNT METADATA
            print(f"{Fore.CYAN}📅 ACCOUNT METADATA")
            if posts:
                print(f"Date of Latest Post   : {posts[0].date_utc}")
            else:
                print("Date of Latest Post   : N/A")
            print(f"Account Type          : {'Business' if profile.business_category_name else 'Personal'}")
            print(f"Has Highlight Reels   : {profile.has_highlight_reels}\n")

            # PROFILE PICTURE
            print(f"{Fore.CYAN}📸 PROFILE PICTURE")
            print(f"HD Profile Picture    : {profile.profile_pic_url}")
            print(f"Is Default Picture    : {profile.has_anonymous_profile_picture}")

        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}")

if __name__ == '__main__':
    username = input(f"{Fore.CYAN}📸 Enter Instagram username: {Style.RESET_ALL}").strip()
    insta = InstaMapper()
    insta.fetch_profile(username)
