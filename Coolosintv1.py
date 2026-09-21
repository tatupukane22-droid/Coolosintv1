import requests
import sys
import time
def typewriter(text):
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush
		time.sleep(0.006)
	print()
typewriter("COOLOSINTV1")
username = input("username: ").strip()

sites = {
    "github": f"https://github.com/{username}",
    "reddit": f"https://reddit.com/user/l{username}",
    "Fur Affinity": f"https://www.furaffinity.net/user/{username}",
    "Sketchfab": f"https://sketchfab.com/{username}",
     "Spotify": f"https://open.spotify.com/user/{username}",
     	"YouTube": f"https://www.youtube.com/@{username}",
     	"x": f"https://x.com/{username}",
     	    "Instagram": f"https://www.instagram.com/{username}",
    "TikTok": f"https://www.tiktok.com/@{username}",
    "Twitch": f"https://www.twitch.tv/{username}",
    "Pinterest": f"https://www.pinterest.com/{username}",
    "LinkedIn": f"https://www.linkedin.com/in/{username}",
    "Medium": f"https://medium.com/@{username}",
    "Steam": f"https://steamcommunity.com/id/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
    "Behance": f"https://www.behance.net/				{username}",
    "Telegram": f"https://t.me/{username}",
    "DeviantArt": f"https://www.deviantart.com/{username}",
    "Vimeo": f"https://vimeo.com/{username}",
    "Patreon": f"https://www.patreon.com/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
    "HackerRank": f"https://www.hackerrank.com/{username}",
    "Buy Me a Coffee": f"https://buymeacoffee.com/{username}",
    "Codecademy": f"https://www.codecademy.com/profiles/{username}",
    "Replit": f"https://replit.com/@{username}",
    "Goodreads": f"https://www.goodreads.com/{username}",
        "Chess": f"https://www.chess.com/member/{username}",
    "Quora": f"https://www.quora.com/profile/{username}",
    "Wattpad": f"https://www.wattpad.com/user/{username}",
    "Flickr": f"https://www.flickr.com/people/{username}",
    "Last.fm": f"https://www.last.fm/user/{username}",
    "About.me": f"https://about.me/{username}",
        "Dev.to": f"https://dev.to/{username}",
    "Product Hunt": f"https://www.producthunt.com/@{username}",
    "Disqus": f"https://disqus.com/by/{username}/",
    "Kaggle": f"https://www.kaggle.com/{username}",
    "Mastodon": f"https://mastodon.social/@{username}",
    "Tripadvisor": f"https://www.tripadvisor.com/members/{username}",
        "Hacker News": f"https://news.ycombinator.com/user?id={username}",
    "Substack": f"https://{username}.substack.com",
    "Blogger": f"https://{username}.blogspot.com",
    "WordPress": f"https://{username}.wordpress.com",
    "Keybase": f"https://keybase.io/{username}",
    "Vercel": f"https://{username}.vercel.app",
    "Netlify": f"https://{username}.netlify.app",
    "Giphy": f"https://giphy.com/{username}",
    "Bandcamp": f"https://bandcamp.com/{username}",
    "SoundClick": f"https://www.soundclick.com/{username}",
    "Roblox": f"https://www.roblox.com/user.aspx?username={username}",
    "Hugging Face": f"https://huggingface.co/{username}",
    "Stack Overflow": f"https://stackoverflow.com/users/{username}",
    "Itch.io": f"https://{username}.itch.io",
        "Substack": f"https://{username}.substack.com",
    "Blogger": f"https://{username}.blogspot.com",
    "WordPress": f"https://{username}.wordpress.com",
    "Keybase": f"https://keybase.io/{username}",
    "Vercel": f"https://{username}.vercel.app",
    "Netlify": f"https://{username}.netlify.app",
    "Giphy": f"https://giphy.com/{username}",
    "Bandcamp": f"https://bandcamp.com/{username}",
    "SoundClick": f"https://www.soundclick.com/{username}",
    "Roblox": f"https://www.roblox.com/user.aspx?username={username}",
    "Hugging Face": f"https://huggingface.co/{username}",
    "Stack Overflow": f"https://stackoverflow.com/users/{username}",
    "Itch.io": f"https://{username}.itch.io",
    "Codewars": f"https://www.codewars.com/users/{username}",
    "TryHackMe": f"https://tryhackme.com/p/{username}",
    "Mixcloud": f"https://www.mixcloud.com/{username}",
    "OpenStreetMap": f"https://www.openstreetmap.org/user/{username}",
    "Genius": f"https://genius.com/{username}",
    "Duolingo": f"https://www.duolingo.com/profile/{username}",
    "Strava": f"https://www.strava.com/athletes/{username}",
        "Letterboxd": f"https://letterboxd.com/{username}",
    "MyAnimeList": f"https://myanimelist.net/profile/{username}",
    "CodePen": f"https://codepen.io/{username}",
    "Archive.org": f"https://archive.org/people/{username}",
    "Speedrun.com": f"https://www.speedrun.com/user/{username}",
    "Scratch": f"https://scratch.mit.edu/users/{username}",
    "Faceit": f"https://www.faceit.com/en/players/{username}",
    "Wikipedia": f"https://en.wikipedia.org/wiki/User:{username}",
    "Vero": f"https://vero.co/{username}",
    "Substack": f"https://{username}.substack.com",
}
headers = {"User-Agent": "freshosintv1"}
typewriter("scanning")
for name, url in sites.items():
    try:
        r = requests.get(url, headers=headers, timeout=8)
        if r.status_code == 404:
            typewriter(f"[-] {name}: not found")
        else:
            typewriter(f"[+] {name}: FOUND → {url}")
    except:
        typewriter(f"[?] {name}: error")
typewriter("END OF SCAN")
