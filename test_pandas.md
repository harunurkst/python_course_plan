

```python
import pandas as pd
```


```python
df = pd.read_csv("pokemon_data.csv")
```


```python
df.tail(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>795</th>
      <td>719</td>
      <td>Diancie</td>
      <td>Rock</td>
      <td>Fairy</td>
      <td>50</td>
      <td>100</td>
      <td>150</td>
      <td>100</td>
      <td>150</td>
      <td>50</td>
      <td>6</td>
      <td>True</td>
    </tr>
    <tr>
      <th>796</th>
      <td>719</td>
      <td>DiancieMega Diancie</td>
      <td>Rock</td>
      <td>Fairy</td>
      <td>50</td>
      <td>160</td>
      <td>110</td>
      <td>160</td>
      <td>110</td>
      <td>110</td>
      <td>6</td>
      <td>True</td>
    </tr>
    <tr>
      <th>797</th>
      <td>720</td>
      <td>HoopaHoopa Confined</td>
      <td>Psychic</td>
      <td>Ghost</td>
      <td>80</td>
      <td>110</td>
      <td>60</td>
      <td>150</td>
      <td>130</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
    </tr>
    <tr>
      <th>798</th>
      <td>720</td>
      <td>HoopaHoopa Unbound</td>
      <td>Psychic</td>
      <td>Dark</td>
      <td>80</td>
      <td>160</td>
      <td>60</td>
      <td>170</td>
      <td>130</td>
      <td>80</td>
      <td>6</td>
      <td>True</td>
    </tr>
    <tr>
      <th>799</th>
      <td>721</td>
      <td>Volcanion</td>
      <td>Fire</td>
      <td>Water</td>
      <td>80</td>
      <td>110</td>
      <td>120</td>
      <td>130</td>
      <td>90</td>
      <td>70</td>
      <td>6</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.columns
```




    Index(['#', 'Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Sp. Atk',
           'Sp. Def', 'Speed', 'Generation', 'Legendary'],
          dtype='object')




```python
df[["Name", "Type 1"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Type 1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bulbasaur</td>
      <td>Grass</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ivysaur</td>
      <td>Grass</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Venusaur</td>
      <td>Grass</td>
    </tr>
    <tr>
      <th>3</th>
      <td>VenusaurMega Venusaur</td>
      <td>Grass</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Charmander</td>
      <td>Fire</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Charmeleon</td>
      <td>Fire</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Charizard</td>
      <td>Fire</td>
    </tr>
    <tr>
      <th>7</th>
      <td>CharizardMega Charizard X</td>
      <td>Fire</td>
    </tr>
    <tr>
      <th>8</th>
      <td>CharizardMega Charizard Y</td>
      <td>Fire</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Squirtle</td>
      <td>Water</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wartortle</td>
      <td>Water</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Blastoise</td>
      <td>Water</td>
    </tr>
    <tr>
      <th>12</th>
      <td>BlastoiseMega Blastoise</td>
      <td>Water</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Caterpie</td>
      <td>Bug</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Metapod</td>
      <td>Bug</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Butterfree</td>
      <td>Bug</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Weedle</td>
      <td>Bug</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Kakuna</td>
      <td>Bug</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Beedrill</td>
      <td>Bug</td>
    </tr>
    <tr>
      <th>19</th>
      <td>BeedrillMega Beedrill</td>
      <td>Bug</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Pidgey</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Pidgeotto</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Pidgeot</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PidgeotMega Pidgeot</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Rattata</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Raticate</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Spearow</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Fearow</td>
      <td>Normal</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Ekans</td>
      <td>Poison</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Arbok</td>
      <td>Poison</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>770</th>
      <td>Sylveon</td>
      <td>Fairy</td>
    </tr>
    <tr>
      <th>771</th>
      <td>Hawlucha</td>
      <td>Fighting</td>
    </tr>
    <tr>
      <th>772</th>
      <td>Dedenne</td>
      <td>Electric</td>
    </tr>
    <tr>
      <th>773</th>
      <td>Carbink</td>
      <td>Rock</td>
    </tr>
    <tr>
      <th>774</th>
      <td>Goomy</td>
      <td>Dragon</td>
    </tr>
    <tr>
      <th>775</th>
      <td>Sliggoo</td>
      <td>Dragon</td>
    </tr>
    <tr>
      <th>776</th>
      <td>Goodra</td>
      <td>Dragon</td>
    </tr>
    <tr>
      <th>777</th>
      <td>Klefki</td>
      <td>Steel</td>
    </tr>
    <tr>
      <th>778</th>
      <td>Phantump</td>
      <td>Ghost</td>
    </tr>
    <tr>
      <th>779</th>
      <td>Trevenant</td>
      <td>Ghost</td>
    </tr>
    <tr>
      <th>780</th>
      <td>PumpkabooAverage Size</td>
      <td>Ghost</td>
    </tr>
    <tr>
      <th>781</th>
      <td>PumpkabooSmall Size</td>
      <td>Ghost</td>
    </tr>
    <tr>
      <th>782</th>
      <td>PumpkabooLarge Size</td>
      <td>Ghost</td>
    </tr>
    <tr>
      <th>783</th>
      <td>PumpkabooSuper Size</td>
      <td>Ghost</td>
    </tr>
    <tr>
      <th>784</th>
      <td>GourgeistAverage Size</td>
      <td>Ghost</td>
    </tr>
    <tr>
      <th>785</th>
      <td>GourgeistSmall Size</td>
      <td>Ghost</td>
    </tr>
    <tr>
      <th>786</th>
      <td>GourgeistLarge Size</td>
      <td>Ghost</td>
    </tr>
    <tr>
      <th>787</th>
      <td>GourgeistSuper Size</td>
      <td>Ghost</td>
    </tr>
    <tr>
      <th>788</th>
      <td>Bergmite</td>
      <td>Ice</td>
    </tr>
    <tr>
      <th>789</th>
      <td>Avalugg</td>
      <td>Ice</td>
    </tr>
    <tr>
      <th>790</th>
      <td>Noibat</td>
      <td>Flying</td>
    </tr>
    <tr>
      <th>791</th>
      <td>Noivern</td>
      <td>Flying</td>
    </tr>
    <tr>
      <th>792</th>
      <td>Xerneas</td>
      <td>Fairy</td>
    </tr>
    <tr>
      <th>793</th>
      <td>Yveltal</td>
      <td>Dark</td>
    </tr>
    <tr>
      <th>794</th>
      <td>Zygarde50% Forme</td>
      <td>Dragon</td>
    </tr>
    <tr>
      <th>795</th>
      <td>Diancie</td>
      <td>Rock</td>
    </tr>
    <tr>
      <th>796</th>
      <td>DiancieMega Diancie</td>
      <td>Rock</td>
    </tr>
    <tr>
      <th>797</th>
      <td>HoopaHoopa Confined</td>
      <td>Psychic</td>
    </tr>
    <tr>
      <th>798</th>
      <td>HoopaHoopa Unbound</td>
      <td>Psychic</td>
    </tr>
    <tr>
      <th>799</th>
      <td>Volcanion</td>
      <td>Fire</td>
    </tr>
  </tbody>
</table>
<p>800 rows × 2 columns</p>
</div>




```python
# Read specific location
df.iloc[0:2]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bulbasaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>45</td>
      <td>49</td>
      <td>49</td>
      <td>65</td>
      <td>65</td>
      <td>45</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Ivysaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>60</td>
      <td>62</td>
      <td>63</td>
      <td>80</td>
      <td>80</td>
      <td>60</td>
      <td>1</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
for index, row in df.iterrows():
    print(index, row["Name"])
```

    0 Bulbasaur
    1 Ivysaur
    2 Venusaur
    3 VenusaurMega Venusaur
    4 Charmander
    5 Charmeleon
    6 Charizard
    7 CharizardMega Charizard X
    8 CharizardMega Charizard Y
    9 Squirtle
    10 Wartortle
    11 Blastoise
    12 BlastoiseMega Blastoise
    13 Caterpie
    14 Metapod
    15 Butterfree
    16 Weedle
    17 Kakuna
    18 Beedrill
    19 BeedrillMega Beedrill
    20 Pidgey
    21 Pidgeotto
    22 Pidgeot
    23 PidgeotMega Pidgeot
    24 Rattata
    25 Raticate
    26 Spearow
    27 Fearow
    28 Ekans
    29 Arbok
    30 Pikachu
    31 Raichu
    32 Sandshrew
    33 Sandslash
    34 Nidoran (Female)
    35 Nidorina
    36 Nidoqueen
    37 Nidoran (Male)
    38 Nidorino
    39 Nidoking
    40 Clefairy
    41 Clefable
    42 Vulpix
    43 Ninetales
    44 Jigglypuff
    45 Wigglytuff
    46 Zubat
    47 Golbat
    48 Oddish
    49 Gloom
    50 Vileplume
    51 Paras
    52 Parasect
    53 Venonat
    54 Venomoth
    55 Diglett
    56 Dugtrio
    57 Meowth
    58 Persian
    59 Psyduck
    60 Golduck
    61 Mankey
    62 Primeape
    63 Growlithe
    64 Arcanine
    65 Poliwag
    66 Poliwhirl
    67 Poliwrath
    68 Abra
    69 Kadabra
    70 Alakazam
    71 AlakazamMega Alakazam
    72 Machop
    73 Machoke
    74 Machamp
    75 Bellsprout
    76 Weepinbell
    77 Victreebel
    78 Tentacool
    79 Tentacruel
    80 Geodude
    81 Graveler
    82 Golem
    83 Ponyta
    84 Rapidash
    85 Slowpoke
    86 Slowbro
    87 SlowbroMega Slowbro
    88 Magnemite
    89 Magneton
    90 Farfetch'd
    91 Doduo
    92 Dodrio
    93 Seel
    94 Dewgong
    95 Grimer
    96 Muk
    97 Shellder
    98 Cloyster
    99 Gastly
    100 Haunter
    101 Gengar
    102 GengarMega Gengar
    103 Onix
    104 Drowzee
    105 Hypno
    106 Krabby
    107 Kingler
    108 Voltorb
    109 Electrode
    110 Exeggcute
    111 Exeggutor
    112 Cubone
    113 Marowak
    114 Hitmonlee
    115 Hitmonchan
    116 Lickitung
    117 Koffing
    118 Weezing
    119 Rhyhorn
    120 Rhydon
    121 Chansey
    122 Tangela
    123 Kangaskhan
    124 KangaskhanMega Kangaskhan
    125 Horsea
    126 Seadra
    127 Goldeen
    128 Seaking
    129 Staryu
    130 Starmie
    131 Mr. Mime
    132 Scyther
    133 Jynx
    134 Electabuzz
    135 Magmar
    136 Pinsir
    137 PinsirMega Pinsir
    138 Tauros
    139 Magikarp
    140 Gyarados
    141 GyaradosMega Gyarados
    142 Lapras
    143 Ditto
    144 Eevee
    145 Vaporeon
    146 Jolteon
    147 Flareon
    148 Porygon
    149 Omanyte
    150 Omastar
    151 Kabuto
    152 Kabutops
    153 Aerodactyl
    154 AerodactylMega Aerodactyl
    155 Snorlax
    156 Articuno
    157 Zapdos
    158 Moltres
    159 Dratini
    160 Dragonair
    161 Dragonite
    162 Mewtwo
    163 MewtwoMega Mewtwo X
    164 MewtwoMega Mewtwo Y
    165 Mew
    166 Chikorita
    167 Bayleef
    168 Meganium
    169 Cyndaquil
    170 Quilava
    171 Typhlosion
    172 Totodile
    173 Croconaw
    174 Feraligatr
    175 Sentret
    176 Furret
    177 Hoothoot
    178 Noctowl
    179 Ledyba
    180 Ledian
    181 Spinarak
    182 Ariados
    183 Crobat
    184 Chinchou
    185 Lanturn
    186 Pichu
    187 Cleffa
    188 Igglybuff
    189 Togepi
    190 Togetic
    191 Natu
    192 Xatu
    193 Mareep
    194 Flaaffy
    195 Ampharos
    196 AmpharosMega Ampharos
    197 Bellossom
    198 Marill
    199 Azumarill
    200 Sudowoodo
    201 Politoed
    202 Hoppip
    203 Skiploom
    204 Jumpluff
    205 Aipom
    206 Sunkern
    207 Sunflora
    208 Yanma
    209 Wooper
    210 Quagsire
    211 Espeon
    212 Umbreon
    213 Murkrow
    214 Slowking
    215 Misdreavus
    216 Unown
    217 Wobbuffet
    218 Girafarig
    219 Pineco
    220 Forretress
    221 Dunsparce
    222 Gligar
    223 Steelix
    224 SteelixMega Steelix
    225 Snubbull
    226 Granbull
    227 Qwilfish
    228 Scizor
    229 ScizorMega Scizor
    230 Shuckle
    231 Heracross
    232 HeracrossMega Heracross
    233 Sneasel
    234 Teddiursa
    235 Ursaring
    236 Slugma
    237 Magcargo
    238 Swinub
    239 Piloswine
    240 Corsola
    241 Remoraid
    242 Octillery
    243 Delibird
    244 Mantine
    245 Skarmory
    246 Houndour
    247 Houndoom
    248 HoundoomMega Houndoom
    249 Kingdra
    250 Phanpy
    251 Donphan
    252 Porygon2
    253 Stantler
    254 Smeargle
    255 Tyrogue
    256 Hitmontop
    257 Smoochum
    258 Elekid
    259 Magby
    260 Miltank
    261 Blissey
    262 Raikou
    263 Entei
    264 Suicune
    265 Larvitar
    266 Pupitar
    267 Tyranitar
    268 TyranitarMega Tyranitar
    269 Lugia
    270 Ho-oh
    271 Celebi
    272 Treecko
    273 Grovyle
    274 Sceptile
    275 SceptileMega Sceptile
    276 Torchic
    277 Combusken
    278 Blaziken
    279 BlazikenMega Blaziken
    280 Mudkip
    281 Marshtomp
    282 Swampert
    283 SwampertMega Swampert
    284 Poochyena
    285 Mightyena
    286 Zigzagoon
    287 Linoone
    288 Wurmple
    289 Silcoon
    290 Beautifly
    291 Cascoon
    292 Dustox
    293 Lotad
    294 Lombre
    295 Ludicolo
    296 Seedot
    297 Nuzleaf
    298 Shiftry
    299 Taillow
    300 Swellow
    301 Wingull
    302 Pelipper
    303 Ralts
    304 Kirlia
    305 Gardevoir
    306 GardevoirMega Gardevoir
    307 Surskit
    308 Masquerain
    309 Shroomish
    310 Breloom
    311 Slakoth
    312 Vigoroth
    313 Slaking
    314 Nincada
    315 Ninjask
    316 Shedinja
    317 Whismur
    318 Loudred
    319 Exploud
    320 Makuhita
    321 Hariyama
    322 Azurill
    323 Nosepass
    324 Skitty
    325 Delcatty
    326 Sableye
    327 SableyeMega Sableye
    328 Mawile
    329 MawileMega Mawile
    330 Aron
    331 Lairon
    332 Aggron
    333 AggronMega Aggron
    334 Meditite
    335 Medicham
    336 MedichamMega Medicham
    337 Electrike
    338 Manectric
    339 ManectricMega Manectric
    340 Plusle
    341 Minun
    342 Volbeat
    343 Illumise
    344 Roselia
    345 Gulpin
    346 Swalot
    347 Carvanha
    348 Sharpedo
    349 SharpedoMega Sharpedo
    350 Wailmer
    351 Wailord
    352 Numel
    353 Camerupt
    354 CameruptMega Camerupt
    355 Torkoal
    356 Spoink
    357 Grumpig
    358 Spinda
    359 Trapinch
    360 Vibrava
    361 Flygon
    362 Cacnea
    363 Cacturne
    364 Swablu
    365 Altaria
    366 AltariaMega Altaria
    367 Zangoose
    368 Seviper
    369 Lunatone
    370 Solrock
    371 Barboach
    372 Whiscash
    373 Corphish
    374 Crawdaunt
    375 Baltoy
    376 Claydol
    377 Lileep
    378 Cradily
    379 Anorith
    380 Armaldo
    381 Feebas
    382 Milotic
    383 Castform
    384 Kecleon
    385 Shuppet
    386 Banette
    387 BanetteMega Banette
    388 Duskull
    389 Dusclops
    390 Tropius
    391 Chimecho
    392 Absol
    393 AbsolMega Absol
    394 Wynaut
    395 Snorunt
    396 Glalie
    397 GlalieMega Glalie
    398 Spheal
    399 Sealeo
    400 Walrein
    401 Clamperl
    402 Huntail
    403 Gorebyss
    404 Relicanth
    405 Luvdisc
    406 Bagon
    407 Shelgon
    408 Salamence
    409 SalamenceMega Salamence
    410 Beldum
    411 Metang
    412 Metagross
    413 MetagrossMega Metagross
    414 Regirock
    415 Regice
    416 Registeel
    417 Latias
    418 LatiasMega Latias
    419 Latios
    420 LatiosMega Latios
    421 Kyogre
    422 KyogrePrimal Kyogre
    423 Groudon
    424 GroudonPrimal Groudon
    425 Rayquaza
    426 RayquazaMega Rayquaza
    427 Jirachi
    428 DeoxysNormal Forme
    429 DeoxysAttack Forme
    430 DeoxysDefense Forme
    431 DeoxysSpeed Forme
    432 Turtwig
    433 Grotle
    434 Torterra
    435 Chimchar
    436 Monferno
    437 Infernape
    438 Piplup
    439 Prinplup
    440 Empoleon
    441 Starly
    442 Staravia
    443 Staraptor
    444 Bidoof
    445 Bibarel
    446 Kricketot
    447 Kricketune
    448 Shinx
    449 Luxio
    450 Luxray
    451 Budew
    452 Roserade
    453 Cranidos
    454 Rampardos
    455 Shieldon
    456 Bastiodon
    457 Burmy
    458 WormadamPlant Cloak
    459 WormadamSandy Cloak
    460 WormadamTrash Cloak
    461 Mothim
    462 Combee
    463 Vespiquen
    464 Pachirisu
    465 Buizel
    466 Floatzel
    467 Cherubi
    468 Cherrim
    469 Shellos
    470 Gastrodon
    471 Ambipom
    472 Drifloon
    473 Drifblim
    474 Buneary
    475 Lopunny
    476 LopunnyMega Lopunny
    477 Mismagius
    478 Honchkrow
    479 Glameow
    480 Purugly
    481 Chingling
    482 Stunky
    483 Skuntank
    484 Bronzor
    485 Bronzong
    486 Bonsly
    487 Mime Jr.
    488 Happiny
    489 Chatot
    490 Spiritomb
    491 Gible
    492 Gabite
    493 Garchomp
    494 GarchompMega Garchomp
    495 Munchlax
    496 Riolu
    497 Lucario
    498 LucarioMega Lucario
    499 Hippopotas
    500 Hippowdon
    501 Skorupi
    502 Drapion
    503 Croagunk
    504 Toxicroak
    505 Carnivine
    506 Finneon
    507 Lumineon
    508 Mantyke
    509 Snover
    510 Abomasnow
    511 AbomasnowMega Abomasnow
    512 Weavile
    513 Magnezone
    514 Lickilicky
    515 Rhyperior
    516 Tangrowth
    517 Electivire
    518 Magmortar
    519 Togekiss
    520 Yanmega
    521 Leafeon
    522 Glaceon
    523 Gliscor
    524 Mamoswine
    525 Porygon-Z
    526 Gallade
    527 GalladeMega Gallade
    528 Probopass
    529 Dusknoir
    530 Froslass
    531 Rotom
    532 RotomHeat Rotom
    533 RotomWash Rotom
    534 RotomFrost Rotom
    535 RotomFan Rotom
    536 RotomMow Rotom
    537 Uxie
    538 Mesprit
    539 Azelf
    540 Dialga
    541 Palkia
    542 Heatran
    543 Regigigas
    544 GiratinaAltered Forme
    545 GiratinaOrigin Forme
    546 Cresselia
    547 Phione
    548 Manaphy
    549 Darkrai
    550 ShayminLand Forme
    551 ShayminSky Forme
    552 Arceus
    553 Victini
    554 Snivy
    555 Servine
    556 Serperior
    557 Tepig
    558 Pignite
    559 Emboar
    560 Oshawott
    561 Dewott
    562 Samurott
    563 Patrat
    564 Watchog
    565 Lillipup
    566 Herdier
    567 Stoutland
    568 Purrloin
    569 Liepard
    570 Pansage
    571 Simisage
    572 Pansear
    573 Simisear
    574 Panpour
    575 Simipour
    576 Munna
    577 Musharna
    578 Pidove
    579 Tranquill
    580 Unfezant
    581 Blitzle
    582 Zebstrika
    583 Roggenrola
    584 Boldore
    585 Gigalith
    586 Woobat
    587 Swoobat
    588 Drilbur
    589 Excadrill
    590 Audino
    591 AudinoMega Audino
    592 Timburr
    593 Gurdurr
    594 Conkeldurr
    595 Tympole
    596 Palpitoad
    597 Seismitoad
    598 Throh
    599 Sawk
    600 Sewaddle
    601 Swadloon
    602 Leavanny
    603 Venipede
    604 Whirlipede
    605 Scolipede
    606 Cottonee
    607 Whimsicott
    608 Petilil
    609 Lilligant
    610 Basculin
    611 Sandile
    612 Krokorok
    613 Krookodile
    614 Darumaka
    615 DarmanitanStandard Mode
    616 DarmanitanZen Mode
    617 Maractus
    618 Dwebble
    619 Crustle
    620 Scraggy
    621 Scrafty
    622 Sigilyph
    623 Yamask
    624 Cofagrigus
    625 Tirtouga
    626 Carracosta
    627 Archen
    628 Archeops
    629 Trubbish
    630 Garbodor
    631 Zorua
    632 Zoroark
    633 Minccino
    634 Cinccino
    635 Gothita
    636 Gothorita
    637 Gothitelle
    638 Solosis
    639 Duosion
    640 Reuniclus
    641 Ducklett
    642 Swanna
    643 Vanillite
    644 Vanillish
    645 Vanilluxe
    646 Deerling
    647 Sawsbuck
    648 Emolga
    649 Karrablast
    650 Escavalier
    651 Foongus
    652 Amoonguss
    653 Frillish
    654 Jellicent
    655 Alomomola
    656 Joltik
    657 Galvantula
    658 Ferroseed
    659 Ferrothorn
    660 Klink
    661 Klang
    662 Klinklang
    663 Tynamo
    664 Eelektrik
    665 Eelektross
    666 Elgyem
    667 Beheeyem
    668 Litwick
    669 Lampent
    670 Chandelure
    671 Axew
    672 Fraxure
    673 Haxorus
    674 Cubchoo
    675 Beartic
    676 Cryogonal
    677 Shelmet
    678 Accelgor
    679 Stunfisk
    680 Mienfoo
    681 Mienshao
    682 Druddigon
    683 Golett
    684 Golurk
    685 Pawniard
    686 Bisharp
    687 Bouffalant
    688 Rufflet
    689 Braviary
    690 Vullaby
    691 Mandibuzz
    692 Heatmor
    693 Durant
    694 Deino
    695 Zweilous
    696 Hydreigon
    697 Larvesta
    698 Volcarona
    699 Cobalion
    700 Terrakion
    701 Virizion
    702 TornadusIncarnate Forme
    703 TornadusTherian Forme
    704 ThundurusIncarnate Forme
    705 ThundurusTherian Forme
    706 Reshiram
    707 Zekrom
    708 LandorusIncarnate Forme
    709 LandorusTherian Forme
    710 Kyurem
    711 KyuremBlack Kyurem
    712 KyuremWhite Kyurem
    713 KeldeoOrdinary Forme
    714 KeldeoResolute Forme
    715 MeloettaAria Forme
    716 MeloettaPirouette Forme
    717 Genesect
    718 Chespin
    719 Quilladin
    720 Chesnaught
    721 Fennekin
    722 Braixen
    723 Delphox
    724 Froakie
    725 Frogadier
    726 Greninja
    727 Bunnelby
    728 Diggersby
    729 Fletchling
    730 Fletchinder
    731 Talonflame
    732 Scatterbug
    733 Spewpa
    734 Vivillon
    735 Litleo
    736 Pyroar
    737 Flabébé
    738 Floette
    739 Florges
    740 Skiddo
    741 Gogoat
    742 Pancham
    743 Pangoro
    744 Furfrou
    745 Espurr
    746 MeowsticMale
    747 MeowsticFemale
    748 Honedge
    749 Doublade
    750 AegislashBlade Forme
    751 AegislashShield Forme
    752 Spritzee
    753 Aromatisse
    754 Swirlix
    755 Slurpuff
    756 Inkay
    757 Malamar
    758 Binacle
    759 Barbaracle
    760 Skrelp
    761 Dragalge
    762 Clauncher
    763 Clawitzer
    764 Helioptile
    765 Heliolisk
    766 Tyrunt
    767 Tyrantrum
    768 Amaura
    769 Aurorus
    770 Sylveon
    771 Hawlucha
    772 Dedenne
    773 Carbink
    774 Goomy
    775 Sliggoo
    776 Goodra
    777 Klefki
    778 Phantump
    779 Trevenant
    780 PumpkabooAverage Size
    781 PumpkabooSmall Size
    782 PumpkabooLarge Size
    783 PumpkabooSuper Size
    784 GourgeistAverage Size
    785 GourgeistSmall Size
    786 GourgeistLarge Size
    787 GourgeistSuper Size
    788 Bergmite
    789 Avalugg
    790 Noibat
    791 Noivern
    792 Xerneas
    793 Yveltal
    794 Zygarde50% Forme
    795 Diancie
    796 DiancieMega Diancie
    797 HoopaHoopa Confined
    798 HoopaHoopa Unbound
    799 Volcanion



```python
df.loc[df["Type 1"] == 'Grass']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bulbasaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>45</td>
      <td>49</td>
      <td>49</td>
      <td>65</td>
      <td>65</td>
      <td>45</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Ivysaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>60</td>
      <td>62</td>
      <td>63</td>
      <td>80</td>
      <td>80</td>
      <td>60</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>80</td>
      <td>82</td>
      <td>83</td>
      <td>100</td>
      <td>100</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>VenusaurMega Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>80</td>
      <td>100</td>
      <td>123</td>
      <td>122</td>
      <td>120</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>48</th>
      <td>43</td>
      <td>Oddish</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>45</td>
      <td>50</td>
      <td>55</td>
      <td>75</td>
      <td>65</td>
      <td>30</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>49</th>
      <td>44</td>
      <td>Gloom</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>60</td>
      <td>65</td>
      <td>70</td>
      <td>85</td>
      <td>75</td>
      <td>40</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>50</th>
      <td>45</td>
      <td>Vileplume</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>75</td>
      <td>80</td>
      <td>85</td>
      <td>110</td>
      <td>90</td>
      <td>50</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>75</th>
      <td>69</td>
      <td>Bellsprout</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>50</td>
      <td>75</td>
      <td>35</td>
      <td>70</td>
      <td>30</td>
      <td>40</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>76</th>
      <td>70</td>
      <td>Weepinbell</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>65</td>
      <td>90</td>
      <td>50</td>
      <td>85</td>
      <td>45</td>
      <td>55</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>77</th>
      <td>71</td>
      <td>Victreebel</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>80</td>
      <td>105</td>
      <td>65</td>
      <td>100</td>
      <td>70</td>
      <td>70</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>110</th>
      <td>102</td>
      <td>Exeggcute</td>
      <td>Grass</td>
      <td>Psychic</td>
      <td>60</td>
      <td>40</td>
      <td>80</td>
      <td>60</td>
      <td>45</td>
      <td>40</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>111</th>
      <td>103</td>
      <td>Exeggutor</td>
      <td>Grass</td>
      <td>Psychic</td>
      <td>95</td>
      <td>95</td>
      <td>85</td>
      <td>125</td>
      <td>65</td>
      <td>55</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>122</th>
      <td>114</td>
      <td>Tangela</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>65</td>
      <td>55</td>
      <td>115</td>
      <td>100</td>
      <td>40</td>
      <td>60</td>
      <td>1</td>
      <td>False</td>
    </tr>
    <tr>
      <th>166</th>
      <td>152</td>
      <td>Chikorita</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>45</td>
      <td>49</td>
      <td>65</td>
      <td>49</td>
      <td>65</td>
      <td>45</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>167</th>
      <td>153</td>
      <td>Bayleef</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>60</td>
      <td>62</td>
      <td>80</td>
      <td>63</td>
      <td>80</td>
      <td>60</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>168</th>
      <td>154</td>
      <td>Meganium</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>80</td>
      <td>82</td>
      <td>100</td>
      <td>83</td>
      <td>100</td>
      <td>80</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>197</th>
      <td>182</td>
      <td>Bellossom</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>75</td>
      <td>80</td>
      <td>95</td>
      <td>90</td>
      <td>100</td>
      <td>50</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>202</th>
      <td>187</td>
      <td>Hoppip</td>
      <td>Grass</td>
      <td>Flying</td>
      <td>35</td>
      <td>35</td>
      <td>40</td>
      <td>35</td>
      <td>55</td>
      <td>50</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>203</th>
      <td>188</td>
      <td>Skiploom</td>
      <td>Grass</td>
      <td>Flying</td>
      <td>55</td>
      <td>45</td>
      <td>50</td>
      <td>45</td>
      <td>65</td>
      <td>80</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>204</th>
      <td>189</td>
      <td>Jumpluff</td>
      <td>Grass</td>
      <td>Flying</td>
      <td>75</td>
      <td>55</td>
      <td>70</td>
      <td>55</td>
      <td>95</td>
      <td>110</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>206</th>
      <td>191</td>
      <td>Sunkern</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>30</td>
      <td>30</td>
      <td>30</td>
      <td>30</td>
      <td>30</td>
      <td>30</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>207</th>
      <td>192</td>
      <td>Sunflora</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>75</td>
      <td>75</td>
      <td>55</td>
      <td>105</td>
      <td>85</td>
      <td>30</td>
      <td>2</td>
      <td>False</td>
    </tr>
    <tr>
      <th>272</th>
      <td>252</td>
      <td>Treecko</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>40</td>
      <td>45</td>
      <td>35</td>
      <td>65</td>
      <td>55</td>
      <td>70</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>273</th>
      <td>253</td>
      <td>Grovyle</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>50</td>
      <td>65</td>
      <td>45</td>
      <td>85</td>
      <td>65</td>
      <td>95</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>274</th>
      <td>254</td>
      <td>Sceptile</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>70</td>
      <td>85</td>
      <td>65</td>
      <td>105</td>
      <td>85</td>
      <td>120</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>275</th>
      <td>254</td>
      <td>SceptileMega Sceptile</td>
      <td>Grass</td>
      <td>Dragon</td>
      <td>70</td>
      <td>110</td>
      <td>75</td>
      <td>145</td>
      <td>85</td>
      <td>145</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>296</th>
      <td>273</td>
      <td>Seedot</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>40</td>
      <td>40</td>
      <td>50</td>
      <td>30</td>
      <td>30</td>
      <td>30</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>297</th>
      <td>274</td>
      <td>Nuzleaf</td>
      <td>Grass</td>
      <td>Dark</td>
      <td>70</td>
      <td>70</td>
      <td>40</td>
      <td>60</td>
      <td>40</td>
      <td>60</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>298</th>
      <td>275</td>
      <td>Shiftry</td>
      <td>Grass</td>
      <td>Dark</td>
      <td>90</td>
      <td>100</td>
      <td>60</td>
      <td>90</td>
      <td>60</td>
      <td>80</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>309</th>
      <td>285</td>
      <td>Shroomish</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>60</td>
      <td>40</td>
      <td>60</td>
      <td>40</td>
      <td>60</td>
      <td>35</td>
      <td>3</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>467</th>
      <td>420</td>
      <td>Cherubi</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>45</td>
      <td>35</td>
      <td>45</td>
      <td>62</td>
      <td>53</td>
      <td>35</td>
      <td>4</td>
      <td>False</td>
    </tr>
    <tr>
      <th>468</th>
      <td>421</td>
      <td>Cherrim</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>70</td>
      <td>60</td>
      <td>70</td>
      <td>87</td>
      <td>78</td>
      <td>85</td>
      <td>4</td>
      <td>False</td>
    </tr>
    <tr>
      <th>505</th>
      <td>455</td>
      <td>Carnivine</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>74</td>
      <td>100</td>
      <td>72</td>
      <td>90</td>
      <td>72</td>
      <td>46</td>
      <td>4</td>
      <td>False</td>
    </tr>
    <tr>
      <th>509</th>
      <td>459</td>
      <td>Snover</td>
      <td>Grass</td>
      <td>Ice</td>
      <td>60</td>
      <td>62</td>
      <td>50</td>
      <td>62</td>
      <td>60</td>
      <td>40</td>
      <td>4</td>
      <td>False</td>
    </tr>
    <tr>
      <th>510</th>
      <td>460</td>
      <td>Abomasnow</td>
      <td>Grass</td>
      <td>Ice</td>
      <td>90</td>
      <td>92</td>
      <td>75</td>
      <td>92</td>
      <td>85</td>
      <td>60</td>
      <td>4</td>
      <td>False</td>
    </tr>
    <tr>
      <th>511</th>
      <td>460</td>
      <td>AbomasnowMega Abomasnow</td>
      <td>Grass</td>
      <td>Ice</td>
      <td>90</td>
      <td>132</td>
      <td>105</td>
      <td>132</td>
      <td>105</td>
      <td>30</td>
      <td>4</td>
      <td>False</td>
    </tr>
    <tr>
      <th>516</th>
      <td>465</td>
      <td>Tangrowth</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>100</td>
      <td>100</td>
      <td>125</td>
      <td>110</td>
      <td>50</td>
      <td>50</td>
      <td>4</td>
      <td>False</td>
    </tr>
    <tr>
      <th>521</th>
      <td>470</td>
      <td>Leafeon</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>65</td>
      <td>110</td>
      <td>130</td>
      <td>60</td>
      <td>65</td>
      <td>95</td>
      <td>4</td>
      <td>False</td>
    </tr>
    <tr>
      <th>550</th>
      <td>492</td>
      <td>ShayminLand Forme</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>4</td>
      <td>True</td>
    </tr>
    <tr>
      <th>551</th>
      <td>492</td>
      <td>ShayminSky Forme</td>
      <td>Grass</td>
      <td>Flying</td>
      <td>100</td>
      <td>103</td>
      <td>75</td>
      <td>120</td>
      <td>75</td>
      <td>127</td>
      <td>4</td>
      <td>True</td>
    </tr>
    <tr>
      <th>554</th>
      <td>495</td>
      <td>Snivy</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>45</td>
      <td>45</td>
      <td>55</td>
      <td>45</td>
      <td>55</td>
      <td>63</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>555</th>
      <td>496</td>
      <td>Servine</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>60</td>
      <td>60</td>
      <td>75</td>
      <td>60</td>
      <td>75</td>
      <td>83</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>556</th>
      <td>497</td>
      <td>Serperior</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>75</td>
      <td>75</td>
      <td>95</td>
      <td>75</td>
      <td>95</td>
      <td>113</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>570</th>
      <td>511</td>
      <td>Pansage</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>50</td>
      <td>53</td>
      <td>48</td>
      <td>53</td>
      <td>48</td>
      <td>64</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>571</th>
      <td>512</td>
      <td>Simisage</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>75</td>
      <td>98</td>
      <td>63</td>
      <td>98</td>
      <td>63</td>
      <td>101</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>606</th>
      <td>546</td>
      <td>Cottonee</td>
      <td>Grass</td>
      <td>Fairy</td>
      <td>40</td>
      <td>27</td>
      <td>60</td>
      <td>37</td>
      <td>50</td>
      <td>66</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>607</th>
      <td>547</td>
      <td>Whimsicott</td>
      <td>Grass</td>
      <td>Fairy</td>
      <td>60</td>
      <td>67</td>
      <td>85</td>
      <td>77</td>
      <td>75</td>
      <td>116</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>608</th>
      <td>548</td>
      <td>Petilil</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>45</td>
      <td>35</td>
      <td>50</td>
      <td>70</td>
      <td>50</td>
      <td>30</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>609</th>
      <td>549</td>
      <td>Lilligant</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>70</td>
      <td>60</td>
      <td>75</td>
      <td>110</td>
      <td>75</td>
      <td>90</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>617</th>
      <td>556</td>
      <td>Maractus</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>75</td>
      <td>86</td>
      <td>67</td>
      <td>106</td>
      <td>67</td>
      <td>60</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>651</th>
      <td>590</td>
      <td>Foongus</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>69</td>
      <td>55</td>
      <td>45</td>
      <td>55</td>
      <td>55</td>
      <td>15</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>652</th>
      <td>591</td>
      <td>Amoonguss</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>114</td>
      <td>85</td>
      <td>70</td>
      <td>85</td>
      <td>80</td>
      <td>30</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>658</th>
      <td>597</td>
      <td>Ferroseed</td>
      <td>Grass</td>
      <td>Steel</td>
      <td>44</td>
      <td>50</td>
      <td>91</td>
      <td>24</td>
      <td>86</td>
      <td>10</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>659</th>
      <td>598</td>
      <td>Ferrothorn</td>
      <td>Grass</td>
      <td>Steel</td>
      <td>74</td>
      <td>94</td>
      <td>131</td>
      <td>54</td>
      <td>116</td>
      <td>20</td>
      <td>5</td>
      <td>False</td>
    </tr>
    <tr>
      <th>701</th>
      <td>640</td>
      <td>Virizion</td>
      <td>Grass</td>
      <td>Fighting</td>
      <td>91</td>
      <td>90</td>
      <td>72</td>
      <td>90</td>
      <td>129</td>
      <td>108</td>
      <td>5</td>
      <td>True</td>
    </tr>
    <tr>
      <th>718</th>
      <td>650</td>
      <td>Chespin</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>56</td>
      <td>61</td>
      <td>65</td>
      <td>48</td>
      <td>45</td>
      <td>38</td>
      <td>6</td>
      <td>False</td>
    </tr>
    <tr>
      <th>719</th>
      <td>651</td>
      <td>Quilladin</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>61</td>
      <td>78</td>
      <td>95</td>
      <td>56</td>
      <td>58</td>
      <td>57</td>
      <td>6</td>
      <td>False</td>
    </tr>
    <tr>
      <th>720</th>
      <td>652</td>
      <td>Chesnaught</td>
      <td>Grass</td>
      <td>Fighting</td>
      <td>88</td>
      <td>107</td>
      <td>122</td>
      <td>74</td>
      <td>75</td>
      <td>64</td>
      <td>6</td>
      <td>False</td>
    </tr>
    <tr>
      <th>740</th>
      <td>672</td>
      <td>Skiddo</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>66</td>
      <td>65</td>
      <td>48</td>
      <td>62</td>
      <td>57</td>
      <td>52</td>
      <td>6</td>
      <td>False</td>
    </tr>
    <tr>
      <th>741</th>
      <td>673</td>
      <td>Gogoat</td>
      <td>Grass</td>
      <td>NaN</td>
      <td>123</td>
      <td>100</td>
      <td>62</td>
      <td>97</td>
      <td>81</td>
      <td>68</td>
      <td>6</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>70 rows × 12 columns</p>
</div>




```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>800.000000</td>
      <td>800.000000</td>
      <td>800.000000</td>
      <td>800.000000</td>
      <td>800.000000</td>
      <td>800.000000</td>
      <td>800.000000</td>
      <td>800.00000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>362.813750</td>
      <td>69.258750</td>
      <td>79.001250</td>
      <td>73.842500</td>
      <td>72.820000</td>
      <td>71.902500</td>
      <td>68.277500</td>
      <td>3.32375</td>
    </tr>
    <tr>
      <th>std</th>
      <td>208.343798</td>
      <td>25.534669</td>
      <td>32.457366</td>
      <td>31.183501</td>
      <td>32.722294</td>
      <td>27.828916</td>
      <td>29.060474</td>
      <td>1.66129</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>10.000000</td>
      <td>20.000000</td>
      <td>5.000000</td>
      <td>1.00000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>184.750000</td>
      <td>50.000000</td>
      <td>55.000000</td>
      <td>50.000000</td>
      <td>49.750000</td>
      <td>50.000000</td>
      <td>45.000000</td>
      <td>2.00000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>364.500000</td>
      <td>65.000000</td>
      <td>75.000000</td>
      <td>70.000000</td>
      <td>65.000000</td>
      <td>70.000000</td>
      <td>65.000000</td>
      <td>3.00000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>539.250000</td>
      <td>80.000000</td>
      <td>100.000000</td>
      <td>90.000000</td>
      <td>95.000000</td>
      <td>90.000000</td>
      <td>90.000000</td>
      <td>5.00000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>721.000000</td>
      <td>255.000000</td>
      <td>190.000000</td>
      <td>230.000000</td>
      <td>194.000000</td>
      <td>230.000000</td>
      <td>180.000000</td>
      <td>6.00000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_values("Name", ascending=True)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
      <th>total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>510</th>
      <td>460</td>
      <td>Abomasnow</td>
      <td>Grass</td>
      <td>Ice</td>
      <td>90</td>
      <td>92</td>
      <td>75</td>
      <td>92</td>
      <td>85</td>
      <td>60</td>
      <td>4</td>
      <td>False</td>
      <td>182</td>
    </tr>
    <tr>
      <th>511</th>
      <td>460</td>
      <td>AbomasnowMega Abomasnow</td>
      <td>Grass</td>
      <td>Ice</td>
      <td>90</td>
      <td>132</td>
      <td>105</td>
      <td>132</td>
      <td>105</td>
      <td>30</td>
      <td>4</td>
      <td>False</td>
      <td>222</td>
    </tr>
    <tr>
      <th>68</th>
      <td>63</td>
      <td>Abra</td>
      <td>Psychic</td>
      <td>NaN</td>
      <td>25</td>
      <td>20</td>
      <td>15</td>
      <td>105</td>
      <td>55</td>
      <td>90</td>
      <td>1</td>
      <td>False</td>
      <td>45</td>
    </tr>
    <tr>
      <th>392</th>
      <td>359</td>
      <td>Absol</td>
      <td>Dark</td>
      <td>NaN</td>
      <td>65</td>
      <td>130</td>
      <td>60</td>
      <td>75</td>
      <td>60</td>
      <td>75</td>
      <td>3</td>
      <td>False</td>
      <td>195</td>
    </tr>
    <tr>
      <th>393</th>
      <td>359</td>
      <td>AbsolMega Absol</td>
      <td>Dark</td>
      <td>NaN</td>
      <td>65</td>
      <td>150</td>
      <td>60</td>
      <td>115</td>
      <td>60</td>
      <td>115</td>
      <td>3</td>
      <td>False</td>
      <td>215</td>
    </tr>
    <tr>
      <th>678</th>
      <td>617</td>
      <td>Accelgor</td>
      <td>Bug</td>
      <td>NaN</td>
      <td>80</td>
      <td>70</td>
      <td>40</td>
      <td>100</td>
      <td>60</td>
      <td>145</td>
      <td>5</td>
      <td>False</td>
      <td>150</td>
    </tr>
    <tr>
      <th>750</th>
      <td>681</td>
      <td>AegislashBlade Forme</td>
      <td>Steel</td>
      <td>Ghost</td>
      <td>60</td>
      <td>150</td>
      <td>50</td>
      <td>150</td>
      <td>50</td>
      <td>60</td>
      <td>6</td>
      <td>False</td>
      <td>210</td>
    </tr>
    <tr>
      <th>751</th>
      <td>681</td>
      <td>AegislashShield Forme</td>
      <td>Steel</td>
      <td>Ghost</td>
      <td>60</td>
      <td>50</td>
      <td>150</td>
      <td>50</td>
      <td>150</td>
      <td>60</td>
      <td>6</td>
      <td>False</td>
      <td>110</td>
    </tr>
    <tr>
      <th>153</th>
      <td>142</td>
      <td>Aerodactyl</td>
      <td>Rock</td>
      <td>Flying</td>
      <td>80</td>
      <td>105</td>
      <td>65</td>
      <td>60</td>
      <td>75</td>
      <td>130</td>
      <td>1</td>
      <td>False</td>
      <td>185</td>
    </tr>
    <tr>
      <th>154</th>
      <td>142</td>
      <td>AerodactylMega Aerodactyl</td>
      <td>Rock</td>
      <td>Flying</td>
      <td>80</td>
      <td>135</td>
      <td>85</td>
      <td>70</td>
      <td>95</td>
      <td>150</td>
      <td>1</td>
      <td>False</td>
      <td>215</td>
    </tr>
    <tr>
      <th>332</th>
      <td>306</td>
      <td>Aggron</td>
      <td>Steel</td>
      <td>Rock</td>
      <td>70</td>
      <td>110</td>
      <td>180</td>
      <td>60</td>
      <td>60</td>
      <td>50</td>
      <td>3</td>
      <td>False</td>
      <td>180</td>
    </tr>
    <tr>
      <th>333</th>
      <td>306</td>
      <td>AggronMega Aggron</td>
      <td>Steel</td>
      <td>NaN</td>
      <td>70</td>
      <td>140</td>
      <td>230</td>
      <td>60</td>
      <td>80</td>
      <td>50</td>
      <td>3</td>
      <td>False</td>
      <td>210</td>
    </tr>
    <tr>
      <th>205</th>
      <td>190</td>
      <td>Aipom</td>
      <td>Normal</td>
      <td>NaN</td>
      <td>55</td>
      <td>70</td>
      <td>55</td>
      <td>40</td>
      <td>55</td>
      <td>85</td>
      <td>2</td>
      <td>False</td>
      <td>125</td>
    </tr>
    <tr>
      <th>70</th>
      <td>65</td>
      <td>Alakazam</td>
      <td>Psychic</td>
      <td>NaN</td>
      <td>55</td>
      <td>50</td>
      <td>45</td>
      <td>135</td>
      <td>95</td>
      <td>120</td>
      <td>1</td>
      <td>False</td>
      <td>105</td>
    </tr>
    <tr>
      <th>71</th>
      <td>65</td>
      <td>AlakazamMega Alakazam</td>
      <td>Psychic</td>
      <td>NaN</td>
      <td>55</td>
      <td>50</td>
      <td>65</td>
      <td>175</td>
      <td>95</td>
      <td>150</td>
      <td>1</td>
      <td>False</td>
      <td>105</td>
    </tr>
    <tr>
      <th>655</th>
      <td>594</td>
      <td>Alomomola</td>
      <td>Water</td>
      <td>NaN</td>
      <td>165</td>
      <td>75</td>
      <td>80</td>
      <td>40</td>
      <td>45</td>
      <td>65</td>
      <td>5</td>
      <td>False</td>
      <td>240</td>
    </tr>
    <tr>
      <th>365</th>
      <td>334</td>
      <td>Altaria</td>
      <td>Dragon</td>
      <td>Flying</td>
      <td>75</td>
      <td>70</td>
      <td>90</td>
      <td>70</td>
      <td>105</td>
      <td>80</td>
      <td>3</td>
      <td>False</td>
      <td>145</td>
    </tr>
    <tr>
      <th>366</th>
      <td>334</td>
      <td>AltariaMega Altaria</td>
      <td>Dragon</td>
      <td>Fairy</td>
      <td>75</td>
      <td>110</td>
      <td>110</td>
      <td>110</td>
      <td>105</td>
      <td>80</td>
      <td>3</td>
      <td>False</td>
      <td>185</td>
    </tr>
    <tr>
      <th>768</th>
      <td>698</td>
      <td>Amaura</td>
      <td>Rock</td>
      <td>Ice</td>
      <td>77</td>
      <td>59</td>
      <td>50</td>
      <td>67</td>
      <td>63</td>
      <td>46</td>
      <td>6</td>
      <td>False</td>
      <td>136</td>
    </tr>
    <tr>
      <th>471</th>
      <td>424</td>
      <td>Ambipom</td>
      <td>Normal</td>
      <td>NaN</td>
      <td>75</td>
      <td>100</td>
      <td>66</td>
      <td>60</td>
      <td>66</td>
      <td>115</td>
      <td>4</td>
      <td>False</td>
      <td>175</td>
    </tr>
    <tr>
      <th>652</th>
      <td>591</td>
      <td>Amoonguss</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>114</td>
      <td>85</td>
      <td>70</td>
      <td>85</td>
      <td>80</td>
      <td>30</td>
      <td>5</td>
      <td>False</td>
      <td>199</td>
    </tr>
    <tr>
      <th>195</th>
      <td>181</td>
      <td>Ampharos</td>
      <td>Electric</td>
      <td>NaN</td>
      <td>90</td>
      <td>75</td>
      <td>85</td>
      <td>115</td>
      <td>90</td>
      <td>55</td>
      <td>2</td>
      <td>False</td>
      <td>165</td>
    </tr>
    <tr>
      <th>196</th>
      <td>181</td>
      <td>AmpharosMega Ampharos</td>
      <td>Electric</td>
      <td>Dragon</td>
      <td>90</td>
      <td>95</td>
      <td>105</td>
      <td>165</td>
      <td>110</td>
      <td>45</td>
      <td>2</td>
      <td>False</td>
      <td>185</td>
    </tr>
    <tr>
      <th>379</th>
      <td>347</td>
      <td>Anorith</td>
      <td>Rock</td>
      <td>Bug</td>
      <td>45</td>
      <td>95</td>
      <td>50</td>
      <td>40</td>
      <td>50</td>
      <td>75</td>
      <td>3</td>
      <td>False</td>
      <td>140</td>
    </tr>
    <tr>
      <th>29</th>
      <td>24</td>
      <td>Arbok</td>
      <td>Poison</td>
      <td>NaN</td>
      <td>60</td>
      <td>85</td>
      <td>69</td>
      <td>65</td>
      <td>79</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>145</td>
    </tr>
    <tr>
      <th>64</th>
      <td>59</td>
      <td>Arcanine</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>90</td>
      <td>110</td>
      <td>80</td>
      <td>100</td>
      <td>80</td>
      <td>95</td>
      <td>1</td>
      <td>False</td>
      <td>200</td>
    </tr>
    <tr>
      <th>552</th>
      <td>493</td>
      <td>Arceus</td>
      <td>Normal</td>
      <td>NaN</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>120</td>
      <td>4</td>
      <td>True</td>
      <td>240</td>
    </tr>
    <tr>
      <th>627</th>
      <td>566</td>
      <td>Archen</td>
      <td>Rock</td>
      <td>Flying</td>
      <td>55</td>
      <td>112</td>
      <td>45</td>
      <td>74</td>
      <td>45</td>
      <td>70</td>
      <td>5</td>
      <td>False</td>
      <td>167</td>
    </tr>
    <tr>
      <th>628</th>
      <td>567</td>
      <td>Archeops</td>
      <td>Rock</td>
      <td>Flying</td>
      <td>75</td>
      <td>140</td>
      <td>65</td>
      <td>112</td>
      <td>65</td>
      <td>110</td>
      <td>5</td>
      <td>False</td>
      <td>215</td>
    </tr>
    <tr>
      <th>182</th>
      <td>168</td>
      <td>Ariados</td>
      <td>Bug</td>
      <td>Poison</td>
      <td>70</td>
      <td>90</td>
      <td>70</td>
      <td>60</td>
      <td>60</td>
      <td>40</td>
      <td>2</td>
      <td>False</td>
      <td>160</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>607</th>
      <td>547</td>
      <td>Whimsicott</td>
      <td>Grass</td>
      <td>Fairy</td>
      <td>60</td>
      <td>67</td>
      <td>85</td>
      <td>77</td>
      <td>75</td>
      <td>116</td>
      <td>5</td>
      <td>False</td>
      <td>127</td>
    </tr>
    <tr>
      <th>604</th>
      <td>544</td>
      <td>Whirlipede</td>
      <td>Bug</td>
      <td>Poison</td>
      <td>40</td>
      <td>55</td>
      <td>99</td>
      <td>40</td>
      <td>79</td>
      <td>47</td>
      <td>5</td>
      <td>False</td>
      <td>95</td>
    </tr>
    <tr>
      <th>372</th>
      <td>340</td>
      <td>Whiscash</td>
      <td>Water</td>
      <td>Ground</td>
      <td>110</td>
      <td>78</td>
      <td>73</td>
      <td>76</td>
      <td>71</td>
      <td>60</td>
      <td>3</td>
      <td>False</td>
      <td>188</td>
    </tr>
    <tr>
      <th>317</th>
      <td>293</td>
      <td>Whismur</td>
      <td>Normal</td>
      <td>NaN</td>
      <td>64</td>
      <td>51</td>
      <td>23</td>
      <td>51</td>
      <td>23</td>
      <td>28</td>
      <td>3</td>
      <td>False</td>
      <td>115</td>
    </tr>
    <tr>
      <th>45</th>
      <td>40</td>
      <td>Wigglytuff</td>
      <td>Normal</td>
      <td>Fairy</td>
      <td>140</td>
      <td>70</td>
      <td>45</td>
      <td>85</td>
      <td>50</td>
      <td>45</td>
      <td>1</td>
      <td>False</td>
      <td>210</td>
    </tr>
    <tr>
      <th>301</th>
      <td>278</td>
      <td>Wingull</td>
      <td>Water</td>
      <td>Flying</td>
      <td>40</td>
      <td>30</td>
      <td>30</td>
      <td>55</td>
      <td>30</td>
      <td>85</td>
      <td>3</td>
      <td>False</td>
      <td>70</td>
    </tr>
    <tr>
      <th>217</th>
      <td>202</td>
      <td>Wobbuffet</td>
      <td>Psychic</td>
      <td>NaN</td>
      <td>190</td>
      <td>33</td>
      <td>58</td>
      <td>33</td>
      <td>58</td>
      <td>33</td>
      <td>2</td>
      <td>False</td>
      <td>223</td>
    </tr>
    <tr>
      <th>586</th>
      <td>527</td>
      <td>Woobat</td>
      <td>Psychic</td>
      <td>Flying</td>
      <td>55</td>
      <td>45</td>
      <td>43</td>
      <td>55</td>
      <td>43</td>
      <td>72</td>
      <td>5</td>
      <td>False</td>
      <td>100</td>
    </tr>
    <tr>
      <th>209</th>
      <td>194</td>
      <td>Wooper</td>
      <td>Water</td>
      <td>Ground</td>
      <td>55</td>
      <td>45</td>
      <td>45</td>
      <td>25</td>
      <td>25</td>
      <td>15</td>
      <td>2</td>
      <td>False</td>
      <td>100</td>
    </tr>
    <tr>
      <th>458</th>
      <td>413</td>
      <td>WormadamPlant Cloak</td>
      <td>Bug</td>
      <td>Grass</td>
      <td>60</td>
      <td>59</td>
      <td>85</td>
      <td>79</td>
      <td>105</td>
      <td>36</td>
      <td>4</td>
      <td>False</td>
      <td>119</td>
    </tr>
    <tr>
      <th>459</th>
      <td>413</td>
      <td>WormadamSandy Cloak</td>
      <td>Bug</td>
      <td>Ground</td>
      <td>60</td>
      <td>79</td>
      <td>105</td>
      <td>59</td>
      <td>85</td>
      <td>36</td>
      <td>4</td>
      <td>False</td>
      <td>139</td>
    </tr>
    <tr>
      <th>460</th>
      <td>413</td>
      <td>WormadamTrash Cloak</td>
      <td>Bug</td>
      <td>Steel</td>
      <td>60</td>
      <td>69</td>
      <td>95</td>
      <td>69</td>
      <td>95</td>
      <td>36</td>
      <td>4</td>
      <td>False</td>
      <td>129</td>
    </tr>
    <tr>
      <th>288</th>
      <td>265</td>
      <td>Wurmple</td>
      <td>Bug</td>
      <td>NaN</td>
      <td>45</td>
      <td>45</td>
      <td>35</td>
      <td>20</td>
      <td>30</td>
      <td>20</td>
      <td>3</td>
      <td>False</td>
      <td>90</td>
    </tr>
    <tr>
      <th>394</th>
      <td>360</td>
      <td>Wynaut</td>
      <td>Psychic</td>
      <td>NaN</td>
      <td>95</td>
      <td>23</td>
      <td>48</td>
      <td>23</td>
      <td>48</td>
      <td>23</td>
      <td>3</td>
      <td>False</td>
      <td>118</td>
    </tr>
    <tr>
      <th>192</th>
      <td>178</td>
      <td>Xatu</td>
      <td>Psychic</td>
      <td>Flying</td>
      <td>65</td>
      <td>75</td>
      <td>70</td>
      <td>95</td>
      <td>70</td>
      <td>95</td>
      <td>2</td>
      <td>False</td>
      <td>140</td>
    </tr>
    <tr>
      <th>792</th>
      <td>716</td>
      <td>Xerneas</td>
      <td>Fairy</td>
      <td>NaN</td>
      <td>126</td>
      <td>131</td>
      <td>95</td>
      <td>131</td>
      <td>98</td>
      <td>99</td>
      <td>6</td>
      <td>True</td>
      <td>257</td>
    </tr>
    <tr>
      <th>623</th>
      <td>562</td>
      <td>Yamask</td>
      <td>Ghost</td>
      <td>NaN</td>
      <td>38</td>
      <td>30</td>
      <td>85</td>
      <td>55</td>
      <td>65</td>
      <td>30</td>
      <td>5</td>
      <td>False</td>
      <td>68</td>
    </tr>
    <tr>
      <th>208</th>
      <td>193</td>
      <td>Yanma</td>
      <td>Bug</td>
      <td>Flying</td>
      <td>65</td>
      <td>65</td>
      <td>45</td>
      <td>75</td>
      <td>45</td>
      <td>95</td>
      <td>2</td>
      <td>False</td>
      <td>130</td>
    </tr>
    <tr>
      <th>520</th>
      <td>469</td>
      <td>Yanmega</td>
      <td>Bug</td>
      <td>Flying</td>
      <td>86</td>
      <td>76</td>
      <td>86</td>
      <td>116</td>
      <td>56</td>
      <td>95</td>
      <td>4</td>
      <td>False</td>
      <td>162</td>
    </tr>
    <tr>
      <th>793</th>
      <td>717</td>
      <td>Yveltal</td>
      <td>Dark</td>
      <td>Flying</td>
      <td>126</td>
      <td>131</td>
      <td>95</td>
      <td>131</td>
      <td>98</td>
      <td>99</td>
      <td>6</td>
      <td>True</td>
      <td>257</td>
    </tr>
    <tr>
      <th>367</th>
      <td>335</td>
      <td>Zangoose</td>
      <td>Normal</td>
      <td>NaN</td>
      <td>73</td>
      <td>115</td>
      <td>60</td>
      <td>60</td>
      <td>60</td>
      <td>90</td>
      <td>3</td>
      <td>False</td>
      <td>188</td>
    </tr>
    <tr>
      <th>157</th>
      <td>145</td>
      <td>Zapdos</td>
      <td>Electric</td>
      <td>Flying</td>
      <td>90</td>
      <td>90</td>
      <td>85</td>
      <td>125</td>
      <td>90</td>
      <td>100</td>
      <td>1</td>
      <td>True</td>
      <td>180</td>
    </tr>
    <tr>
      <th>582</th>
      <td>523</td>
      <td>Zebstrika</td>
      <td>Electric</td>
      <td>NaN</td>
      <td>75</td>
      <td>100</td>
      <td>63</td>
      <td>80</td>
      <td>63</td>
      <td>116</td>
      <td>5</td>
      <td>False</td>
      <td>175</td>
    </tr>
    <tr>
      <th>707</th>
      <td>644</td>
      <td>Zekrom</td>
      <td>Dragon</td>
      <td>Electric</td>
      <td>100</td>
      <td>150</td>
      <td>120</td>
      <td>120</td>
      <td>100</td>
      <td>90</td>
      <td>5</td>
      <td>True</td>
      <td>250</td>
    </tr>
    <tr>
      <th>286</th>
      <td>263</td>
      <td>Zigzagoon</td>
      <td>Normal</td>
      <td>NaN</td>
      <td>38</td>
      <td>30</td>
      <td>41</td>
      <td>30</td>
      <td>41</td>
      <td>60</td>
      <td>3</td>
      <td>False</td>
      <td>68</td>
    </tr>
    <tr>
      <th>632</th>
      <td>571</td>
      <td>Zoroark</td>
      <td>Dark</td>
      <td>NaN</td>
      <td>60</td>
      <td>105</td>
      <td>60</td>
      <td>120</td>
      <td>60</td>
      <td>105</td>
      <td>5</td>
      <td>False</td>
      <td>165</td>
    </tr>
    <tr>
      <th>631</th>
      <td>570</td>
      <td>Zorua</td>
      <td>Dark</td>
      <td>NaN</td>
      <td>40</td>
      <td>65</td>
      <td>40</td>
      <td>80</td>
      <td>40</td>
      <td>65</td>
      <td>5</td>
      <td>False</td>
      <td>105</td>
    </tr>
    <tr>
      <th>46</th>
      <td>41</td>
      <td>Zubat</td>
      <td>Poison</td>
      <td>Flying</td>
      <td>40</td>
      <td>45</td>
      <td>35</td>
      <td>30</td>
      <td>40</td>
      <td>55</td>
      <td>1</td>
      <td>False</td>
      <td>85</td>
    </tr>
    <tr>
      <th>695</th>
      <td>634</td>
      <td>Zweilous</td>
      <td>Dark</td>
      <td>Dragon</td>
      <td>72</td>
      <td>85</td>
      <td>70</td>
      <td>65</td>
      <td>70</td>
      <td>58</td>
      <td>5</td>
      <td>False</td>
      <td>157</td>
    </tr>
    <tr>
      <th>794</th>
      <td>718</td>
      <td>Zygarde50% Forme</td>
      <td>Dragon</td>
      <td>Ground</td>
      <td>108</td>
      <td>100</td>
      <td>121</td>
      <td>81</td>
      <td>95</td>
      <td>95</td>
      <td>6</td>
      <td>True</td>
      <td>208</td>
    </tr>
  </tbody>
</table>
<p>800 rows × 13 columns</p>
</div>




```python
df["total"] = df["HP"] + df["Attack"]
```


```python
df.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
      <th>total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bulbasaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>45</td>
      <td>49</td>
      <td>49</td>
      <td>65</td>
      <td>65</td>
      <td>45</td>
      <td>1</td>
      <td>False</td>
      <td>94</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Ivysaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>60</td>
      <td>62</td>
      <td>63</td>
      <td>80</td>
      <td>80</td>
      <td>60</td>
      <td>1</td>
      <td>False</td>
      <td>122</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>80</td>
      <td>82</td>
      <td>83</td>
      <td>100</td>
      <td>100</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>162</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>VenusaurMega Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>80</td>
      <td>100</td>
      <td>123</td>
      <td>122</td>
      <td>120</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>180</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Charmander</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>39</td>
      <td>52</td>
      <td>43</td>
      <td>60</td>
      <td>50</td>
      <td>65</td>
      <td>1</td>
      <td>False</td>
      <td>91</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.to_csv('modified.csv', index=False)
```


```python
df.loc[(df["Type 1"] == 'Grass') & (df["Type 2"] == 'Poison')]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>#</th>
      <th>Name</th>
      <th>Type 1</th>
      <th>Type 2</th>
      <th>HP</th>
      <th>Attack</th>
      <th>Defense</th>
      <th>Sp. Atk</th>
      <th>Sp. Def</th>
      <th>Speed</th>
      <th>Generation</th>
      <th>Legendary</th>
      <th>total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bulbasaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>45</td>
      <td>49</td>
      <td>49</td>
      <td>65</td>
      <td>65</td>
      <td>45</td>
      <td>1</td>
      <td>False</td>
      <td>94</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Ivysaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>60</td>
      <td>62</td>
      <td>63</td>
      <td>80</td>
      <td>80</td>
      <td>60</td>
      <td>1</td>
      <td>False</td>
      <td>122</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>80</td>
      <td>82</td>
      <td>83</td>
      <td>100</td>
      <td>100</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>162</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>VenusaurMega Venusaur</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>80</td>
      <td>100</td>
      <td>123</td>
      <td>122</td>
      <td>120</td>
      <td>80</td>
      <td>1</td>
      <td>False</td>
      <td>180</td>
    </tr>
    <tr>
      <th>48</th>
      <td>43</td>
      <td>Oddish</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>45</td>
      <td>50</td>
      <td>55</td>
      <td>75</td>
      <td>65</td>
      <td>30</td>
      <td>1</td>
      <td>False</td>
      <td>95</td>
    </tr>
    <tr>
      <th>49</th>
      <td>44</td>
      <td>Gloom</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>60</td>
      <td>65</td>
      <td>70</td>
      <td>85</td>
      <td>75</td>
      <td>40</td>
      <td>1</td>
      <td>False</td>
      <td>125</td>
    </tr>
    <tr>
      <th>50</th>
      <td>45</td>
      <td>Vileplume</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>75</td>
      <td>80</td>
      <td>85</td>
      <td>110</td>
      <td>90</td>
      <td>50</td>
      <td>1</td>
      <td>False</td>
      <td>155</td>
    </tr>
    <tr>
      <th>75</th>
      <td>69</td>
      <td>Bellsprout</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>50</td>
      <td>75</td>
      <td>35</td>
      <td>70</td>
      <td>30</td>
      <td>40</td>
      <td>1</td>
      <td>False</td>
      <td>125</td>
    </tr>
    <tr>
      <th>76</th>
      <td>70</td>
      <td>Weepinbell</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>65</td>
      <td>90</td>
      <td>50</td>
      <td>85</td>
      <td>45</td>
      <td>55</td>
      <td>1</td>
      <td>False</td>
      <td>155</td>
    </tr>
    <tr>
      <th>77</th>
      <td>71</td>
      <td>Victreebel</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>80</td>
      <td>105</td>
      <td>65</td>
      <td>100</td>
      <td>70</td>
      <td>70</td>
      <td>1</td>
      <td>False</td>
      <td>185</td>
    </tr>
    <tr>
      <th>344</th>
      <td>315</td>
      <td>Roselia</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>50</td>
      <td>60</td>
      <td>45</td>
      <td>100</td>
      <td>80</td>
      <td>65</td>
      <td>3</td>
      <td>False</td>
      <td>110</td>
    </tr>
    <tr>
      <th>451</th>
      <td>406</td>
      <td>Budew</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>40</td>
      <td>30</td>
      <td>35</td>
      <td>50</td>
      <td>70</td>
      <td>55</td>
      <td>4</td>
      <td>False</td>
      <td>70</td>
    </tr>
    <tr>
      <th>452</th>
      <td>407</td>
      <td>Roserade</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>60</td>
      <td>70</td>
      <td>65</td>
      <td>125</td>
      <td>105</td>
      <td>90</td>
      <td>4</td>
      <td>False</td>
      <td>130</td>
    </tr>
    <tr>
      <th>651</th>
      <td>590</td>
      <td>Foongus</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>69</td>
      <td>55</td>
      <td>45</td>
      <td>55</td>
      <td>55</td>
      <td>15</td>
      <td>5</td>
      <td>False</td>
      <td>124</td>
    </tr>
    <tr>
      <th>652</th>
      <td>591</td>
      <td>Amoonguss</td>
      <td>Grass</td>
      <td>Poison</td>
      <td>114</td>
      <td>85</td>
      <td>70</td>
      <td>85</td>
      <td>80</td>
      <td>30</td>
      <td>5</td>
      <td>False</td>
      <td>199</td>
    </tr>
  </tbody>
</table>
</div>


