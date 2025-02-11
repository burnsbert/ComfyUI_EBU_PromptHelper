# color_data.py

# Master COLORS dictionary
COLORS = {
    # Reds
    'CRIMSON': '#DC143C',
    'CADMIUM RED': '#E30022',
    'CADMIUM RED DEEP': '#B31B1B',
    'PYRROLE RED': '#FF3A2A',
    'SCARLET': '#FF2400',
    'CARMINE': '#960018',
    'MAGENTA': '#FF00FF',
    'VENETIAN RED': '#C80815',
    'INDIAN RED': '#CD5C5C',
    'RUBY RED': '#9B111E',
    'TRUE RED': '#FF0000',

    # Pinks
    'POWDER PINK': '#FFB6C1',
    'STRAWBERRY PINK': '#FF9899',
    'HOT PINK': '#FF69B4',
    'PERSIAN ROSE': '#FE28A2',
    'FLAMINGO PINK': '#FC8EAC',
    'ROSE BLUSH': '#FFE4E1',
    'BALLET PINK': '#F4C2C2',
    'BLUSH ROSE': '#FEC5E5',
    'FUCHSIA': '#FF00FF',
    'MAGENTA': '#FF00FF',
    'ELECTRIC PINK': '#FF1493',
    'COTTON CANDY PINK': '#FFB7D5',

    # Oranges
    'CADMIUM ORANGE': '#FF6103',
    'BURNT ORANGE': '#CC5500',
    'PERSIMMON': '#EC5800',
    'SUNSET ORANGE': '#FD5E53',
    'APRICOT ORANGE': '#FFA500',
    'PASTEL ORANGE': '#FFB347',
    'BURNT SIENNA': '#E97451',
    'RAW SIENNA': '#D68A59',
    'TANGERINE': '#FFA500',
    'ORANGE CREAM': '#FFD8B1',
    'MANGO': '#FFA62B',

    # Yellows
    'GOLD OCHRE': '#D4AF37',
    'YELLOW OCHRE': '#DFAF2C',
    'NAPLES YELLOW': '#FADA5E',
    'INDIAN YELLOW': '#E3A857',
    'AZO YELLOW': '#FAFA33',
    'HANSA YELLOW': '#E9D66B',
    'CANARY YELLOW': '#FFEF00',
    'MARIGOLD': '#EAA221',
    'AMBER': '#FFBF00',
    'WARM YELLOW': '#FFAA33',
    'LEMON YELLOW': '#FFF44F',
    'PASTEL YELLOW': '#FFF9A5',
    'ELECTRIC YELLOW': '#FFFF33',
    'BUTTERMILK': '#F8E4A0',
    'LEMON CHIFFON': '#FFFACD',

    # Additional warm hues
    'VERMILION': '#E34234',
    'TANGERINE': '#F28500',
    'TERRACOTTA': '#E2725B',
    'BURGUNDY': '#800020',
    'MARS RED': '#CE1620',

    # Greens
    'LIME GREEN': '#32CD32',
    'VIRIDIAN': '#40826D',
    'PHTHALO GREEN': '#123524',
    "HOOKER'S GREEN": '#49796B',
    'SAP GREEN': '#507D2A',
    'OLIVE GREEN': '#BAB86C',
    'CINNABAR GREEN': '#61B329',
    'EMERALD GREEN': '#50C878',
    'AQUA GREEN CHROMIUM': '#65B8A7',
    'MINT GREEN': '#98FF98',
    'FOREST GREEN': '#228B22',
    'CHROME GREEN': '#2E4A25',
    'CERULEAN GREEN': '#0F9B8E',
    'PISTACHIO': '#93C572',
    'SEAFOAM': '#98FF98',
    'HONEYDEW': '#F0FFF0',
    'YELLOW GREEN': '#9ACD32',
    'CELADON': '#ACE1AF',
    'VERDIGRIS': '#43B3AE',
    'AQUAMARINE': '#7FFFD4',
    'TURQUOISE': '#40E0D0',

    # Blues
    'ULTRAMARINE BLUE': '#1B1B7A',
    'COBALT BLUE': '#0047AB',
    'CERULEAN BLUE': '#2A52BE',
    'PHTHALO BLUE': '#000F89',
    'PRUSSIAN BLUE': '#003153',
    'ROYAL BLUE': '#4169E1',
    'SKY BLUE': '#87CEEB',
    'EGYPTIAN BLUE': '#1034A6',
    'AQUAMARINE': '#7FFFD4',
    'DENIM BLUE': '#1560BD',
    'NAVY': '#000080',
    'LAPIS LAZULI': '#26619C',
    'INDIGO': '#4B0082',
    'POWDER BLUE': '#B6D0E2',
    'BABY BLUE': '#89CFF0',
    'DUCK EGG BLUE': '#E0FFFF',
    'TURQUOISE': '#40E0D0',
    'AZURE': '#007FFF',
    'SAPPHIRE BLUE': '#0F52BA',
    'DODGER BLUE': '#1E90FF',

    # Purples
    'COBALT VIOLET LIGHT': '#CF71AF',
    'DIOXAZINE PURPLE': '#6C3082',
    'QUINACRIDONE VIOLET': '#B385BB',
    'LILAC': '#C8A2C8',
    'AMETHYST PURPLE': '#9966CC',
    'PLUM': '#8E4585',
    'ORCHID': '#DA70D6',
    'LAVENDER': '#E6E6FA',
    'PERIWINKLE': '#CCCCFF',
    'ULTRAMARINE VIOLET': '#5C246E',
    'MAUVE': '#E0B0FF',
    'FUCHSIA': '#FF00FF',
    'BLUE-VIOLET': '#8A2BE2',

    # Browns
    'BURNT SIENNA': '#E97451',
    'RAW SIENNA': '#D68A59',
    'TERRACOTTA': '#E2725B',
    'BURNT UMBER': '#8A3324',
    'TAUPE': '#483C32',
    'SEPIA': '#704214',

    # Greys and Neutrals
    'BEIGE': '#F5F5DC',
    'ALABASTER': '#FEFEE2',
    'WHITE': '#FFFFFF',
    'PEARL WHITE': '#FDEEF4',
    "PAYNE'S GRAY": '#536878',
    'NEUTRAL GRAY': '#808080',
    'WARM GRAY': '#808077',
    'COOL GRAY': '#798081',
    'CHARCOAL GRAY': '#364135',
    'GRAPHITE GRAY': '#474A51',
    'STONE GRAY': '#928E85',
    'SILVER GRAY': '#C0C0C0',
    'DARK SLATE GRAY': '#2F4F4F',
    'IVORY BLACK': '#292421',
    'MARS BLACK': '#232323',

    # Neutrals (lighter tones)
    'CREAM': '#FFFDD0',
    'EGGSHELL': '#F0EAD6',

    # Peach/Coral tones
    'PEACH': '#FFE5B4',
    'CORAL': '#FF7F50',
    'APRICOT': '#FBCEB1',

    # Specialty/Metallic
    'GOLD': '#FFD700',
    'SILVER': '#C0C0C0',
    'COPPER': '#B87333',
    'BRONZE': '#CD7F32',
    'ROSE GOLD': '#B76E79',
    'ROSE BRONZE': '#B76E43',
    'GUNMETAL': '#2C3539',
    'PLATINUM': '#E5E4E2',
    'ANTIQUE GOLD': '#CFB53B',

    # Specialty Finishes
    'MINT CREAM': '#F5FFFA',
    'PEWTER': '#899499'
}

# Color Families
color_families = {
    'Reds': [
        'CRIMSON', 'CADMIUM RED', 'CADMIUM RED DEEP', 'PYRROLE RED',
        'SCARLET', 'CARMINE', 'MAGENTA',
        'VENETIAN RED', 'INDIAN RED', 'RUBY RED',
        'VERMILION', 'MARS RED', 'TRUE RED'
    ],
    'Pinks': [
        'POWDER PINK', 'STRAWBERRY PINK', 'HOT PINK', 'PERSIAN ROSE',
        'FLAMINGO PINK', 'ROSE BLUSH', 'BALLET PINK', 'BLUSH ROSE',
        'FUCHSIA', 'MAGENTA', 'ELECTRIC PINK', 'COTTON CANDY PINK', 'CORAL'
    ],
    'Oranges': [
        'CADMIUM ORANGE', 'BURNT ORANGE', 'PERSIMMON', 'SUNSET ORANGE',
        'APRICOT ORANGE', 'PASTEL ORANGE', 'BURNT SIENNA', 'RAW SIENNA',
        'TANGERINE', 'ORANGE CREAM', 'MANGO'
    ],
    'Yellows': [
        'GOLD OCHRE', 'YELLOW OCHRE', 'NAPLES YELLOW', 'INDIAN YELLOW',
        'AZO YELLOW', 'HANSA YELLOW', 'CANARY YELLOW', 'MARIGOLD',
        'AMBER', 'WARM YELLOW', 'LEMON YELLOW', 'PASTEL YELLOW',
        'ELECTRIC YELLOW', 'BUTTERMILK', 'LEMON CHIFFON'
    ],
    'Greens': [
        'LIME GREEN', 'VIRIDIAN', 'PHTHALO GREEN', "HOOKER'S GREEN",
        'SAP GREEN', 'OLIVE GREEN', 'CINNABAR GREEN', 'EMERALD GREEN',
        'AQUA GREEN CHROMIUM', 'MINT GREEN', 'FOREST GREEN', 'CHROME GREEN',
        'CERULEAN GREEN', 'PISTACHIO', 'SEAFOAM', 'HONEYDEW',
        'YELLOW GREEN', 'CELADON', 'VERDIGRIS', 'AQUAMARINE', 'TURQUOISE'
    ],
    'Blues': [
        'ULTRAMARINE BLUE', 'COBALT BLUE', 'CERULEAN BLUE', 'PHTHALO BLUE',
        'PRUSSIAN BLUE', 'ROYAL BLUE', 'SKY BLUE', 'EGYPTIAN BLUE',
        'AQUAMARINE', 'DENIM BLUE', 'NAVY', 'LAPIS LAZULI', 'INDIGO',
        'POWDER BLUE', 'BABY BLUE', 'DUCK EGG BLUE',
        'TURQUOISE', 'AZURE', 'SAPPHIRE BLUE', 'DODGER BLUE'
    ],
    'Purples': [
        'COBALT VIOLET LIGHT', 'DIOXAZINE PURPLE', 'QUINACRIDONE VIOLET',
        'LILAC', 'AMETHYST PURPLE', 'PLUM', 'ORCHID', 'LAVENDER',
        'PERIWINKLE', 'ULTRAMARINE VIOLET', 'MAUVE', 'FUCHSIA',
        'BLUE-VIOLET'
    ],
    'Browns': [
        'BURNT SIENNA', 'RAW SIENNA', 'TERRACOTTA', 'BURNT UMBER',
        'TAUPE', 'SEPIA'
    ],
    'Greys': [
        "PAYNE'S GRAY", 'NEUTRAL GRAY', 'WARM GRAY', 'COOL GRAY',
        'CHARCOAL GRAY', 'GRAPHITE GRAY', 'STONE GRAY', 'SILVER GRAY',
        'DARK SLATE GRAY', 'GUNMETAL', 'PEWTER',
        'WHITE', 'ALABASTER', 'PEARL WHITE',
        'IVORY BLACK', 'MARS BLACK'
    ],
    'Neutrals': [
        'BEIGE', 'ALABASTER', 'WHITE', 'PEARL WHITE',
        'CREAM', 'EGGSHELL'
    ],
    'Metallics': [
        'GOLD', 'SILVER', 'COPPER', 'BRONZE', 'ROSE GOLD', 'ROSE BRONZE',
        'PLATINUM', 'ANTIQUE GOLD', 'GUNMETAL'
    ],
    'Broad Neutrals': [],  # Will be computed dynamically.
    'Pastels': [
        'POWDER PINK', 'BALLET PINK', 'ROSE BLUSH', 'PASTEL ORANGE',
        'POWDER BLUE', 'BABY BLUE', 'DUCK EGG BLUE',
        'HONEYDEW', 'MINT CREAM', 'LILAC', 'MAUVE', 'ORANGE CREAM',
        'LEMON CHIFFON', 'CELADON', 'PASTEL YELLOW',
    ],
    'Peaches': [
        'PEACH', 'CORAL', 'APRICOT', 'APRICOT ORANGE'
    ],
    'Warm Colors': [
        'CRIMSON', 'CADMIUM RED', 'CADMIUM RED DEEP', 'PYRROLE RED',
        'SCARLET', 'CARMINE', 'MAGENTA',
        'VENETIAN RED', 'INDIAN RED', 'RUBY RED',
        'VERMILION', 'MARS RED', 'TRUE RED',
        'POWDER PINK', 'STRAWBERRY PINK', 'HOT PINK', 'PERSIAN ROSE',
        'FLAMINGO PINK', 'ROSE BLUSH', 'BALLET PINK', 'BLUSH ROSE',
        'ELECTRIC PINK', 'COTTON CANDY PINK',
        'CADMIUM ORANGE', 'BURNT ORANGE', 'PERSIMMON', 'SUNSET ORANGE',
        'APRICOT ORANGE', 'PASTEL ORANGE', 'BURNT SIENNA', 'RAW SIENNA', 'TANGERINE',
        'ORANGE CREAM', 'MANGO',
        'GOLD OCHRE', 'YELLOW OCHRE', 'NAPLES YELLOW', 'INDIAN YELLOW',
        'AZO YELLOW', 'HANSA YELLOW', 'CANARY YELLOW', 'MARIGOLD',
        'AMBER', 'WARM YELLOW', 'LEMON YELLOW', 'PASTEL YELLOW',
        'TERRACOTTA', 'BURNT UMBER', 'PEACH', 'CORAL', 'APRICOT',
        'GOLD', 'ANTIQUE GOLD'
    ],
	'Cool Colors': [
	    'LIME GREEN', 'VIRIDIAN', 'PHTHALO GREEN', "HOOKER'S GREEN",
	    'SAP GREEN', 'OLIVE GREEN', 'CINNABAR GREEN', 'EMERALD GREEN',
	    'AQUA GREEN CHROMIUM', 'MINT GREEN', 'FOREST GREEN', 'CHROME GREEN',
	    'CERULEAN GREEN', 'PISTACHIO', 'SEAFOAM', 'HONEYDEW',
	    'ULTRAMARINE BLUE', 'ROYAL BLUE', 'SKY BLUE', 'EGYPTIAN BLUE', 'AQUAMARINE',
	    'DENIM BLUE', 'NAVY', 'LAPIS LAZULI', 'INDIGO',
	    'POWDER BLUE', 'BABY BLUE', 'DUCK EGG BLUE', 'TURQUOISE',
	    'COBALT VIOLET LIGHT', 'DIOXAZINE PURPLE', 'QUINACRIDONE VIOLET',
	    'LILAC', 'AMETHYST PURPLE', 'PLUM', 'ORCHID', 'LAVENDER',
	    'PERIWINKLE', 'ULTRAMARINE VIOLET', 'MAUVE',
	    'AZURE', 'DODGER BLUE', 'CERULEAN BLUE', 'COBALT BLUE', 'PRUSSIAN BLUE'
	]
}

# Dynamically compute Broad Neutrals as the union of Neutrals, Greys, Browns, and Metallics.
broad_neutrals = set(color_families['Neutrals'] + color_families['Greys'] + color_families['Browns'] + color_families['Metallics'])
color_families['Broad Neutrals'] = sorted(list(broad_neutrals))

# Each palette is defined as one list:
# The first element is the palette name (a descriptive title),
# and the remaining elements are the color names.
# All categories are stored as one large list of palettes.
COLOR_PALETTES = {
    # each complementary entry should be two complementary colors and a 'broad neutral' color
    'complementary': [
    ],

    # 4 similar or adjacent colors
    'analogous': [
    ],

    #A Triadic color scheme uses three colors that are evenly spaced 120 degrees apart on the color wheel. This creates a balanced, vibrant, and high-contrast palette while maintaining harmony.
    'triadic': [
    ],

    # A Split Complementary color scheme consists of a base color and the two colors adjacent to its direct complement on the color wheel. This provides strong contrast like a complementary scheme but with less tension and more harmony.
    'split_complementary': [
    ],

    # A Tetradic color scheme uses two complementary color pairs (four colors total), forming a rectangle on the color wheel. This creates a vibrant, diverse palette but requires balance to avoid clashing
    'tetradic': [
    ],

    # A Rectangular Tetradic color scheme is a variation of Tetradic, where the four colors are spaced unevenly around the color wheel, forming a rectangle. It typically includes one dominant color and three supporting colors, offering rich contrast and versatility while requiring careful balance.
    'rectangular_tetradic': [
    ]
}
