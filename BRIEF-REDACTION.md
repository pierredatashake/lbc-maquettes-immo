# Brief : transformer une maquette leboncoin en vraie page du site

Contexte : restitution leboncoin demain matin. datashake propose à leboncoin une stratégie éditoriale immo : des pages qui répondent aux questions des Français (prix, quartiers, budget, démarches, travaux, projets de vie, collections de biens, nouveaux habitats) et **ramènent toujours vers les annonces leboncoin**. Le client doit pouvoir se projeter : « voilà à quoi ressemblerait cette page sur leboncoin.fr, avec son texte SEO, ses outils, ses formats ».

Les pages existent déjà, courtes, dans `/Users/pierregaudard/AO/leboncoin-phase2/maquettes-site/tN.html` (N = 1 à 8), avec `style.css` à côté. **Tu édites directement tes fichiers `tN.html`** (outil Edit ou réécriture du fichier) :
- garde **tel quel** tout ce qui est avant `<main class="wrap">` (bandeau maquette, en-tête leboncoin, catégories) et tout ce qui est après `</main>` (pied de page) ;
- garde le fil d'Ariane, le H1, le chapô, la signature et le premier module (outil, chiffres clés, etc.), tu peux les améliorer ;
- **enrichis** la colonne principale pour en faire une vraie page complète, et garde la colonne de droite (`aside.side`).

## Ce que doit contenir la page (colonne principale, dans cet ordre indicatif)
1. Le module de tête existant (outil / chiffres clés / note…), plus un bloc `.retenir` « À retenir » de 3 ou 4 puces.
2. **Un vrai texte SEO de 900 à 1 200 mots**, en `<section>` avec `<h2>` en forme de question parlée (« Combien coûte… ? », « Comment… ? ») et des `<h3>` si besoin, paragraphes courts, listes à puces quand c'est utile.
3. **Des modules insérés dans le texte**, au moins 3 parmi : tableau de données (`<table>` avec `<th>`/`<td>`, classe `num` pour les nombres), module d'annonces (grille `.ads` de 4 cartes, copier le HTML d'une grille existante de la page), encadré outil (`.card` ou `.soft` avec un bouton `.btn.btn-main`), étapes numérotées (`<ol class="steps">`), deux colonnes (`.two`), citation d'expert (`<blockquote>`), chips de liens (`.chips` / `.chip`).
4. Un bloc CTA vers les annonces (bouton `.btn.btn-main.btn-lg` « Voir les X annonces … ») au milieu du texte et en fin d'article.
5. Une FAQ de 5 à 6 questions (`<section class="faq">` avec `<details><summary>`), questions formulées comme on les tape ou les pose à une IA, réponses de 1 à 3 phrases qui donnent la réponse d'abord.
6. Un bloc de maillage « Dans les villes voisines » ou « Pour aller plus loin » (chips ou liste de liens) vers d'autres pages du même type.
7. La ligne `.method` en bas : méthode et « Chiffres fictifs pour la maquette ».

N'ajoute pas de CSS. Utilise uniquement les classes existantes de `style.css` (lis-le). Si tu as vraiment besoin d'un style en plus, mets un `style=""` minimal en ligne, avec uniquement les couleurs `#152233`, `#ec5a13`, `#f4f6f7`, `#fff4ec`, `#5f6c7a`, `#e6ebef`.

## Règles de rédaction (non négociables)
- Français impeccable, accents, apostrophes typographiques ’, espaces insécables avant ? ! : % € et dans les nombres (`&nbsp;` ou le caractère).
- **Aucun tiret cadratin ni demi-cadratin** (— –). Pas de « : » dans les titres H1/H2/H3.
- Ton leboncoin : simple, concret, chaleureux, vouvoiement, phrases courtes. Pas de jargon SEO. Pas de formules creuses (« Dans un monde où… », « Que vous soyez… ou… », « Il est essentiel de… », « En somme »), pas de structure « X, et Y » répétitive, pas d'énumérations de trois adjectifs.
- **Chaque section apporte une info concrète** : chiffre, exemple local, démarche, coût, délai.
- **Les chiffres de marché sont fictifs mais réalistes et cohérents avec ceux déjà sur la page** (reprends-les, ne les contredis pas). Les règles légales, fiscales et techniques doivent être **exactes** (droit du bail, quittance, DPE et calendrier d'interdiction de location G 2025 / F 2028 / E 2034, frais de notaire ~7-8 % dans l'ancien, taux d'endettement 35 %, viager, SCI, PTZ, etc.). En cas de doute sur une règle, reste général plutôt que d'inventer.
- Chaque page cite leboncoin comme source de ses données (« d’après les annonces leboncoin ») et ramène vers les annonces, le dépôt d'annonce, l'alerte ou l'estimation.
- Pas de concurrent nommé de façon négative.

## Contrôle avant de rendre
- Ouvre la page via un serveur local (`cd /Users/pierregaudard/AO/leboncoin-phase2/maquettes-site && python3 -m http.server <port libre 8800-8899>`), capture-la avec `playwright-cli -s=<nom-unique> open http://127.0.0.1:<port>/tN.html` puis `resize 1440 900`, `screenshot`, regarde le rendu (haut, milieu, bas en faisant `eval "() => window.scrollTo(0, Y)"`). Corrige ce qui déborde ou casse. Ferme ta session playwright et ton serveur à la fin.
- Vérifie : pas de « — » ni « – », pas de « : » dans les h1/h2/h3, balises équilibrées.
- Ne touche à aucun autre fichier que tes `tN.html`. Pas de git, pas de push.

Rends en 3 lignes : fichiers modifiés, nombre de mots du texte par page, modules ajoutés.
