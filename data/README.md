# Breakdown of Data
Feature descriptions of the notification and context data for each user.
---

### 1. Feature detail of _notifications.csv_
* __appPackage__ - The app which posted the notification.
Unique values: 
       ['com.google.android.gm', 'com.tinder', 'com.facebook.katana',
       'com.spotify.music', 'com.samsung.android.scloud',
       'com.microsoft.office.outlook', 'com.instagram.android',
       'com.facebook.appmanager', 'com.samsung.android.lool',
       'com.sec.android.app.samsungapps', 'com.samsung.android.app.spage',
       'com.samsung.android.calendar', 'com.microsoft.skydrive',
       'com.google.android.gms', 'com.facebook.orca',
       'com.google.android.youtube', 'com.whatsapp',
       'com.sec.android.daemonapp', 'com.snapchat.android', 'ie.rte.news',
       'com.android.server.telecom', 'com.samsung.android.messaging',
       'com.sec.android.app.clockpackage', 'bbc.mobile.news.ww',
       'com.android.phone', 'com.android.mms', 'com.huawei.systemmanager',
       'com.google.android.googlequicksearchbox', 'com.nuance.swype.emui',
       'com.huawei.phoneservice', 'com.google.android.apps.maps',
       'com.android.chrome', 'com.samsung.android.email.provider',
       'flipboard.boxer.app', 'com.twitter.android',
       'com.sec.android.app.shealth', 'com.samsung.android.sm',
       'com.android.calendar', 'com.google.android.calendar',
       'com.mobisystems.office', 'com.udemy.android',
       'com.sec.android.app.sns3', 'com.vodafone.vodafone360updates',
       'com.amazon.dee.app', 'com.android.bluetooth',
       'com.blinkslabs.blinkist.android', 'com.ubercab',
       'com.google.android.apps.docs', 'com.sec.android.inputmethod',
       'com.cilabs.moneyconf', 'com.srkenl.confmzaywo',
       'org.mozilla.firefox', 'com.resurrection.ota',
       'projekt.substratum', 'com.android.messaging',
       'com.touchtype.swiftkey', 'com.android.dialer',
       'com.lyndir.masterpassword', 'org.thoughtcrime.securesms',
       'com.google.android.deskclock', 'org.fdroid.fdroid',
       'com.google.android.apps.messaging', 'com.viber.voip',
       'com.motorola.actions', 'at.bitfire.davdroid',
       'au.com.shiftyjelly.pocketcasts', 'com.fsck.k9', 'com.pof.android',
       'com.shapr', 'com.bskyb.sportnews',
       'fm.castbox.audiobook.radio.podcast', 'com.fitbit.FitbitMobile',
       'com.alibaba.aliexpresshd', 'com.meetup', 'uk.co.dominos.android',
       'com.netflix.mediaclient', 'com.bumble.app',
       'com.oneplus.screenshot', 'com.intermedia.hq', 'com.Slack',
       'com.revolut.revolut', 'com.oneplus.deskclock',
       'com.linkedin.android', 'com.asana.app', 'uk.co.bbc.goodfood2',
       'com.bankofireland.mobilebanking', 'com.ryanair.cheapflights',
       'taxi.android.client', 'com.deliveroo.orderapp',
       'com.ascendik.eyeshield', 'io.wia.wia', 'com.pzizz.android',
       'com.google.android.apps.photos', 'com.douglas.upflix',
       'com.google.android.music', 'ie.bambooapp.customer',
       'com.oneplus.opbackup', 'com.distilledmedia.thescore',
       'com.soundcloud.android', 'io.intercom.android',
       'com.google.android.apps.tachyon', 'com.mastercard.labs.qkr',
       'com.amazon.mShop.android.shopping', 'net.oneplus.weather',
       'com.pixonic.wwr', 'com.paddypower.sportsbook.u.inhouse']

* __category__ - The category of the notification, as set by the posting app.
Unique values: 
       ['email', 'unknown', 'msg', 'transport', 'event', 'status', 'call',
       'alarm', 'recommendation', 'err', 'service', 'reminder']

* __numberOfUpdates__ - The number of times the posting app updated the contents of the notification.
Unique values: 
        ['none', 'low', 'medium', 'high']
        
* __subject__ - The subject of the notification content.
Unique values:
        ['unknown', 'online communities', 'web services', 'education',
       'reference', 'politics', 'air travel', 'computer science',
       'computers & electronics', 'tv shows & programs',
       'autos & vehicles', 'internet & telecom', 'email & messaging',
       'books & literature', 'neuroscience', 'people & society',
       'arts & entertainment', 'sports', 'music & audio',
       'mobile apps & add-ons', 'candy & sweets',
       'colleges & universities', 'business & industrial',
       'holidays & seasonal events', 'social networks',
       'corporate events', 'jobs & education', 'finance',
       'computer security', 'fitness', 'e-commerce services',
       'dating & personals', 'news', 'online video',
       'consumer electronics', 'travel', 'beauty & fitness',
       'credit cards', 'hotels & accommodations', 'pets & animals',
       'residential rentals', 'software', 'food & grocery retailers',
       'special occasions', 'business services', 'hobbies & leisure',
       'movies', 'restaurants', 'science', 'food & drink', 'food', 'golf',
       'adult', 'accounting & auditing', 'nutrition', 'job listings',
       'engineering & technology', 'coffee & tea', 'basketball',
       'text & instant messaging', 'insurance', 'online media',
       'shopping', 'footwear', 'audio equipment', 'government',
       'hair care', 'service providers', 'team sports', 'tv & video',
       'sensitive subjects', 'gambling', 'security products & services',
       'motor vehicles (by type)', 'games', 'sports news', 'soccer',
       'motor sports', 'cycling', 'tourist destinations', 'maps',
       'bus & rail', 'family', 'individual sports', 'admin',
       'religion & belief', 'oral & dental care', 'health',
       'law & government', 'charity & philanthropy', 'military',
       'cooking & recipes', 'online image galleries',
       'social issues & advocacy', 'health conditions', 'pain management',
       'earth sciences', 'food and drink', 'world music',
       'primary & secondary schooling (k-12)', 'legal',
       'photographic & digital arts', 'investing', 'other',
       'vehicle parts & accessories', 'apparel', 'humor',
       'casual apparel', 'cards & greetings', 'mail & package delivery',
       'currencies & foreign exchange', 'fiber & textile arts',
       'racquet sports', 'astronomy', 'enterprise technology',
       'foreign language resources', 'banking', 'computer & video games',
       'college sports', 'training & certification', 'rugby',
       'fun tests & silly surveys', 'transportation & logistics',
       'billing & invoicing', 'networking', 'coupons & discount offers',
       'lottery', 'real estate listings', 'rock music', 'programming',
       'special & restricted diets', 'dictionaries & encyclopedias',
       'urban & hip-hop', 'radio', 'simulation games',
       'network monitoring & management', 'hiking & camping',
       'classical music', 'scientific institutions', 'e-books',
       'events & listings', 'pop music', 'mathematics', 'performing arts',
       'expos & conventions', 'biological sciences', 'country music',
       'career resources & planning', 'mobile & wireless',
       'business operations', 'credit & lending', 'virtual worlds',
       'real estate', 'international sports competitions',
       'american football', 'residential sales', 'poetry',
       'comics & animation', 'family & relationships',
       'standardized & admissions tests', 'business and industrial',
       'other - conversation chatter', 'chemicals industry',
       'space technology', 'crafts', 'music reference', 'desserts',
       'beverages', 'crime & justice', 'funny pictures & videos', 'jobs',
       'internet software', 'combat sports', 'libraries & museums',
       'computer hardware', 'clip art & animated gifs',
       'green living & environmental issues', 'marriage',
       "children's literature", 'distance learning',
       'biographies & quotations', 'cricket', 'boxing', 'food service',
       'martial arts', 'electronic components',
       'electronics & electrical', 'law enforcement', 'public safety',
       'clothing accessories', 'bed & bath', 'construction & maintenance',
       'visual art & design', 'animal sports', 'roleplaying games',
       'pizzerias', 'wrestling', 'baked goods', 'home & garden',
       'medical facilities & services', 'weddings',
       'hybrid & alternative vehicles', 'general reference', 'horses',
       'hockey', 'home storage & shelving', 'multimedia software',
       'entertainment media', 'energy & utilities', 'weather', 'wildlife',
       'legal services', 'fast food', 'car rental & taxi services',
       'emergency services']
       
* __priority__ - The priority of the notification as set by the posting app.
Unique values:
        ['default', 'high', 'max', 'low', 'unknown', 'min']
        
* __ongoing__ - Whether or not notification is classified as _ongoing_ such that it stays in the notification bar as a task completes.
Unique values: 
        [False, True]
        
* __visibility__ - The visibility level of the notification as set by the posting app. _Private_ = Show this notification on all lockscreens, but conceal sensitive or private information on secure lockscreens; _Public_ = Show this notification in its entirety on all lockscreens; _Secret_ = Do not reveal any part of this notification on a secure lockscreen.
Unique values:
        ['private', 'public', 'secret']
        
        
### 2. Feature detail of *context_on_posting.csv*

* _day_ - The day the notification was posted. 0 = Monday; 6 = Sunday.
Unique values: 
        [0, 1, 2, 3, 4, 5, 6]
    
* _time_ - The time of the day the notification was posted. Unique values:
        ['night', 'morning', 'afternoon', 'evening', 'early-morning']
        
* _place_ - The type of place in which the notification was received. Unique values:
        ['TYPE_ACCOUNTING', 'TYPE_AIRPORT', 'TYPE_AMUSEMENT_PARK', 'TYPE_AQUARIUM',
         'TYPE_ART_GALLERY', 'TYPE_ATM', 'TYPE_BAKERY', 'TYPE_BANK', 'TYPE_BAR',
         'TYPE_OTHER']
         
* _activity_ - The activity identified by the device when the notification was posted. Unique values:
        ['still', 'unknown', 'foot walking', 'vehicle', 'tilting',
       'foot running', 'bicycle']
       
* _noise_ - The average noise (over 5 seconds) of the surrounding environment when the notification was posted. Unique values:
        ['low', 'medium', 'high']
        
* _batteryLevel_ - The battery level of the device when the notification was posted. Unique values:
        ['low', 'high', 'medium']
        
* _charging_ - Whether or not the device was charging when the notification was posted. Unique values:
        [True, False]
        
* _headphonesIn_ - Whether or not the headphones were connected to the device when the notification was posted. Unique values:
        [False,  True]
   
* _musicActive_ - Whether or not the device was playing music when the notification was posted. Unique values:
        [False,  True]
        
* _proximity_ - Level of how close something was to the front of the device when the notification was posted, ranging from near to medium to far. Unique values:
        ['med', 'near', 'far']
        
* _ringerMode_ - The ringer mode of the device when the notification was posted. Unique values:
        ['vibrate', 'normal', 'silent']
        
* _lightIntensity_ - The level of light ambience sensed by the device when the notification was posted. Unique values:
        ['low', 'med', 'high']
        
        
### 3. Feature detail of *context_on_removal.csv*
       
* _activity_ - The activity identified by the device when the notification was posted. Unique values:
       ['still', 'unknown', 'vehicle', 'tilting', 'foot walking',
       'bicycle']
       
* _noise_ - The average noise (over 5 seconds) of the surrounding environment when the notification was posted. Unique values:
        ['low', 'medium', 'high']
        
* _batteryLevel_ - The battery level of the device when the notification was posted. Unique values:
        ['low', 'high', 'medium']
        
* _charging_ - Whether or not the device was charging when the notification was posted. Unique values:
        [True, False]
        
* _contactSignificantContext_ - Whether or not the contact sending the notification was significant to the context. Unique values:
        [True, False]
        
* _contactSignificantOverall_ - Whether or not the contact sending the notification was significant to the user based on the history of previous notifications opened/dismissed. Unique values:
         [True, False]
         
* _decisionTime_ - The time taken (in seconds) from when the user saw the new notification to when they acted upon it (opened/dismissed it).
        
* _headphonesIn_ - Whether or not the headphones were connected to the device when the notification was posted. Unique values:
        [False,  True]
        
* _lightIntensity_ - The level of light ambience sensed by the device when the notification was posted. Unique values:
        ['low', 'med', 'high']
   
* _musicActive_ - Whether or not the device was playing music when the notification was posted. Unique values:
        [False,  True]
        
* _place_ - The type of place in which the notification was received. Unique values:
        ['TYPE_ACCOUNTING', 'TYPE_AIRPORT', 'TYPE_AMUSEMENT_PARK', 'TYPE_AQUARIUM',
         'TYPE_ART_GALLERY', 'TYPE_ATM', 'TYPE_BAKERY', 'TYPE_BANK', 'TYPE_BAR',
         'TYPE_OTHER']
        
* _proximity_ - Level of how close something was to the front of the device when the notification was posted, ranging from near to medium to far. Unique values:
        ['med', 'near', 'far']
        
* _responseTime_ - The time taken (in seconds) from when the notification was posted to the device to when the user acted upon it (opened/dismissed it).
        
* _ringerMode_ - The ringer mode of the device when the notification was posted. Unique values:
        ['vibrate', 'normal', 'silent']
        
* _seenTime_ - The time taken (in seconds) from when the notification was posted to the device to when the user noticed it.

* _action_ - The action taken by the user on the notification. _True_ = Notification opened; _False_ = Notification dismissed. Unique values:
        [True, False]

* _timeAppLastUsed_ - The amount of time since the user last used the app which posted the notification. Unique values:
        ['over a week ago', 'within last week', 'immediate',
       'within half hour', 'within 24 hours', 'within hour', 'few hours',
       'few mins']
     
* _postDate_ - The datetime the notification was posted to the device.

* _removedDate_ - The datetime the notification was removed from the device.