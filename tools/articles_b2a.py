A = []
def add(slug, title, cat, desc, lead, sections, kw=None, kw2=None):
    A.append(dict(slug=slug, title=title, cat=cat, desc=desc, lead=lead, sections=sections,
                  kw=kw or title.split(':')[0].lower(), kw2=kw2 or []))

B = "IPTV for Beginners"; S = "IPTV Setup & Installation"; D = "IPTV Devices"; P = "IPTV Applications"

add("iptv-glossary-for-beginners", "IPTV Glossary: Common Terms in Plain English", B,
 "A plain-English glossary of IPTV terms such as bitrate, buffering, EPG, M3U, HLS, codec, latency and simultaneous streams, with a line on why each matters.",
 "IPTV comes with its own vocabulary. This glossary explains the terms you will meet in apps, support chats and guides, in everyday language.",
 [("Delivery and quality",[("ul",["Stream: the video and audio data sent to your device as you watch.","Bitrate: how much data per second a stream uses. Higher usually means a sharper picture and more bandwidth needed.","Resolution: the number of pixels in the picture, such as 720p, 1080p or 4K.","Codec: the method used to compress and decompress video. Your device must support it.","Latency: the delay between something happening and you seeing it."])]),
  ("Playback and apps",[("ul",["Buffering: the player pausing to load more data because its reserve ran out.","Player app: the program that plays your channels.","EPG: the on-screen programme guide.","Catch-up: watching a programme after it has aired, where offered.","VOD: video on demand, a library you start when you like."])]),
  ("Sign-in and lists",[("ul",["M3U: a playlist file or link listing channels.","Xtream style login: a server address, username and password entered into an app.","Simultaneous streams: how many screens can play at the same moment on one plan."]),"These terms appear again in our guides on {post:m3u-playlist-explained} and {post:xtream-codes-login-explained}."]),
  ("Network words",["Bandwidth is how much data your connection can carry. Throughput is what you actually get. Wi-Fi band means the radio frequency, usually 2.4 GHz or 5 GHz. If a support agent asks about any of these, a short answer is fine. See {post:streaming-internet-requirements} for targets."])])

add("what-you-need-to-start-iptv", "What You Need to Start Watching IPTV", B,
 "The short list of what you need for IPTV: a compatible device, a steady internet connection, a player app, sign-in details and a way to pay safely.",
 "Starting with IPTV needs less than most people expect. Here is the whole list, in the order you will use it.",
 [("1. A compatible screen",["A smart TV, streaming stick, Android TV box, phone, tablet or computer can all work. Check yours on the {devices} before you pay."]),
  ("2. A steady connection",["Stability matters more than a big headline speed. A cable or a strong Wi-Fi signal near the device helps. Read {post:streaming-internet-requirements} for targets."]),
  ("3. A player app",["The app plays your channels. Choose one from your device's store. Our guide to the {post:what-is-an-iptv-player-app} explains what to look for."]),
  ("4. Sign-in details",["After you subscribe you receive details privately. Keep them safe and enter them exactly."]),
  ("5. A safe way to pay",["Use methods that give you a receipt. We accept PayPal, Binance Pay and Wise. Read {post:iptv-scams-and-safe-payment} if you are unsure about a seller."]),
  ("Optional extras",[("ul",["An Ethernet cable for the steadiest picture.","A second device as a backup on match days.","A router in a central spot."])])])

add("iptv-myths-explained", "IPTV Myths and Misunderstandings Explained", B,
 "Common IPTV myths examined calmly: speed, price, legality, devices, set-top boxes and what a free trial can and cannot tell you about a service.",
 "A lot of IPTV advice online is half true. These are the misunderstandings we hear most, with a straight answer to each.",
 [("\"You need a special box\"",["Not usually. Most services run in an app on devices you may already own. A dedicated box is a choice, not a requirement."]),
  ("\"A fast speed test means no buffering\"",["A speed test measures a short burst. Live television needs steadiness over hours. A connection with a good headline speed can still stutter if it is unstable or the Wi-Fi is weak."]),
  ("\"Cheaper always means worse\"",["Price alone tells you little. Test on your own device, ask about support and read the refund policy. Our {post:how-to-choose-an-iptv-plan} guide gives a checklist."]),
  ("\"If it works for someone else it will work for me\"",["Devices, routers and evenings differ. Only a trial on your setup answers the question. See {post:iptv-free-trial-what-to-test}."]),
  ("\"The licence question does not apply\"",["Viewers in the UK may need a TV Licence however they watch live television. See {post:uk-tv-licence-and-iptv}. Rules elsewhere differ, so check your own country."])])

add("simple-iptv-setup-for-older-viewers", "A Simple IPTV Setup for Less Technical Viewers", B,
 "A calm, step-by-step approach to setting up IPTV for someone who does not enjoy technology: one device, one app, large text and a helper on the phone.",
 "Setting up television should not feel like a test. This approach keeps everything small and calm, whether you are doing it for yourself or for a relative.",
 [("Choose the simplest device",["A single streaming stick on the main TV is usually easiest. Fewer devices means fewer things to go wrong. Ask support to confirm that your TV and stick suit each other."]),
  ("Have help ready",["Set up while someone you trust is on the phone or beside you. We can guide you on WhatsApp, which many people already use for messages."]),
  ("Write it down once",["Keep the sign-in details on a card by the TV, not in a drawer. Write the channel numbers or names used most often."]),
  ("Make it comfortable",[("ul",["Turn on large text if the app allows.","Add favourite channels so there is less scrolling.","Keep the remote simple: one for the TV, one for the stick, labelled."])]),
  ("When something goes wrong",["Restart the stick first, then the router. If it is still wrong, send a photo of the screen to support. Our {post:iptv-channels-not-loading} checklist lists the usual causes."])])

add("watch-iptv-without-a-smart-tv", "Can You Watch IPTV Without a Smart TV?", B,
 "You can watch IPTV on a TV that is not smart by adding a streaming stick or box through HDMI. Learn the options, costs to expect and what to check.",
 "Yes. A TV does not need to be smart if it has an HDMI port and you add a small streaming device.",
 [("The HDMI route",["Most TVs sold in the last fifteen years have at least one HDMI socket. A streaming stick or box plugs into it and brings the apps. The TV then simply shows what the device sends."]),
  ("Choices",[("ul",["A streaming stick: small, cheap and portable.","An Android TV style box: more storage and often an Ethernet port.","A computer connected by HDMI: flexible, but less convenient on the sofa."])]),
  ("Older TVs without HDMI",["Very old sets may only have older connectors. Adapters exist, but quality and compatibility vary. It may be simpler to replace the TV or use a tablet or computer instead."]),
  ("Check before you buy",["Confirm the device is supported by the player app you want. The {post:device-compatibility} guide shows how to identify your equipment, and our {devices} lists the types we check."])])

add("how-to-install-an-iptv-app-safely", "How to Install an IPTV App Safely", S,
 "Install IPTV apps from official stores, check developers and permissions, avoid unknown downloads and what to do if an app behaves strangely.",
 "The player app is software on your device, so the same caution applies as with any app.",
 [("Prefer the official store",["Use the Amazon Appstore, Google Play, the Apple App Store or the store on your TV. These stores check apps before listing them, which reduces risk."]),
  ("Check before you tap install",[("ul",["Developer name and website.","Number of downloads and recent reviews.","Date of the last update.","Permissions requested: a video player does not need your contacts."])]),
  ("Unknown downloads",["If an app is not in a store, ask us to explain exactly why and which file to use before you do anything. Do not follow links from random messages or social media posts."]),
  ("After installing",["Open the app, sign in, and watch how it behaves. If it floods you with pop-ups, asks for odd permissions or slows the device, uninstall it. Read {post:iptv-scams-and-safe-payment} for wider safety habits."])])

add("first-time-iptv-setup-checklist", "First-Time IPTV Setup Checklist", S,
 "A tick-list for your first IPTV setup: confirm the device, update it, free storage, test the network, install the app, sign in and test properly.",
 "Work through this list in order and most first-time problems never appear.",
 [("Before you subscribe",[("ul",["Note your device model and system version.","Ask support to confirm it is suitable.","Request a trial."])]),
  ("Prepare the device",[("ul",["Install system updates and restart.","Free at least a couple of gigabytes of storage.","Set the correct time and date automatically."])]),
  ("Prepare the network",[("ul",["Use a cable if you can.","Otherwise place the router in a central, open spot.","Pause large downloads during testing."])]),
  ("Install and sign in",["Install the app from the official store, then enter the details we send, copying and pasting where possible."]),
  ("Test properly",["Watch live channels for at least an hour during the evening. Open the guide, change channels repeatedly and check sound. If anything is wrong, note it and message support. See {post:iptv-free-trial-what-to-test}."])])

add("iptv-on-two-tvs", "Setting Up IPTV on Two TVs in One Home", S,
 "How to run IPTV on two televisions: simultaneous stream limits, bandwidth, router load, device choices and how to test both at the same time.",
 "Two TVs mean two screens streaming at once, and that changes what your plan and network need to handle.",
 [("Check the plan first",["Ask how many simultaneous streams your plan allows. Two TVs in use at the same time need two. Installing on both devices is not the same as using them together. See {post:how-many-devices-can-i-use-with-iptv}."]),
  ("Count the bandwidth",["Two HD streams need roughly twice the connection of one. Our {post:how-much-data-does-iptv-use} guide gives rough figures."]),
  ("Network layout",["Put the router centrally, and use a cable for the TV nearest it. A second Wi-Fi device in another room may need a mesh node or an Ethernet run."]),
  ("Test both together",["Start both TVs on different live channels in the evening and watch for pauses. If only one struggles, the problem is that room's signal, not the service."])])

add("move-iptv-to-a-new-device", "How to Move Your IPTV Setup to a New Device", S,
 "Switching to a new TV, stick or phone? Learn how to move your IPTV access safely: sign-in details, app install, settings and what to tell support.",
 "A new device does not mean starting again. Most of the work is installing the app and entering your details once more.",
 [("Before you switch",["Check that the new device is supported. Keep your sign-in details to hand and note any favourites or settings you want to recreate."]),
  ("Install and sign in",["Install the same or a compatible player from the store and enter your details. If your plan limits connections, sign out of the old device first to avoid conflicts."]),
  ("Recreate your settings",["Favourites and layout are often stored in the app, so they may need to be set up again. Use favourites for your top channels to save scrolling."]),
  ("If it does not work",["Message support with the new device model and the app name. See {post:iptv-wont-sign-in} for a sign-in checklist."])])

add("reinstall-iptv-app", "Reinstalling an IPTV App Without Losing Access", S,
 "How to reinstall an IPTV player app safely: keeping sign-in details, clearing old data, avoiding duplicate lists and checking stream limits.",
 "Reinstalling can fix a misbehaving app, and it does not cost you your subscription. Your access belongs to your account details, not to the app.",
 [("Keep your details",["Before you uninstall, make sure you have your sign-in details saved somewhere private. Without them you will need to ask support to resend."]),
  ("Clean reinstall",[("ul",["Uninstall the app.","Restart the device.","Install the latest version from the official store.","Sign in once and let the channel list and guide load fully."])]),
  ("Avoid duplicates",["Adding the same list twice can slow the app and cause confusion. Remove old entries before adding a new one."]),
  ("Related",["If a reinstall does not help, work through {post:iptv-app-keeps-restarting} or {post:iptv-app-cache-and-storage}."])])

add("iptv-on-samsung-tv", "IPTV on a Samsung Smart TV: What to Check", S,
 "Before using IPTV on a Samsung smart TV, check the model year, system version, available apps and whether a streaming stick would work better.",
 "Samsung TVs use their own system, so which apps you can install depends on the model and year.",
 [("Find your model",["Open Settings, then Support, then About This TV. Note the model code and software version. Send them to support to check against the apps we can recommend."]),
  ("Check the app store",["Search the TV's app store for the player you plan to use. If it is not listed for your model, a streaming stick on an HDMI port is a common alternative."]),
  ("Keep it updated",["Install software updates, which can improve app stability and security. Free storage by removing apps you do not use."]),
  ("Network",["Use Ethernet if your TV has a port and the router is close. Otherwise use the 5 GHz Wi-Fi band at short range. See {post:iptv-wifi-vs-ethernet}. For general smart TV advice read {post:iptv-on-smart-tv}."])])

add("iptv-on-lg-tv", "IPTV on an LG Smart TV: What to Check", S,
 "Using IPTV on an LG smart TV: identify the webOS version, check the app store, plan for a streaming stick if needed and prepare your network.",
 "LG TVs run webOS. App availability depends on the model year, so a short check beforehand saves trouble.",
 [("Identify your TV",["Go to Settings, then General, then About This TV. Note the model and webOS version. Older models may not receive new apps."]),
  ("Look in the LG Content Store",["Search for the player app you want. If it is missing or outdated, a streaming stick is a reliable alternative."]),
  ("Settings that can help",[("ul",["Turn on automatic software updates.","Restart the TV occasionally rather than leaving it on standby for weeks.","Disable energy saving modes that dim or interrupt playback if they annoy you."])]),
  ("Next",["Compare with {post:iptv-on-samsung-tv}, and use the {post:device-compatibility} guide to confirm what you have."])])

add("iptv-on-nvidia-shield", "IPTV on Nvidia Shield: Setup Notes", D,
 "Notes on using IPTV with an Nvidia Shield: Android TV system, storage, Ethernet, player app choice and keeping the device stable.",
 "The Shield is a powerful Android TV device with a wired Ethernet port, which suits live streaming well.",
 [("Why it works well",["It has plenty of processing power and an Ethernet port. Together those give smooth decoding and a steady connection."]),
  ("Setup",["Update the system, then install your player app from Google Play on the device. Sign in and test. See {post:iptv-on-android-tv} for the general Android TV checklist."]),
  ("Good habits",[("ul",["Use Ethernet where possible.","Keep storage free by removing unused apps.","Restart now and then.","Check that your TV is set to the correct resolution and refresh rate."])]),
  ("Check support",["Always confirm your exact model and software version with support before subscribing."])])

add("iptv-on-chromecast-with-google-tv", "IPTV on Chromecast with Google TV", D,
 "How Chromecast with Google TV handles IPTV player apps: the Google TV system, storage limits, remote use and Wi-Fi tips.",
 "Chromecast with Google TV is a small streaming device with its own app store and remote, so it behaves like other Android TV style devices.",
 [("Storage is limited",["These devices have modest storage. Remove unused apps and clear caches. A full device is a common cause of slow or crashing apps."]),
  ("Install from the store",["Use the built-in store for your player app. Follow the same steps as in {post:iptv-on-android-tv}."]),
  ("Network tips",["Wi-Fi is usual because many models have no Ethernet port. Place the router close and use 5 GHz. An Ethernet adapter may be available for some models."]),
  ("Heat",["Keep the device where air can flow, not pressed tight behind the television."])])

add("iptv-on-roku", "IPTV on Roku: Compatibility Questions", D,
 "Roku devices use their own system and app channels, so IPTV player availability is limited. Learn how to check and what alternatives exist.",
 "Roku works differently from Android and Apple devices, so you should check compatibility before subscribing.",
 [("A different platform",["Roku apps are called channels and come from the Roku channel store. Availability of IPTV player apps there is limited and can change."]),
  ("What to do",[("ul",["Note your Roku model and software version.","Ask support whether a supported app exists for it.","If not, consider a different streaming stick."])]),
  ("Do not use unofficial methods",["Avoid sideloading or following guides from unknown sources. Ask us to explain any method clearly first."]),
  ("Alternatives",["Fire TV and Android TV sticks are widely supported. See {post:iptv-on-fire-tv}."])])

add("iptv-on-xbox", "IPTV on Xbox: What Is Possible", D,
 "Can you watch IPTV on an Xbox? Learn how app availability, the Microsoft Store and a connected PC change what works on Xbox consoles.",
 "Xbox consoles can run some media apps, but they are not designed as IPTV players, so results depend on app availability.",
 [("App availability",["Look in the Microsoft Store on the console for a player that supports your type of sign-in. Availability changes over time."]),
  ("Be realistic",["A console is a heavy device for a simple job. A streaming stick uses less power and is usually easier."]),
  ("Network",["Consoles have Ethernet ports. A wired connection helps if you do use one."]),
  ("Check first",["Ask support before subscribing. See {post:device-compatibility} for how to describe your device."])])

add("iptv-on-playstation", "IPTV on PlayStation: What Is Possible", D,
 "Whether IPTV works on PlayStation consoles depends on available apps. Learn how to check, what to expect and when another device is simpler.",
 "PlayStation consoles run a limited set of media apps, so you should confirm what is available for your console before you pay.",
 [("What to check",["Search the PlayStation Store for a suitable player. If none is available, the console is not the right device for IPTV."]),
  ("A simpler route",["A streaming stick or Android TV box on another HDMI port is cheap and focused on the task."]),
  ("Network notes",["A wired connection is sensible if you use the console. Avoid downloading games while you watch live television."]),
  ("Related",["Read {post:iptv-on-xbox} for similar notes and the {devices} for our usual supported types."])])

add("iptv-on-android-tv-boxes", "Choosing an Android TV Box for IPTV", D,
 "What to look for in an Android TV box for IPTV: system version, memory, storage, Ethernet, Wi-Fi standards, updates and avoiding poor quality devices.",
 "An Android TV box can be an excellent IPTV device, but quality varies a lot between brands.",
 [("What matters",[("ul",["A recent Android TV or Google TV system with security updates.","At least 2 GB of memory and 16 GB of storage.","An Ethernet port for stable streaming.","Dual band Wi-Fi if you rely on wireless.","Official access to the Google Play store."])]),
  ("Warnings",["Be cautious of unbranded boxes with unclear software and no updates. They can be slow, insecure or unreliable."]),
  ("Test it",["Buy from a seller with a returns policy so that you can test with your service and return it if it falls short."]),
  ("Next",["Read {post:iptv-on-android-tv} and compare with {post:firestick-vs-android-box-for-iptv}."])])

add("iptv-on-chromebook", "IPTV on a Chromebook", D,
 "Chromebooks can run Android apps or use the browser. Learn the options for watching IPTV on a Chromebook and how to check support.",
 "A Chromebook can be a useful low-cost screen for IPTV, subject to which apps your model supports.",
 [("Two routes",["Many Chromebooks can install Android apps from Google Play. Others rely on the browser. Check Settings to see whether Google Play is available."]),
  ("Performance",["Entry level models have modest processors. Choose a lower quality if video stutters and close other tabs."]),
  ("Sound and screen",["Use headphones or external speakers for better sound, and an HDMI adapter to connect to a TV."]),
  ("Next",["See {post:iptv-on-android-phones} for notes on Android apps."])])

add("firestick-vs-android-box-for-iptv", "Fire Stick vs Android TV Box for IPTV", D,
 "Compare Fire TV Sticks and Android TV boxes for IPTV: price, app stores, Ethernet, storage, performance and which suits different homes.",
 "Both are popular, and both can work well. The better one depends on your room, your budget and your network.",
 [("Fire TV Stick",[("ul",["Small, simple and usually inexpensive.","Uses the Amazon Appstore.","Often Wi-Fi only unless you add an adapter.","Limited storage on some models."])]),
  ("Android TV box",[("ul",["Often more storage and a built-in Ethernet port.","Uses Google Play on proper Android TV devices.","Quality varies widely by brand.","Larger and may need its own power adapter."])]),
  ("How to decide",["If your Wi-Fi is strong and you want simplicity, a stick is fine. If you want a cable and more space, a good box may suit you better. Check {post:iptv-on-fire-tv} and {post:iptv-on-android-tv-boxes}."])])

add("iptv-player-comparison-checklist", "IPTV Player Comparison Checklist", P,
 "A checklist for comparing IPTV player apps: device support, sign-in methods, guide quality, favourites, stability, update history and privacy.",
 "Rather than naming a winner, this checklist helps you judge any player app on your own device.",
 [("Compatibility",[("ul",["Is it available for your device from an official store?","Does it support your sign-in method?"])]),
  ("Daily use",[("ul",["Is the guide readable on a TV?","Can you search and favourite channels?","Does it remember your place and settings?"])]),
  ("Reliability",[("ul",["Does it stay stable for a full evening?","Is it updated regularly?","Is it free of intrusive adverts?"])]),
  ("Privacy",["Read what data the app collects. Prefer apps with a clear privacy policy and sensible permissions."]),
  ("Run the same test on each",["Install two candidates, load the same list and watch the same channels for the same time. Notice differences in start time, picture and crashes. See {post:what-is-an-iptv-player-app}."])])

add("parental-controls-in-iptv-apps", "Parental Controls in IPTV Apps", P,
 "How parental controls work in IPTV player apps and on devices: PIN locks, hidden categories, profiles and what no app can guarantee.",
 "If children use your TV, set up controls before they find the channel list.",
 [("In the app",["Many apps allow a PIN to lock channels or categories. Look in Settings for parental control or lock options."]),
  ("On the device",["Streaming devices and smart TVs have their own profiles and PIN protection for app installs and purchases. Use those too."]),
  ("Limits to know",["Channel lists are supplied by the service, and category names may not match what is inside. Controls reduce risk but cannot guarantee that nothing unsuitable appears."]),
  ("Good habits",[("ul",["Use a PIN that children cannot guess.","Keep sign-in details private.","Talk with children about what to do if something upsets them."]),"See also {post:child-safety-and-streaming}."])])

add("favourites-and-categories-in-iptv-apps", "Using Favourites and Categories in IPTV Apps", P,
 "Make a long channel list manageable: use favourites, category filters, search and hidden groups in your IPTV player for faster daily viewing.",
 "A long list is only helpful if you can find what you want in seconds. A few minutes of tidying pays off every day.",
 [("Start with favourites",["Mark the twenty or so channels you use most. Put them at the top so the remote needs fewer presses."]),
  ("Use categories",["Most apps group channels by type. Hide groups you never use so that scrolling is shorter."]),
  ("Use search",["Learn how search works in your app. On some remotes, voice search is quicker than typing."]),
  ("Keep it stable",["If you reinstall the app, favourites may reset, so keep a short list somewhere. See {post:what-is-an-iptv-player-app}."])])

add("catch-up-and-recording-explained", "Catch-Up and Recording in IPTV Explained", P,
 "What catch-up and recording mean in IPTV apps, how they differ, why availability varies by service and what to ask before you subscribe.",
 "Catch-up and recording both let you watch later, but they work in different ways and not every service offers them.",
 [("Catch-up",["Catch-up lets you go back to programmes that have already aired, using material the service stores for a limited time. Whether it is available depends on the service and the channel."]),
  ("Recording",["Recording saves a programme either on the service or on your device. It needs storage and, sometimes, extra features in the app."]),
  ("Do not assume",["Never assume either is included. Ask support, and test during your trial."]),
  ("Storage tips",["If recording is local, make sure there is enough free space and the device stays powered on. See {post:iptv-app-cache-and-storage}."])])

add("subtitles-in-iptv-apps", "Subtitles and Audio Languages in IPTV Apps", P,
 "How to turn on subtitles and change audio tracks in IPTV apps, why options vary by channel and how to fix missing subtitles.",
 "Subtitles and alternative audio are available on many streams, but not all, and the menu differs from app to app.",
 [("Finding the menu",["During playback, open the options menu with the remote and look for subtitles, audio or language settings."]),
  ("Why options vary",["The choices come from the stream itself. If a channel does not carry subtitles or another audio track, the app has nothing to show."]),
  ("Fixing problems",[("ul",["Switch the track off and on again.","Try a different channel to see whether it is a stream issue.","Check text size settings on the app and the TV."])]),
  ("Sound problems",["If audio is missing instead, see {post:iptv-no-audio-or-out-of-sync}."])])

add("iptv-app-cache-and-storage", "Clearing Cache and Storage for IPTV Apps", P,
 "How to clear cache and free storage so that your IPTV app runs smoothly: where to find the settings on Android, Fire TV, Apple devices and Windows.",
 "Apps store temporary data to speed things up, but too much can slow them down or fill your device.",
 [("Cache versus data",["Clearing the cache removes temporary files and is safe. Clearing data resets the app, so you will need to sign in again. Clear the cache first."]),
  ("Where to look",[("ul",["Android and Fire TV: Settings, Applications, choose the app, then Clear cache.","Apple devices: delete and reinstall the app, as there is no separate cache button.","Windows: use the app's own settings or reset option."])]),
  ("Free more space",["Remove apps you no longer use, delete downloads and restart. Aim to keep a couple of gigabytes free."]),
  ("If problems return",["Check {post:iptv-app-keeps-restarting} and consider a device with more storage."])])
