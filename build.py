#!/usr/bin/env python3
"""Génère 8 maquettes de pages leboncoin immo (chiffres fictifs) + index."""
import os
D = os.path.dirname(os.path.abspath(__file__))
LOGO = open(os.path.join(D, 'ref/logo.svg')).read()
NB = ' '

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Nunito Sans',system-ui,sans-serif;color:#152233;background:#fff;font-size:16px;line-height:1.5}
a{color:inherit}
.wrap{max-width:1066px;margin:0 auto;padding:0 16px}
.proto{background:#152233;color:#fff;font-size:13px;text-align:center;padding:6px 10px}
.proto a{color:#fff}
header.top{border-bottom:1px solid #e6ebef;background:#fff;position:sticky;top:0;z-index:5}
.top .row{display:flex;align-items:center;gap:20px;height:72px}
.logo{color:#ec5a13;width:164px;height:30px;flex:none}
.btn{display:inline-flex;align-items:center;gap:8px;border:0;border-radius:9999px;font:inherit;font-weight:700;cursor:pointer;text-decoration:none;white-space:nowrap}
.btn-main{background:#ec5a13;color:#fff;padding:10px 18px;font-size:15px}
.btn-main:hover{background:#d14e10}
.btn-ghost{background:#fff;color:#152233;border:1px solid #152233;padding:9px 18px;font-size:15px}
.btn-lg{padding:14px 26px;font-size:16px}
.search{flex:1;display:flex;align-items:center;background:#f4f6f7;border-radius:12px;height:44px;padding:0 6px 0 16px;color:#5f6c7a;font-size:15px;max-width:320px}
.search span{flex:1}.search b{width:34px;height:34px;border-radius:10px;background:#ec5a13;display:grid;place-items:center;color:#fff;font-size:14px}
.icons{display:flex;gap:22px;margin-left:auto;font-size:12px;text-align:center}
.icons div{display:flex;flex-direction:column;align-items:center;gap:4px}
.icons i{font-style:normal;font-size:18px;line-height:1}
.cats{display:flex;gap:16px;font-size:15px;padding:10px 0;white-space:nowrap;overflow:auto}
.cats span+span:before{content:"·";margin-right:16px;color:#9aa5b1}
.cats .on{font-weight:700;color:#ec5a13}
.crumb{font-size:13px;color:#5f6c7a;padding:18px 0 6px}
.crumb a{text-decoration:underline}
h1{font-size:32px;line-height:1.2;font-weight:800;margin:6px 0 10px}
h2{font-size:22px;font-weight:800;margin:0 0 14px}
h3{font-size:17px;font-weight:700}
.lead{font-size:17px;color:#3c4a5a;max-width:760px}
.byline{display:flex;gap:10px;align-items:center;font-size:13px;color:#5f6c7a;margin:14px 0 26px}
.byline .av{width:32px;height:32px;border-radius:50%;background:#ffe3d3;color:#ec5a13;display:grid;place-items:center;font-weight:800}
.layout{display:grid;grid-template-columns:1fr 300px;gap:32px;align-items:start}
section{margin:0 0 34px}
.card{border:1px solid #e6ebef;border-radius:16px;padding:20px;background:#fff}
.soft{background:#f4f6f7;border-radius:16px;padding:20px}
.retenir{background:#fff4ec;border-radius:16px;padding:20px 22px}
.retenir h3{margin-bottom:8px;color:#ec5a13}
.retenir li{margin:6px 0 6px 18px}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.kpi{background:#f4f6f7;border-radius:16px;padding:16px}
.kpi b{display:block;font-size:24px;font-weight:800}
.kpi span{font-size:13px;color:#5f6c7a}
.kpi.hot b{color:#ec5a13}
table{width:100%;border-collapse:separate;border-spacing:0 6px;font-size:15px}
th{text-align:left;font-size:13px;color:#5f6c7a;font-weight:600;padding:0 12px}
td{background:#f4f6f7;padding:12px}
td:first-child{border-radius:10px 0 0 10px;font-weight:700}td:last-child{border-radius:0 10px 10px 0}
.num{text-align:right;font-variant-numeric:tabular-nums}
.bar{height:10px;border-radius:5px;background:#e6ebef;position:relative;min-width:120px}
.bar i{position:absolute;inset:0 auto 0 0;border-radius:5px;background:#ec5a13}
.ads{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.ad{text-decoration:none}
.ph{aspect-ratio:4/3;border-radius:14px;background:linear-gradient(135deg,var(--a,#d9cfc4),var(--b,#b9ab9c));position:relative;overflow:hidden}
.ph:after{content:"";position:absolute;left:50%;top:50%;width:46px;height:40px;transform:translate(-50%,-40%);background:rgba(255,255,255,.55);clip-path:polygon(50% 0,100% 45%,88% 45%,88% 100%,12% 100%,12% 45%,0 45%)}
.ph .badge{position:absolute;left:10px;top:10px;background:#fff;border-radius:9999px;font-size:12px;font-weight:700;padding:3px 10px;z-index:1}
.ad h3{font-size:15px;margin-top:8px}.ad .p{font-weight:800;font-size:16px}.ad small{color:#5f6c7a;font-size:13px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{border:1px solid #cdd5dc;border-radius:9999px;padding:6px 14px;font-size:14px;font-weight:600;background:#fff}
.chip.on{background:#152233;color:#fff;border-color:#152233}
.faq details{border-bottom:1px solid #e6ebef;padding:14px 0}
.faq summary{font-weight:700;cursor:pointer;list-style:none;display:flex;justify-content:space-between}
.faq summary:after{content:"+";color:#ec5a13;font-weight:800}
.faq details[open] summary:after{content:"–"}
.faq p{margin-top:8px;color:#3c4a5a}
.side{position:sticky;top:96px;display:flex;flex-direction:column;gap:14px}
.side .card h3{margin-bottom:6px}.side .card p{font-size:14px;color:#3c4a5a;margin-bottom:12px}
.links a{display:block;font-size:14px;padding:6px 0;text-decoration:underline}
.method{font-size:13px;color:#5f6c7a;border-top:1px solid #e6ebef;padding-top:14px;margin-top:10px}
.form{display:grid;gap:12px}
.form label{font-size:13px;color:#5f6c7a;font-weight:600}
.form .f{border:1px solid #cdd5dc;border-radius:12px;padding:12px 14px;font-weight:700;background:#fff}
.result{background:#152233;color:#fff;border-radius:16px;padding:24px}
.result b{font-size:40px;font-weight:800;display:block;line-height:1.1}
.result small{opacity:.8}
.two{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.dpe{display:grid;gap:8px}
.dpe div{display:flex;align-items:center;gap:12px}
.dpe span.l{color:#fff;font-weight:800;border-radius:6px;padding:6px 10px;min-width:40px}
.note{display:flex;gap:20px;align-items:center}
.note .big{background:#152233;color:#fff;border-radius:16px;padding:18px 22px;text-align:center}
.note .big b{font-size:44px;font-weight:800;display:block;line-height:1}
.crit{flex:1;display:grid;gap:8px;font-size:14px}
.crit div{display:grid;grid-template-columns:150px 1fr 34px;gap:10px;align-items:center}
.crit .bar i{background:#152233}
blockquote{background:#f4f6f7;border-radius:14px;padding:14px 16px;font-size:15px}
blockquote footer{font-size:13px;color:#5f6c7a;margin-top:6px}
.hero{background:#152233;color:#fff;border-radius:20px;padding:30px;display:flex;justify-content:space-between;gap:20px;align-items:center}
.hero h1{color:#fff;margin:4px 0 8px}.hero p{opacity:.85;max-width:560px}
.hero .chips .chip{background:transparent;color:#fff;border-color:#fff}.hero .chips .chip.on{background:#ec5a13;border-color:#ec5a13}
.doc{background:#fff;border:1px solid #e6ebef;border-radius:12px;padding:22px;box-shadow:0 6px 20px rgba(21,34,51,.08)}
.doc i{display:block;height:9px;border-radius:5px;background:#e6ebef;margin:10px 0}
.steps{counter-reset:s;display:grid;gap:10px}
.steps li{list-style:none;counter-increment:s;display:flex;gap:12px;align-items:flex-start}
.steps li:before{content:counter(s);background:#ec5a13;color:#fff;border-radius:50%;width:26px;height:26px;display:grid;place-items:center;font-weight:800;font-size:13px;flex:none}
footer.site{background:#152233;color:#cdd5dc;margin-top:50px;padding:34px 0 26px;font-size:14px}
footer.site .cols{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-bottom:24px}
footer.site h4{color:#fff;font-size:13px;text-transform:uppercase;letter-spacing:.04em;margin-bottom:10px}
footer.site p{margin:4px 0}
footer.site .sis{border-top:1px solid #33465c;padding-top:14px;text-align:center}
@media(max-width:900px){.layout{grid-template-columns:1fr}.kpis,.ads{grid-template-columns:1fr 1fr}.icons,.search{display:none}.two{grid-template-columns:1fr}.hero{flex-direction:column;align-items:flex-start}.side{position:static}}
"""

HEAD = '''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>{title}</title><link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700;800&display=swap" rel="stylesheet"><link rel="stylesheet" href="style.css"></head><body>
<div class="proto">Maquette datashake pour leboncoin, chiffres fictifs. <a href="index.html">Toutes les maquettes</a></div>
<header class="top"><div class="wrap row">{logo}<a class="btn btn-main" href="#">⊕ Déposer une annonce</a><div class="search"><span>Rechercher sur leboncoin</span><b>⌕</b></div>
<div class="icons"><div><i>🔔</i>Mes recherches</div><div><i>♡</i>Favoris</div><div><i>💬</i>Messages</div><div><i>👤</i>Se connecter</div></div></div>
<div class="wrap cats"><span class="on">Immobilier</span><span>Véhicules</span><span>Matériel pro</span><span>Emploi</span><span>Mode</span><span>Maison &amp; Jardin</span><span>Famille</span><span>Électronique</span><span>Loisirs</span><span>Autres</span></div></header>
<main class="wrap">'''

FOOT = '''</main><footer class="site"><div class="wrap"><div class="cols">
<div><h4>À propos du boncoin</h4><p>Qui sommes-nous ?</p><p>Nous rejoindre</p><p>Plan du site</p></div>
<div><h4>Le guide immo</h4><p>Prix immobilier par ville</p><p>Vivre à</p><p>Simulateurs</p><p>Modèles gratuits</p></div>
<div><h4>Des questions ?</h4><p>Aide</p><p>Le boncoin vous informe</p><p>Paiement sécurisé</p></div>
<div><h4>Nos applications</h4><p>App Store</p><p>Google Play</p></div></div>
<div class="sis">leboncoin · AVendreALouer · leboncoin Immobilier Neuf<br>leboncoin 2006 - 2026</div></div></footer></body></html>'''

def ads(items, colors=('#d9cfc4', '#b9ab9c')):
    pal = [('#d9cfc4', '#b9ab9c'), ('#cbd3dc', '#9fb0c2'), ('#d6d9c8', '#aeb39a'), ('#e2d2c4', '#c3a98f')]
    h = '<div class="ads">'
    for i, (p, t, l, b) in enumerate(items):
        a, c = pal[i % 4]
        badge = f'<span class="badge">{b}</span>' if b else ''
        h += f'<a class="ad" href="#"><div class="ph" style="--a:{a};--b:{c}">{badge}</div><div class="p">{p}</div><h3>{t}</h3><small>{l}</small></a>'
    return h + '</div>'

def faq(qs):
    return '<section class="faq"><h2>Questions fréquentes</h2>' + ''.join(f'<details{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(qs)) + '</section>'

def byline(expert):
    return f'<div class="byline"><div class="av">lbc</div><div>Par <b>la rédaction leboncoin immo</b>, relu par {expert}<br>Mis à jour le 1er novembre 2026</div></div>'

def side(title, text, btn, links):
    return f'<aside class="side"><div class="card"><h3>{title}</h3><p>{text}</p><a class="btn btn-main" href="#">{btn}</a></div><div class="card links"><h3>À lire aussi</h3>{"".join(f"<a href=#>{l}</a>" for l in links)}</div></aside>'

def page(fn, title, crumb, body):
    html = HEAD.format(title=title, logo=LOGO) + f'<div class="crumb"><a href="#">Accueil</a> › <a href="#">Immobilier</a> › {crumb}</div>' + body + FOOT
    open(os.path.join(D, fn), 'w').write(html)

# 1 Prix Lyon
arr = [('Lyon 6e', 5900, 6400, '+0,8'), ('Lyon 2e', 5600, 6100, '−0,4'), ('Lyon 3e', 4700, 5200, '−1,6'), ('Lyon 7e', 4500, 5000, '−2,1'), ('Lyon 4e', 4900, 5600, '−0,9'), ('Lyon 8e', 3900, 4300, '−2,4'), ('Lyon 9e', 3800, 4200, '−1,8')]
rows = ''.join(f'<tr><td>{a}</td><td class="num">{f"{p:,}".replace(",",NB)}{NB}€</td><td class="num">{f"{m:,}".replace(",",NB)}{NB}€</td><td class="num">{e}{NB}%</td><td style="width:30%"><div class="bar"><i style="width:{int(p/6400*100)}%"></i></div></td></tr>' for a, p, m, e in arr)
page('t1.html', 'Prix immobilier à Lyon en novembre 2026, prix au m² par quartier | leboncoin', 'Prix immobilier › Lyon', f'''
<h1>Prix immobilier à Lyon en novembre 2026</h1><p class="lead">Combien coûte le mètre carré à Lyon ? Les prix calculés sur les annonces leboncoin de la ville, quartier par quartier, mis à jour le 1er de chaque mois.</p>{byline("un expert de l’équipe Études leboncoin")}
<div class="layout"><div>
<section class="kpis"><div class="kpi hot"><b>4{NB}650{NB}€</b><span>prix moyen au m², appartements</span></div><div class="kpi"><b>−1,2{NB}%</b><span>sur un an</span></div><div class="kpi"><b>7{NB}166</b><span>annonces en vente</span></div><div class="kpi"><b>54 jours</b><span>pour vendre en moyenne</span></div></section>
<section class="retenir"><h3>À retenir</h3><ul><li>Le prix moyen d’un appartement à Lyon est de 4{NB}650{NB}€ le m², en baisse de 1,2{NB}% sur un an.</li><li>Le 6e arrondissement reste le plus cher, le 9e le plus accessible.</li><li>Un bien au bon prix se vend en 54 jours en moyenne.</li></ul></section>
<section><h2>Prix au m² par arrondissement</h2><table><tr><th>Quartier</th><th class="num">Appartement</th><th class="num">Maison</th><th class="num">Sur un an</th><th></th></tr>{rows}</table></section>
<section><h2>Les annonces à vendre à Lyon</h2>{ads([("385"+NB+"000"+NB+"€","T3, 68 m²","Lyon 3e",""),("520"+NB+"000"+NB+"€","T4, 92 m², balcon","Lyon 6e","Nouveau"),("249"+NB+"000"+NB+"€","T2, 45 m²","Lyon 8e",""),("410"+NB+"000"+NB+"€","T3, 75 m²","Lyon 7e","Baisse de prix")])}<p style="margin-top:16px"><a class="btn btn-main btn-lg" href="#">Voir les 7{NB}166 annonces à Lyon</a></p></section>
<section><h2>Comment évoluent les prix à Lyon ?</h2><p>Les prix lyonnais reculent légèrement depuis un an, surtout dans les 7e et 8e arrondissements, où l’offre a augmenté. Les biens bien situés et avec une bonne étiquette énergie se vendent toujours vite. Pour vendre au bon prix, comparez votre bien aux annonces similaires de votre quartier.</p></section>
{faq([("Quel est le prix au m² à Lyon ?","4"+NB+"650"+NB+"€ en moyenne pour un appartement en novembre 2026, d’après les annonces leboncoin de la ville."),("Les prix baissent-ils à Lyon ?","Oui, de 1,2"+NB+"% sur un an. La baisse est plus marquée dans les 7e et 8e arrondissements."),("Quel est le quartier le moins cher de Lyon ?","Le 9e arrondissement, autour de 3"+NB+"800"+NB+"€ le m² pour un appartement.")])}
<p class="method">Méthode : prix moyens calculés sur les annonces de vente publiées sur leboncoin à Lyon le mois précédent, hors biens atypiques. Chiffres fictifs pour la maquette.</p>
</div>{side("Estimez votre bien","Un prix calé sur les annonces de votre quartier, en 2 minutes.","Estimer mon bien",["Prix immobilier à Villeurbanne","Vivre à Lyon, le guide","Combien emprunter pour acheter à Lyon ?"])}</div>''')

# 2 Vivre à Nantes
crit = [('Commerces', 8.6), ('Écoles', 8.0), ('Transports', 7.8), ('Sécurité', 7.2), ('Prix du logement', 6.4)]
cr = ''.join(f'<div><span>{c}</span><div class="bar"><i style="width:{v*10}%"></i></div><b>{str(v).replace(".",",")}</b></div>' for c, v in crit)
page('t2.html', 'Vivre à Nantes, la ville notée par ses habitants | leboncoin', 'Vivre à › Nantes', f'''
<h1>Vivre à Nantes</h1><p class="lead">La ville notée par ceux qui y vivent, et ce qu’elle coûte vraiment, d’après les annonces leboncoin.</p>{byline("la rédaction locale")}
<div class="layout"><div>
<section class="card note"><div class="big"><b>8,1</b>sur 10<br><small>1{NB}240 avis</small></div><div class="crit">{cr}</div></section>
<section class="kpis"><div class="kpi"><b>3{NB}950{NB}€</b><span>prix moyen au m²</span></div><div class="kpi"><b>790{NB}€</b><span>loyer moyen d’un T2</span></div><div class="kpi"><b>2{NB}870</b><span>biens en vente</span></div><div class="kpi hot"><b>3e</b><span>du palmarès leboncoin 2026</span></div></section>
<section><h2>Les quartiers les mieux notés</h2><table><tr><th>Quartier</th><th class="num">Note</th><th class="num">Prix au m²</th><th class="num">Annonces</th></tr>
<tr><td>Chantenay</td><td class="num">8,6</td><td class="num">3{NB}420{NB}€</td><td class="num"><a href="#">214</a></td></tr><tr><td>Île de Nantes</td><td class="num">8,4</td><td class="num">4{NB}180{NB}€</td><td class="num"><a href="#">186</a></td></tr><tr><td>Doulon</td><td class="num">8,1</td><td class="num">3{NB}260{NB}€</td><td class="num"><a href="#">152</a></td></tr><tr><td>Centre</td><td class="num">7,9</td><td class="num">4{NB}870{NB}€</td><td class="num"><a href="#">301</a></td></tr></table></section>
<section><h2>Ce qu’en disent les habitants</h2><div class="two"><blockquote>« Une ville à taille humaine, tout se fait à vélo. Les prix ont monté mais restent loin de Paris. »<footer>Camille, Chantenay, 8/10</footer></blockquote><blockquote>« Beaucoup d’offre culturelle, des écoles de qualité. Il faut s’y prendre tôt pour louer. »<footer>Yanis, Île de Nantes, 9/10</footer></blockquote></div></section>
<section><h2>Les annonces à Nantes</h2>{ads([("295"+NB+"000"+NB+"€","T3, 64 m²","Chantenay",""),("890"+NB+"€/mois","T2 à louer, 48 m²","Centre","Location"),("410"+NB+"000"+NB+"€","Maison, 110 m²","Doulon","Nouveau"),("238"+NB+"000"+NB+"€","T2, 46 m²","Île de Nantes","")])}<p style="margin-top:16px"><a class="btn btn-main btn-lg" href="#">Voir les 2{NB}870 annonces à Nantes</a> <a class="btn btn-ghost btn-lg" href="#">Noter ma ville</a></p></section>
{faq([("Fait-il bon vivre à Nantes ?","Ses habitants lui donnent 8,1 sur 10, avec de très bonnes notes pour les commerces et les écoles."),("Combien coûte un logement à Nantes ?","3"+NB+"950"+NB+"€ le m² en moyenne à l’achat, 790"+NB+"€ par mois pour louer un T2."),("Quel est le meilleur quartier de Nantes ?","Chantenay est le mieux noté par les habitants, avec 8,6 sur 10.")])}
<p class="method">Méthode : notes données par les utilisateurs leboncoin qui habitent la ville, prix et loyers calculés sur les annonces. Chiffres fictifs pour la maquette.</p>
</div>{side("Créez une alerte","Recevez les nouvelles annonces de Nantes dès leur publication.","Créer une alerte",["Le palmarès leboncoin des villes 2026","Prix immobilier à Nantes","Vivre à Rennes"])}</div>''')

# 3 Budget
page('t3.html', 'Combien pouvez-vous emprunter ? Simulateur avec Meilleurtaux | leboncoin', 'Simulateurs › Capacité d’emprunt', f'''
<h1>Combien pouvez-vous emprunter ?</h1><p class="lead">Calculez votre budget en 1 minute, avec les taux du mois de Meilleurtaux, puis voyez directement les biens à ce prix dans votre ville.</p>{byline("Meilleurtaux, partenaire de leboncoin")}
<div class="layout"><div>
<section class="two"><div class="soft form"><label>Revenus nets du foyer</label><div class="f">4{NB}200{NB}€ par mois</div><label>Apport</label><div class="f">35{NB}000{NB}€</div><label>Durée</label><div class="f">25 ans</div><label>Ville</label><div class="f">Lyon</div><a class="btn btn-main" href="#" style="justify-content:center">Calculer mon budget</a></div>
<div class="result"><small>Votre budget</small><b>312{NB}000{NB}€</b><small>mensualité de 1{NB}470{NB}€, taux de 3,4{NB}% sur 25 ans, frais de notaire compris</small><p style="margin:22px 0 12px"><a class="btn btn-main btn-lg" href="#">Voir les 1{NB}245 biens à ce budget à Lyon</a></p><a href="#" style="font-size:14px">Être rappelé par un conseiller Meilleurtaux</a></div></section>
<section><h2>Les biens à votre budget à Lyon</h2>{ads([("298"+NB+"000"+NB+"€","T3, 68 m²","Lyon 8e",""),("305"+NB+"000"+NB+"€","Maison, 92 m²","Vénissieux","Jardin"),("289"+NB+"000"+NB+"€","T4, 81 m²","Villeurbanne",""),("310"+NB+"000"+NB+"€","T3, 64 m²","Lyon 3e","Nouveau")])}</section>
<section class="retenir"><h3>À retenir</h3><ul><li>Les banques limitent la mensualité à 35{NB}% de vos revenus, assurance comprise.</li><li>Un apport de 10{NB}% couvre en général les frais de notaire.</li><li>Une durée plus longue augmente le budget, mais aussi le coût du crédit.</li></ul></section>
{faq([("Comment calculer sa capacité d’emprunt ?","On part de vos revenus nets, on applique un taux d’endettement de 35"+NB+"%, puis on tient compte de la durée, du taux et de votre apport."),("Quel taux pour un crédit immobilier en novembre 2026 ?","Autour de 3,4"+NB+"% sur 25 ans selon Meilleurtaux, à affiner selon votre profil."),("Les frais de notaire sont-ils compris ?","Oui, le budget affiché les inclut, environ 8"+NB+"% du prix dans l’ancien.")])}
<p class="method">Simulateur co-signé avec Meilleurtaux, taux du mois. Résultat indicatif, chiffres fictifs pour la maquette.</p>
</div>{side("Estimez vos frais de notaire","Le montant exact selon le prix et la ville.","Calculer",["Frais de notaire, le guide","Le prêt à taux zéro en 2026","Acheter à Lyon avec 300 000 €"])}</div>''')

# 4 Quittance
page('t4.html', 'Quittance de loyer, modèle gratuit à remplir en ligne | leboncoin', 'Modèles › Quittance de loyer', f'''
<h1>Quittance de loyer, modèle gratuit</h1><p class="lead">Remplissez, téléchargez en PDF, envoyez à votre locataire. Un modèle à jour de la loi du 6 juillet 1989.</p>{byline("un juriste partenaire")}
<div class="layout"><div>
<section class="two"><div class="soft form"><label>Bailleur</label><div class="f">Marie Dupont</div><label>Locataire</label><div class="f">Thomas Martin</div><label>Adresse du logement</label><div class="f">12 rue Paul Bert, Lyon 3e</div><label>Période</label><div class="f">Novembre 2026</div><label>Loyer et charges</label><div class="f">780{NB}€ + 60{NB}€</div><a class="btn btn-main" href="#" style="justify-content:center">Télécharger ma quittance en PDF</a></div>
<div class="doc"><h3>QUITTANCE DE LOYER</h3><small>Novembre 2026</small><i></i><i></i><i style="width:60%"></i><i></i><i></i><i style="width:60%"></i><i></i><p style="margin-top:14px;font-weight:800">Total reçu 840{NB}€</p></div></section>
<section><h2>Comment faire une quittance de loyer ?</h2><ol class="steps"><li>Indiquez le nom du bailleur, du locataire et l’adresse du logement.</li><li>Précisez la période, le loyer et les charges payés.</li><li>Téléchargez le PDF, signez-le et envoyez-le au locataire.</li></ol></section>
<section class="retenir"><h3>À retenir</h3><ul><li>Le bailleur doit remettre gratuitement une quittance si le locataire la demande.</li><li>Elle distingue toujours le loyer et les charges.</li><li>Un envoi par e-mail est possible si le locataire est d’accord.</li></ul></section>
<section class="card" style="display:flex;justify-content:space-between;gap:16px;align-items:center"><div><h3>Vous louez un bien ?</h3><p>Trouvez votre prochain locataire sur leboncoin, gratuitement.</p></div><a class="btn btn-main btn-lg" href="#">Déposer une annonce</a></section>
{faq([("La quittance de loyer est-elle obligatoire ?","Oui, si le locataire la demande, et elle doit être gratuite."),("Peut-on envoyer une quittance par e-mail ?","Oui, avec l’accord du locataire."),("Que faire en cas de paiement partiel ?","On remet un reçu, pas une quittance, en précisant la somme reçue.")])}
<p class="method">Modèle à jour au 1er novembre 2026. Maquette, données fictives.</p>
</div>{side("Tous les modèles gratuits","Bail, état des lieux, préavis, avenant.","Voir les modèles",["Taxe foncière, le calculateur par commune","La garantie Visale, pas à pas","Encadrement des loyers, vérifier son loyer"])}</div>''')

# 5 DPE Lille
dpe = [('A', '#1b8a4c', 4120), ('B', '#4da84a', 3980), ('C', '#a6c83a', 3760), ('D', '#e8c51b', 3540), ('E', '#f0b323', 3310), ('F', '#ec7e2e', 2980), ('G', '#d8312c', 2760)]
dp = ''.join(f'<div><span class="l" style="background:{c};width:{int(60+(v-2600)/1600*300)}px">{l}</span><b>{f"{v:,}".replace(",",NB)}{NB}€/m²</b></div>' for l, c, v in dpe)
page('t5.html', 'DPE à Lille, ce que l’étiquette énergie change au prix | leboncoin', 'Guides › DPE', f'''
<h1>Le DPE fait-il baisser le prix d’une maison à Lille ?</h1><p class="lead">Le prix moyen au m² des maisons en vente sur leboncoin à Lille, selon leur étiquette énergie, et les travaux qui font gagner une classe.</p>{byline("un diagnostiqueur certifié")}
<div class="layout"><div>
<section class="two"><div class="card dpe">{dp}<small style="color:#5f6c7a">Maisons à Lille, annonces leboncoin</small></div><div class="result"><small>Passer de F à C sur une maison de 100 m²</small><b>+78{NB}000{NB}€</b><small>de valeur à la revente, d’après les prix affichés</small></div></section>
<section><h2>Les travaux qui font gagner une classe</h2><table><tr><th>Travaux</th><th class="num">Gain</th><th class="num">Coût moyen</th><th class="num">Aide possible</th></tr><tr><td>Isolation des combles</td><td class="num">1 à 2 classes</td><td class="num">4{NB}000{NB}€</td><td class="num">MaPrimeRénov’</td></tr><tr><td>Pompe à chaleur</td><td class="num">1 à 2 classes</td><td class="num">12{NB}000{NB}€</td><td class="num">MaPrimeRénov’</td></tr><tr><td>Fenêtres double vitrage</td><td class="num">1 classe</td><td class="num">8{NB}000{NB}€</td><td class="num">CEE</td></tr></table></section>
<section><h2>Filtrer les annonces par étiquette</h2><div class="chips" style="margin-bottom:16px"><span class="chip on">A</span><span class="chip on">B</span><span class="chip on">C</span><span class="chip">D</span><span class="chip">E</span><span class="chip">F</span><span class="chip">G</span></div>{ads([("412"+NB+"000"+NB+"€","Maison, 110 m², DPE B","Lille Vauban",""),("365"+NB+"000"+NB+"€","Maison, 95 m², DPE C","Lambersart","Rénovée"),("298"+NB+"000"+NB+"€","Maison, 88 m², DPE C","Lille Fives",""),("455"+NB+"000"+NB+"€","Maison, 120 m², DPE A","Marcq-en-Barœul","Neuf")])}<p style="margin-top:16px"><a class="btn btn-main btn-lg" href="#">Voir les 412 maisons classées A à C</a></p></section>
{faq([("Le DPE fait-il baisser le prix d’une maison ?","Oui. À Lille, une maison classée G se vend en moyenne 33"+NB+"% moins cher au m² qu’une maison classée A."),("Peut-on louer un logement classé G en 2026 ?","Non, les logements classés G ne peuvent plus être mis en location depuis 2025."),("Combien coûte un DPE ?","Entre 100 et 250"+NB+"€ selon la surface.")])}
<p class="method">Méthode : prix moyens au m² des maisons en vente sur leboncoin à Lille, par étiquette DPE. Chiffres fictifs pour la maquette.</p>
</div>{side("Vendez au bon prix","Estimez votre maison selon son étiquette énergie.","Estimer mon bien",["MaPrimeRénov’ 2026, le guide","Isoler ses combles","DPE à Roubaix"])}</div>''')

# 6 Viager
page('t6.html', 'Acheter en viager, le calcul et les annonces | leboncoin', 'Projets de vie › Viager', f'''
<h1>Comment acheter en viager ?</h1><p class="lead">Bouquet, rente, décote : comprendre le viager et trouver un bien, au même endroit.</p>{byline("un notaire partenaire")}
<div class="layout"><div>
<section class="two"><div class="soft form"><label>Valeur du bien</label><div class="f">300{NB}000{NB}€</div><label>Âge du vendeur</label><div class="f">78 ans</div><label>Type</label><div class="f">Viager occupé</div><a class="btn btn-main" href="#" style="justify-content:center">Calculer</a></div><div class="result"><small>Estimation indicative</small><b>60{NB}000{NB}€</b><small>de bouquet</small><b style="font-size:30px;margin-top:12px">820{NB}€/mois</b><small>de rente</small></div></section>
<section><h2>Les annonces en viager à Bordeaux</h2>{ads([("72"+NB+"000"+NB+"€ + 640"+NB+"€/mois","T3, 68 m², femme 81 ans","Bordeaux Chartrons","38 % de décote"),("48"+NB+"000"+NB+"€ + 910"+NB+"€/mois","Maison, 120 m², homme 84 ans","Mérignac","45 % de décote"),("95"+NB+"000"+NB+"€ + 520"+NB+"€/mois","T2, 52 m², couple 79 ans","Talence","31 % de décote"),("60"+NB+"000"+NB+"€, sans rente","Maison, 85 m², viager libre","Pessac","Libre")])}<p style="margin-top:16px"><a class="btn btn-main btn-lg" href="#">Voir les 1{NB}180 annonces en viager</a></p></section>
<section class="retenir"><h3>À retenir</h3><ul><li>Le bouquet est payé à la signature, la rente chaque mois.</li><li>La décote dépend de l’âge du vendeur et du type de viager.</li><li>Un viager libre se loue ou s’habite tout de suite.</li></ul></section>
<section><h2>Les autres moments de vie</h2><div class="chips"><a class="chip" href="#">Hériter d’une maison</a><a class="chip" href="#">Créer une SCI familiale</a><a class="chip" href="#">Se séparer et vendre</a><a class="chip" href="#">Premier achat</a></div></section>
{faq([("Comment se calcule un viager ?","À partir de la valeur du bien, de l’âge du vendeur et d’une table d’espérance de vie, on fixe une décote, puis on répartit entre bouquet et rente."),("Quelle différence entre viager occupé et viager libre ?","En viager occupé, le vendeur reste dans le logement. En viager libre, l’acheteur peut l’occuper tout de suite."),("Le viager est-il risqué ?","Il comporte un aléa sur la durée de la rente, que la décote compense.")])}
<p class="method">Calcul indicatif, à confirmer par un notaire. Chiffres fictifs pour la maquette.</p>
</div>{side("Vendre en viager","Estimez le bouquet et la rente de votre bien.","Estimer",["Hériter d’une maison, les étapes","La SCI familiale, le guide","Indivision, comment en sortir"])}</div>''')

# 7 Longères
page('t7.html', 'Longères de caractère, la collection leboncoin | leboncoin', 'Collections › Longères', f'''
<section class="hero" style="margin-top:10px"><div><small style="opacity:.8">La collection de la semaine</small><h1>Longères de caractère</h1><p>Pierre, poutres et grands terrains, les plus belles longères en vente en Bretagne et en Normandie, choisies parmi vos annonces.</p></div>
<div class="chips"><span class="chip on">Longères</span><span class="chip">Avec piscine</span><span class="chip">Lofts et ateliers</span><span class="chip">Vue mer</span><span class="chip">Maisons d’architecte</span></div></section>
<div style="margin-top:28px">{ads([("385"+NB+"000"+NB+"€","Longère de 1820, 180 m²","Pont-Aven (29)","Coup de cœur"),("498"+NB+"000"+NB+"€","Longère rénovée, 140 m²","Honfleur (14)","Coup de cœur"),("149"+NB+"000"+NB+"€","Longère à rénover, 110 m²","Josselin (56)","Coup de cœur"),("420"+NB+"000"+NB+"€","Corps de ferme, 230 m²","Lamballe (22)","Coup de cœur")])}</div>
<div style="margin-top:14px">{ads([("265"+NB+"000"+NB+"€","Longère en pierre, 120 m²","Quimperlé (29)",""),("540"+NB+"000"+NB+"€","Longère et gîte, 260 m²","Dinan (22)",""),("189"+NB+"000"+NB+"€","Longère, 95 m², 2 ha","Mortain (50)",""),("349"+NB+"000"+NB+"€","Longère, 150 m², dépendance","Vannes (56)","")])}</div>
<p style="margin:20px 0 34px"><a class="btn btn-main btn-lg" href="#">Voir les 318 longères de la collection</a></p>
<div class="layout"><div><section><h2>Acheter une longère, ce qu’il faut savoir</h2><p>La longère est la maison rurale traditionnelle de Bretagne et de Normandie, tout en longueur, souvent en pierre. Avant d’acheter, vérifiez la toiture, l’humidité des murs et l’assainissement. Les longères à rénover se trouvent encore sous 150{NB}000{NB}€ dans le centre Bretagne.</p></section>
{faq([("Combien coûte une longère en Bretagne ?","Entre 150"+NB+"000 et 500"+NB+"000"+NB+"€ selon l’état et le terrain, d’après les annonces de la collection."),("Faut-il rénover une longère ?","Souvent l’isolation et la toiture. Comptez 800 à 1"+NB+"500"+NB+"€ le m² pour une rénovation complète.")])}</div>
<aside class="side"><div class="card"><h3>La collection du lundi</h3><p>Recevez chaque lundi la nouvelle collection par e-mail.</p><a class="btn btn-main" href="#">Je m’abonne</a></div></aside></div>''')

# 8 Tiny house
page('t8.html', 'Tiny house, combien ça coûte vraiment ? Prix et annonces | leboncoin', 'Habitats › Tiny house', f'''
<h1>Tiny house, combien ça coûte vraiment ?</h1><p class="lead">Les prix relevés sur les tiny houses en vente sur leboncoin, neuves et d’occasion, et tout ce qu’il faut savoir avant d’acheter.</p>{byline("un constructeur partenaire")}
<div class="layout"><div>
<section class="kpis"><div class="kpi hot"><b>41{NB}500{NB}€</b><span>prix médian</span></div><div class="kpi"><b>19 à 38 k€</b><span>d’occasion</span></div><div class="kpi"><b>38 à 64 k€</b><span>neuve</span></div><div class="kpi"><b>640</b><span>annonces en France</span></div></section>
<section class="retenir"><h3>À retenir</h3><ul><li>Une tiny house neuve coûte entre 38{NB}000 et 64{NB}000{NB}€, d’occasion à partir de 19{NB}000{NB}€.</li><li>Il faut un terrain et, au-delà de 3 mois par an, une déclaration en mairie.</li><li>Comptez 2{NB}000 à 5{NB}000{NB}€ de raccordement.</li></ul></section>
<section><h2>Comparer les habitats</h2><table><tr><th>Habitat</th><th class="num">Prix médian</th><th class="num">Annonces</th></tr><tr><td>Tiny house</td><td class="num">41{NB}500{NB}€</td><td class="num"><a href="#">640</a></td></tr><tr><td>Maison container</td><td class="num">96{NB}000{NB}€</td><td class="num"><a href="#">212</a></td></tr><tr><td>Maison en bois</td><td class="num">189{NB}000{NB}€</td><td class="num"><a href="#">3{NB}480</a></td></tr><tr><td>Mobil-home</td><td class="num">28{NB}000{NB}€</td><td class="num"><a href="#">5{NB}120</a></td></tr></table></section>
<section><h2>Les tiny houses en vente en ce moment</h2>{ads([("36"+NB+"000"+NB+"€","Tiny house 18 m², 2021","Annecy (74)",""),("52"+NB+"000"+NB+"€","Tiny house neuve, 22 m²","Nantes (44)","Neuve"),("29"+NB+"500"+NB+"€","Tiny house nomade, 15 m²","Bordeaux (33)",""),("68"+NB+"000"+NB+"€","Tiny house sur terrain","Vannes (56)","Avec terrain")])}<p style="margin-top:16px"><a class="btn btn-main btn-lg" href="#">Voir les 640 tiny houses en vente</a> <a class="btn btn-ghost btn-lg" href="#">Créer une alerte</a></p></section>
{faq([("Quel est le prix d’une tiny house ?","41"+NB+"500"+NB+"€ en prix médian sur leboncoin, de 19"+NB+"000"+NB+"€ d’occasion à 64"+NB+"000"+NB+"€ neuve."),("Où installer une tiny house ?","Sur un terrain constructible ou de loisirs, avec une déclaration en mairie au-delà de 3 mois par an."),("Une tiny house se revend-elle bien ?","Oui, le marché de l’occasion est actif, avec 640 annonces en France.")])}
<p class="method">Méthode : prix relevés sur les annonces de tiny houses publiées sur leboncoin. Chiffres fictifs pour la maquette.</p>
</div>{side("Vous vendez une tiny house ?","Publiez votre annonce gratuitement.","Déposer une annonce",["Maison container, le prix","Maison en bois en kit","Le coliving, comment ça marche"])}</div>''')

open(os.path.join(D, 'style.css'), 'w').write(CSS)
print('ok')
