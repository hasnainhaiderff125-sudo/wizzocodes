A = []
def add(slug, title, cat, desc, lead, sections, kw=None, kw2=None):
    A.append(dict(slug=slug, title=title, cat=cat, desc=desc, lead=lead, sections=sections,
                  kw=kw or title.split(':')[0].lower(), kw2=kw2 or []))

C = "IPTV Comparisons"; Q = "IPTV Streaming Quality"; SE = "IPTV Security & Privacy"; UK = "IPTV UK Guides"; CA = "IPTV Canada Guides"; FQ = "IPTV FAQs"

add("iptv-vs-freeview-and-freesat", "IPTV vs Freeview and Freesat", C,
 "Compare IPTV with Freeview and Freesat: channel choice, equipment, cost, reliability, features such as catch-up and who each suits best.",
 "Freeview and Freesat are free-to-air services. IPTV is an internet service you pay for. They are not direct rivals, and some homes use both.",
 [("What free-to-air gives you",["Freeview uses an aerial and Freesat uses a dish to receive a set group of channels with no monthly subscription. Quality is steady and does not use your broadband."]),
  ("What IPTV adds",["A wider range of channels and, on some services, on-demand libraries, delivered over the internet and usable on several kinds of screen."]),
  ("Costs",["Free-to-air has equipment cost but no subscription. IPTV has a subscription plus the cost of any streaming device and your broadband."]),
  ("Using both",["Many households keep an aerial as a dependable backup and use IPTV for more choice. Remember that UK viewers may need a TV Licence for live television however they watch it. See {post:uk-tv-licence-and-iptv}."])])

add("iptv-vs-streaming-costs", "IPTV vs Stacking On-Demand Subscriptions: Cost Compared", C,
 "A method for comparing IPTV with several on-demand subscriptions: list what you watch, add yearly costs and check overlaps before you cancel.",
 "Subscriptions add up quietly. This method compares them honestly instead of guessing.",
 [("Step 1: list what you actually watch",["Open each app's history. Write down the shows and live content you used in the past three months."]),
  ("Step 2: add yearly costs",["Multiply each monthly price by twelve. For IPTV, use the total for the length you would choose, such as the twelve month totals on our {plans}."]),
  ("Step 3: find overlaps",["If you rarely open an app, it is a candidate to pause. Many on-demand services let you rejoin later."]),
  ("Step 4: check the other costs",["Include a streaming device and broadband. Our guide to {post:iptv-subscription-length-guide} shows the per-month arithmetic."]),
  ("Step 5: decide",["Keep what you use weekly. Test a replacement with a trial before cancelling anything."])])

add("iptv-box-vs-app", "IPTV Box vs App: Which Is Simpler?", C,
 "Compare using a dedicated IPTV set-top box against an app on a device you already own, covering cost, simplicity, updates and flexibility.",
 "The choice is between a box built for the job and an app on something general-purpose.",
 [("A dedicated box",["Pros: everything in one place and often an Ethernet port. Cons: another device to buy, power and update, and some boxes are poorly supported."]),
  ("An app on your current device",["Pros: no extra purchase, updates through the store, can run on several devices. Cons: depends on your TV or stick being capable."]),
  ("Which to pick",["If your current TV or stick runs apps smoothly, start there. If it is slow or unsupported, a good Android TV or Fire TV device is a sensible upgrade. See {post:firestick-vs-android-box-for-iptv}."]),
  ("Be careful with boxes",["Avoid unbranded devices with unclear software. See {post:iptv-on-android-tv-boxes}."])])

add("smart-tv-app-vs-streaming-stick", "Smart TV App vs Streaming Stick for IPTV", C,
 "Should you use the app on your smart TV or add a streaming stick? Compare speed, updates, app choice and long-term reliability.",
 "A smart TV already has apps. A stick is a small computer built for streaming. Each has strengths.",
 [("Smart TV apps",["Convenient and tidy, but TV processors are often modest and app choice is limited. Updates may stop as a TV ages."]),
  ("Streaming sticks",["Usually faster, with a wider choice of apps and regular updates. They are cheap to replace when they age."]),
  ("A simple rule",["If the TV app runs smoothly and the player you want is available, use it. If it is slow, missing or outdated, add a stick."]),
  ("Related",["See {post:iptv-on-smart-tv} and {post:iptv-on-fire-tv}."])])

add("iptv-vs-ott-explained", "IPTV vs OTT: What Is the Difference?", C,
 "IPTV and OTT both send video over the internet. Learn how the terms differ, where they overlap and why the label matters less than the experience.",
 "Both terms describe television over the internet, so confusion is common.",
 [("OTT",["Over the top means video delivered over the public internet without a traditional cable or satellite operator. On-demand apps are the best known examples."]),
  ("IPTV",["Strictly, IPTV began as television delivered over an operator's managed IP network. In everyday talk it now often means live channels delivered over the internet to apps."]),
  ("Why people mix them up",["Both use your internet connection, and the line between them has blurred. What matters is the content, support and stability you get."]),
  ("What to compare",["Look at channel choice, device support, trial and refund terms. See {post:iptv-vs-streaming-apps}."])])

add("why-quality-varies-by-channel", "Why Picture Quality Varies Between Channels", Q,
 "Why some IPTV channels look sharper than others: source quality, resolution, bitrate, upscaling, sport versus news and your own screen.",
 "It is normal for one channel to look crisp while another looks soft. Several things explain it.",
 [("Source quality",["Each channel starts with its own source. Some are produced in high definition, others in lower resolution."]),
  ("Bitrate",["A channel sent with a low bitrate can look soft or blocky even at a high resolution."]),
  ("Upscaling",["Lower resolution video shown on a large screen is stretched, which softens it. See {post:upscaling-explained}."]),
  ("Content type",["Fast sport needs more data to look clean than a news desk. Your screen and viewing distance also affect what you notice."]),
  ("What you can do",["Check whether it is every channel or one. See {post:iptv-picture-pixelated}."])])

add("best-settings-for-smooth-playback", "Best App Settings for Smooth Playback", Q,
 "Settings worth checking in IPTV apps and devices for smoother playback: buffer size, hardware decoding, refresh rate and automatic quality.",
 "A few settings make a real difference. Change one at a time and test.",
 [("Hardware decoding",["Use the device's hardware decoder if the app offers it. It reduces load on the processor and heat."]),
  ("Buffer size",["A larger buffer gives more protection against short dips but increases start time and delay. Try a modest increase before a big evening."]),
  ("Quality",["If the app offers automatic quality, try it. If a stream struggles, pick a lower fixed quality."]),
  ("Refresh rate",["Let the device match the refresh rate to the content if your TV supports it. See {post:tv-motion-settings-and-sport}."]),
  ("Test method",["After each change, watch a busy live channel for twenty minutes. Revert anything that does not help."])])

add("tv-motion-settings-and-sport", "TV Motion Settings for Watching Sport", Q,
 "How motion smoothing and picture modes affect sport on your TV, with a simple way to compare modes and choose what looks natural.",
 "Your TV's picture processing can make sport look better or oddly artificial.",
 [("Motion smoothing",["This adds extra frames to make movement look smoother. Some people like it for sport. Others find it unnatural, a so-called soap opera look."]),
  ("Picture modes",["Standard or sport modes often balance brightness and colour. Vivid modes can exaggerate noise in compressed video."]),
  ("How to compare",["Watch the same live match with each mode for a few minutes and pick the one that looks natural to you. Change only one setting at a time."]),
  ("Note on delay",["Heavy processing can add small delay. Game mode reduces it but may look less polished. See {post:reduce-delay-in-live-sport-streams}."])])

add("upscaling-explained", "Upscaling Explained: Why SD Can Look Soft on a 4K TV", Q,
 "What upscaling is, why standard definition video looks soft on large 4K screens and what you can do to make it look better.",
 "A 4K TV has about eight million pixels. A standard definition picture has far fewer, so the TV must invent the rest.",
 [("What upscaling does",["Your TV or device stretches the lower resolution image to fill the screen and smooths the result. It cannot add real detail that was not in the source."]),
  ("Why SD looks softest",["The bigger the gap between source and screen, the softer the picture. HD upscaled looks better than SD upscaled."]),
  ("Helping it",[("ul",["Sit a little further back.","Try the TV's sharpness and noise reduction settings gently.","Prefer HD versions of channels when available."])]),
  ("Related",["See {post:why-quality-varies-by-channel}."])])

add("protect-your-router-for-streaming", "Protecting Your Router: Basics for Streamers", SE,
 "Simple steps to secure a home router: change the default password, update firmware, use WPA2 or WPA3 and review connected devices.",
 "Your router is the front door of your home network. A few habits keep it secure.",
 [("Change default passwords",["Replace the router's admin password and set a unique Wi-Fi password. Defaults are widely known."]),
  ("Use modern encryption",["Choose WPA2 or WPA3 for your Wi-Fi. Avoid older WEP or open networks."]),
  ("Keep firmware updated",["Check your provider's guidance. Many routers update automatically."]),
  ("Look at who is connected",["Most routers list connected devices. Remove ones you do not recognise and change the password."]),
  ("Guest network",["Use a guest network for visitors and smart devices so that your main devices stay separate."])])

add("passwords-and-two-factor-for-streaming", "Passwords and Two-Factor Basics for Streaming Accounts", SE,
 "How to protect streaming accounts: unique passwords, a password manager, two-factor login where offered and how to spot phishing messages.",
 "A stolen password is the most common way accounts are lost. These habits make that much harder.",
 [("Use unique passwords",["Never reuse a password between services. If one site is breached, the rest stay safe."]),
  ("Use a password manager",["It creates and stores long random passwords so you do not have to remember them."]),
  ("Turn on two-factor login",["Where a service offers it, enable it. Even if someone learns your password, they cannot sign in without the second step."]),
  ("Spot phishing",["Be wary of messages that create urgency or ask for codes or passwords. Go to the official site yourself instead of following links. See {post:iptv-scams-and-safe-payment}."])])

add("public-wifi-and-streaming", "Streaming on Public Wi-Fi: Risks and Habits", SE,
 "Is it safe to stream on hotel, cafe or airport Wi-Fi? Learn the risks, how to reduce them and why speeds are often poor.",
 "Public Wi-Fi is convenient but shared with strangers, and it is often slow.",
 [("Risks",["Other people on the same network may be able to attempt to observe traffic that is not encrypted. Fake networks with familiar names can also trick you."]),
  ("Reduce the risk",[("ul",["Confirm the network name with staff.","Use secure websites and apps that encrypt traffic.","Avoid entering payment details on public networks.","Consider a VPN from a trusted provider."])]),
  ("Quality expectations",["Many public networks limit speed and block some services. If a stream stutters, try your mobile data for a short test, keeping your allowance in mind."]),
  ("Related",["See {post:should-you-use-a-vpn-with-iptv}."])])

add("child-safety-and-streaming", "Child Safety and Streaming at Home", SE,
 "How to keep children safer when your home uses streaming services: profiles, PIN codes, device settings and conversations about what they see.",
 "Technology can help, but your involvement matters most.",
 [("Set up the basics",[("ul",["Use separate profiles and PINs on devices.","Lock app installs and purchases behind a PIN.","Use parental controls where apps offer them."])]),
  ("Know the limits",["No filter is perfect. Channel names and categories can be misleading, so check what a service actually contains. See {post:parental-controls-in-iptv-apps}."]),
  ("Talk to children",["Explain what to do if they see something upsetting: close it and tell you, without fear of being punished."]),
  ("Keep devices in shared spaces",["Where possible, keep screens in family rooms rather than behind closed doors."])])

add("iptv-for-students-and-shared-houses", "IPTV in Student and Shared Houses", UK,
 "Using IPTV in a student or shared house: shared Wi-Fi, stream limits, who pays, TV Licence questions and keeping the connection steady.",
 "Shared houses bring shared connections, shared costs and sometimes shared arguments about both.",
 [("The network",["Many people on one connection means evening congestion. Agree quiet times for big downloads and consider wiring the main TV."]),
  ("Plan and stream limits",["Check how many simultaneous streams a plan allows. One account used on several TVs at once may exceed it. See {post:how-many-devices-can-i-use-with-iptv}."]),
  ("Splitting the cost",["Agree who pays and what happens when someone leaves. A shorter term may suit changing households."]),
  ("TV Licence",["Licence rules differ for shared houses and student rooms, so check the official guidance. See {post:uk-tv-licence-and-iptv}."])])

add("uk-broadband-outage-what-to-do", "UK Broadband Outage: What to Do When Streaming Stops", UK,
 "When your internet goes down, how to tell whether it is local or wider, what to check, how to contact your provider and what compensation may exist.",
 "If everything stops at once, the cause is probably your broadband rather than your IPTV service.",
 [("Check the basics",["Restart the router. Check lights and cables. See whether a phone on mobile data can reach the internet, which shows whether the problem is your line."]),
  ("Is it wider?",["Use your provider's outage checker or social channels from your phone's mobile data."]),
  ("Contact your provider",["Report the fault with the times and what you tried. Keep a reference number."]),
  ("Compensation",["Many UK broadband providers take part in an automatic compensation scheme for certain delays and missed appointments. Check your provider's terms."]),
  ("In the meantime",["Use a phone as a hotspot only if your mobile plan has enough data. See {post:how-much-data-does-iptv-use}."])])

add("uk-consumer-rights-digital-services", "UK Consumer Rights for Digital Services: A Plain Overview", UK,
 "A short, general overview of consumer rights that may apply to digital services in the UK, and where to get official advice. Not legal advice.",
 "This is general information, not legal advice. Official sources are the best place to check your own position.",
 [("The idea behind the rules",["In the UK, consumer law generally expects digital content and services to be as described, of satisfactory quality and fit for the purpose you buy them for. Detailed rights depend on the situation."]),
  ("Where to check",["Citizens Advice and the government's consumer pages explain the rules in plain English. Use them rather than guessing."]),
  ("What you can do as a buyer",[("ul",["Read the terms and refund policy before paying.","Keep proof of what you were told.","Report faults promptly and in writing.","Use your payment method's dispute process if it applies."])]),
  ("Our position",["Our terms and refund policy are on the site. We cannot give legal advice. See {post:iptv-refund-expectations}."])])

add("iptv-across-the-four-nations", "UK Broadband Across the Four Nations for IPTV", UK,
 "How broadband and mobile coverage differ across the four UK nations and what it means for IPTV: rural lines, full fibre and testing before you subscribe.",
 "Connection quality varies more by street than by country, but some patterns matter for streaming.",
 [("Cities versus rural areas",["Towns and cities tend to have more choice of providers and faster options. Rural homes may rely on longer copper lines, fixed wireless or mobile broadband."]),
  ("Check your address",["Use provider checkers to see what is available at your exact address. Do not assume from the area."]),
  ("Test your own line",["Run speed tests at different times and note stability. For live television, consistency matters most. See {post:iptv-uk-broadband-guide}."]),
  ("If your line is weak",["A lower quality setting and a wired connection help. Ask us about a trial before committing, and see {post:streaming-internet-requirements}."])])

add("uk-sport-calendar-streaming-prep", "Planning Your Viewing Around the UK Sport Calendar", UK,
 "How to plan IPTV around the year's biggest UK sporting events: test early, avoid last minute fixes and know what to ask about availability.",
 "The sporting year has predictable busy periods. Plan for them as you would for any peak.",
 [("The pattern",["Football runs across the winter months, with big international tournaments in the summer. Major events in rugby, cricket, tennis, racing and boxing arrive on their own calendars."]),
  ("Before a big event",[("ul",["Test the app a week before.","Update the device and restart.","Check the guide times for the day.","Prepare a second device."])]),
  ("Availability",["Rights change and some events are only on certain channels. Always ask support about a specific event before you rely on it."]),
  ("Keep it calm",["Aim to be set up an hour early. See {post:iptv-for-live-sports-tips}."])])

add("canadian-broadband-for-iptv", "Canadian Broadband for IPTV: What Matters", CA,
 "What Canadian viewers should know about broadband for IPTV: connection types, data caps, rural access, evening congestion and testing before you subscribe.",
 "Canada's size means connection quality varies widely, so a careful test is more valuable than any rule of thumb.",
 [("Connection types",["Urban homes may have cable or fibre. Rural homes may have DSL, fixed wireless or satellite internet, which can have higher delay."]),
  ("Data caps",["Some plans have monthly data limits. Streaming uses data constantly, so estimate with {post:how-much-data-does-iptv-use} and read your plan terms."]),
  ("Test properly",["Run speed tests at your usual viewing time and watch for stability, not just the top number."]),
  ("Ask us",["We offer a trial so you can test on your own line. See {post:iptv-in-canada-what-to-know}."])])

add("iptv-devices-in-canada", "IPTV Setup on Common Devices in Canada", CA,
 "Which devices Canadian viewers commonly use for IPTV: smart TVs, Fire TV, Android TV, Apple TV and phones, and how to check support.",
 "The device choices are much the same as elsewhere, and the checks are the same too.",
 [("Common devices",[("ul",["Smart TVs from the major brands.","Amazon Fire TV devices.","Android TV and Google TV boxes.","Apple TV.","Phones and tablets."])]),
  ("Check before you pay",["Note your model and system version and send them to support. Our {devices} lists what we check."]),
  ("App stores in Canada",["Use the official store for your device in your region. Availability can differ slightly between countries, so check that your player appears in your store."]),
  ("Network",["Use a wired connection if you can, and see {post:iptv-wifi-vs-ethernet}."])])

add("canada-time-zones-and-live-guides", "Canadian Time Zones and Live TV Guides", CA,
 "Canada spans several time zones. Learn how to set your device correctly so that programme guides and live event start times line up.",
 "Canada has six main time zones, so live guide times are easy to misread if your device is set wrongly.",
 [("Set automatic time",["Turn on automatic date and time on your device and make sure it is set to your province's zone."]),
  ("Reading the guide",["Guides may show times in your device's zone or the source's zone. Compare a known programme to check."]),
  ("Live events",["An event described in one zone starts at a different clock time in another. Convert before you plan. See {post:what-is-epg-tv-guide}."]),
  ("If times look wrong",["Refresh the guide, restart the app and contact support with your location and the channel."])])

add("iptv-payment-and-currency-canada", "Paying a UK Provider From Canada: Currency and Checks", CA,
 "What Canadian customers should check when paying a UK based service: pounds sterling pricing, exchange rates, fees and keeping receipts.",
 "Our prices are in pounds sterling, so there is an exchange step when you pay from Canada.",
 [("Prices are in GBP",["The total you see on the {plans} is in pounds. Your payment method converts it from Canadian dollars."]),
  ("Check the final amount",["Exchange rates and fees vary by method. Check the amount your bank or payment app shows before you confirm."]),
  ("Methods",["PayPal, Binance Pay and Wise are accepted. See {post:iptv-payment-methods-explained} for how they differ."]),
  ("Keep records",["Save the receipt and our confirmation message in case you need to refer to it later."])])

add("can-i-pause-live-tv", "Can You Pause Live TV on IPTV?", FQ,
 "Whether you can pause or rewind live television on IPTV depends on the app and the service. Learn what to check and how buffering relates to pausing.",
 "Sometimes yes, sometimes only briefly, sometimes not at all.",
 [("Short pauses",["Most players keep a small buffer, so you can pause for a short time, but the player may jump back to live afterwards."]),
  ("Longer rewind",["Longer rewind needs storage on the service or on the device. Not all services provide it. See {post:catch-up-and-recording-explained}."]),
  ("How to find out",["Test during your trial: press pause, wait a minute, resume and see what happens. Ask support if unclear."])])

add("how-long-does-iptv-setup-take", "How Long Does IPTV Setup Take?", FQ,
 "How long IPTV setup normally takes, what slows it down and how to prepare so that you can be watching within minutes of receiving your details.",
 "For most people, setup is quick once the app is installed and the details are in hand.",
 [("The usual steps",["Check your device, request a trial or choose a plan, receive your details, install the app, sign in and test."]),
  ("What takes time",[("ul",["Updating an old device.","Downloading the app on a slow connection.","Loading a large channel list the first time.","Typing details by hand."])]),
  ("How to be quick",["Update and free space beforehand, have your details ready to paste, and use a stable connection. See {post:first-time-iptv-setup-checklist}."])])

add("why-some-channels-have-no-guide", "Why Some Channels Have No Programme Guide", FQ,
 "Why a few channels show no programme information: data matching, missing feeds, time zone mismatches and what to try.",
 "If most channels have a guide and a few do not, the issue is data, not your device.",
 [("Matching",["The guide data must be matched to each channel. If the match is missing, you see blanks."]),
  ("Feeds",["Some channels have no schedule data available, so there is nothing to show."]),
  ("What to try",[("ul",["Refresh the guide in the app.","Check your device time zone.","Wait after first sign-in while data downloads.","Tell support which channels are affected."])]),
  ("Related",["Read {post:what-is-epg-tv-guide}."])])

add("what-happens-when-subscription-expires", "What Happens When an IPTV Subscription Expires?", FQ,
 "What to expect when your IPTV subscription reaches its end date, how to renew, whether details change and how to avoid a gap in viewing.",
 "When your period ends, access stops until you renew. Knowing the date avoids an unwelcome surprise.",
 [("What you will see",["The app may show an empty list, a login error or a message about expired access. It looks like a sign-in problem, so check your date first."]),
  ("Renewing",["Contact us through the official route and confirm your plan and length. See {post:how-to-renew-iptv-safely}."]),
  ("Avoiding gaps",["Set a reminder a few days before the end date. Ask whether renewing early extends your current period or restarts it."]),
  ("Not renewing",["If you decide not to continue, you can simply let it end. Check the terms for anything you should do first."])])
