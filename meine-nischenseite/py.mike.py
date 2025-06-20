import os
import random
from datetime import datetime

# Pfad zu deinem GitHub-Ordner (bitte ggf. anpassen)
github_ordner = r"C:\Users\Mike\Desktop\meine-nischenseite"

# Liste von Nischen-Themen
nischen = [
    "Camping Ausrüstung",
    "Minimalismus Zuhause",
    "Katzenpflege Tipps",
    "Gadgets für das Home Office",
    "Nachhaltige Produkte"
]

# Deine echten Affiliate-Links
affiliate_links = {
    "Amazon": "https://www.amazon.de/?tag=mike123-21",
    "eBay": "https://www.ebay.de/?_trkparms=mikeaffiliateid"
}

# SEO Meta-Texte
def meta_description():
    return "Täglich neue Nischenseiten mit ehrlichen Produktempfehlungen und Partnerlinks. Praktisch, unabhängig und kostenlos."

def meta_keywords():
    return "Affiliate, Produktempfehlung, Amazon, eBay, Camping, Technik, Haushalt, Tipps"

# HTML-Seite generieren
def generiere_html(nische):
    html = f"""
    <!DOCTYPE html>
    <html lang=\"de\">
    <head>
        <meta charset=\"UTF-8\">
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
        <meta name=\"description\" content=\"{meta_description()}\">
        <meta name=\"keywords\" content=\"{meta_keywords()}\">
        <title>{nische} Empfehlungen</title>
    </head>
    <body>
        <h1>{nische} – Unsere Empfehlungen</h1>
        <p>Hier findest du empfohlene Produkte mit Partnerlinks:</p>
        <ul>
    """
    for name, link in affiliate_links.items():
        html += f'<li><a href="{link}" target="_blank">{name} Link</a></li>\n'

    html += """
        </ul>
        <p><em>Mit Klick auf die Links unterstützt du diese Seite. Vielen Dank!</em></p>
    </body>
    </html>
    """
    return html

# HTML-Datei speichern
def speichere_html(dateiname, html_inhalt):
    pfad = os.path.join(github_ordner, dateiname)
    with open(pfad, "w", encoding="utf-8") as file:
        file.write(html_inhalt)

# Index-Datei aktualisieren oder erstellen
def aktualisiere_index(dateiname):
    index_datei = os.path.join(github_ordner, "index.html")
    eintrag = f'<li><a href="{dateiname}">{dateiname}</a></li>\n'

    if not os.path.exists(index_datei):
        with open(index_datei, "w", encoding="utf-8") as f:
            f.write("""
<!DOCTYPE html>
<html lang=\"de\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Startseite – Nischenseite</title>
</head>
<body>
    <h1>Willkommen auf meiner Nischenseite</h1>
    <ul>
""")
            f.write(eintrag)
            f.write("""
    </ul>
</body>
</html>
""")
    else:
        with open(index_datei, "r", encoding="utf-8") as f:
            lines = f.readlines()

        with open(index_datei, "w", encoding="utf-8") as f:
            for line in lines:
                if line.strip() == "</ul>":
                    f.write(eintrag)
                f.write(line)

# Sitemap aktualisieren
def aktualisiere_sitemap(dateiname):
    sitemap_datei = os.path.join(github_ordner, "sitemap.xml")
    url = f"https://mike181812.github.io/meine-nischenseite/{dateiname}"
    eintrag = f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{datetime.now().date()}</lastmod>\n  </url>\n"

    if not os.path.exists(sitemap_datei):
        with open(sitemap_datei, "w", encoding="utf-8") as f:
            f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
            f.write("<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n")
            f.write(eintrag)
            f.write("</urlset>")
    else:
        with open(sitemap_datei, "r", encoding="utf-8") as f:
            lines = f.readlines()

        with open(sitemap_datei, "w", encoding="utf-8") as f:
            for line in lines:
                if line.strip() == "</urlset>":
                    f.write(eintrag)
                f.write(line)

# Hauptfunktion
def erstelle_webseite():
    nische = random.choice(nischen)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dateiname = f"{nische.replace(' ', '_')}_{timestamp}.html"
    html_inhalt = generiere_html(nische)
    speichere_html(dateiname, html_inhalt)
    aktualisiere_index(dateiname)
    aktualisiere_sitemap(dateiname)
    print(f"HTML-Seite '{dateiname}' erstellt, index.html und sitemap.xml aktualisiert.")

if __name__ == "__main__":
    erstelle_webseite()
