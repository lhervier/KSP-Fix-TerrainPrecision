# TODO

Ce qu'il reste à faire, et seulement ça. Tout ce qui est déjà mesuré est dans [le README](README.md) et
ses chapitres sous [docs/](docs), un dossier par objet corrigé (`ground`, `statics`, `scatter`, `rocs`,
`ground-anchor`) plus `common`, avec ses logs dans [diag/](diag) (les perfs dans
[diag/common/perfs/](diag/common/perfs)) et dans les dépôts des Diags ; aucun résultat n'est consigné ici.
**Les tests à jouer n'y sont pas non plus** : ils sont dans le *Work in progress* de la page d'entrée de
chaque objet (`docs/<objet>/README.md`), un sous-chapitre par mod (stock d'abord) ; le coût dans
[Performance](docs/common/performance.md). Un nouveau test s'ajoute là-bas (une page dans
`docs/<objet>/work-in-progress/<mod>/` et son résumé dans `docs/<objet>/README.md`), pas ici. Une fois
joué, il passe, de la même façon, dans *Non-regression tests* (`docs/<objet>/non-regression/<mod>/`) si
rien n'empire, dans *Limits and solutions* (`docs/<objet>/limits/<mod>/`) sinon. Ses données vont dans
`diag/<objet>/` et ses images dans `imgs/<objet>/`, au même chemin que sa page. Ce qui vaut pour tous les
objets à la fois va dans `common`.

## Sans ordre imposé

- **L'écart diffère-t-il d'un point du sol à l'autre ?** C'est ce qui casse une structure posée sur
  plusieurs pieds (un pied enterré, un autre en l'air) : sans lui, le sol monte ou descend d'un bloc et
  la structure suit. Je le crois, puisque chaque quad arrondit sa propre position, mais rien ne le
  mesure. Diag TerrainHeight sur quelques points éloignés de plusieurs quads, six chargements, sans le correctif ;
  faisable sur Kerbin dans `ksp-dev\`, sur les deux PC. Si la mesure le confirme, une phrase à ajouter
  au texte de #440, là où il dit que les grosses bases explosent : un pied enterré, un autre en l'air.
- **Séparer le décalage d'origine du déchargement.** Dans le protocole d'approche, le vaisseau est
  déchargé et l'origine se décale à la même frame : aucune mesure ne dit encore lequel des deux fait
  bouger le sol ; le code stock désigne le décalage. ⚠️ Changer de vaisseau (`]`) **ne** décale **pas**
  l'origine (vérifié dans `FlightGlobals.setActiveVessel`, 2026-09-24), et un décalage sans
  déchargement est impossible tant que le témoin posé est chargé (verrou). Le test faisable est
  l'inverse : **un déchargement sans décalage**. Une sauvegarde avec le rover à ~2,15 km du témoin
  (chargé au départ, sous 2,25 km) : en s'éloignant, le témoin se décharge à 2,5 km alors que le rover
  n'est qu'à ~350 m de l'origine, donc sous le seuil de 500 m ; puis retour sous 2,25 km (rechargement)
  et approche sous 200 m (le témoin, chargé, verrouille l'origine). Diag LandedVessel et Diag TerrainHeight visent le témoin
  comme dans le protocole d'approche, Diag FloatingOrigin doit afficher **Shifts** = 0 du début à la fin. Si le sol
  du témoin ne bouge pas, le déchargement seul n'y est pour rien : c'est le décalage. En complément,
  avec le correctif en `logLevel = Debug`, le décalage du protocole d'approche doit apparaître comme une
  salve de lignes `origin moved by … mm`.
- **Les sauvegardes existantes, ce qu'il reste à faire** (le cas lui-même est le chapitre
  [Existing saves](docs/common/existing-saves.md)). Décider où va la mise en garde sur
  les modules amarrés posés sur des jambes d'atterrissage, la configuration qui souffre le plus au
  premier chargement (le *Disclaimer* est partagé mot pour mot avec les README des Diags) ; vérifier
  dans le mécanisme de réglages de KSPCF qu'un patch se désactive, avant d'écrire qu'un joueur peut le
  couper, charger, relever un vaisseau et le remettre ; un outil de migration du `.sfs` seulement si un
  coût réel apparaît.
- **Poster sur #435** une fois sûr de ce que Diag FloatingOrigin montre aux chargements, comme le commentaire
  l'annonce.
- **Rejouer toutes les campagnes en automatique, et reconstituer mesures et logs** (Lionel,
  2026-10-03). Chaque protocole publié (chargement par corps, approche, changement de vaisseau, piste,
  roulage, cas RSS, cas de *Limits and solutions*, tests de non-régression) reçoit un script KSP-MCPServer, **à côté** de sa
  procédure à la main, qui reste ; on rejoue sans le correctif et avec, puis on remplace les séries, les
  logs et les chiffres publiés par ceux des scripts. Fait en grande partie : les scripts vivent dans
  ce dépôt (`diag/<objet>/automation/`, les Diags ensemble dans la même session). Reste à passer la liste des
  protocoles publiés pour trouver ceux qui n'ont pas encore de script, ou dont les chiffres publiés ne
  viennent pas encore d'un script.
- **Vérifier que les scripts de pilotage du jeu recourent le moins possible à l'introspection**
  (`get_member`, `set_member`, `call_method` de KSP-MCPServer) (Lionel, 2026-10-06). Cas connus :
  `diag/statics/automation/run-rotation-threshold.py` active deux `CheatOptions` (`IgnoreMaxTemperature`,
  `NoCrashDamage`) par `set_member`, que `set_cheats` ne couvre pas (électricité et carburant infinis
  seulement) ; `diag/statics/automation/run-station-approach.py` lit le coût du lien CommNet par `get_member`.
