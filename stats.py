from array import array
from namegen import namegen

def statread(pkm):
    p = array('B')
    p.fromstring(pkm)

    pid = p[0x00] + (p[0x01] << 8) + (p[0x02] << 16) + (p[0x03] << 24)
    nickname = namegen(pkm[0x48:0x5e])
    nat = nature.get(pid % 25)
    spec = species.get((p[0x09] << 8) + p[0x08])
    abil = ability.get(p[0x15])
    otname = namegen(pkm[0x68:0x78])
    otid = (p[0x0d] << 8) + p[0x0c]
    secid = (p[0x0f] << 8) + p[0x0e]
    ivs = ivcheck(p[0x38:0x3c])
    evs = evcheck(p[0x18:0x1e])
    happy = p[0x14]
    shiny = shinycheck(pid, otid, secid)
    if shiny: shiny = 'Shiny!'
    else: shiny = ''

    s = '%s: %s\n' % (nickname, shiny)
    s += '    %s %s with %s\n' % (nat, spec, abil)
    s += '    OT: %s, ID: %05d, Secret ID: %05d\n' % (otname, otid, secid)
    s += '    IVs: HP  %02d, Atk  %02d, Def  %02d, Spe  %02d, SpA  %02d, SpD  %02d\n' % ivs
    s += '    EVs: HP %03d, Atk %03d, Def %03d, Spe %03d, SpA %03d, SpD %03d, Total %03d\n' % evs
    s += '    Happiness: %d\n\n' % happy
    s += '=' * 80 + '\n\n'

    with open('pokemon.txt', 'a') as f:
        f.write(s)

def ivcheck(b):
    ivs = b[0] + (b[1] << 8) + (b[2] << 16) + (b[3] << 24)
    hp =  (ivs & 0x0000001f)
    atk = (ivs & 0x000003e0) >> 5
    df =  (ivs & 0x00007c00) >> 10
    spe = (ivs & 0x000f8000) >> 15
    spa = (ivs & 0x01f00000) >> 20
    spd = (ivs & 0x3e000000) >> 25
    return (hp, atk, df, spe, spa, spd)

def evcheck(b):
    hp = b[0]
    atk = b[1]
    df = b[2]
    spe = b[3]
    spa = b[4]
    spd = b[5]
    total = hp + atk + df + spe + spa + spd
    return (hp, atk, df, spe, spa, spd, total)

def shinycheck(pid, otid, secid):
    pida = pid >> 16
    pidb = pid & 0xffff
    ids = otid ^ secid
    pids = pida ^ pidb
    return (ids ^ pids) < 8

species = {
    1: 'Bulbasaur',
    2: 'Ivysaur',
    3: 'Venusaur',
    4: 'Charmander',
    5: 'Charmeleon',
    6: 'Charizard',
    7: 'Squirtle',
    8: 'Wartortle',
    9: 'Blastoise',
    10: 'Caterpie',
    11: 'Metapod',
    12: 'Butterfree',
    13: 'Weedle',
    14: 'Kakuna',
    15: 'Beedrill',
    16: 'Pidgey',
    17: 'Pidgeotto',
    18: 'Pidgeot',
    19: 'Rattata',
    20: 'Raticate',
    21: 'Spearow',
    22: 'Fearow',
    23: 'Ekans',
    24: 'Arbok',
    25: 'Pikachu',
    26: 'Raichu',
    27: 'Sandshrew',
    28: 'Sandslash',
    29: 'Nidoran (F)',
    30: 'Nidorina',
    31: 'Nidoqueen',
    32: 'Nidoran (M)',
    33: 'Nidorino',
    34: 'Nidoking',
    35: 'Clefairy',
    36: 'Clefable',
    37: 'Vulpix',
    38: 'Ninetales',
    39: 'Jigglypuff',
    40: 'Wigglytuff',
    41: 'Zubat',
    42: 'Golbat',
    43: 'Oddish',
    44: 'Gloom',
    45: 'Vileplume',
    46: 'Paras',
    47: 'Parasect',
    48: 'Venonat',
    49: 'Venomoth',
    50: 'Diglett',
    51: 'Dugtrio',
    52: 'Meowth',
    53: 'Persian',
    54: 'Psyduck',
    55: 'Golduck',
    56: 'Mankey',
    57: 'Primeape',
    58: 'Growlithe',
    59: 'Arcanine',
    60: 'Poliwag',
    61: 'Poliwhirl',
    62: 'Poliwrath',
    63: 'Abra',
    64: 'Kadabra',
    65: 'Alakazam',
    66: 'Machop',
    67: 'Machoke',
    68: 'Machamp',
    69: 'Bellsprout',
    70: 'Weepinbell',
    71: 'Victreebel',
    72: 'Tentacool',
    73: 'Tentacruel',
    74: 'Geodude',
    75: 'Graveler',
    76: 'Golem',
    77: 'Ponyta',
    78: 'Rapidash',
    79: 'Slowpoke',
    80: 'Slowbro',
    81: 'Magnemite',
    82: 'Magneton',
    83: 'Farfetch\'d',
    84: 'Doduo',
    85: 'Dodrio',
    86: 'Seel',
    87: 'Dewgong',
    88: 'Grimer',
    89: 'Muk',
    90: 'Shellder',
    91: 'Cloyster',
    92: 'Gastly',
    93: 'Haunter',
    94: 'Gengar',
    95: 'Onix',
    96: 'Drowzee',
    97: 'Hypno',
    98: 'Krabby',
    99: 'Kingler',
    100: 'Voltorb',
    101: 'Electrode',
    102: 'Exeggcute',
    103: 'Exeggutor',
    104: 'Cubone',
    105: 'Marowak',
    106: 'Hitmonlee',
    107: 'Hitmonchan',
    108: 'Lickitung',
    109: 'Koffing',
    110: 'Weezing',
    111: 'Rhyhorn',
    112: 'Rhydon',
    113: 'Chansey',
    114: 'Tangela',
    115: 'Kangaskhan',
    116: 'Horsea',
    117: 'Seadra',
    118: 'Goldeen',
    119: 'Seaking',
    120: 'Staryu',
    121: 'Starmie',
    122: 'Mr. Mime',
    123: 'Scyther',
    124: 'Jynx',
    125: 'Electabuzz',
    126: 'Magmar',
    127: 'Pinsir',
    128: 'Tauros',
    129: 'Magikarp',
    130: 'Gyarados',
    131: 'Lapras',
    132: 'Ditto',
    133: 'Eevee',
    134: 'Vaporeon',
    135: 'Jolteon',
    136: 'Flareon',
    137: 'Porygon',
    138: 'Omanyte',
    139: 'Omastar',
    140: 'Kabuto',
    141: 'Kabutops',
    142: 'Aerodactyl',
    143: 'Snorlax',
    144: 'Articuno',
    145: 'Zapdos',
    146: 'Moltres',
    147: 'Dratini',
    148: 'Dragonair',
    149: 'Dragonite',
    150: 'Mewtwo',
    151: 'Mew',
    152: 'Chikorita',
    153: 'Bayleef',
    154: 'Meganium',
    155: 'Cyndaquil',
    156: 'Quilava',
    157: 'Typhlosion',
    158: 'Totodile',
    159: 'Croconaw',
    160: 'Feraligatr',
    161: 'Sentret',
    162: 'Furret',
    163: 'Hoothoot',
    164: 'Noctowl',
    165: 'Ledyba',
    166: 'Ledian',
    167: 'Spinarak',
    168: 'Ariados',
    169: 'Crobat',
    170: 'Chinchou',
    171: 'Lanturn',
    172: 'Pichu',
    173: 'Cleffa',
    174: 'Igglybuff',
    175: 'Togepi',
    176: 'Togetic',
    177: 'Natu',
    178: 'Xatu',
    179: 'Mareep',
    180: 'Flaaffy',
    181: 'Ampharos',
    182: 'Bellossom',
    183: 'Marill',
    184: 'Azumarill',
    185: 'Sudowoodo',
    186: 'Politoed',
    187: 'Hoppip',
    188: 'Skiploom',
    189: 'Jumpluff',
    190: 'Aipom',
    191: 'Sunkern',
    192: 'Sunflora',
    193: 'Yanma',
    194: 'Wooper',
    195: 'Quagsire',
    196: 'Espeon',
    197: 'Umbreon',
    198: 'Murkrow',
    199: 'Slowking',
    200: 'Misdreavus',
    201: 'Unown',
    202: 'Wobbuffet',
    203: 'Girafarig',
    204: 'Pineco',
    205: 'Forretress',
    206: 'Dunsparce',
    207: 'Gligar',
    208: 'Steelix',
    209: 'Snubbull',
    210: 'Granbull',
    211: 'Qwilfish',
    212: 'Scizor',
    213: 'Shuckle',
    214: 'Heracross',
    215: 'Sneasel',
    216: 'Teddiursa',
    217: 'Ursaring',
    218: 'Slugma',
    219: 'Magcargo',
    220: 'Swinub',
    221: 'Piloswine',
    222: 'Corsola',
    223: 'Remoraid',
    224: 'Octillery',
    225: 'Delibird',
    226: 'Mantine',
    227: 'Skarmory',
    228: 'Houndour',
    229: 'Houndoom',
    230: 'Kingdra',
    231: 'Phanpy',
    232: 'Donphan',
    233: 'Porygon2',
    234: 'Stantler',
    235: 'Smeargle',
    236: 'Tyrogue',
    237: 'Hitmontop',
    238: 'Smoochum',
    239: 'Elekid',
    240: 'Magby',
    241: 'Miltank',
    242: 'Blissey',
    243: 'Raikou',
    244: 'Entei',
    245: 'Suicune',
    246: 'Larvitar',
    247: 'Pupitar',
    248: 'Tyranitar',
    249: 'Lugia',
    250: 'Ho-Oh',
    251: 'Celebi',
    252: 'Treecko',
    253: 'Grovyle',
    254: 'Sceptile',
    255: 'Torchic',
    256: 'Combusken',
    257: 'Blaziken',
    258: 'Mudkip',
    259: 'Marshtomp',
    260: 'Swampert',
    261: 'Poochyena',
    262: 'Mightyena',
    263: 'Zigzagoon',
    264: 'Linoone',
    265: 'Wurmple',
    266: 'Silcoon',
    267: 'Beautifly',
    268: 'Cascoon',
    269: 'Dustox',
    270: 'Lotad',
    271: 'Lombre',
    272: 'Ludicolo',
    273: 'Seedot',
    274: 'Nuzleaf',
    275: 'Shiftry',
    276: 'Taillow',
    277: 'Swellow',
    278: 'Wingull',
    279: 'Pelipper',
    280: 'Ralts',
    281: 'Kirlia',
    282: 'Gardevoir',
    283: 'Surskit',
    284: 'Masquerain',
    285: 'Shroomish',
    286: 'Breloom',
    287: 'Slakoth',
    288: 'Vigoroth',
    289: 'Slaking',
    290: 'Nincada',
    291: 'Ninjask',
    292: 'Shedinja',
    293: 'Whismur',
    294: 'Loudred',
    295: 'Exploud',
    296: 'Makuhita',
    297: 'Hariyama',
    298: 'Azurill',
    299: 'Nosepass',
    300: 'Skitty',
    301: 'Delcatty',
    302: 'Sableye',
    303: 'Mawile',
    304: 'Aron',
    305: 'Lairon',
    306: 'Aggron',
    307: 'Meditite',
    308: 'Medicham',
    309: 'Electrike',
    310: 'Manectric',
    311: 'Plusle',
    312: 'Minun',
    313: 'Volbeat',
    314: 'Illumise',
    315: 'Roselia',
    316: 'Gulpin',
    317: 'Swalot',
    318: 'Carvanha',
    319: 'Sharpedo',
    320: 'Wailmer',
    321: 'Wailord',
    322: 'Numel',
    323: 'Camerupt',
    324: 'Torkoal',
    325: 'Spoink',
    326: 'Grumpig',
    327: 'Spinda',
    328: 'Trapinch',
    329: 'Vibrava',
    330: 'Flygon',
    331: 'Cacnea',
    332: 'Cacturne',
    333: 'Swablu',
    334: 'Altaria',
    335: 'Zangoose',
    336: 'Seviper',
    337: 'Lunatone',
    338: 'Solrock',
    339: 'Barboach',
    340: 'Whiscash',
    341: 'Corphish',
    342: 'Crawdaunt',
    343: 'Baltoy',
    344: 'Claydol',
    345: 'Lileep',
    346: 'Cradily',
    347: 'Anorith',
    348: 'Armaldo',
    349: 'Feebas',
    350: 'Milotic',
    351: 'Castform',
    352: 'Kecleon',
    353: 'Shuppet',
    354: 'Banette',
    355: 'Duskull',
    356: 'Dusclops',
    357: 'Tropius',
    358: 'Chimecho',
    359: 'Absol',
    360: 'Wynaut',
    361: 'Snorunt',
    362: 'Glalie',
    363: 'Spheal',
    364: 'Sealeo',
    365: 'Walrein',
    366: 'Clamperl',
    367: 'Huntail',
    368: 'Gorebyss',
    369: 'Relicanth',
    370: 'Luvdisc',
    371: 'Bagon',
    372: 'Shelgon',
    373: 'Salamence',
    374: 'Beldum',
    375: 'Metang',
    376: 'Metagross',
    377: 'Regirock',
    378: 'Regice',
    379: 'Registeel',
    380: 'Latias',
    381: 'Latios',
    382: 'Kyogre',
    383: 'Groudon',
    384: 'Rayquaza',
    385: 'Jirachi',
    386: 'Deoxys',
    387: 'Turtwig',
    388: 'Grotle',
    389: 'Torterra',
    390: 'Chimchar',
    391: 'Monferno',
    392: 'Infernape',
    393: 'Piplup',
    394: 'Prinplup',
    395: 'Empoleon',
    396: 'Starly',
    397: 'Staravia',
    398: 'Staraptor',
    399: 'Bidoof',
    400: 'Bibarel',
    401: 'Kricketot',
    402: 'Kricketune',
    403: 'Shinx',
    404: 'Luxio',
    405: 'Luxray',
    406: 'Budew',
    407: 'Roserade',
    408: 'Cranidos',
    409: 'Rampardos',
    410: 'Shieldon',
    411: 'Bastiodon',
    412: 'Burmy',
    413: 'Wormadam',
    414: 'Mothim',
    415: 'Combee',
    416: 'Vespiquen',
    417: 'Pachirisu',
    418: 'Buizel',
    419: 'Floatzel',
    420: 'Cherubi',
    421: 'Cherrim',
    422: 'Shellos',
    423: 'Gastrodon',
    424: 'Ambipom',
    425: 'Drifloon',
    426: 'Drifblim',
    427: 'Buneary',
    428: 'Lopunny',
    429: 'Mismagius',
    430: 'Honchkrow',
    431: 'Glameow',
    432: 'Purugly',
    433: 'Chingling',
    434: 'Stunky',
    435: 'Skuntank',
    436: 'Bronzor',
    437: 'Bronzong',
    438: 'Bonsly',
    439: 'Mime Jr.',
    440: 'Happiny',
    441: 'Chatot',
    442: 'Spiritomb',
    443: 'Gible',
    444: 'Gabite',
    445: 'Garchomp',
    446: 'Munchlax',
    447: 'Riolu',
    448: 'Lucario',
    449: 'Hippopotas',
    450: 'Hippowdon',
    451: 'Skorupi',
    452: 'Drapion',
    453: 'Croagunk',
    454: 'Toxicroak',
    455: 'Carnivine',
    456: 'Finneon',
    457: 'Lumineon',
    458: 'Mantyke',
    459: 'Snover',
    460: 'Abomasnow',
    461: 'Weavile',
    462: 'Magnezone',
    463: 'Lickilicky',
    464: 'Rhyperior',
    465: 'Tangrowth',
    466: 'Electivire',
    467: 'Magmortar',
    468: 'Togekiss',
    469: 'Yanmega',
    470: 'Leafeon',
    471: 'Glaceon',
    472: 'Gliscor',
    473: 'Mamoswine',
    474: 'Porygon-Z',
    475: 'Gallade',
    476: 'Probopass',
    477: 'Dusknoir',
    478: 'Froslass',
    479: 'Rotom',
    480: 'Uxie',
    481: 'Mesprit',
    482: 'Azelf',
    483: 'Dialga',
    484: 'Palkia',
    485: 'Heatran',
    486: 'Regigigas',
    487: 'Giratina',
    488: 'Cresselia',
    489: 'Phione',
    490: 'Manaphy',
    491: 'Darkrai',
    492: 'Shaymin',
    493: 'Arceus'
}

nature = {
    0: 'Hardy',
    1: 'Lonely',
    2: 'Brave',
    3: 'Adamant',
    4: 'Naughty',
    5: 'Bold',
    6: 'Docile',
    7: 'Relaxed',
    8: 'Impish',
    9: 'Lax',
    10: 'Timid',
    11: 'Hasty',
    12: 'Serious',
    13: 'Jolly',
    14: 'Naive',
    15: 'Modest',
    16: 'Mild',
    17: 'Quiet',
    18: 'Bashful',
    19: 'Rash',
    20: 'Calm',
    21: 'Gentle',
    22: 'Sassy',
    23: 'Careful',
    24: 'Quirky'
}

ability = {
    1: 'Stench',
    2: 'Drizzle',
    3: 'Speed Boost',
    4: 'Battle Armor',
    5: 'Sturdy',
    6: 'Damp',
    7: 'Limber',
    8: 'Sand Veil',
    9: 'Static',
    10: 'Volt Absorb',
    11: 'Water Absorb',
    12: 'Oblivious',
    13: 'Cloud Nine',
    14: 'Compoundeyes',
    15: 'Insomnia',
    16: 'Color Change',
    17: 'Immunity',
    18: 'Flash Fire',
    19: 'Shield Dust',
    20: 'Own Tempo',
    21: 'Suction Cups',
    22: 'Intimidate',
    23: 'Shadow Tag',
    24: 'Rough Skin',
    25: 'Wonder Guard',
    26: 'Levitate',
    27: 'Effect Spore',
    28: 'Synchronize',
    29: 'Clear Body',
    30: 'Natural Cure',
    31: 'Lightningrod',
    32: 'Serene Grace',
    33: 'Swift Swim',
    34: 'Chlorophyll',
    35: 'Illuminate',
    36: 'Trace',
    37: 'Huge Power',
    38: 'Poison Point',
    39: 'Inner Focus',
    40: 'Magma Armor',
    41: 'Water Veil',
    42: 'Magnet Pull',
    43: 'Soundproof',
    44: 'Rain Dish',
    45: 'Sand Stream',
    46: 'Pressure',
    47: 'Thick Fat',
    48: 'Early Bird',
    49: 'Flame Body',
    50: 'Run Away',
    51: 'Keen Eye',
    52: 'Hyper Cutter',
    53: 'Pickup',
    54: 'Truant',
    55: 'Hustle',
    56: 'Cute Charm',
    57: 'Plus',
    58: 'Minus',
    59: 'Forecast',
    60: 'Sticky Hold',
    61: 'Shed Skin',
    62: 'Guts',
    63: 'Marvel Scale',
    64: 'Liquid Ooze',
    65: 'Overgrow',
    66: 'Blaze',
    67: 'Torrent',
    68: 'Swarm',
    69: 'Rock Head',
    70: 'Drought',
    71: 'Arena Trap',
    72: 'Vital Spirit',
    73: 'White Smoke',
    74: 'Pure Power',
    75: 'Shell Armor',
    76: 'Air Lock',
    77: 'Tangled Feet',
    78: 'Motor Drive',
    79: 'Rivalry',
    80: 'Steadfast',
    81: 'Snow Cloak',
    82: 'Gluttony',
    83: 'Anger Point',
    84: 'Unburden',
    85: 'Heatproof',
    86: 'Simple',
    87: 'Dry Skin',
    88: 'Download',
    89: 'Iron Fist',
    90: 'Poison Heal',
    91: 'Adaptability',
    92: 'Skill Link',
    93: 'Hydration',
    94: 'Solar Power',
    95: 'Quick Feet',
    96: 'Normalize',
    97: 'Sniper',
    98: 'Magic Guard',
    99: 'No Guard',
    100: 'Stall',
    101: 'Technician',
    102: 'Leaf Guard',
    103: 'Klutz',
    104: 'Mold Breaker',
    105: 'Super Luck',
    106: 'Aftermath',
    107: 'Anticipation',
    108: 'Forewarn',
    109: 'Unaware',
    110: 'Tinted Lens',
    111: 'Filter',
    112: 'Slow Start',
    113: 'Scrappy',
    114: 'Storm Drain',
    115: 'Ice Body',
    116: 'Solid Rock',
    117: 'Snow Warning',
    118: 'Honey Gather',
    119: 'Frisk',
    120: 'Reckless',
    121: 'Multitype',
    122: 'Flower Gift',
    123: 'Bad Dreams'
}