A = []
def add(slug, title, cat, desc, lead, sections, kw=None, kw2=None):
    A.append(dict(slug=slug, title=title, cat=cat, desc=desc, lead=lead, sections=sections,
                  kw=kw or title.split(':')[0].lower(), kw2=kw2 or []))

T = "IPTV Troubleshooting"; SP = "IPTV Sports"; F = "IPTV Features & Technology"; SU = "IPTV Subscription Guides"

add("iptv-error-messages-explained", "IPTV Error Messages Explained", T,
 "Common IPTV error messages decoded: connection failed, invalid login, stream not found, timeout and unsupported format, and what to try for each.",
 "Error messages look alarming but each one points in a direction. Here is what the common ones usually mean.",
 [("Connection or network errors",["Messages such as connection failed or timeout mean the app could not reach the server. Check your internet, then restart the router and the device."]),
  ("Invalid login or authentication",["The app does not accept your details. Check every character, remove stray spaces and confirm your subscription is active. See {post:iptv-wont-sign-in}."]),
  ("Stream not found or unavailable",["One channel is not responding. Try another channel. If only that one fails, tell support the name and time."]),
  ("Unsupported format",["Your device cannot decode that video format. Try another player, update the app or choose a lower quality if one is offered."]),
  ("What to send support",["The exact wording of the message, a screenshot, the device and app name, and when it began."])])

add("iptv-wont-sign-in", "IPTV Will Not Sign In: Causes and Fixes", T,
 "When your IPTV app refuses to sign in, work through typing mistakes, expired access, wrong server details, device time and stream limits.",
 "Sign-in failures almost always come from a small mismatch. Check these in order.",
 [("Typing and spaces",["Copy and paste the details instead of typing. Check for a space at the start or end, and for letters that look alike such as l and I."]),
  ("Subscription status",["If your period has ended, the app will fail like a wrong password. Check the date you subscribed and the length you chose."]),
  ("Server address and port",["If the app asks for a server address, enter it exactly, including any port number after a colon."]),
  ("Device date and time",["Wrong time or date can block secure connections. Turn on automatic time."]),
  ("Too many streams",["If your plan allows a limited number of simultaneous streams and they are in use, a new sign-in may fail. Close the app on other devices and try again. See {post:how-many-devices-can-i-use-with-iptv}."]),
  ("Still stuck",["Message us on WhatsApp with the app name and what the screen says. Never post your password in a public place."])])

add("iptv-app-keeps-restarting", "IPTV App Keeps Restarting or Closing", T,
 "If your IPTV app crashes or closes by itself, check device storage, memory, updates, large lists and overheating before reinstalling.",
 "An app that closes on its own is usually short of memory or storage, or out of date.",
 [("Storage and memory",["Free space and close other apps. Low-end sticks have little memory, and a very large channel list can push them over the edge."]),
  ("Updates",["Update the app and the device system. Developers often fix crashes in new versions."]),
  ("Large lists",["Remove duplicate lists and unused categories. A smaller list loads faster and uses less memory."]),
  ("Heat",["Overheating can make devices restart. Make sure the device has airflow."]),
  ("Reinstall",["If nothing helps, reinstall using {post:reinstall-iptv-app}, and consider a more powerful device if crashes continue."])])

add("iptv-picture-pixelated", "IPTV Picture Pixelated or Blocky: What to Check", T,
 "Blocky or pixelated IPTV pictures usually mean the stream is starved of data or your device is struggling. Learn the checks that find the cause.",
 "A blocky picture means the video is arriving damaged, too slowly or at too low a quality for the screen.",
 [("Is it every channel?",["If only one channel is blocky, the source may be poor. If all are, look at your connection or device."]),
  ("Connection",["Test with a cable. If the picture clears up, your Wi-Fi was dropping data. See {post:improve-wifi-for-streaming}."]),
  ("Device",["Older devices can struggle with high resolutions. Choose a lower quality or use a newer device."]),
  ("Screen settings",["Some TVs have strong picture processing that can exaggerate blockiness. Try a standard or game picture mode to compare."]),
  ("Related",["Read {post:why-quality-varies-by-channel} for why quality differs."])])

add("iptv-works-on-phone-not-tv", "IPTV Works on a Phone but Not on the TV", T,
 "If IPTV plays on your phone but fails on your TV, the cause is usually the TV app, its network connection, storage or settings. Here is how to find it.",
 "This is a useful clue: your subscription and sign-in clearly work, so the problem is on the TV side.",
 [("What the clue tells you",["The service is fine and your details are correct. Focus on the TV or stick."]),
  ("Check these",[("ul",["Is the TV on the same network and getting internet?","Is the app up to date?","Is storage full?","Is the date and time correct?","Is the TV using Wi-Fi at the edge of its range?"])]),
  ("Try a clean start",["Restart the TV, then the router. If still no change, reinstall the app. See {post:reinstall-iptv-app}."]),
  ("Consider the device",["Some older TVs cannot run current apps. A streaming stick may be the answer. See {post:watch-iptv-without-a-smart-tv}."])])

add("router-restart-vs-factory-reset", "Router Restart vs Factory Reset for Streaming", T,
 "Know the difference between restarting a router and resetting it to factory settings, and when each one helps with streaming problems.",
 "People mix these up, and one of them can leave you without internet until you reconfigure the router.",
 [("A restart",["Power it off for about thirty seconds, then on. Nothing is erased. It clears temporary faults and is safe to try first."]),
  ("A factory reset",["This wipes all your settings, including the Wi-Fi name and password and your internet login. Do it only if your provider tells you to, and make sure you have the details to set it up again."]),
  ("When to do which",[("ul",["Streaming stutters at times: restart.","Nothing connects after a change: restart, then ask your provider.","Router is behaving strangely and your provider agrees: reset."])]),
  ("After any change",["Test with a live channel at your usual viewing time. See {post:iptv-freezing-at-peak-times}."])])

add("iptv-after-changing-broadband", "IPTV Stopped After Changing Broadband Provider", T,
 "If IPTV stopped working after you switched broadband, check the new router, Wi-Fi name, device connection, speeds and any network restrictions.",
 "A new provider usually means a new router, a new Wi-Fi name and sometimes different network behaviour.",
 [("Reconnect your devices",["Devices remember the old Wi-Fi name. Join the new network and enter the new password. Restart the TV or stick afterwards."]),
  ("Test the connection",["Open a web page and run a speed test. If the line is slower than expected, contact your new provider."]),
  ("Check the router",["Position the new router well, and try 5 GHz at short range. See {post:improve-wifi-for-streaming}."]),
  ("Tell us",["If the internet is fine but IPTV still fails, message support with your new provider's name and what the app shows."])])

add("dns-settings-and-streaming", "DNS Settings and Streaming: What They Do", T,
 "A plain explanation of DNS, how it affects loading time for streaming apps, and when changing it on your router or device might be worth testing.",
 "DNS is the internet's address book. It turns names into the numbers computers use to connect.",
 [("Why it matters",["When your app contacts a server, it first looks up its address. A slow lookup can add delay before a channel starts. It rarely affects a stream once it is playing."]),
  ("Should you change it?",["Usually not. Your provider's default works for most people. If you notice slow starts but a healthy stream afterwards, you can test a different public DNS service."]),
  ("How to test safely",["Note your current settings first. Change one device or the router, test for a day and revert if there is no improvement. Do not follow instructions from unknown sources."]),
  ("Privacy",["DNS providers can see which names you look up. Read the privacy policy of any service you choose. See also {post:should-you-use-a-vpn-with-iptv}."])])

add("football-season-iptv-checklist", "Football Season IPTV Checklist", SP,
 "A checklist for the football season on IPTV: test devices, check the guide, prepare your network, plan for busy kick-off times and backup options.",
 "Football weekends are the busiest time for streaming. Preparing once at the start of the season saves repeated stress.",
 [("Before the season",[("ul",["Update the app and the device.","Check storage and restart.","Confirm the guide is working.","Decide which room and screen you will use."])]),
  ("Test at kick-off time",["Do a trial run at a time when many people stream. If the picture pauses, work on the network before a big match."]),
  ("Know about delay",["Internet streams run behind the live broadcast. Mute alerts from sports apps if spoilers bother you."]),
  ("Rights and availability",["Which matches are shown on which channels changes by competition and country. Never assume a particular match is included. Ask support, and see {post:iptv-for-live-sports-tips}."])])

add("combat-sports-streaming-prep", "Preparing to Stream Boxing and Combat Sports", SP,
 "How to prepare for big fight nights on IPTV: start times, late events, network load, guide checks and a backup plan if the stream drops.",
 "Fight nights run late, start on uncertain schedules and attract heavy viewing, so planning matters.",
 [("Schedules move",["Cards often start earlier than the main event and run long. Check the guide a day ahead and again on the day."]),
  ("Network load",["Pause large downloads and ask others in the house to avoid heavy use during the key bout."]),
  ("Devices",["Use the device you have tested, restart it earlier in the day and keep a second device ready."]),
  ("Availability",["Some events are sold separately and may not be part of any subscription. Ask in advance. See {post:iptv-for-live-sports-tips}."])])

add("f1-weekend-streaming-tips", "Formula 1 Weekend Streaming Tips", SP,
 "Tips for watching Formula 1 weekends on IPTV: early starts, time zones, practice and qualifying, delay, and network and device preparation.",
 "A race weekend has several sessions across a couple of days, often at awkward hours, so a little planning helps.",
 [("Know the schedule",["Sessions run at times set by the circuit's local time zone. Check your device time zone, and the guide, so start times line up."]),
  ("Pick your screen",["For fast action, a stable 1080p picture often looks smoother than a struggling 4K one. See {post:hd-vs-4k-iptv-streaming}."]),
  ("Prepare early",["Restart the device, close other apps and test a live channel before the session."]),
  ("Do not assume",["Which channels carry which sessions varies by country and season. Confirm before you rely on it."])])

add("cricket-and-rugby-streaming-tips", "Cricket and Rugby Streaming Tips", SP,
 "Streaming long cricket matches and rugby fixtures on IPTV: long sessions, stability, battery and heat, scheduling and fixture timing.",
 "Cricket can run for hours and rugby has set kick-offs, and both are tests of stability rather than raw speed.",
 [("Long sessions",["Choose a device that will not overheat and keep it on mains power. Restart it before play begins."]),
  ("Quality choice",["A steady HD picture is better than an unstable 4K one. Lower the quality if the stream pauses."]),
  ("Time zones",["Overseas matches may start very early or very late in your time. Check the guide and your device time."]),
  ("Plan around the day",["Rain delays and extra time change the schedule, so keep the app open and the guide refreshed. See {post:what-is-epg-tv-guide}."])])

add("reduce-delay-in-live-sport-streams", "Why Live Sport Streams Lag and How to Reduce Delay", SP,
 "Why internet streams run behind live broadcasts, what you can control, what you cannot and how to limit spoilers from phones and social apps.",
 "Delay is built into how internet streaming works, though some of it is under your control.",
 [("Where the delay comes from",["The stream is encoded, split into segments, sent across the network, buffered by your player and decoded. Each step adds a little time."]),
  ("What you can influence",[("ul",["Use a wired connection.","Choose a player with a smaller buffer if the option exists.","Avoid running a VPN if you do not need it."])]),
  ("What you cannot",["The service's own processing and internet distance are fixed. Differences of several seconds, even tens of seconds, versus broadcast are normal."]),
  ("Avoiding spoilers",["Turn off score notifications and mute chats on your phone while watching. See {post:latency-in-live-streaming}."])])

add("hls-streaming-explained", "HLS Streaming Explained Simply", F,
 "HLS is a common method for delivering video over the internet in small chunks. Learn how it works and why it matters for buffering and delay.",
 "HLS stands for HTTP Live Streaming. It is one of the most common ways to deliver video over the internet.",
 [("How it works",["The video is cut into short pieces, each a few seconds long. A list tells the player which pieces exist. The player downloads them one after another and plays them in order."]),
  ("Quality switching",["The same video is often prepared at several qualities. If your connection slows, the player can pick lower quality pieces to keep going."]),
  ("Why delay exists",["Because the player waits for whole pieces, there is a delay. Shorter pieces reduce it but make streams more sensitive to network hiccups."]),
  ("What this means for you",["If your picture softens now and then without stopping, HLS style switching is probably working. See {post:how-iptv-works} for the wider picture."])])

add("bitrate-and-resolution-explained", "Bitrate and Resolution Explained", F,
 "Resolution is how many pixels, bitrate is how much data per second. Learn why both affect picture quality and what they mean for your connection.",
 "People often mix up these two. They are related but different.",
 [("Resolution",["The number of pixels in the picture. 1080p has more detail than 720p, and 4K has more than 1080p."]),
  ("Bitrate",["How much data the video uses each second. Two streams at the same resolution can look different if one has a higher bitrate, because it keeps more detail in motion."]),
  ("Why both matter",["A high resolution with a low bitrate can look soft or blocky. A good bitrate at a modest resolution can look cleaner than you expect."]),
  ("Practical advice",["Pick the quality your screen and connection support. See {post:hd-vs-4k-iptv-streaming} and {post:how-much-data-does-iptv-use}."])])

add("latency-in-live-streaming", "Latency in Live Streaming Explained", F,
 "What latency is, why live streams run behind broadcasts, what is normal and how it differs from buffering and low speed.",
 "Latency is delay. It is not the same as speed, and it is not the same as buffering.",
 [("Three different things",[("ul",["Speed is how much data per second you can receive.","Buffering is a pause while data catches up.","Latency is how far behind real time you are."])]),
  ("Why it exists",["Streaming adds processing and buffering steps, each costing time. This is normal for internet video."]),
  ("What is normal",["Several seconds behind a broadcast is common. Large and growing delay can suggest a problem."]),
  ("What helps",["A steady wired connection and a fast device help a little. See {post:reduce-delay-in-live-sport-streams}."])])

add("catch-up-tv-explained", "Catch-Up TV Explained", F,
 "How catch-up television works, how long programmes may be stored, how it differs from recording and why it may not exist on every channel.",
 "Catch-up lets you watch a programme after it has been shown, without having set a recording.",
 [("How it works",["A service stores programmes for a limited time and lets you pick them from the guide. It uses the same internet delivery as live viewing."]),
  ("Limits",[("ul",["Only certain channels may offer it.","Programmes are kept for a limited window.","Quality and availability can vary."])]),
  ("Compare with recording",["Recording saves a copy you choose. Catch-up is a service feature. See {post:catch-up-and-recording-explained}."]),
  ("Ask before you rely on it",["Check during your trial whether the channels you care about offer it."])])

add("multicast-vs-unicast-iptv", "Multicast vs Unicast in IPTV", F,
 "A simple explanation of multicast and unicast streaming and why internet IPTV on home connections normally uses unicast.",
 "These terms describe how a stream is sent to viewers.",
 [("Unicast",["One stream is sent to each viewer. If ten people watch, ten streams cross the network. This is how most internet video works."]),
  ("Multicast",["One stream is shared by many viewers on a managed network, which saves capacity. It is used by some telecom operators inside their own networks."]),
  ("What it means for you",["On a normal home internet connection you use unicast. The load on your line scales with the number of screens you use."]),
  ("Practical effect",["Each screen counts, so plan your bandwidth accordingly. See {post:how-much-data-does-iptv-use}."])])

add("how-to-renew-iptv-safely", "How to Renew an IPTV Subscription Safely", SU,
 "How to renew safely: check your expiry date, use the same trusted channel, confirm prices and receipts and avoid pressure and look-alike messages.",
 "Renewal time is when scammers and mistakes both appear, so a short routine helps.",
 [("Know your expiry",["Note the date and length you chose when you subscribed. Set a reminder a few days earlier."]),
  ("Use the original contact route",["Contact us through the details on our site or the WhatsApp number you used before. Do not follow links from unknown senders."]),
  ("Confirm before you pay",["Ask for the plan, length and total in writing. Prices are totals for the length chosen. See {plans}."]),
  ("Keep records",["Save the receipt and the message confirming the new period. See {post:iptv-scams-and-safe-payment}."])])

add("upgrade-your-iptv-plan", "Upgrading Your IPTV Plan Mid-Term", SU,
 "Thinking of moving to a higher IPTV plan before your term ends? Learn the questions to ask about pricing, dates and what changes.",
 "If your needs change, upgrading may make sense. Ask first so there are no surprises.",
 [("Why people upgrade",["More simultaneous screens, a larger channel list or a different mix of content are common reasons."]),
  ("Ask these questions",[("ul",["Is a mid-term upgrade possible?","How is the price worked out?","Does my end date change?","Will my sign-in details change?"])]),
  ("Compare first",["Look at the differences between plans on the {plans} and read {post:how-to-choose-an-iptv-plan}."]),
  ("Get it in writing",["Ask for the agreed change by message so there is a clear record."])])

add("iptv-payment-methods-explained", "IPTV Payment Methods Explained: PayPal, Binance Pay and Wise", SU,
 "How PayPal, Binance Pay and Wise differ for paying an IPTV subscription: speed, protection, fees, currencies and what to keep as proof.",
 "We accept three payment methods. Each suits different people.",
 [("PayPal",["Familiar to many customers and quick to use. Buyer protection rules apply in some situations, subject to PayPal's own terms."]),
  ("Binance Pay",["A crypto-linked payment method for people who already use that platform. Check the amount, the network and the recipient carefully, because crypto payments are hard to reverse."]),
  ("Wise",["Useful for transfers between currencies, which can suit customers outside the UK. Check the exchange rate and fee shown before you confirm."]),
  ("For any method",[("ul",["Prices are shown in pounds sterling.","Check the total before you send.","Keep a receipt or screenshot.","Never share card numbers or passwords in chat."]),"See {post:how-to-renew-iptv-safely}."])])

add("iptv-refund-expectations", "IPTV Refunds: What to Expect and What to Ask", SU,
 "How to approach IPTV refunds: read the policy, understand what a trial covers, what counts as a fault and how to make a clear request.",
 "A refund policy is a promise about what happens if things go wrong. Read it before you pay, not after.",
 [("Read the policy",["Our refund policy explains the conditions. Any provider's policy should say when a refund is possible and how to ask."]),
  ("Trials and refunds",["A trial reduces the need for refunds because you can test first. Use it fully. See {post:iptv-free-trial-what-to-test}."]),
  ("Making a clear request",[("ul",["Give your payment details and date.","Describe the problem and when it began.","Include screenshots and what you already tried."])]),
  ("Stay calm and keep records",["Keep messages and receipts. If you paid by a method with its own dispute process, you may also be able to use it, subject to its rules."])])

add("iptv-vs-pay-per-view", "IPTV vs Pay-Per-View for Sport", SU,
 "Compare a channel-based IPTV subscription with buying individual pay-per-view events: cost per event, flexibility, availability and planning.",
 "If you only care about a handful of big events, pay-per-view might look cheaper. If you watch regularly, it often is not.",
 [("How each works",["Pay-per-view sells a single event for a one-off fee. A subscription gives access to many channels for a period."]),
  ("Do the sums",["Count how many events you watch in a year and the total cost of buying each one. Compare it with the total price for a subscription. Our prices are totals, shown on the {plans}."]),
  ("Availability",["Some events are sold only by the rights holder and may not appear in any subscription. Do not assume."]),
  ("Convenience",["A subscription removes per-event purchases but depends on your connection. See {post:iptv-for-live-sports-tips}."])])
