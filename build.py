"""Builds the Dawa2 website (English at /, Arabic at /ar/) from one template.

Run: python build.py   (writes index.html, privacy.html, ar/index.html, ar/privacy.html)
Policy texts live in content/privacy.en.html and content/privacy.ar.html.
"""

import os

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = "amrcs92/dawa2-site"
SITE = "https://amrcs92.github.io/dawa2-site/"
DOWNLOAD = f"https://github.com/{REPO}/releases/latest/download/dawa2.apk"
RELEASES = f"https://github.com/{REPO}/releases"
CONTACT = "amrcs1992@gmail.com"

ICONS = {
    "bell": '<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20a2 2 0 0 0 4 0"/><path d="M3.5 7.5A9 9 0 0 1 6 4M20.5 7.5A9 9 0 0 0 18 4"/>',
    "power": '<path d="M12 3v8"/><path d="M6.3 7.3a8 8 0 1 0 11.4 0"/>',
    "pill": '<rect x="3.5" y="8.5" width="17" height="7" rx="3.5" transform="rotate(-45 12 12)"/><path d="m9.2 9.2 5.6 5.6"/>',
    "calendar": '<rect x="3.5" y="5" width="17" height="15.5" rx="3"/><path d="M3.5 10h17M8 3v4M16 3v4"/><path d="m9 15 2 2 4-4"/>',
    "chart": '<path d="M4 20h16"/><rect x="5.5" y="12" width="3" height="5" rx="1"/><rect x="10.5" y="8" width="3" height="9" rx="1"/><rect x="15.5" y="5" width="3" height="12" rx="1"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/>',
    "check": '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    "download": '<path d="M12 4v11M7 10l5 5 5-5M5 20h14"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6 6 6M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/>',
    "moon": '<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/>',
    "layers": '<rect x="4" y="4" width="16" height="5" rx="2"/><rect x="4" y="11" width="16" height="5" rx="2"/><path d="M7 20h10"/>',
    "shield": '<path d="M12 3 5 6v5c0 4.5 3 8.3 7 10 4-1.7 7-5.5 7-10V6z"/><path d="m9 12 2 2 4-4"/>',
    "save": '<path d="M5 4h11l3 3v13H5z"/><path d="M8 4v5h7V4M8 20v-6h8v6"/>',
}


def icon(name):
    return (
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" '
        f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'
    )


T = {
    "en": {
        "dir": "ltr",
        "title": "Dawa2 · Medication reminders with real alarms for Android",
        "desc": "Dawa2 is a free, private medication reminder for Android in English and Arabic. Real full-screen alarms that keep ringing until you answer. No account, no cloud.",
        "nav": ["Features", "Screenshots", "Install", "Privacy"],
        "other_lang": "العربية",
        "download": "Download",
        "eyebrow": "Free for Android · Private and offline",
        "h1": "Your medicines, on time.",
        "lead": "Dawa2 (<bdi>دواء</bdi>, “medicine”) rings a real full-screen alarm for every dose, and it keeps ringing until you answer: <strong>Taken</strong>, <strong>Snooze</strong> or <strong>Skip</strong>. Every answer goes into a private history on your phone, in English or Arabic.",
        "cta": "Download for Android",
        "cta2": "See screenshots",
        "meta": "Android 7.0 or later (64-bit) · Free · About 38 MB",
        "trust": ["No account", "No cloud", "No ads", "Works offline", "English and Arabic"],
        "features_h": "An alarm you can't miss",
        "features_p": "Most reminder apps send a notification that is easy to swipe away. Dawa2 uses a real alarm, and remembers what you did.",
        "features": [
            ("bell", "Keeps ringing until you answer", "A full-screen alarm over the lock screen, and over other apps if you allow it. Touching the screen or opening the notification shade doesn't silence it: only Taken, Snooze or Skip do. It can also read the medicine aloud."),
            ("power", "Rings through everything", "Exact alarms ring through Doze, battery saver and restarts, and keep going even if you don't open the app for days. Unanswered doses ring once more."),
            ("pill", "Every kind of medicine", "Tablets, capsules, syrups, drops, sprays, inhalers, injections, creams, patches and more, each with its own dose rules and safety notes, added in four short steps."),
            ("calendar", "Schedules that fit your day", "Every day or chosen weekdays, several times a day, with start and end dates. Pause for a few days or stop with a reason, without counting those days as missed."),
            ("chart", "Today and history", "The next dose and a progress ring, a “Did you take it?” follow-up for unanswered alarms, a history log and insights. Dismissed is never counted as taken."),
            ("globe", "English and Arabic", "Full right-to-left Arabic with correct plurals, Western digits so doses match the label, and light and dark themes with checked contrast, down to the alarm screen."),
            ("layers", "Several medicines at once", "When doses are due together, one alarm screen lists them all, each with Taken, Snooze and Skip, plus “I've taken all” and “Snooze all”. It keeps ringing until every dose is answered, with a moment to undo."),
            ("shield", "Ready in a minute", "On first launch Dawa2 walks you through the few Android permissions an alarm needs, and Today warns you if one gets turned off later, so a reminder never fails silently."),
            ("save", "Backup and export", "Export your history as a spreadsheet (CSV) or back up everything to a file and restore it on a new phone. Only when you choose: nothing is ever sent anywhere."),
        ],
        "gallery_h": "A closer look",
        "gallery_p": "Nine screens from a real phone, in light and dark.",
        "light": "Light",
        "dark": "Dark",
        "shots": [("today", "Today"), ("alarm", "Alarm"), ("alarm-multi", "Several at once"), ("medicines", "Medicines"), ("add", "Add medicine"), ("insights", "Insights"), ("settings", "Settings"), ("settings-speak", "Speak the title"), ("medicine-delete", "Delete a medicine")],
        "onboarding_h": "A guided first launch",
        "onboarding_p": "Dawa2 shows how the alarm works and what stays private, then turns on each permission in one tap. If something stays off, it says so, and you can still continue.",
        "onboarding": [("onboarding-1-welcome", "Welcome"), ("onboarding-2-alarm", "The alarm"), ("onboarding-3-together", "Together + history"), ("onboarding-4-privacy", "Privacy"), ("onboarding-5-permissions", "Permissions"), ("onboarding-6-ready", "Ready")],
        "install_h": "Install in a minute",
        "install_p": "Dawa2 isn't on Google Play. Download the APK and install it directly.",
        "card_h": "Dawa2 for Android",
        "card_p": "The latest version, ready to install.",
        "facts": ["Version", "Size", "Requires"],
        "requires": "Android 7.0+",
        "checksum": "SHA-256",
        "steps": [
            ("Download the APK", "Tap Download on your Android phone. The file is called dawa2.apk."),
            ("Allow the install", "Open the file. If Android asks, allow installing apps from your browser or file manager."),
            ("Open Dawa2", "A short first-launch guide shows how the alarm works, then turns on what alarms need, one tap each: notifications, exact alarms and the alarm over the lock screen. “Battery: unrestricted” and “Alarm over other apps” are optional but recommended."),
        ],
        "note": "Google Play Protect may warn about an unrecognized app. That's expected, because Dawa2 isn't on Google Play. Tap “More details” › “Install anyway”. New versions install over the old one and keep your data.",
        "privacy_h": "Private by design",
        "privacy_p": "Your medicines are nobody else's business. Dawa2 has no servers to send them to: everything stays on your phone.",
        "privacy_link": "Read the privacy policy",
        "checks": [
            "No account and no sign-up",
            "No servers, cloud sync, analytics or ads",
            "Medicines and history stay on your phone",
            "Backups and exports only when you make them, and only where you send them",
        ],
        "faq_h": "Questions",
        "faq": [
            ("Is Dawa2 free?", "Yes. No ads, no subscriptions and no in-app purchases."),
            ("Does it need the internet?", "No. Dawa2 works fully offline and its own code makes no network requests."),
            ("How do I move to a new phone?", "Use Settings › Back up everything and keep the file somewhere safe, then restore it on the new phone. Android's automatic backup is off, so uninstalling the app deletes your data."),
            ("Does Dawa2 give medical advice?", "No. It records exactly what you enter and never suggests or changes doses."),
            ("Which phones are supported?", "Android 7.0 or later on a 64-bit (arm64) phone, which covers almost every phone from recent years. Some brands hold apps back in the background; turning on “Battery: unrestricted” keeps alarms on time."),
            ("Why does an alarm show only as a banner?", "While you use your phone, Android shows alarms as a banner unless the app may display over other apps. Allow “Alarm over other apps” in Settings › Alarm readiness, and alarms take the whole screen."),
        ],
        "privacy": "Privacy policy",
        "contact": "Contact",
        "rights": "Dawa2 · دواء",
        "loading": "Latest",
        "news_h": "What's new in",
        "news_link": "What's new in",
        "all_versions": "All versions and changes",
        "policy_title": "Privacy policy · Dawa2",
        "theme": "Switch light or dark",
    },
    "ar": {
        "dir": "rtl",
        "title": "دواء · تذكير بالأدوية بمنبّهات حقيقية لأندرويد",
        "desc": "دواء تطبيق مجاني وخاص للتذكير بالأدوية على أندرويد بالعربية والإنجليزية. منبّه حقيقي بملء الشاشة يستمر بالرنين حتى تجيب. بلا حساب ولا سحابة.",
        "nav": ["المزايا", "لقطات الشاشة", "التثبيت", "الخصوصية"],
        "other_lang": "English",
        "download": "تنزيل",
        "eyebrow": "مجاني لأندرويد · خاص ويعمل دون إنترنت",
        "h1": "أدويتك في موعدها.",
        "lead": "يرنّ «دواء» بمنبّه حقيقي بملء الشاشة لكل جرعة، ويستمر بالرنين حتى تجيب: <strong>تناولتها</strong> أو <strong>غفوة</strong> أو <strong>تخطّي الجرعة</strong>. وتُحفظ كل إجابة في سجل خاص على هاتفك، بالعربية أو الإنجليزية.",
        "cta": "نزّل لأندرويد",
        "cta2": "شاهد لقطات الشاشة",
        "meta": "أندرويد 7.0 أو أحدث (64-بت) · مجاني · نحو 38 ميغابايت",
        "trust": ["بلا حساب", "بلا سحابة", "بلا إعلانات", "يعمل دون إنترنت", "عربي وإنجليزي"],
        "features_h": "منبّه لا يفوتك",
        "features_p": "معظم تطبيقات التذكير ترسل إشعاراً يسهل تجاهله. أما «دواء» فيستخدم منبّهاً حقيقياً، ويتذكّر ما فعلت.",
        "features": [
            ("bell", "يرنّ حتى تجيب", "منبّه بملء الشاشة فوق شاشة القفل، وفوق التطبيقات الأخرى إن سمحت بذلك. لمس الشاشة أو فتح لوحة الإشعارات لا يُسكته؛ وحدها «تناولتها» أو «تأجيل» أو «تخطٍّ» تفعل. ويمكنه أيضًا قراءة اسم الدواء بصوت عالٍ."),
            ("power", "يرنّ مهما حدث", "منبّهات دقيقة ترنّ رغم وضع السكون وتوفير البطارية وإعادة التشغيل، وتستمر حتى لو لم تفتح التطبيق أياماً. والجرعة التي لم تُجب عنها ترنّ مرة أخرى."),
            ("pill", "لكل أنواع الأدوية", "أقراص وكبسولات وشراب وقطرات وبخاخات وأجهزة استنشاق وحقن وكريمات ولصقات وغيرها، لكلٍّ قواعد جرعته وملاحظات السلامة الخاصة به، تُضاف في أربع خطوات قصيرة."),
            ("calendar", "مواعيد تناسب يومك", "كل يوم أو أيام محددة، عدة مرات في اليوم، مع تاريخ بداية ونهاية. أوقف مؤقتاً لبضعة أيام أو نهائياً مع ذكر السبب، دون أن تُحسب تلك الأيام فائتة."),
            ("chart", "اليوم والسجل", "الجرعة التالية وحلقة التقدّم، وسؤال «هل أخذتها؟» للمنبّهات التي لم تُجب، وسجل يومي وإحصاءات. والتجاهل لا يُحسب أبداً تناولاً للجرعة."),
            ("globe", "العربية والإنجليزية", "عربية كاملة من اليمين لليسار مع جمع صحيح (قرص · قرصان · أقراص)، وأرقام غربية لتطابق الجرعة ما على العلبة، ومظهر فاتح وداكن بتباين مدروس حتى شاشة المنبّه."),
            ("layers", "عدة أدوية معاً", "عندما يحين موعد عدة جرعات معاً، تعرضها شاشة منبّه واحدة، لكلٍّ منها «تناولتها» و«تأجيل» و«تخطٍّ»، ومعها «تناولتها كلها» و«تأجيل الكل». ويستمر الرنين حتى تجيب عن كل الجرعات، مع لحظة للتراجع."),
            ("shield", "جاهز في دقيقة", "عند أول تشغيل يرشدك «دواء» إلى أذونات أندرويد القليلة التي يحتاجها المنبّه، وتنبّهك شاشة اليوم إن تعطّل أحدها لاحقاً، كي لا يفشل التذكير بصمت."),
            ("save", "نسخ احتياطي وتصدير", "صدّر سجلّك جدولاً (CSV) أو انسخ كل شيء احتياطياً في ملف واستعده على هاتف جديد. فقط حين تختار ذلك: لا يُرسل شيء إلى أي مكان."),
        ],
        "gallery_h": "نظرة أقرب",
        "gallery_p": "تسع شاشات من هاتف حقيقي، بالمظهر الفاتح والداكن.",
        "light": "فاتح",
        "dark": "داكن",
        "shots": [("today", "اليوم"), ("alarm", "المنبّه"), ("alarm-multi", "عدة أدوية معاً"), ("medicines", "الأدوية"), ("add", "إضافة دواء"), ("insights", "الإحصاءات"), ("settings", "الإعدادات"), ("settings-speak", "قراءة العنوان"), ("medicine-delete", "حذف دواء")],
        "onboarding_h": "أول تشغيل بخطوات واضحة",
        "onboarding_p": "يوضح «دواء» كيف يعمل المنبّه وما يبقى خاصًا، ثم يفعّل كل إذن بلمسة واحدة. وإن بقي شيء متوقفًا يخبرك بذلك، ويمكنك المتابعة رغم ذلك.",
        "onboarding": [("onboarding-1-welcome", "الترحيب"), ("onboarding-2-alarm", "المنبّه"), ("onboarding-3-together", "معًا والسجل"), ("onboarding-4-privacy", "الخصوصية"), ("onboarding-5-permissions", "الأذونات"), ("onboarding-6-ready", "جاهز")],
        "install_h": "ثبّته في دقيقة",
        "install_p": "«دواء» غير متاح على Google Play. نزّل ملف APK وثبّته مباشرة.",
        "card_h": "دواء لأندرويد",
        "card_p": "أحدث إصدار، جاهز للتثبيت.",
        "facts": ["الإصدار", "الحجم", "يتطلّب"],
        "requires": "أندرويد 7.0+",
        "checksum": "SHA-256",
        "steps": [
            ("نزّل ملف APK", "اضغط «تنزيل» على هاتفك الأندرويد. اسم الملف dawa2.apk."),
            ("اسمح بالتثبيت", "افتح الملف. إذا طلب أندرويد ذلك، اسمح بتثبيت التطبيقات من المتصفح أو مدير الملفات."),
            ("افتح «دواء»", "يوضح دليل أول تشغيل القصير كيف يعمل المنبّه، ثم يفعّل ما تحتاجه المنبّهات بلمسة لكل منها: الإشعارات والمنبّهات الدقيقة والمنبّه فوق شاشة القفل. أما «البطارية: بلا قيود» و«المنبّه فوق التطبيقات الأخرى» فاختياريان لكنهما مستحسنان."),
        ],
        "note": "قد يحذّرك Google Play Protect من تطبيق غير معروف، وهذا متوقّع لأن «دواء» غير متاح على Google Play. اضغط «مزيد من التفاصيل» ثم «التثبيت على أي حال». الإصدارات الجديدة تُثبَّت فوق القديمة وتحتفظ ببياناتك.",
        "privacy_h": "الخصوصية من الأساس",
        "privacy_p": "أدويتك شأنك وحدك. ليس لدى «دواء» خوادم يرسلها إليها: كل شيء يبقى على هاتفك.",
        "privacy_link": "اقرأ سياسة الخصوصية",
        "checks": [
            "بلا حساب ولا تسجيل",
            "بلا خوادم ولا مزامنة سحابية ولا تحليلات ولا إعلانات",
            "أدويتك وسجلك يبقيان على هاتفك",
            "النسخ الاحتياطي والتصدير فقط حين تطلبهما، وإلى حيث ترسلهما فقط",
        ],
        "faq_h": "أسئلة شائعة",
        "faq": [
            ("هل «دواء» مجاني؟", "نعم. بلا إعلانات ولا اشتراكات ولا مشتريات داخل التطبيق."),
            ("هل يحتاج إلى الإنترنت؟", "لا. يعمل «دواء» دون إنترنت بالكامل، ولا يرسل التطبيق نفسه أي طلبات عبر الشبكة."),
            ("كيف أنتقل إلى هاتف جديد؟", "من الإعدادات › «نسخ احتياطي لكل شيء» احفظ الملف في مكان آمن، ثم استعده على الهاتف الجديد. النسخ الاحتياطي التلقائي في أندرويد معطّل، لذا فحذف التطبيق يحذف بياناتك."),
            ("هل يقدّم «دواء» نصائح طبية؟", "لا. يسجّل ما تُدخله كما هو، ولا يقترح الجرعات ولا يغيّرها أبداً."),
            ("ما الهواتف المدعومة؟", "أندرويد 7.0 أو أحدث على هاتف 64-بت (arm64)، وهذا يشمل معظم هواتف السنوات الأخيرة. بعض الشركات تقيّد التطبيقات في الخلفية؛ وتفعيل «البطارية: بلا قيود» يُبقي المنبّهات في موعدها."),
            ("لماذا يظهر المنبّه كإشعار فقط؟", "أثناء استخدامك للهاتف، يعرض أندرويد المنبّهات كإشعار ما لم يُسمح للتطبيق بالظهور فوق التطبيقات الأخرى. فعّل «المنبّه فوق التطبيقات الأخرى» من الإعدادات › جاهزية المنبّه، ليظهر المنبّه بملء الشاشة."),
        ],
        "privacy": "سياسة الخصوصية",
        "contact": "للتواصل",
        "rights": "دواء · Dawa2",
        "loading": "الأحدث",
        "news_h": "الجديد في الإصدار",
        "news_link": "الجديد في الإصدار",
        "all_versions": "كل الإصدارات وتغييراتها",
        "policy_title": "سياسة الخصوصية · دواء",
        "theme": "التبديل بين الفاتح والداكن",
    },
}


def head(t, lang, prefix, title):
    return f"""<!doctype html>
<html lang="{lang}" dir="{t['dir']}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{t['desc']}">
  <meta name="theme-color" content="#0F766E">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{t['desc']}">
  <meta property="og:image" content="{SITE}assets/icon.png">
  <link rel="icon" href="{prefix}assets/icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=IBM+Plex+Sans+Arabic:wght@400;500;700&family=Plus+Jakarta+Sans:wght@700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}style.css">
  <script>try {{ const t = localStorage.getItem('theme'); if (t === 'light' || t === 'dark') document.documentElement.dataset.theme = t; }} catch (e) {{}}</script>
</head>
<body>
"""


def topbar(t, lang, prefix, home, other_href, anchors=True):
    logo = (
        f'<a class="brand" href="{home}"><img class="logo-light" src="{prefix}assets/logo-{lang}-light.png" alt="{t["rights"]}">'
        f'<img class="logo-dark" src="{prefix}assets/logo-{lang}-dark.png" alt="{t["rights"]}"></a>'
    )
    ids = ["features", "screenshots", "install", "privacy"]
    links = "".join(f'<a href="{home if not anchors else ""}#{i}">{n}</a>' for i, n in zip(ids, t["nav"]))
    return f"""  <header class="topbar">
    <div class="container">
      {logo}
      <nav class="links" aria-label="Sections">{links}</nav>
      <a class="lang-switch" href="{other_href}" hreflang="{'ar' if lang == 'en' else 'en'}">{t['other_lang']}</a>
      <button type="button" class="theme-toggle" aria-label="{t['theme']}" title="{t['theme']}"><span class="sun">{icon('sun')}</span><span class="moon">{icon('moon')}</span></button>
      <a class="btn btn-primary btn-sm" href="{DOWNLOAD}">{icon('download')}{t['download']}</a>
    </div>
  </header>
"""


def footer(t, lang, prefix, home, privacy):
    return f"""  <footer>
    <div class="container">
      <a href="{home}"><img class="logo-light" src="{prefix}assets/logo-{lang}-light.png" alt="{t['rights']}"><img class="logo-dark" src="{prefix}assets/logo-{lang}-dark.png" alt="{t['rights']}"></a>
      <nav>
        <a href="{privacy}">{t['privacy']}</a>
        <a href="mailto:{CONTACT}">{t['contact']}: {CONTACT}</a>
        <a href="{DOWNLOAD}">{t['download']}</a>
      </nav>
    </div>
  </footer>
  <script>
    // Light / dark switch: starts from the phone's setting, remembers the visitor's choice.
    const isDark = () =>
      document.documentElement.dataset.theme
        ? document.documentElement.dataset.theme === 'dark'
        : matchMedia('(prefers-color-scheme: dark)').matches;
    document.querySelector('.theme-toggle').addEventListener('click', () => {{
      const next = isDark() ? 'light' : 'dark';
      document.documentElement.dataset.theme = next;
      try {{ localStorage.setItem('theme', next); }} catch (e) {{}}
      document.dispatchEvent(new CustomEvent('themechange', {{ detail: next }}));
    }});
  </script>
"""


def index(lang):
    t = T[lang]
    prefix = "../" if lang == "ar" else ""
    other = "../" if lang == "ar" else "ar/"
    shots = lambda theme, items=t["shots"]: "".join(
        f'<figure><div class="phone"><img loading="lazy" src="{prefix}assets/shots/{lang}-{theme}-{k}.png" '
        f'data-light="{prefix}assets/shots/{lang}-light-{k}.png" data-dark="{prefix}assets/shots/{lang}-dark-{k}.png" '
        f'alt="{name}" width="540" height="1125"></div><figcaption>{name}</figcaption></figure>'
        for k, name in items
    )
    features = "".join(
        f'<div class="feature"><div class="icon">{icon(i)}</div><h3>{h}</h3><p>{p}</p></div>' for i, h, p in t["features"]
    )
    trust = "".join(f"<li>{icon('check')}{x}</li>" for x in t["trust"])
    steps = "".join(f"<li><h4>{h}</h4><p>{p}</p></li>" for h, p in t["steps"])
    checks = "".join(f"<li>{icon('check')}<span>{x}</span></li>" for x in t["checks"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    html = head(t, lang, prefix, t["title"]) + topbar(t, lang, prefix, "./", other) + f"""
  <main>
    <section class="hero">
      <div class="container">
        <div>
          <span class="eyebrow"><span class="dot"></span>{t['eyebrow']}</span>
          <h1>{t['h1']}</h1>
          <p class="lead">{t['lead']}</p>
          <div class="cta">
            <a class="btn btn-primary" href="{DOWNLOAD}">{icon('download')}{t['cta']}</a>
            <a class="btn btn-ghost" href="#screenshots">{t['cta2']}</a>
          </div>
          <p class="meta">{t['meta']}</p>
          <p class="release-line"><a href="#whats-new">{t['news_link']} <span class="rel-v" dir="ltr">{t['loading']}</span></a><span aria-hidden="true">·</span><a href="{RELEASES}">{t['all_versions']}</a></p>
        </div>
        <div class="phones" aria-hidden="true">
          <div class="phone back"><img src="{prefix}assets/shots/{lang}-dark-alarm.png" alt="" width="540" height="1125"></div>
          <div class="phone front"><img src="{prefix}assets/shots/{lang}-light-today.png" alt="" width="540" height="1125"></div>
        </div>
      </div>
    </section>

    <div class="trust"><div class="container"><ul>{trust}</ul></div></div>

    <section class="block" id="features">
      <div class="container">
        <div class="section-head"><h2>{t['features_h']}</h2><p>{t['features_p']}</p></div>
        <div class="features">{features}</div>
      </div>
    </section>

    <section class="block" id="screenshots" style="background: var(--bg2)">
      <div class="container">
        <div class="section-head"><h2>{t['gallery_h']}</h2><p>{t['gallery_p']}</p></div>
        <div class="gallery-bar"><div class="seg" role="group">
          <button type="button" data-theme="light" aria-pressed="true">{t['light']}</button>
          <button type="button" data-theme="dark" aria-pressed="false">{t['dark']}</button>
        </div></div>
        <div class="gallery">{shots('light')}</div>
      </div>
    </section>

    <section class="block" id="first-launch">
      <div class="container">
        <div class="section-head"><h2>{t['onboarding_h']}</h2><p>{t['onboarding_p']}</p></div>
        <div class="gallery">{shots('light', t['onboarding'])}</div>
      </div>
    </section>

    <section class="block" id="install">
      <div class="container">
        <div class="section-head"><h2>{t['install_h']}</h2><p>{t['install_p']}</p></div>
        <div class="install">
          <div class="download-card">
            <h3>{t['card_h']}</h3>
            <p>{t['card_p']}</p>
            <a class="btn btn-primary" href="{DOWNLOAD}">{icon('download')}{t['cta']}</a>
            <dl class="facts">
              <div><dt>{t['facts'][0]}</dt><dd id="rel-version" dir="ltr">{t['loading']}</dd></div>
              <div><dt>{t['facts'][1]}</dt><dd id="rel-size" dir="ltr">~37 MB</dd></div>
              <div><dt>{t['facts'][2]}</dt><dd>{t['requires']}</dd></div>
            </dl>
            <div class="whats-new" id="whats-new" hidden>
              <h4>{t['news_h']} <span class="rel-v" dir="ltr"></span></h4>
              <ul id="rel-news"></ul>
            </div>
            <p class="all-versions"><a href="{RELEASES}">{t['all_versions']}</a></p>
            <p class="checksum" id="rel-sha-wrap" hidden>{t['checksum']}: <code id="rel-sha"></code></p>
          </div>
          <div>
            <ol class="steps">{steps}</ol>
            <p class="note">{t['note']}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="block" id="privacy">
      <div class="container">
        <div class="privacy-band">
          <div>
            <h2>{t['privacy_h']}</h2>
            <p>{t['privacy_p']}</p>
            <a class="btn btn-ghost" href="privacy.html">{t['privacy_link']}</a>
          </div>
          <ul class="checks">{checks}</ul>
        </div>
      </div>
    </section>

    <section class="block" style="padding-top: 0">
      <div class="container">
        <div class="section-head"><h2>{t['faq_h']}</h2></div>
        <div class="faq">{faq}</div>
      </div>
    </section>
  </main>
""" + footer(t, lang, prefix, "./", "privacy.html") + f"""
  <script>
    // Screenshot theme switch; it follows the page theme and can be changed on its own.
    const showShots = (theme) => {{
      document.querySelectorAll('.seg button').forEach((x) => x.setAttribute('aria-pressed', String(x.dataset.theme === theme)));
      document.querySelectorAll('.gallery img').forEach((img) => (img.src = img.dataset[theme]));
    }};
    document.querySelectorAll('.seg button').forEach((b) => b.addEventListener('click', () => showShots(b.dataset.theme)));
    if (isDark()) showShots('dark');
    document.addEventListener('themechange', (e) => showShots(e.detail));
    // Gentle motion: sections rise into view and the hero phones lean toward the pointer. Off for reduced motion.
    if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {{
      if ('IntersectionObserver' in window) {{
        const io = new IntersectionObserver(
          (entries) => entries.forEach((e) => {{
            if (!e.isIntersecting) return;
            e.target.classList.add('in');
            io.unobserve(e.target);
          }}),
          {{ rootMargin: '0px 0px -8% 0px' }}
        );
        document.querySelectorAll('.section-head, .feature, .gallery, .download-card, .steps li, .note, .privacy-band, .faq details').forEach((el) => {{
          el.style.setProperty('--d', ([...el.parentElement.children].indexOf(el) % 3) * 0.1 + 's');
          el.classList.add('reveal');
          io.observe(el);
        }});
      }}
      const hero = document.querySelector('.hero');
      const phones = document.querySelector('.phones');
      if (matchMedia('(hover: hover) and (pointer: fine)').matches) {{
        hero.addEventListener('pointermove', (e) => {{
          const r = hero.getBoundingClientRect();
          phones.style.setProperty('--mx', (((e.clientX - r.left) / r.width) * 2 - 1).toFixed(3));
          phones.style.setProperty('--my', (((e.clientY - r.top) / r.height) * 2 - 1).toFixed(3));
        }});
        hero.addEventListener('pointerleave', () => {{
          phones.style.setProperty('--mx', 0);
          phones.style.setProperty('--my', 0);
        }});
      }}
    }}
    // Latest release facts (version, size, checksum) from GitHub; the page works without them.
    // Dawa2 shows Western digits in Arabic too, so doses and versions match the label.
    fetch('https://api.github.com/repos/{REPO}/releases/latest')
      .then((r) => (r.ok ? r.json() : null))
      .then((rel) => {{
        if (!rel) return;
        const ver = rel.tag_name.replace(/^v/, '');
        document.getElementById('rel-version').textContent = ver;
        document.querySelectorAll('.rel-v').forEach((el) => (el.textContent = ver));
        // What's new: release notes hold English bullets, then a '### بالعربية' list, then '---' and the checksum.
        const body = (rel.body || '').split(/\\n---/)[0];
        const parts = body.split(/^###\\s*بالعربية\\s*$/m);
        const plain = (x) => x.replace(/\\*\\*|`/g, '').trim();
        const bullets = (s) => s.split('\\n').filter((l) => /^\\s*-\\s/.test(l)).map((l) => plain(l.replace(/^\\s*-\\s/, '')));
        const items = bullets({'parts[1] || ""' if lang == 'ar' else 'parts[0]'});
        if (items.length) {{
          const ul = document.getElementById('rel-news');
          items.slice(0, 4).forEach((x) => {{
            const li = document.createElement('li');
            li.textContent = x;
            ul.appendChild(li);
          }});
          document.getElementById('whats-new').hidden = false;
        }}
        const apk = (rel.assets || []).find((a) => a.name === 'dawa2.apk');
        if (apk) document.getElementById('rel-size').textContent = Math.round(apk.size / 1e6) + ' MB';
        const m = /SHA-256[^:]*:\\s*`?([a-f0-9]{{64}})/i.exec(rel.body || '');
        if (m) {{
          document.getElementById('rel-sha').textContent = m[1];
          document.getElementById('rel-sha-wrap').hidden = false;
        }}
      }})
      .catch(() => {{}});
  </script>
</body>
</html>
"""
    out = os.path.join(ROOT, "ar" if lang == "ar" else "", "index.html")
    open(out, "w", encoding="utf-8", newline="\n").write(html)


def privacy(lang):
    t = T[lang]
    prefix = "../" if lang == "ar" else ""
    other = "../privacy.html" if lang == "ar" else "ar/privacy.html"
    body = open(os.path.join(ROOT, "content", f"privacy.{lang}.html"), encoding="utf-8").read()
    html = (
        head(t, lang, prefix, t["policy_title"])
        + topbar(t, lang, prefix, "./", other, anchors=False)
        + f'  <main class="policy">\n{body}\n  </main>\n'
        + footer(t, lang, prefix, "./", "privacy.html")
        + "</body>\n</html>\n"
    )
    out = os.path.join(ROOT, "ar" if lang == "ar" else "", "privacy.html")
    open(out, "w", encoding="utf-8", newline="\n").write(html)


if __name__ == "__main__":
    for language in ("en", "ar"):
        index(language)
        privacy(language)
    print("built")
