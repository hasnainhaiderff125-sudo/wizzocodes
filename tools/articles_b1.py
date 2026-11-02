# Batch 1 articles. Links: {plans} {devices} {howitworks} {faq} {contact} {post:slug}
# Fields: slug, title, desc, cat, kw (primary), kw2 (secondary list), lead, sections [(h2, [paragraphs or ('ul',[items])])]

A = []
def add(**k): A.append(k)

add(slug="how-iptv-works", cat="IPTV Features & Technology",
 title="How IPTV Works: From Server to Your Screen",
 desc="A clear look at how IPTV delivers television over the internet: streams, servers, players, buffering and what affects picture quality at home.",
 kw="how IPTV works", kw2=["IPTV streaming explained","IPTV technology","how internet TV works"],
 lead="IPTV sends television as data over an internet connection instead of through an aerial, dish or cable. Here is what actually happens between the broadcaster and your screen.",
 sections=[
 ("The journey of a stream",["A live channel starts as a video and audio feed. A provider encodes it into a compressed digital format, then publishes it from servers connected to the internet. When you press play, your player app asks a server for that stream and the server starts sending small chunks of video to your device.","Because the data travels over the same internet connection you use for everything else, the quality you get depends on every step in the chain: the provider's servers, the route across the internet, your router, and your device."]),
 ("Where the player app fits",["The player app is the piece you actually see. It connects to the service, reads the channel list, requests the stream and decodes the video. Different apps have different menus and features, but they all do these same jobs. Our guide to the {post:what-is-an-iptv-player-app} covers what to look for."]),
 ("Why buffering exists",["Your player keeps a few seconds of video stored ahead of what you are watching. That small reserve smooths over brief slowdowns. If your connection cannot keep refilling it, the reserve runs out and playback pauses to catch up. That pause is buffering.","Live television is less forgiving than on-demand video, because the player cannot download far ahead of a live event. This is why a connection that copes with a pre-recorded film can still struggle with live sport."]),
 ("What affects quality at home",[("ul",["Signal strength between your device and the router, which matters most on Wi-Fi.","How many other people and devices are using the connection at the same time.","The age and power of the streaming device itself.","The resolution of the stream: higher quality needs more bandwidth."])]),
 ("What to do with this",["If you are choosing a service, test it on your own device and at the time of day you normally watch. A trial is the most reliable way to see how the whole chain performs in your home. See how to {howitworks} with Wizzo Codes, or read the {post:streaming-internet-requirements} guide."])])

add(slug="iptv-vs-cable-tv", cat="IPTV Comparisons",
 title="IPTV vs Cable TV: Key Differences for UK Viewers",
 desc="IPTV and cable TV both bring you channels, but they work differently. Compare delivery, equipment, flexibility, contracts and what each needs from you.",
 kw="IPTV vs cable TV", kw2=["IPTV or cable","internet TV vs cable","cable TV alternatives UK"],
 lead="Cable television and IPTV can both give you a long list of channels. The real differences are how the signal reaches you, what equipment you need and how much flexibility you get.",
 sections=[
 ("How the signal arrives",["Cable TV sends channels over a dedicated cable network into a set-top box. Your channels are delivered on the provider's own infrastructure, separate from your broadband.","IPTV sends channels over the internet. There is no dedicated line for television: it uses your broadband connection, so the quality of that connection becomes part of your TV quality."]),
 ("Equipment and installation",["Cable usually involves a provider-supplied box and sometimes an engineer visit. IPTV normally runs on a device you may already own, such as a smart TV, a Fire TV Stick, an Android TV box or a phone. The {devices} page lists what we can check for you."]),
 ("Contracts and flexibility",["Cable and bundled TV packages commonly come with minimum terms. IPTV subscriptions are often sold by length, such as one, three, six or twelve months, and some can be started or stopped without hardware changes. Always read the terms of whichever service you consider."]),
 ("Where each one wins",[("ul",["Cable is simpler if you want a managed box with no thought about your own network.","IPTV is more portable: the same subscription can often be used on several kinds of device, subject to the plan.","Cable does not depend on your broadband speed, while IPTV does.","IPTV pricing is usually lower, but you take on more responsibility for your own setup."])]),
 ("Which is right for you",["If your broadband is reliable and you are comfortable setting up an app, IPTV is worth testing. If you want a fully managed service and do not want to think about internet quality, cable may suit you better. Whichever you choose, check that you can legally view what you pay for and that a trial or clear refund policy is available."])])

add(slug="iptv-vs-satellite-tv", cat="IPTV Comparisons",
 title="IPTV vs Satellite TV: Which Suits Your Home?",
 desc="Compare IPTV and satellite TV on installation, weather, equipment, flexibility and reliance on broadband, so you can pick what fits your home.",
 kw="IPTV vs satellite TV", kw2=["IPTV or satellite","satellite TV alternative UK","dish vs internet TV"],
 lead="Satellite television and IPTV solve the same problem in opposite ways. One uses a dish pointed at the sky, the other uses your broadband.",
 sections=[
 ("Installation",["Satellite needs a dish fixed to the outside of the building, cabling into the home and a receiver. That is a physical job and may need landlord or building permission in flats. IPTV needs no installation beyond an app on a compatible device and a good connection."]),
 ("Weather and reliability",["Heavy rain or snow can weaken a satellite signal. IPTV is not affected by weather in the same way, but it is affected by anything that weakens your broadband: congestion, a faulty router, or poor Wi-Fi coverage."]),
 ("Flexibility",["A satellite dish is fixed to one location. IPTV follows the app, so you can often use the same account on a TV at home and on a phone or tablet elsewhere, depending on the plan. Ask support what applies to the plan you choose."]),
 ("Quality and bandwidth",["Satellite delivers its signal without using your internet data. IPTV uses data every hour you watch, which matters if your broadband has a data cap. Our {post:how-much-data-does-iptv-use} guide gives rough figures."]),
 ("A practical way to decide",[("ul",["Poor broadband and a clear view of the sky: satellite may be more dependable.","Good broadband, a rented flat or no wish to drill into walls: IPTV is easier.","Several rooms and several devices: IPTV avoids extra receivers, as long as your Wi-Fi is strong."]),"If you are unsure, compare plans on our {plans} page and request a trial to see how it behaves on your own connection."])])

add(slug="iptv-vs-streaming-apps", cat="IPTV Comparisons",
 title="IPTV vs On-Demand Streaming Apps: What Is the Difference?",
 desc="IPTV mainly delivers live channels, while on-demand apps focus on a library you pick from. Learn how they differ and why many homes use both.",
 kw="IPTV vs streaming services", kw2=["live TV vs on demand","IPTV or Netflix style apps"],
 lead="People often ask whether IPTV replaces on-demand streaming apps. Usually it does not. They do different jobs, and many households use both.",
 sections=[
 ("Live channels versus a library",["IPTV is built around live channels that run to a schedule, much like traditional television, often with a guide that shows what is on now and next. On-demand apps are built around a library you browse and start whenever you like."]),
 ("Where IPTV tends to help",["Live events, news and sport are the main reasons people look at IPTV. These are things you want to watch as they happen, which is exactly what channel-based television does well."]),
 ("Where on-demand tends to help",["Box sets and films that you want to start at a time of your choosing suit a library service. Some IPTV plans also include movies and series, but the experience and catalogue depend on the service."]),
 ("Cost and overlap",["Paying for several overlapping services adds up. Before adding any subscription, list what you actually watch and where you watch it. Choosing by length and plan, as explained in our guide on how to {post:how-to-choose-an-iptv-plan}, helps avoid paying for more than you need."]),
 ("Our view",["Treat IPTV as a way to get live channels, not as a replacement for everything. If most of your viewing is on-demand series, a library app may already cover you."])])

add(slug="what-is-an-iptv-player-app", cat="IPTV Applications",
 title="What Is an IPTV Player App and How Do You Choose One?",
 desc="An IPTV player is the app that plays your channels. Learn what it does, what features matter and what to check before installing one on your device.",
 kw="IPTV player app", kw2=["best IPTV player","IPTV app for smart TV","IPTV player features"],
 lead="An IPTV subscription gives you access to channels. A player app is what lets you watch them. The two are separate, and choosing a suitable app makes daily use much easier.",
 sections=[
 ("What the app does",["The player signs in to your service, loads the channel list, shows a programme guide where one is provided and plays the video. It does not create content. It is simply the window through which you watch."]),
 ("Features worth checking",[("ul",["Support for your device and system version.","Favourites and channel search, which save time with a long list.","A programme guide view that is easy to read on a TV.","Playback controls that work well with a remote.","Stable behaviour: does it crash or restart often?","Clear privacy information from the app developer."])]),
 ("Where to get it",["Install apps from your device's official store where possible. If your device needs another method, ask support to explain the steps before you start rather than downloading from unknown websites. Our {post:iptv-scams-and-safe-payment} guide explains what to watch for."]),
 ("Test before you commit",["Whichever app you pick, test it with a trial. Check that channels load quickly, that the guide displays, and that the app stays stable for a full evening. Your device guides, such as {post:iptv-on-android-tv} or {post:iptv-on-fire-tv}, list what to check on each platform."])])

add(slug="m3u-playlist-explained", cat="IPTV Features & Technology",
 title="M3U Playlists Explained for IPTV Beginners",
 desc="What an M3U playlist is, how IPTV apps use it to list channels, and what to keep private when you receive a playlist link from a provider.",
 kw="M3U playlist IPTV", kw2=["what is M3U","M3U URL explained","IPTV playlist"],
 lead="If you have heard the term M3U in connection with IPTV, it refers to a simple playlist format. Understanding it helps you set up an app and keep your details safe.",
 sections=[
 ("What an M3U file is",["An M3U file is a plain text list. Each entry points to a stream and carries a name, and sometimes a group and a logo. A player reads the list and shows the entries as channels. It is the same basic idea as a music playlist, but for video streams."]),
 ("M3U links versus files",["Some services give you a web link to a playlist rather than a file. The player downloads the list from that link when you add it, and can refresh it later so the channel list stays current."]),
 ("Keep it private",["A playlist link can contain details tied to your account. Do not post it publicly or share it in screenshots. If you think it has been exposed, ask your provider how to reset your access."]),
 ("Common problems",[("ul",["A typo when entering the link: copy and paste instead of typing.","An old link after the provider has changed details: ask for the current one.","A very large list loading slowly on an older device."]),"If you are not sure which sign-in method suits your app, see {post:xtream-codes-login-explained} and our {post:what-is-an-iptv-player-app} guide."])])

add(slug="xtream-codes-login-explained", cat="IPTV Features & Technology",
 title="Xtream Codes Login Explained: Username, Password and Server",
 desc="Many IPTV apps offer an Xtream Codes style login. Learn what the server address, username and password fields mean and how to avoid common mistakes.",
 kw="Xtream Codes login", kw2=["Xtream codes IPTV","IPTV username password server","IPTV app login"],
 lead="Some player apps offer a login that asks for a server address, a username and a password. It is often called an Xtream Codes style login, and it is usually quicker than adding a playlist file.",
 sections=[
 ("The three fields",["The server address tells the app where to connect. The username and password identify your subscription. Your provider supplies all three. Enter them exactly as given, including any numbers in the address and any capital letters."]),
 ("Why apps offer it",["With this method the app can load the channel list, guide and categories itself, which can feel tidier than a single large playlist. Not every app supports it, and not every service uses it, so check which method your provider recommends."]),
 ("Typical mistakes",[("ul",["Adding a space at the start or end when pasting.","Leaving out the port number when the address includes one.","Mixing up a lowercase l with a capital I or the number 1.","Entering details in the wrong field."])]),
 ("Security",["Treat these details like a password. Do not share them in public groups. After subscribing, we send sign-in details privately on WhatsApp; see {howitworks} for the full process."])])

add(slug="what-is-epg-tv-guide", cat="IPTV Features & Technology",
 title="What Is an EPG? The IPTV TV Guide Explained",
 desc="The EPG is the on-screen programme guide in an IPTV app. Learn how it works, why it sometimes shows the wrong times and how to fix common issues.",
 kw="IPTV EPG", kw2=["electronic programme guide","IPTV TV guide","EPG not working"],
 lead="EPG stands for electronic programme guide. It is the grid that shows what is on now and what is coming next, similar to the guide on a traditional set-top box.",
 sections=[
 ("Where the data comes from",["The guide is not part of the video stream. It is a separate data feed that the player loads and matches to each channel. When the match is wrong or the feed is delayed, you see gaps or the wrong titles."]),
 ("Why times can be wrong",["Time zones are the most common cause. If your device or app is set to the wrong zone, every programme appears shifted. Check that your device is set to UK time and that automatic time is turned on."]),
 ("Fixing a missing guide",[("ul",["Refresh the guide or playlist inside the app.","Restart the app and then the device.","Make sure the app has time to download the data after first sign-in.","Free storage if the device is full, as the guide needs space to save data."]),"If the problem remains, message support with the app name and a description of what you see."]),
 ("Why it is worth having",["A working guide makes a large channel list far easier to use, especially for live sport where start times matter. See also {post:iptv-for-live-sports-tips} for how to prepare for match days."])])

add(slug="iptv-on-apple-tv", cat="IPTV Devices",
 title="IPTV on Apple TV: What to Check Before You Subscribe",
 desc="How to prepare an Apple TV for an IPTV player app: checking the model and tvOS version, installing from the App Store and testing your connection.",
 kw="IPTV on Apple TV", kw2=["IPTV app Apple TV","Apple TV 4K IPTV","tvOS IPTV player"],
 lead="Apple TV boxes are fast and have a clean interface, which makes them a good fit for many IPTV player apps, provided your model is recent enough.",
 sections=[
 ("Identify your model",["Open Settings, then General, then About. Note the model and the tvOS version. Older boxes may not be supported by current apps, so send these details to support before you pay."]),
 ("Use the App Store",["Player apps for Apple TV are installed from the App Store. Search by app name, check that it lists Apple TV as supported and look at its update date, which tells you whether it is maintained."]),
 ("Network tips",["If you can, use an Ethernet cable. Some Apple TV models have an Ethernet port, so check yours, because a wired connection avoids many Wi-Fi problems. If you must use Wi-Fi, place the router within clear range."]),
 ("Sign in and test",["After subscribing you receive sign-in details privately. Enter them carefully, then test live channels for a full evening before relying on the service. If you meet problems, follow {post:streaming-buffering-troubleshooting}.","You can also confirm your device on our {devices} page, or ask for a trial."])])

add(slug="iptv-on-iphone-and-ipad", cat="IPTV Devices",
 title="IPTV on iPhone and iPad: Setup Tips and Common Issues",
 desc="Prepare an iPhone or iPad for an IPTV player app: iOS updates, storage, mobile data use, Wi-Fi tips and how to sign in safely.",
 kw="IPTV on iPhone", kw2=["IPTV iPad","iOS IPTV player","watch IPTV on iPhone"],
 lead="Phones and tablets are handy for watching away from the living room. A few checks beforehand make the experience smoother.",
 sections=[
 ("Update iOS first",["Open Settings, then General, then Software Update. Current apps usually need a recent iOS version. If your device cannot update far enough, check with support before subscribing."]),
 ("Storage and battery",["Video apps cache data and can use a lot of battery. Keep at least a couple of gigabytes free and plug in for longer sessions."]),
 ("Mobile data warning",["Live video on mobile data can use a lot of your allowance. On Wi-Fi it uses your broadband instead. Check your plan limits and see {post:how-much-data-does-iptv-use} for rough estimates."]),
 ("Screen and sound",["Use the app's own full-screen option and check that the silent switch is not muting audio. For bigger screens, you can mirror to a compatible TV, though performance varies."]),
 ("Next steps",["Look at {post:iptv-on-phones-tablets-computers} for general phone and tablet advice, or contact support on WhatsApp with your device model."])])

add(slug="iptv-on-windows-pc", cat="IPTV Devices",
 title="IPTV on a Windows PC: Player Options and Setup Checklist",
 desc="A checklist for watching IPTV on Windows: choosing a player, checking system updates, graphics drivers, network settings and keeping your login safe.",
 kw="IPTV on Windows", kw2=["IPTV player Windows 11","IPTV on PC","watch IPTV on laptop"],
 lead="A Windows computer can be a flexible way to watch IPTV, especially if you already use a laptop or a PC connected to a TV.",
 sections=[
 ("Choose a player carefully",["Pick an app from a source you trust, such as the Microsoft Store or the developer's own site, and read recent reviews. Avoid downloading installers from unknown pages, as fake player downloads are a common way to spread unwanted software."]),
 ("Keep Windows ready",[("ul",["Install pending Windows updates.","Update your graphics driver for smooth video decoding.","Close heavy background programs while watching.","Use a wired connection if your PC has a network port."])]),
 ("Sound and display",["If you connect to a TV over HDMI, check which audio output Windows is using. Many sound problems on PC are simply the wrong output selected."]),
 ("Security habits",["Do not store your sign-in details in unprotected notes. If a player asks for permissions that seem unrelated to video, close it and choose another."]),
 ("Related reading",["See {post:iptv-on-mac} for Apple computers, and {post:iptv-wifi-vs-ethernet} for network choices."])])

add(slug="iptv-on-mac", cat="IPTV Devices",
 title="IPTV on a Mac: Setting Up a Player App",
 desc="How to watch IPTV on macOS: choosing a player app, checking system requirements, handling downloads safely and fixing common playback problems.",
 kw="IPTV on Mac", kw2=["IPTV player macOS","IPTV MacBook","watch IPTV on Mac"],
 lead="Macs handle video well, so IPTV playback is mostly about choosing a suitable app and keeping the system tidy.",
 sections=[
 ("Check your macOS version",["Click the Apple menu, then About This Mac. Note the version. Some player apps require a fairly recent macOS, so check the app's listing before you subscribe."]),
 ("Where to download",["The Mac App Store is the safest source. If an app is distributed outside the store, macOS may show a security prompt. Only continue if you are certain of the source."]),
 ("Everyday tips",[("ul",["Keep the Mac plugged in for long sessions.","Close browser tabs that stream other video.","Use Ethernet through an adapter if Wi-Fi is weak.","Restart the app if the guide stops updating."])]),
 ("When something goes wrong",["Start with {post:streaming-buffering-troubleshooting}, and if you are choosing between a computer and a TV device, our {devices} page can help you decide."])])

add(slug="iptv-on-android-phones", cat="IPTV Devices",
 title="IPTV on Android Phones and Tablets: A Practical Guide",
 desc="Prepare an Android phone or tablet for IPTV: update the system, manage storage, choose a player from Google Play and keep battery and data use under control.",
 kw="IPTV on Android phone", kw2=["IPTV Android tablet","Android IPTV player","watch IPTV on Android"],
 lead="Android phones and tablets are popular for IPTV because the choice of player apps is wide. That freedom also means it is worth being careful about what you install.",
 sections=[
 ("Update and free space",["Open Settings, then System, then Software update. Then check storage and remove apps you do not use. Low storage is a frequent cause of crashes."]),
 ("Choose from Google Play",["Install from Google Play where possible. Check the developer name, the number of downloads and recent reviews, and read the permissions the app asks for."]),
 ("Battery and heat",["Long streaming sessions warm a phone. Remove thick cases if it gets very hot and avoid charging on a bed or cushion."]),
 ("Wi-Fi or mobile data",["Wi-Fi is better for long viewing. If you do use mobile data, lower the video quality inside the app, if it offers the option, to protect your allowance.","For TVs and set-top devices, see {post:iptv-on-android-tv}."])])

add(slug="iptv-wifi-vs-ethernet", cat="IPTV Streaming Quality",
 title="Wi-Fi or Ethernet for IPTV? Which Gives a Steadier Stream",
 desc="Compare Wi-Fi and Ethernet for IPTV streaming. Learn when a cable is worth it, how to improve Wi-Fi and what powerline or mesh adapters can and cannot do.",
 kw="Ethernet vs Wi-Fi for IPTV", kw2=["IPTV wired connection","improve Wi-Fi for streaming","powerline adapter IPTV"],
 lead="For live television a steady connection matters more than a headline speed. That is why a cable is often the simplest fix for a streaming problem.",
 sections=[
 ("Why Ethernet is steadier",["A cable is not affected by walls, microwaves or neighbouring networks. It gives a more consistent connection, which is exactly what live video needs. If your TV box has an Ethernet port and the router is close, use it."]),
 ("Making Wi-Fi better",[("ul",["Move the router out of cupboards and off the floor.","Place it near the room where you watch most.","Use the 5 GHz band for devices close to the router.","Reduce the number of devices doing large downloads while you watch."])]),
 ("Mesh and powerline options",["If running a cable is not possible, a mesh Wi-Fi system can extend coverage. Powerline adapters send the connection through your home wiring, and results depend on the age and quality of that wiring. Neither is guaranteed, so test before you commit."]),
 ("How to test",["Watch a busy live channel at your usual time and note whether it stutters. Our {post:improve-wifi-for-streaming} guide goes deeper into router settings."])])

add(slug="improve-wifi-for-streaming", cat="IPTV Troubleshooting",
 title="How to Improve Home Wi-Fi for Smoother IPTV Streaming",
 desc="Practical Wi-Fi fixes for IPTV: router placement, channels and bands, restarting correctly and spotting what is slowing your stream.",
 kw="improve Wi-Fi for streaming", kw2=["Wi-Fi buffering fix","router placement streaming","5GHz streaming"],
 lead="Most IPTV complaints about freezing come down to the home network rather than the service. These steps fix a large share of them.",
 sections=[
 ("Start with placement",["Wi-Fi weakens through walls and floors. Keep the router in an open area, ideally on a shelf in a central room, and away from other electronics and metal objects."]),
 ("Choose the right band",["Most routers offer two bands. 2.4 GHz travels further but is crowded. 5 GHz is faster and cleaner at shorter range. Put your streaming device on 5 GHz if it is in the same room or the next one."]),
 ("Restart properly",["Power the router off for about thirty seconds, then back on. Do the same for your streaming device. This clears many temporary faults."]),
 ("Find what is competing",[("ul",["Game or console downloads.","Cloud backups on phones and laptops.","Several people on video calls.","Smart cameras uploading footage."]),"Pause large transfers while you watch live events."]),
 ("When to contact your internet provider",["If speed tests are far below what you pay for, contact your broadband provider. If the network is fine but the stream still struggles, see {post:iptv-freezing-at-peak-times}."])])

add(slug="iptv-freezing-at-peak-times", cat="IPTV Troubleshooting",
 title="Why IPTV Freezes in the Evening and What You Can Do",
 desc="Streams that run well in the morning but freeze in the evening point to congestion. Learn the likely causes and practical ways to reduce the problem.",
 kw="IPTV freezing evening", kw2=["IPTV buffering peak time","streaming slow in evenings","IPTV lag at night"],
 lead="If your TV is fine at lunchtime and struggles at eight in the evening, the pattern itself tells you something useful.",
 sections=[
 ("Why evenings are harder",["Many households stream, game and browse at once in the evening. Local network capacity can be shared among many customers, so speeds may drop at busy times. Inside your own home, more devices are also active."]),
 ("Look at your own network first",["Count how many devices are online during your usual viewing time. Pause large downloads and video calls on other devices and see whether the stream improves."]),
 ("Try a cable",["A wired connection removes Wi-Fi from the picture. If the problem disappears, your Wi-Fi was the weak point. See {post:iptv-wifi-vs-ethernet}."]),
 ("Keep a simple log",[("ul",["Note the time and the channel when it freezes.","Note whether other apps also slow down.","Run a speed test at that moment, not just earlier in the day."]),"This information helps your broadband provider and our support team identify the cause quickly."]),
 ("What support can check",["If the problem is limited to certain channels, tell us which ones. We can check whether it relates to the stream or to your connection, and suggest next steps over WhatsApp."])])

add(slug="iptv-no-audio-or-out-of-sync", cat="IPTV Troubleshooting",
 title="IPTV Has No Sound or Audio Out of Sync: How to Fix It",
 desc="Fix silent channels and lip-sync problems in IPTV apps: audio tracks, output settings, HDMI and soundbars, and when the stream itself is the cause.",
 kw="IPTV no sound", kw2=["IPTV audio out of sync","IPTV sound problem","lip sync IPTV fix"],
 lead="Video that works with no sound, or sound that drifts from the picture, is annoying but usually easy to trace.",
 sections=[
 ("Start with the simple checks",["Confirm the TV and the app are not muted, and try another channel. If other channels have sound, the issue is with one stream, not your device."]),
 ("Check the audio track",["Many apps let you pick the audio track or format. Switch between options if there are more than one. Some formats are not supported by every soundbar or TV."]),
 ("Look at HDMI and soundbars",["If you use a soundbar or AV receiver, try connecting the streaming device directly to the TV to see whether the problem disappears. Then reconnect through the soundbar and check its input and format settings."]),
 ("Out of sync",[("ul",["Restart the app and try the channel again.","Check whether the problem happens on one channel or all.","Look for an audio delay setting in the app or the TV.","Lower the picture quality if your device is struggling to decode video."])]),
 ("When to ask for help",["If one channel is silent or drifting while others are fine, tell support the channel name and the time. See also {post:streaming-buffering-troubleshooting}."])])

add(slug="iptv-channels-not-loading", cat="IPTV Troubleshooting",
 title="IPTV Channels Not Loading: A Step-by-Step Checklist",
 desc="When IPTV channels will not load, work through this checklist: connection, app, sign-in details, storage and device restarts, before contacting support.",
 kw="IPTV channels not loading", kw2=["IPTV not working","IPTV black screen","IPTV loading forever"],
 lead="A black screen or endless spinner has a short list of usual causes. Working through them in order saves time.",
 sections=[
 ("1. Check your internet",["Open a web page or another app on the same device. If nothing loads, the problem is the connection, not the IPTV service. Restart the router and try again."]),
 ("2. Check your sign-in details",["Confirm that the details match what was sent to you. An extra space or a changed password is a common culprit. If your access has expired, the app may load an empty list."]),
 ("3. Restart and update",["Close the app fully, restart the device and check for an app update. Out-of-date apps can stop working after system updates."]),
 ("4. Free some space",["Low storage can stop an app from saving its channel list. Remove unused apps and clear the app's cache if your device allows it."]),
 ("5. Try another device",["If a phone works but the TV does not, the problem is the TV app or its network, not your subscription."]),
 ("6. Contact support",["Send us the device model, the app name and what you see on screen. A screenshot helps. Our {faq} page covers other common questions."])])

add(slug="hd-vs-4k-iptv-streaming", cat="IPTV Streaming Quality",
 title="HD vs 4K IPTV Streaming: What You Really Need",
 desc="Understand the difference between SD, HD, Full HD and 4K for IPTV, what your screen and connection need, and when higher quality is worth it.",
 kw="4K IPTV streaming", kw2=["HD vs 4K IPTV","IPTV picture quality","IPTV resolution"],
 lead="Higher resolution looks sharper, but it also asks more from your connection, your device and your screen. It is not always the better choice.",
 sections=[
 ("What the terms mean",["SD is the lowest common resolution. HD is usually 720p, and Full HD is 1080p. 4K, also called Ultra HD, has four times as many pixels as Full HD. More pixels need more data per second."]),
 ("Is your screen able to show it?",["A 4K stream on a Full HD television will not look sharper. Check your TV's specification before assuming you need 4K. Distance matters too: on a small screen across a room, the difference can be hard to see."]),
 ("Does your connection allow it?",["4K needs a much faster and steadier connection than HD, and live channels need stability more than any other type of video. If your connection is borderline, an HD stream that never stops is better than a 4K stream that pauses."]),
 ("Device limits",["Older streaming sticks may struggle with 4K decoding. Check that your device supports the format and that the app does too."]),
 ("Our advice",["Match quality to your equipment and test on your own connection with a trial. Read {post:streaming-internet-requirements} for connection guidance."])])

add(slug="how-much-data-does-iptv-use", cat="IPTV Streaming Quality",
 title="How Much Data Does IPTV Use? Rough Figures by Quality",
 desc="Estimate how much data IPTV streaming uses per hour at different qualities, and how to stay within a data cap or mobile allowance.",
 kw="how much data does IPTV use", kw2=["IPTV data usage per hour","streaming data cap","IPTV mobile data"],
 lead="Live video uses data continuously. Exact usage depends on the stream, but a rough guide helps you plan.",
 sections=[
 ("Rough figures",["As a rough guide, standard definition video can use around one gigabyte per hour, HD around two to three gigabytes per hour and 4K around seven gigabytes per hour or more. Real figures vary by channel and app, so treat these as estimates, not promises."]),
 ("An example",["If you watch three hours of HD each evening at about three gigabytes per hour, that is roughly nine gigabytes a day, or around 270 gigabytes in a month from one screen. Several screens at once multiply this."]),
 ("Do you have a cap?",["Many UK broadband plans are unlimited, but some are not, and mobile data almost always has a limit. Check your provider's terms before streaming heavily."]),
 ("Ways to reduce usage",[("ul",["Choose a lower quality setting when you do not need 4K.","Use Wi-Fi rather than mobile data on phones.","Close the app when you are not watching, so it does not keep streaming in the background."])]),
 ("Related",["For speed advice see {post:streaming-internet-requirements}, and for resolution see {post:hd-vs-4k-iptv-streaming}."])])

add(slug="iptv-subscription-length-guide", cat="IPTV Subscription Guides",
 title="1, 3, 6 or 12 Months? How to Pick an IPTV Subscription Length",
 desc="Compare one, three, six and twelve month IPTV subscriptions using real Wizzo Codes prices, and learn who benefits from short and long terms.",
 kw="IPTV subscription length", kw2=["IPTV 12 month subscription","cheap IPTV UK","IPTV plan duration"],
 lead="Longer subscriptions usually cost less per month, but only if you will actually use them. Here is how to think it through, using our own published prices.",
 sections=[
 ("What our prices show",["Our prices are totals for the length you choose, in pounds sterling. For example, Basic costs £4 for one month and £30 for twelve months, which works out at £2.50 a month over the year. Premium costs £8 for one month and £58 for twelve months, about £4.83 a month. See all four plans on the {plans} page."]),
 ("Who suits one month",["A single month suits anyone testing a service on their own device after a trial, or someone who needs it for a short period, such as a season of sport."]),
 ("Who suits three or six months",["These sit in the middle: a lower monthly cost than a single month without a year-long commitment. They work well once you have confirmed that your device and connection are happy."]),
 ("Who suits twelve months",["If you watch most weeks and your setup is stable, twelve months gives the lowest monthly cost. Read the refund policy first so you know what happens if something goes wrong."]),
 ("Before you pay",["Request a trial, confirm your device works and ask support anything you are unsure about. Our guide to how to {post:how-to-choose-an-iptv-plan} explains the other differences between plans."])])

add(slug="iptv-free-trial-what-to-test", cat="IPTV Subscription Guides",
 title="IPTV Free Trial: What to Test Before You Subscribe",
 desc="A free trial is only useful if you test the right things. Use this checklist for devices, live channels, evening performance, the guide and support.",
 kw="IPTV free trial", kw2=["IPTV trial UK","test IPTV before buying","IPTV trial checklist"],
 lead="A trial is your best protection as a customer. These are the things worth checking before you pay for any IPTV service, including ours.",
 sections=[
 ("Test on the device you will really use",["Do not rely on a result from a different device. Install the player on the TV or stick you plan to use and check that it runs smoothly with your remote."]),
 ("Test at busy times",["Watch in the evening, not just at lunchtime. Evening performance tells you far more about how your connection and the service cope together."]),
 ("Test the channels you care about",[("ul",["Pick the channels you will watch most and check that they load quickly.","Watch live content for at least an hour to look for pauses.","Try changing channels several times in a row.","Open the programme guide and check that it shows the right times."])]),
 ("Test support",["Ask a real question over WhatsApp and see how quickly and clearly you get an answer. Support quality matters most when something goes wrong."]),
 ("Then decide",["If everything works, choose a plan and length on the {plans} page. If not, you have lost nothing. You can request a trial through {contact}."])])

add(slug="iptv-scams-and-safe-payment", cat="IPTV Security & Privacy",
 title="How to Spot IPTV Scams and Pay Safely",
 desc="Warning signs of IPTV scams, how to check a seller before paying and how to protect your payment details and login. Practical advice for UK buyers.",
 kw="IPTV scams", kw2=["safe IPTV payment","IPTV seller red flags","avoid IPTV fraud"],
 lead="Where there is demand, there are also people trying to take advantage of buyers. A few habits protect you.",
 sections=[
 ("Warning signs",[("ul",["Prices that look far too good to be true.","Pressure to pay immediately, with no trial offered.","No clear contact details, refund policy or terms.","Requests for payment methods that cannot be traced or questioned.","Claims of official partnerships with broadcasters that the seller cannot support."])]),
 ("Check before you pay",["Read the terms and the refund policy. Ask a few specific questions and see whether the answers are clear. Test on a trial first. Look for consistent business details across the website and the messaging you receive."]),
 ("Payment habits",["Use payment methods you understand and keep the receipt or screenshot. Never share full card details or banking passwords over a messaging app. We list our accepted methods, PayPal, Binance Pay and Wise, on the site."]),
 ("Protect your login",["Use a unique password where one is chosen by you, do not share your sign-in details publicly and be cautious of links sent by people you do not know."]),
 ("Legal and fair use",["You are responsible for having the right to view the content you choose to watch in the United Kingdom. Read more in {post:streaming-safety-and-privacy}."])])

add(slug="should-you-use-a-vpn-with-iptv", cat="IPTV Security & Privacy",
 title="Should You Use a VPN With IPTV? Pros, Cons and Limits",
 desc="A balanced look at VPNs and IPTV: what a VPN does for privacy, how it can affect speed and stability, and what it cannot change.",
 kw="VPN with IPTV", kw2=["IPTV VPN UK","does IPTV need a VPN","VPN streaming speed"],
 lead="A VPN is often mentioned alongside IPTV. It can be useful for privacy, but it is not required for the service to work and it does have trade-offs.",
 sections=[
 ("What a VPN does",["A VPN sends your internet traffic through an encrypted tunnel to a server run by the VPN company. Websites and services see that server's address instead of yours, and your internet provider sees encrypted traffic instead of the sites you visit."]),
 ("Possible benefits",[("ul",["More privacy on public or shared networks.","Less visibility of your browsing to your internet provider."])]),
 ("Possible drawbacks",[("ul",["Added distance can reduce speed and increase delay.","Some devices, especially older TV sticks, handle VPN apps poorly.","Free VPNs may limit speed or collect data, so read their privacy terms.","Some services restrict VPN connections, so check the terms of your provider."])]),
 ("What a VPN cannot do",["A VPN does not change the legal position of what you watch. You remain responsible for viewing only content you have the right to view."]),
 ("Our suggestion",["Start without a VPN, test the service and add one only if you have a clear reason. If you do, test again at your usual viewing time to make sure speed is still comfortable."])])

add(slug="iptv-for-live-sports-tips", cat="IPTV Sports",
 title="Watching Live Sport on IPTV: Preparation Tips for Match Days",
 desc="Get ready for live sport on IPTV: test your connection, set up the guide, reduce delay and avoid the problems that appear when everyone streams at once.",
 kw="IPTV for live sports", kw2=["IPTV sports streaming tips","watch football on IPTV","live sport buffering"],
 lead="Live sport is the hardest test for any streaming setup. Big events put pressure on both the service and your home network, so a little preparation pays off.",
 sections=[
 ("Test before the event",["Do not wait until kick-off to find a problem. A day or two before, watch a live channel at the same time of day as your event and check that playback is steady."]),
 ("Prepare your network",[("ul",["Use a cable if you can.","Pause large downloads and backups on other devices.","Place the router and streaming device in a clear line.","Restart the router and the device a few hours beforehand."])]),
 ("Know what to expect",["Live streams over the internet are usually a little behind a broadcast. You may see social media alerts before the action reaches your screen. That delay is normal for internet delivery."]),
 ("Rights and channel availability",["Which events are shown, and by whom, differs by region and changes season to season. Do not assume any particular event is included in a plan. Ask support about specific channels and confirm during your trial."]),
 ("Have a backup plan",["Keep a second device ready, such as a phone on mobile data, so that you can switch if your main setup has a problem. See {post:iptv-freezing-at-peak-times} for evening congestion."])])

add(slug="iptv-uk-broadband-guide", cat="IPTV UK Guides",
 title="UK Broadband for IPTV: Full Fibre, FTTC and Cable Compared",
 desc="Which UK broadband types suit IPTV? Compare full fibre, FTTC and cable for stability, upload and evening performance, and how to check what you have.",
 kw="UK broadband for IPTV", kw2=["best broadband for streaming UK","full fibre vs FTTC","broadband speed for streaming"],
 lead="Your broadband type affects how steady your television feels. Here is how the main UK options compare for streaming.",
 sections=[
 ("Full fibre (FTTP)",["Fibre runs all the way to your home. It is usually the most consistent option and tends to cope well with several screens at once."]),
 ("Fibre to the cabinet (FTTC)",["The fibre stops at the street cabinet and copper completes the journey. Speeds depend on how far you are from the cabinet. Many homes get a perfectly comfortable HD experience, but long lines can be slower."]),
 ("Cable",["Cable networks can offer high speeds, though capacity is shared locally, so busy evenings can sometimes show more variation."]),
 ("Mobile and fixed wireless",["These can work, but performance varies with signal and local demand. Test carefully, including at peak times, before relying on it for live television."]),
 ("How to check yours",["Your broadband bill or provider account usually states the type. Run speed tests at different times and look at the consistency, not only the top number. For targets, see {post:streaming-internet-requirements}."])])

add(slug="uk-tv-licence-and-iptv", cat="IPTV UK Guides",
 title="TV Licence and IPTV in the UK: What You Should Check",
 desc="A plain guide to why the UK TV Licence may apply when you watch live television over the internet, and where to check the official rules.",
 kw="TV Licence IPTV UK", kw2=["do I need a TV licence for IPTV","watch live TV online licence","UK TV licence rules"],
 lead="If you live in the UK and watch live television, the TV Licence may apply regardless of how the programmes reach you. This is general information, not legal advice.",
 sections=[
 ("Why it matters",["In the UK, a TV Licence is generally required to watch or record programmes as they are being broadcast, and to watch BBC iPlayer. This applies to many internet-delivered services, not only aerials and dishes."]),
 ("It is separate from your IPTV subscription",["A subscription to any IPTV provider does not include a TV Licence. The licence is a separate legal requirement run by TV Licensing."]),
 ("Check the official source",["Rules can change and have exceptions. Read the current guidance on the official TV Licensing website and, if you are unsure, contact them directly."]),
 ("Our position",["Wizzo Codes is an independent service and not affiliated with any broadcaster, league or device maker. We cannot give legal advice. For other points about responsible use, read {post:iptv-scams-and-safe-payment}."])])

add(slug="how-many-devices-can-i-use-with-iptv", cat="IPTV FAQs",
 title="How Many Devices Can You Use With One IPTV Subscription?",
 desc="How device limits work on IPTV subscriptions, why simultaneous streams matter and what to ask a provider before you plan to watch on several screens.",
 kw="IPTV multiple devices", kw2=["IPTV simultaneous streams","IPTV connections","use IPTV on two TVs"],
 lead="The answer depends on the plan, so it is worth asking before you subscribe. This guide explains the terms so that you ask the right question.",
 sections=[
 ("Devices versus connections",["A device is a piece of hardware, such as a TV or a phone. A connection, or simultaneous stream, is how many of them can be watching at the same moment. A plan may allow you to sign in on many devices but only stream on a limited number at once."]),
 ("Why it matters",["If two people want to watch different channels at the same time, you need two connections. Asking only how many devices you can install on is not enough."]),
 ("Questions to ask",[("ul",["How many streams can run at the same time?","Can I use the same account on a phone and a TV?","What happens if I try to use one more than allowed?","Can I upgrade later if I need more?"])]),
 ("Bandwidth also counts",["Each stream uses data. Two HD streams need roughly double the connection. See {post:how-much-data-does-iptv-use}."]),
 ("Ask us",["Message us on WhatsApp through {contact} and we will confirm the details for the plan you are considering before you pay."])])

add(slug="iptv-in-canada-what-to-know", cat="IPTV Canada Guides",
 title="IPTV in Canada: What Canadian Viewers Should Know",
 desc="A practical guide for Canadian viewers considering IPTV: connection quality, devices, payment checks and what to confirm before subscribing to any provider.",
 kw="IPTV in Canada", kw2=["IPTV subscription Canada","IPTV setup Canada","IPTV for Canadian viewers"],
 lead="Canadian viewers search for IPTV for many of the same reasons as UK viewers. This guide covers the general points worth checking. Wizzo Codes serves viewers in Canada as well as the UK, where our main market is, and a trial lets you test on your own connection first.",
 sections=[
 ("Start with your connection",["Canadian broadband varies widely between cities and rural areas. Test your speed and stability at different times of day. For live television, stability matters more than the headline figure."]),
 ("Check your devices",["Smart TVs, Fire TV, Android TV and Apple TV are all common in Canadian homes. Confirm your model and system version before subscribing. Our {devices} page lists the types we check."]),
 ("Understand what you are buying",[("ul",["Ask what channels and regions are covered and do not assume.","Ask about trials and refund terms in writing.","Check how support is provided and what hours it covers.","Confirm the currency of the price and which payment methods are accepted."])]),
 ("Responsible use",["You are responsible for ensuring that what you watch is lawful for you to view where you live. Rules and licensing in Canada differ from those in the UK, so check the position for yourself."]),
 ("Ask before you pay",["If you are in Canada and interested in our service, message us on WhatsApp through {contact} and ask what is possible for your location and device. We will tell you plainly."])])
