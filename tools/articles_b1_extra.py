# Extra sections inserted before each article's final section. slug -> [(h2, [paras])]
X = {}

X["how-iptv-works"] = [
 ("Live streams versus on-demand files",["A live channel is produced continuously and delivered as it happens, so there is no finished file to download in advance. An on-demand film, by contrast, already exists in full on a server, which lets your player fetch it far ahead of where you are watching. This is why a stream that survives a film can still stumble on a football match: the live player has almost no spare time to recover from a slow moment."]),
 ("Adaptive quality, in plain terms",["Many players can switch between several quality levels while you watch. If your connection weakens, the player may drop to a lower resolution to avoid stopping, then rise again when conditions improve. If you notice a picture that goes soft for a few seconds and then sharpens, that is normally this process working as intended rather than a fault.","Some services offer only one fixed quality per channel. In that case there is no automatic fallback, and a weak connection shows up as a pause instead of a softer picture."]),
 ("Common misunderstandings",[("ul",["IPTV is not a physical box or cable. It is a way of delivering television over the internet.","A fast connection test does not guarantee a smooth stream, because stability and delay matter as much as top speed.","The player app and the service are separate. A fault in one does not always mean a fault in the other."])])]

X["iptv-vs-cable-tv"] = [
 ("Cost over a year",["Compare total yearly cost, not just the monthly figure. For cable, add equipment fees, any installation charge and the effect of price rises when a contract period ends. For IPTV, add the cost of a streaming device if you do not already own one, and remember that you also need working broadband. Our own plans are priced as totals for one, three, six or twelve months, so you can see the full amount before you pay."]),
 ("Picture and sound",["Cable can deliver a very steady picture because the network is built for television. IPTV can match it on a good connection, but its quality moves with your broadband. If your household streams a lot at once, test IPTV in the evening before you decide to switch."]),
 ("Support and responsibility",["With cable, the provider usually owns the whole chain and can send an engineer. With IPTV, the provider looks after the service while you look after your device, router and Wi-Fi. That split is why a trial is sensible: it shows you whether your own side of the chain is ready."])]

X["iptv-vs-satellite-tv"] = [
 ("Moving house or renting",["A satellite dish stays with the building, and removing one can be awkward or restricted in rented property. IPTV moves with you, as long as you can set up broadband at the new address. If you move often, that portability is a real advantage."]),
 ("Several rooms",["Satellite normally needs a receiver or an extra feed for each additional room. With IPTV each room needs a compatible device and a good connection, and plan rules on simultaneous streams apply. Count the screens you want and ask about stream limits before choosing."]),
 ("Power cuts and outages",["Neither option works without power at your end. A broadband outage stops IPTV completely, while a satellite service can carry on during a broadband fault. If an internet outage would leave you without any television at all, keep that in mind, perhaps with an aerial as a backup."])]

X["iptv-vs-streaming-apps"] = [
 ("A simple test for what you need",["Write down the five things you watch most. If they are scheduled and live, such as news and sport, a channel-based service fits. If they are series you start when you like, a library app fits. If it is both, you may genuinely want two services, but you can often cut one after a month by checking what you actually opened."]),
 ("What to watch for in the guide",["Because live television runs to a schedule, a working programme guide matters far more with IPTV than with an on-demand app. Check the guide during your trial. Our article on the {post:what-is-epg-tv-guide} explains why it sometimes goes wrong."])]

X["what-is-an-iptv-player-app"] = [
 ("Free apps and paid apps",["Some player apps are free and show adverts or limit features. Others charge a one-off fee or a subscription. Neither is automatically better. The right question is whether the app runs reliably on your device and whether you are comfortable with its privacy terms."]),
 ("Different devices, different apps",["An app that is excellent on a phone may feel awkward on a television remote. Smart TV apps are often more limited than those on Android TV or Fire TV. Always test on the screen you will actually use, and read our device guides before installing: {post:iptv-on-smart-tv} and {post:iptv-on-android-tv} cover the common cases."]),
 ("Signs an app is not a good choice",[("ul",["It has not been updated for a long time.","It asks for permissions that have nothing to do with video.","It comes from an unofficial site rather than a store.","It crashes during longer viewing sessions."])])]

X["m3u-playlist-explained"] = [
 ("What is inside the list",["Open an M3U file in a text editor and you will see lines that begin with information about a channel, followed by a line with the stream address. The information line can include the channel name, a group such as Sport or News, and a reference used to match the programme guide. The app reads these lines and builds your menu from them."]),
 ("Playlist or login: which is better",["A playlist is simple and works in almost every player. A server login, covered in {post:xtream-codes-login-explained}, lets the app fetch categories and the guide itself and often feels neater. If your provider offers both, try the login first, and fall back to the playlist if your app does not support it."]),
 ("Why a long list can feel slow",["Large lists take time to load on weak devices because the app must read and sort every entry. Be patient the first time, avoid adding the same list twice, and remove old lists you no longer use so they do not clutter the app."])]

X["xtream-codes-login-explained"] = [
 ("Where to find the details",["Your provider sends the server address, username and password after you subscribe. Keep the message somewhere private so you can copy the details again if you reinstall the app. Copying and pasting is far safer than typing them by hand."]),
 ("If login fails",["First check each field character by character. Then check that your subscription is still active, because an expired account will fail in the same way as a typing error. Check that your device time and date are correct, as incorrect time can stop some logins. If it still fails, send support the app name and the exact message you see, but never send your password in public."]),
 ("Why the address may look unusual",["The server address may include a port number after a colon. That is normal and needs to be entered in full. If an app has a separate port field, put the number there instead of in the address."])]

X["what-is-epg-tv-guide"] = [
 ("Matching guide data to channels",["Each channel carries an identifier that the guide uses to find its schedule. If the identifier is missing or different, that channel shows no data. Apps often let you refresh or remap the guide, and a missing guide for one channel while the rest work is usually a data issue, not a fault with your connection."]),
 ("How far ahead should it show",["Most guides show a few days of programmes, though this varies by channel. If yours shows only the current programme, try a refresh and give it time to download. Large guides can take a minute on older devices."]),
 ("Using the guide on match days",["For live events, check the guide earlier in the day because schedules can change. Remember that start times in the guide can differ from what you see if the event runs long or is delayed."])]

X["iptv-on-apple-tv"] = [
 ("Ethernet or Wi-Fi",["Apple TV models differ here, so check yours. If you have an Ethernet port, a cable usually gives the steadiest results for live television. If you rely on Wi-Fi, the 5 GHz band is normally the better choice at short range. Our {post:iptv-wifi-vs-ethernet} article explains the trade-offs."]),
 ("Remote and navigation",["The Siri Remote makes channel lists easy to scroll, but some apps are designed with touch screens in mind and feel clumsy on a remote. During your trial, spend time changing channels, using search and opening the guide to see whether the controls suit you."]),
 ("Keeping it stable",["Keep tvOS and your player app updated, restart the Apple TV if it has been on for a long time and avoid placing it where it can overheat. If problems appear after an update, check the app's listing for notes from the developer."])]

X["iptv-on-iphone-and-ipad"] = [
 ("Phone or tablet",["A tablet gives a larger picture and usually lasts longer for long viewing, while a phone is easier to carry. Whichever you choose, rotate to landscape and use the app's full-screen mode for the best picture."]),
 ("Watching away from home",["On a public or hotel Wi-Fi network, connections can be slow or restricted. If a stream struggles, try your own mobile data for a short test, keeping the usage figures in mind. Avoid signing in to anything on networks you do not trust."]),
 ("Casting to a television",["Many apps support AirPlay so you can send the picture to a compatible TV or Apple TV. Casting adds another link in the chain, so if the picture stutters, test playing directly on the TV instead."])]

X["iptv-on-windows-pc"] = [
 ("Browser or app",["Some services work through a browser. Browsers are convenient but can use more memory than a dedicated player. If your laptop fans spin up or video stutters, a lightweight player app may handle it better."]),
 ("Connecting a PC to a television",["An HDMI cable gives a simple, reliable link. Set the display to extend or duplicate as you prefer, and set the sound output to the TV. If the picture is cropped, check the display scaling setting in Windows."]),
 ("Keeping the machine healthy",["Use a standard user account for everyday viewing, keep security software enabled and avoid installing codec packs from unknown sites. A fresh restart before a long session clears many small problems."])]

X["iptv-on-mac"] = [
 ("Battery and heat",["MacBooks are efficient, but video decoding still uses power. For a long session, plug in. If the case feels very hot, close other heavy apps and make sure the vents are not blocked."]),
 ("Apple silicon and older Macs",["Recent Macs with Apple silicon handle video comfortably. Older Intel Macs may run warmer and struggle with high resolutions. Choose a lower quality setting if playback is not smooth."]),
 ("Privacy and permissions",["Review which permissions the player asks for the first time it runs. A video player has no need to read your contacts or photos. If something looks wrong, deny the request and consider another app."])]

X["iptv-on-android-phones"] = [
 ("Different manufacturers",["Android phones vary widely in power and in how aggressively they stop background apps to save battery. If a stream ends when the screen turns off, check the phone's battery settings for the player app and allow normal activity if you need it."]),
 ("Cast and mirror",["Many Android devices can cast to a TV. As with any casting, an extra link is added, so if quality drops, test on the TV directly or try a different casting method."]),
 ("Staying safe",["Do not install apps from links in messages or social media. Avoid turning on installation from unknown sources unless support has explained exactly why it is needed and which file to use."])]

X["iptv-wifi-vs-ethernet"] = [
 ("What a cable does not fix",["A cable removes Wi-Fi problems, but it cannot fix a slow or unstable internet line. If a wired test is still poor, the problem lies with your broadband or with the service, not your wireless signal."]),
 ("Running a cable neatly",["A flat Ethernet cable can run under a carpet edge or along a skirting board with little fuss. Check that the cable is rated for the speed you need, and avoid sharp bends. If you rent, use adhesive clips that remove cleanly."]),
 ("Quick comparison test",["Watch the same live channel for twenty minutes on Wi-Fi, then twenty minutes on a cable. If the cable is clearly better, it has solved the problem. If they behave the same, look elsewhere, starting with {post:iptv-freezing-at-peak-times}."])]

X["improve-wifi-for-streaming"] = [
 ("Router settings worth a look",["Log in to your router and check which Wi-Fi channel it uses. In a crowded building, switching channels can reduce interference. Many routers have an automatic setting, which is a sensible default. Keep the router's firmware updated through your provider's guidance."]),
 ("When the router is the limit",["Routers older than several years may struggle with many devices. If yours is old and the problems are widespread, a replacement or a mesh system may help. Ask your broadband provider whether a newer router is available."]),
 ("Simple checks that cost nothing",[("ul",["Move the streaming device a metre or two and test again.","Disconnect devices you are not using.","Check whether a neighbour's network is sharing your channel.","Try the other Wi-Fi band for a short test."])])]

X["iptv-freezing-at-peak-times"] = [
 ("Telling congestion from a faulty stream",["If every app slows down at the same hour, the connection is the likely cause. If only the IPTV app suffers while other video apps are fine, the cause may be the stream or the player. Testing another video service at the same time gives you a useful comparison."]),
 ("Lowering the load",["Choose a lower resolution during the busiest hours if your app allows it. A slightly softer picture that never pauses beats a sharp one that stops. If your player has a buffer size option, a larger buffer can absorb short dips at the cost of a slightly longer start."]),
 ("Talking to your internet provider",["Give your provider the times and the results of speed tests when you contact them. Evidence of repeated evening drops makes it easier for them to investigate your line or local area."])]

X["iptv-no-audio-or-out-of-sync"] = [
 ("Surround sound and formats",["Some channels carry surround sound that a basic TV or soundbar cannot decode. If a channel is silent while others play, switch the audio output format in the TV or box to stereo or PCM, which nearly every device understands."]),
 ("Bluetooth delay",["Bluetooth headphones and speakers add delay, which makes speech look out of sync. Use wired headphones, or look for a low-latency option or a delay adjustment on the device."]),
 ("Cleaning up after changes",["If the problem began after you changed settings or installed an update, return the audio settings to automatic, restart the app and then the device, and test again before making further changes."])]

X["iptv-channels-not-loading"] = [
 ("Single channel or every channel",["If only one channel fails, the issue is probably with that stream, not your equipment. Note the channel name and time and tell support. If everything fails, work through connection, sign-in and app checks first."]),
 ("Date and time on your device",["An incorrect date or time can stop an app from connecting securely. Turn on automatic date and time in your device settings, restart and try again."]),
 ("What to send to support",[("ul",["Your device model and app name.","What you see: black screen, spinner or an error message.","When the problem began and what changed before it.","Whether other devices on the same network work."])])]

X["hd-vs-4k-iptv-streaming"] = [
 ("Frame rate matters for sport",["Fast action such as football looks smoother at higher frame rates. A stable 1080p picture at a good frame rate often looks better in motion than a struggling 4K one. Prioritise smoothness for live sport."]),
 ("HDR and other labels",["HDR improves the range of light and dark in the picture but requires support on your TV and your device. Do not pay extra for a label your equipment cannot display."]),
 ("Checking what you are actually getting",["Look at the app's information panel during playback, if it has one, to see the resolution of the stream. Compare a few channels. Not every channel is available at the same quality."])]

X["how-much-data-does-iptv-use"] = [
 ("Measuring your own usage",["Your router or your internet provider's app often shows data used per device. Note the figure before and after a viewing session to get a real number for your setup. That beats any rule of thumb."]),
 ("Households with several screens",["Add up the screens that are likely to run at the same time. Two HD streams in the evening and a phone on video calls can easily double or triple the load on your connection, even if each stream is modest."]),
 ("Background use",["Some apps keep a stream open while paused or minimised. If you have a cap, close the app fully when you finish rather than leaving it on a channel overnight."])]

X["iptv-subscription-length-guide"] = [
 ("Comparing per-month cost properly",["Divide the total by the number of months. Basic at £4 for one month, £10 for three, £17 for six and £30 for twelve works out at about £4.00, £3.33, £2.83 and £2.50 a month. Standard, Premium and Ultimate follow a similar pattern. Longer terms lower the monthly cost, but only matter if you will use the service throughout."]),
 ("Think about what could change",["Your broadband, your device and your viewing habits may change over a year. A shorter term gives you room to move. A longer term rewards a stable setup. If you are unsure, start shorter and extend once you are confident."]),
 ("Read the refund terms",["Whatever length you choose, read the {faq} and the refund policy first, so you understand what happens if something does not work as expected."])]

X["iptv-free-trial-what-to-test"] = [
 ("How long a trial should be",["A short trial can still be useful if you plan it. Decide in advance what to test and when, rather than switching on for ten minutes and switching off. Cover a weekday evening and, if sport matters to you, a live match."]),
 ("Questions that reveal the truth",[("ul",["How is support provided and during which hours?","What happens to my sign-in details after the trial?","Which devices does the plan support?","What is the refund policy once the service is activated?"])]),
 ("Be careful with your details",["During a trial you should never be asked for card numbers or banking passwords. If a provider asks for sensitive payment information before you have even tried the service, treat that as a red flag."])]

X["iptv-scams-and-safe-payment"] = [
 ("What to do if you think you have been scammed",["Stop all further payments, keep screenshots of the conversation and receipts, and contact your payment provider as soon as possible to ask what can be done. In the UK, you can also report the fraud through the official national fraud reporting service, which the police website explains. Change any passwords that you reused."]),
 ("Why a trial protects you",["A real trial lets you check performance before committing. A seller who refuses any trial, or who pushes you to pay first and promises to sort things out later, gives you very little protection."]),
 ("Small habits that help",[("ul",["Save the website address and use it, rather than links sent by strangers.","Keep a record of what you were told about price, length and devices.","Pay only through methods that give you a receipt.","Do not share one-time codes sent to your phone."])])]

X["should-you-use-a-vpn-with-iptv"] = [
 ("Choosing a VPN carefully",["If you decide to use one, pick a paid provider with a clear privacy policy and a good record. Check that it has an app for your streaming device. Avoid anything that asks for more permissions than seem necessary."]),
 ("Testing the effect",["Run a stream with the VPN on and with it off at the same time of day. Compare how quickly channels load and whether playback stays smooth. If the VPN reduces quality, try a nearer server or a different protocol setting."]),
 ("Privacy is bigger than a VPN",["Strong passwords, device updates and caution with links protect you more than most people realise. A VPN is one tool in a larger set of habits."])]

X["iptv-for-live-sports-tips"] = [
 ("Pick a good viewing spot",["Sit within clear reach of the router for Wi-Fi devices, or use a cable. Having the streaming device and the TV set up the evening before removes last-minute stress."]),
 ("Handling a mid-match problem",["If the stream stalls, wait about ten seconds before changing anything, because many stalls clear by themselves. If not, switch to the same channel again, then try a lower quality, and only then restart the app. Avoid restarting the router mid-match unless nothing else works."]),
 ("Shared networks",["If you live in shared housing, agree a quiet period for big downloads during important matches. Streaming works best when the line is not being asked to do several heavy jobs at once."])]

X["iptv-uk-broadband-guide"] = [
 ("Upload speed and why it matters a little",["Streaming is mostly a download activity, but video calls and cloud backups use upload. On connections with low upload capacity, those activities can disturb viewing. Pause backups during live viewing."]),
 ("Router quality",["The router your provider supplies is part of the chain. If it is old, ask about an upgrade. A good router on a modest line can outperform a poor router on a faster one."]),
 ("Switching provider",["If your evenings are consistently poor, compare other providers available at your address, and check contract exit terms before switching."])]

X["uk-tv-licence-and-iptv"] = [
 ("Common situations to check",["People are often unsure about students in halls, lodgers, second homes and holiday lets. Rules differ between situations, so use the official checker rather than guessing. Do not rely on forum posts."]),
 ("Keep your records",["If you believe you do not need a licence, the official guidance explains how to tell TV Licensing. Keep any confirmation they send you."]),
 ("Why we mention it",["We include this because it affects UK viewers directly and is easy to overlook. We do not provide legal advice and we are not connected to TV Licensing."])]

X["how-many-devices-can-i-use-with-iptv"] = [
 ("A worked example",["Suppose a household has a living room TV, a bedroom TV and a phone. If two people watch different things at once, you need at least two simultaneous streams. If the phone is occasionally used while someone else is on a TV, you might need three. Plan for the busiest moment, not the typical one."]),
 ("Sharing an account",["Sign-in details are for the household that bought the plan. Sharing them widely can break the provider's terms and might lead to access being limited. Read the terms of any plan you buy."]),
 ("If you need more later",["Ask whether you can upgrade or add streams mid-term and how that is charged. A clear answer in advance avoids surprises."])]

X["iptv-in-canada-what-to-know"] = [
 ("Time zones and live events",["Live events in Canada run across several time zones. When you read a programme guide, check that your device is set to your local time, so that start times line up with the broadcast you expect."]),
 ("Internet data caps",["Some Canadian internet plans have monthly data caps. Streaming uses data continuously, so estimate your usage using {post:how-much-data-does-iptv-use} and check your provider's terms before heavy viewing."]),
 ("Support and payment",["Before paying any provider from Canada, ask which currency the price is in and which payment methods are accepted. Keep the payment receipt and the written reply you received."])]
