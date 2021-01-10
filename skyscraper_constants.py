# skyscraper/skyscraper_constants.py

from pathlib import Path

from mylogger import get_timelog

# just use the dir the code is in
BASE_PATH = Path('.').absolute()
DATA_DIR = BASE_PATH / 'data/tv_guide/'

if not DATA_DIR.exists():
    print('making a directory at')
    DATA_DIR.mkdir(parents=True)
# LOG = get_timelog(BASE_PATH / 'logs/skyscraper.log.txt')


CHANNELS_JSON = [
    {
        "id": 58,
        "name": "Animal Planet"
    },
    {
        "id": 59,
        "name": "Animal Planet +1"
    },
    {
        "id": 63,
        "name": "Sky Sports Racing"
    },
    {
        "id": 66,
        "name": "BBC News Channel"
    },
    {
        "id": 67,
        "name": "BBC Parliament"
    },
    {
        "id": 72,
        "name": "BBC One East Midlands"
    },
    {
        "id": 73,
        "name": "BBC One East"
    },
    {
        "id": 74,
        "name": "BBC One London"
    },
    {
        "id": 75,
        "name": "BBC One West Midlands"
    },
    {
        "id": 76,
        "name": "BBC One North East & Cumbria"
    },
    {
        "id": 77,
        "name": "BBC One North West"
    },
    {
        "id": 78,
        "name": "BBC One Yorkshire"
    },
    {
        "id": 80,
        "name": "BBC One Northern Ireland"
    },
    {
        "id": 82,
        "name": "BBC One Scotland"
    },
    {
        "id": 83,
        "name": "BBC One South East"
    },
    {
        "id": 84,
        "name": "BBC One South West"
    },
    {
        "id": 85,
        "name": "BBC One South"
    },
    {
        "id": 87,
        "name": "BBC One Wales"
    },
    {
        "id": 88,
        "name": "BBC One West"
    },
    {
        "id": 89,
        "name": "BBC Two England"
    },
    {
        "id": 99,
        "name": "BBC Two Northern Ireland"
    },
    {
        "id": 106,
        "name": "BBC Two Wales"
    },
    {
        "id": 109,
        "name": "BBC Four"
    },
    {
        "id": 112,
        "name": "Bloomberg"
    },
    {
        "id": 113,
        "name": "Boomerang"
    },
    {
        "id": 116,
        "name": "Cartoon Network"
    },
    {
        "id": 118,
        "name": "CBBC"
    },
    {
        "id": 119,
        "name": "CBeebies"
    },
    {
        "id": 120,
        "name": "Challenge"
    },
    {
        "id": 121,
        "name": "Channel 4"
    },
    {
        "id": 123,
        "name": "Trace Xmas"
    },
    {
        "id": 126,
        "name": "CNN"
    },
    {
        "id": 127,
        "name": "Discovery Channel"
    },
    {
        "id": 129,
        "name": "Discovery History"
    },
    {
        "id": 134,
        "name": "Discovery Science"
    },
    {
        "id": 138,
        "name": "E!"
    },
    {
        "id": 139,
        "name": "E4"
    },
    {
        "id": 140,
        "name": "EuroNews"
    },
    {
        "id": 142,
        "name": "Eurosport 1"
    },
    {
        "id": 145,
        "name": "Film4"
    },
    {
        "id": 146,
        "name": "Film4 +1"
    },
    {
        "id": 148,
        "name": "Channel 5"
    },
    {
        "id": 154,
        "name": "FOX"
    },
    {
        "id": 157,
        "name": "Universal TV"
    },
    {
        "id": 160,
        "name": "Sky History"
    },
    {
        "id": 161,
        "name": "Sky History +1"
    },
    {
        "id": 164,
        "name": "STV North"
    },
    {
        "id": 165,
        "name": "ITV Anglia"
    },
    {
        "id": 167,
        "name": "STV North+1"
    },
    {
        "id": 168,
        "name": "ITV Central"
    },
    {
        "id": 169,
        "name": "ITV Westcountry"
    },
    {
        "id": 170,
        "name": "ITV Channel Television"
    },
    {
        "id": 171,
        "name": "ITV Granada"
    },
    {
        "id": 172,
        "name": "ITV London"
    },
    {
        "id": 173,
        "name": "ITV Meridian"
    },
    {
        "id": 174,
        "name": "ITV Tyne Tees"
    },
    {
        "id": 175,
        "name": "ITV Wales"
    },
    {
        "id": 176,
        "name": "ITV West"
    },
    {
        "id": 177,
        "name": "ITV Yorkshire"
    },
    {
        "id": 178,
        "name": "STV Central"
    },
    {
        "id": 179,
        "name": "UTV"
    },
    {
        "id": 180,
        "name": "ITV2"
    },
    {
        "id": 181,
        "name": "Kerrang! TV"
    },
    {
        "id": 182,
        "name": "Kiss TV"
    },
    {
        "id": 183,
        "name": "Sky Witness"
    },
    {
        "id": 184,
        "name": "Sky Witness +1"
    },
    {
        "id": 185,
        "name": "Magic"
    },
    {
        "id": 187,
        "name": "MTV"
    },
    {
        "id": 188,
        "name": "MTV Base"
    },
    {
        "id": 189,
        "name": "Club MTV"
    },
    {
        "id": 190,
        "name": "MTV Hits"
    },
    {
        "id": 191,
        "name": "MTV Rocks"
    },
    {
        "id": 204,
        "name": "MUTV"
    },
    {
        "id": 205,
        "name": "National Geographic Channel"
    },
    {
        "id": 209,
        "name": "Nickelodeon"
    },
    {
        "id": 211,
        "name": "Nick Jr."
    },
    {
        "id": 212,
        "name": "Nicktoons"
    },
    {
        "id": 214,
        "name": "Comedy Central"
    },
    {
        "id": 215,
        "name": "Comedy Central Extra"
    },
    {
        "id": 223,
        "name": "QVC"
    },
    {
        "id": 234,
        "name": "S4C"
    },
    {
        "id": 238,
        "name": "Syfy"
    },
    {
        "id": 247,
        "name": "Sky Cinema Thriller HD"
    },
    {
        "id": 248,
        "name": "Sky Cinema Premiere"
    },
    {
        "id": 249,
        "name": "Sky Cinema Premiere +1"
    },
    {
        "id": 250,
        "name": "Sky Cinema Comedy"
    },
    {
        "id": 251,
        "name": "Sky Cinema Action"
    },
    {
        "id": 252,
        "name": "Sky Cinema Family"
    },
    {
        "id": 253,
        "name": "Sky Cinema Christmas"
    },
    {
        "id": 254,
        "name": "Sky Cinema Sci-fi/Horror HD"
    },
    {
        "id": 257,
        "name": "Sky News"
    },
    {
        "id": 258,
        "name": "Sky One"
    },
    {
        "id": 259,
        "name": "Sky Replay"
    },
    {
        "id": 267,
        "name": "Box Hits"
    },
    {
        "id": 279,
        "name": "BoXmas"
    },
    {
        "id": 280,
        "name": "Together TV"
    },
    {
        "id": 281,
        "name": "Disney Channel"
    },
    {
        "id": 282,
        "name": "Disney Channel +1"
    },
    {
        "id": 286,
        "name": "MTV Pride"
    },
    {
        "id": 289,
        "name": "Travel Channel "
    },
    {
        "id": 315,
        "name": "Good Food"
    },
    {
        "id": 320,
        "name": "Yesterday"
    },
    {
        "id": 322,
        "name": "HGTV"
    },
    {
        "id": 324,
        "name": "VH1"
    },
    {
        "id": 325,
        "name": "MTV XMAS"
    },
    {
        "id": 342,
        "name": "RT\u00c9 One"
    },
    {
        "id": 344,
        "name": "Sony SAB"
    },
    {
        "id": 346,
        "name": "Star Plus"
    },
    {
        "id": 349,
        "name": "TG4"
    },
    {
        "id": 352,
        "name": "Virgin Media One"
    },
    {
        "id": 355,
        "name": "Eden +1"
    },
    {
        "id": 356,
        "name": "Good Food +1"
    },
    {
        "id": 358,
        "name": "HGTV +1"
    },
    {
        "id": 359,
        "name": "Zee TV"
    },
    {
        "id": 360,
        "name": "ITV3"
    },
    {
        "id": 361,
        "name": "More4"
    },
    {
        "id": 363,
        "name": "RT\u00c92"
    },
    {
        "id": 367,
        "name": "ITV4"
    },
    {
        "id": 369,
        "name": "Pick"
    },
    {
        "id": 371,
        "name": "E4 +1"
    },
    {
        "id": 374,
        "name": "5STAR"
    },
    {
        "id": 375,
        "name": "5USA"
    },
    {
        "id": 376,
        "name": "ITV2+1"
    },
    {
        "id": 380,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 381,
        "name": "Discovery Home & Health"
    },
    {
        "id": 382,
        "name": "CITV"
    },
    {
        "id": 384,
        "name": "Sky Arts"
    },
    {
        "id": 385,
        "name": "CBS Reality"
    },
    {
        "id": 386,
        "name": "Discovery Turbo"
    },
    {
        "id": 387,
        "name": "BBC Two HD"
    },
    {
        "id": 389,
        "name": "Boomerang +1"
    },
    {
        "id": 391,
        "name": "Cartoonito"
    },
    {
        "id": 392,
        "name": "Challenge +1"
    },
    {
        "id": 393,
        "name": "Chelsea TV - off air Monday 1st July"
    },
    {
        "id": 394,
        "name": "Crime + Investigation"
    },
    {
        "id": 395,
        "name": "Discovery Channel HD"
    },
    {
        "id": 396,
        "name": "Discovery Home & Health +1"
    },
    {
        "id": 397,
        "name": "Discovery Shed"
    },
    {
        "id": 400,
        "name": "Eurosport 2"
    },
    {
        "id": 402,
        "name": "FOX +1"
    },
    {
        "id": 403,
        "name": "Sky Crime"
    },
    {
        "id": 407,
        "name": "National Geographic WILD"
    },
    {
        "id": 408,
        "name": "National Geographic Channel HD"
    },
    {
        "id": 409,
        "name": "Comedy Central +1"
    },
    {
        "id": 411,
        "name": "Syfy +1"
    },
    {
        "id": 422,
        "name": "Really"
    },
    {
        "id": 423,
        "name": "Yesterday +1"
    },
    {
        "id": 424,
        "name": "CBS Reality +1"
    },
    {
        "id": 425,
        "name": "Horror Channel"
    },
    {
        "id": 426,
        "name": "eir Sport 2"
    },
    {
        "id": 428,
        "name": "Channel 4 +1"
    },
    {
        "id": 429,
        "name": "More4 +1"
    },
    {
        "id": 432,
        "name": "Dave"
    },
    {
        "id": 434,
        "name": "Ideal World Freeview"
    },
    {
        "id": 435,
        "name": "Star Gold"
    },
    {
        "id": 444,
        "name": "Al Jazeera English"
    },
    {
        "id": 446,
        "name": "Racing TV"
    },
    {
        "id": 447,
        "name": "TCM Movies +1"
    },
    {
        "id": 454,
        "name": "DMAX"
    },
    {
        "id": 455,
        "name": "Dave ja vu"
    },
    {
        "id": 457,
        "name": "Cartoon Network +1"
    },
    {
        "id": 468,
        "name": "Pop"
    },
    {
        "id": 474,
        "name": "ITV3+1"
    },
    {
        "id": 476,
        "name": "Channel 4 HD"
    },
    {
        "id": 477,
        "name": "Tiny Pop"
    },
    {
        "id": 478,
        "name": "Sky One HD"
    },
    {
        "id": 483,
        "name": "MTV +1"
    },
    {
        "id": 484,
        "name": "Sky Arts HD"
    },
    {
        "id": 488,
        "name": "FOX HD"
    },
    {
        "id": 489,
        "name": "Sky Cinema Premiere HD"
    },
    {
        "id": 493,
        "name": "CBS Drama"
    },
    {
        "id": 498,
        "name": "CBS Justice"
    },
    {
        "id": 499,
        "name": "Sony Movies Christmas+1"
    },
    {
        "id": 500,
        "name": "Sony Movies Action"
    },
    {
        "id": 502,
        "name": "Eurosport 1 HD"
    },
    {
        "id": 504,
        "name": "Horror Channel +1"
    },
    {
        "id": 505,
        "name": "Sky History 2"
    },
    {
        "id": 506,
        "name": "4Music"
    },
    {
        "id": 508,
        "name": "BBC Alba"
    },
    {
        "id": 511,
        "name": "W"
    },
    {
        "id": 513,
        "name": "Sky Cinema Christmas HD"
    },
    {
        "id": 514,
        "name": "Sky Cinema Action HD"
    },
    {
        "id": 515,
        "name": "W +1"
    },
    {
        "id": 517,
        "name": "GOLD"
    },
    {
        "id": 519,
        "name": "GOLD +1"
    },
    {
        "id": 520,
        "name": "Alibi"
    },
    {
        "id": 521,
        "name": "Alibi +1"
    },
    {
        "id": 522,
        "name": "Sky Cinema Comedy HD"
    },
    {
        "id": 523,
        "name": "Sky Cinema Family HD"
    },
    {
        "id": 524,
        "name": "Sky Cinema Sci-fi/Horror"
    },
    {
        "id": 527,
        "name": "Sky History HD"
    },
    {
        "id": 530,
        "name": "ITV4+1"
    },
    {
        "id": 533,
        "name": "Virgin Media Two"
    },
    {
        "id": 535,
        "name": "Investigation Discovery"
    },
    {
        "id": 540,
        "name": "Eden"
    },
    {
        "id": 545,
        "name": "Syfy HD"
    },
    {
        "id": 547,
        "name": "Sky Crime+1"
    },
    {
        "id": 556,
        "name": "Crime + Investigation HD"
    },
    {
        "id": 557,
        "name": "National Geographic WILD HD"
    },
    {
        "id": 558,
        "name": "Propeller TV"
    },
    {
        "id": 559,
        "name": "Quest"
    },
    {
        "id": 565,
        "name": "Travel Channel +1"
    },
    {
        "id": 566,
        "name": "Phoenix CNE Channel"
    },
    {
        "id": 571,
        "name": "5SELECT"
    },
    {
        "id": 572,
        "name": "5USA +1"
    },
    {
        "id": 575,
        "name": "Crime + Investigation +1"
    },
    {
        "id": 578,
        "name": "BT Sport//ESPN"
    },
    {
        "id": 579,
        "name": "BT Sport//ESPN HD"
    },
    {
        "id": 586,
        "name": "Create and Craft"
    },
    {
        "id": 588,
        "name": "Disney XD"
    },
    {
        "id": 589,
        "name": "Disney XD +1"
    },
    {
        "id": 590,
        "name": "CNBC UK"
    },
    {
        "id": 592,
        "name": "Sky Witness HD"
    },
    {
        "id": 593,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 594,
        "name": "Quest +1"
    },
    {
        "id": 595,
        "name": "Food Network +1"
    },
    {
        "id": 596,
        "name": "Food Network"
    },
    {
        "id": 599,
        "name": "Universal TV +1"
    },
    {
        "id": 601,
        "name": "Christmas 24"
    },
    {
        "id": 602,
        "name": "Pop Max"
    },
    {
        "id": 604,
        "name": "Sky Cinema Musicals"
    },
    {
        "id": 605,
        "name": "Christmas 24+"
    },
    {
        "id": 609,
        "name": "E4 HD"
    },
    {
        "id": 610,
        "name": "NHK World"
    },
    {
        "id": 611,
        "name": "Nick Jr Paw Patrol"
    },
    {
        "id": 614,
        "name": "Sky Cinema Thriller"
    },
    {
        "id": 616,
        "name": "DMAX +1"
    },
    {
        "id": 617,
        "name": "Comedy Central Extra +1"
    },
    {
        "id": 618,
        "name": "Discovery History +1"
    },
    {
        "id": 619,
        "name": "Tiny Pop +1"
    },
    {
        "id": 621,
        "name": "Sony Movies Action +1"
    },
    {
        "id": 624,
        "name": "Horse & Country TV"
    },
    {
        "id": 625,
        "name": "Nickelodeon +1"
    },
    {
        "id": 633,
        "name": "Sony Channel"
    },
    {
        "id": 634,
        "name": "Discovery Science +1"
    },
    {
        "id": 636,
        "name": "BBC Red Button 1"
    },
    {
        "id": 637,
        "name": "Sky Cinema Hits"
    },
    {
        "id": 638,
        "name": "Sky Cinema Hits HD"
    },
    {
        "id": 642,
        "name": "ITV HD London"
    },
    {
        "id": 649,
        "name": "Sky News HD"
    },
    {
        "id": 654,
        "name": "ITV HD STV"
    },
    {
        "id": 655,
        "name": "Universal TV HD"
    },
    {
        "id": 657,
        "name": "Channel 5 HD"
    },
    {
        "id": 660,
        "name": "Film4 HD"
    },
    {
        "id": 661,
        "name": "TCM Movies"
    },
    {
        "id": 664,
        "name": "Comedy Central HD"
    },
    {
        "id": 667,
        "name": "Pick +1"
    },
    {
        "id": 669,
        "name": "Good Food HD"
    },
    {
        "id": 670,
        "name": "Eden HD"
    },
    {
        "id": 671,
        "name": "ITV2HD"
    },
    {
        "id": 672,
        "name": "ITV HD UTV"
    },
    {
        "id": 681,
        "name": "Nickelodeon HD"
    },
    {
        "id": 682,
        "name": "Disney XD HD"
    },
    {
        "id": 683,
        "name": "BBC One HD"
    },
    {
        "id": 690,
        "name": "ITV3HD"
    },
    {
        "id": 691,
        "name": "ITV4HD"
    },
    {
        "id": 695,
        "name": "ITV Yorkshire+1"
    },
    {
        "id": 696,
        "name": "ITV Granada+1"
    },
    {
        "id": 697,
        "name": "ITV London+1"
    },
    {
        "id": 698,
        "name": "UTV +1"
    },
    {
        "id": 699,
        "name": "ITV West+1"
    },
    {
        "id": 700,
        "name": "ITV Central+1"
    },
    {
        "id": 701,
        "name": "STV Central+1"
    },
    {
        "id": 702,
        "name": "MTV Music"
    },
    {
        "id": 703,
        "name": "Sky Atlantic HD"
    },
    {
        "id": 704,
        "name": "Sky Atlantic"
    },
    {
        "id": 706,
        "name": "LFC TV"
    },
    {
        "id": 707,
        "name": "RT"
    },
    {
        "id": 710,
        "name": "Sony Entertainment TV Asia"
    },
    {
        "id": 711,
        "name": "Sony Crime Channel +1"
    },
    {
        "id": 712,
        "name": "Sony Crime Channel"
    },
    {
        "id": 713,
        "name": "Disney Junior"
    },
    {
        "id": 714,
        "name": "Disney Junior +"
    },
    {
        "id": 715,
        "name": "Premier Sports 1 HD"
    },
    {
        "id": 716,
        "name": "RT\u00c9 Jr"
    },
    {
        "id": 717,
        "name": "RTE News"
    },
    {
        "id": 718,
        "name": "RT\u00c92 HD"
    },
    {
        "id": 719,
        "name": "RT\u00c9 One +1"
    },
    {
        "id": 721,
        "name": "ITV HD Meridian"
    },
    {
        "id": 722,
        "name": "ITV HD Granada"
    },
    {
        "id": 723,
        "name": "ITV HD Central"
    },
    {
        "id": 724,
        "name": "Cartoon Network HD"
    },
    {
        "id": 725,
        "name": "Disney Channel HD"
    },
    {
        "id": 726,
        "name": "W HD"
    },
    {
        "id": 727,
        "name": "Dave HD"
    },
    {
        "id": 729,
        "name": "Channel 5 +1"
    },
    {
        "id": 731,
        "name": "BBC One Oxfordshire"
    },
    {
        "id": 732,
        "name": "BBC One Yorkshire & Lincolnshire"
    },
    {
        "id": 733,
        "name": "BBC One Cambridgeshire"
    },
    {
        "id": 734,
        "name": "BBC One Channel Islands"
    },
    {
        "id": 735,
        "name": "Animal Planet HD"
    },
    {
        "id": 739,
        "name": "MTV HD"
    },
    {
        "id": 742,
        "name": "Sony Movies"
    },
    {
        "id": 743,
        "name": "Sony Movies +1"
    },
    {
        "id": 751,
        "name": "PBS America"
    },
    {
        "id": 752,
        "name": "4seven"
    },
    {
        "id": 755,
        "name": "Alibi HD"
    },
    {
        "id": 756,
        "name": "Box Upfront"
    },
    {
        "id": 757,
        "name": "Ideal World"
    },
    {
        "id": 758,
        "name": "Eurosport 2 HD"
    },
    {
        "id": 812,
        "name": "ITV Border England"
    },
    {
        "id": 820,
        "name": "TCM Movies HD"
    },
    {
        "id": 821,
        "name": "Star Plus HD"
    },
    {
        "id": 824,
        "name": "Sky Atlantic +1"
    },
    {
        "id": 826,
        "name": "Nick Jr. +1"
    },
    {
        "id": 827,
        "name": "ITV Westcountry+1"
    },
    {
        "id": 828,
        "name": "ITV Anglia+1"
    },
    {
        "id": 829,
        "name": "ITV Tyne Tees+1"
    },
    {
        "id": 830,
        "name": "ITV Wales+1"
    },
    {
        "id": 831,
        "name": "E! HD"
    },
    {
        "id": 832,
        "name": "ITV Meridian+1"
    },
    {
        "id": 833,
        "name": "BBC One Northern Ireland HD"
    },
    {
        "id": 835,
        "name": "TG4 HD"
    },
    {
        "id": 836,
        "name": "Baby TV"
    },
    {
        "id": 837,
        "name": "Sky One +1"
    },
    {
        "id": 844,
        "name": "National Geographic Channel +1"
    },
    {
        "id": 846,
        "name": "Discovery Channel +1"
    },
    {
        "id": 847,
        "name": "Sky Cinema Musicals HD"
    },
    {
        "id": 850,
        "name": "Sky Cinema Disney"
    },
    {
        "id": 851,
        "name": "Sky Cinema Disney HD"
    },
    {
        "id": 852,
        "name": "Trace Latina"
    },
    {
        "id": 853,
        "name": "RT HD"
    },
    {
        "id": 855,
        "name": "BBC One Scotland HD"
    },
    {
        "id": 856,
        "name": "BBC One Wales HD"
    },
    {
        "id": 859,
        "name": "More4 HD"
    },
    {
        "id": 864,
        "name": "TLC+1"
    },
    {
        "id": 865,
        "name": "TLC"
    },
    {
        "id": 866,
        "name": "TLC HD"
    },
    {
        "id": 868,
        "name": "Colors Rishtey"
    },
    {
        "id": 869,
        "name": "Disney Junior HD"
    },
    {
        "id": 870,
        "name": "Investigation Discovery +1"
    },
    {
        "id": 871,
        "name": "Drama"
    },
    {
        "id": 874,
        "name": "Star Bharat"
    },
    {
        "id": 875,
        "name": "BT Sport 1"
    },
    {
        "id": 876,
        "name": "BT Sport 1HD"
    },
    {
        "id": 877,
        "name": "BT Sport 2"
    },
    {
        "id": 880,
        "name": "BT Sport 2 HD"
    },
    {
        "id": 881,
        "name": "Colors"
    },
    {
        "id": 886,
        "name": "Zing"
    },
    {
        "id": 887,
        "name": "Lifetime"
    },
    {
        "id": 888,
        "name": "Lifetime HD"
    },
    {
        "id": 893,
        "name": "BBC Four HD"
    },
    {
        "id": 894,
        "name": "BBC News Channel HD"
    },
    {
        "id": 895,
        "name": "CBBC HD"
    },
    {
        "id": 896,
        "name": "CBeebies HD"
    },
    {
        "id": 899,
        "name": "Al Jazeera English HD"
    },
    {
        "id": 900,
        "name": "RT\u00c9 One HD"
    },
    {
        "id": 901,
        "name": "5STAR +1"
    },
    {
        "id": 902,
        "name": "ITV3+1 Freeview"
    },
    {
        "id": 904,
        "name": "London Live"
    },
    {
        "id": 906,
        "name": "Pop +1"
    },
    {
        "id": 913,
        "name": "Forces TV"
    },
    {
        "id": 916,
        "name": "Channel 4 +1 HD"
    },
    {
        "id": 917,
        "name": "4seven HD"
    },
    {
        "id": 920,
        "name": "MUTV HD"
    },
    {
        "id": 923,
        "name": "True Crime"
    },
    {
        "id": 926,
        "name": "ITVBe"
    },
    {
        "id": 927,
        "name": "True Crime +1"
    },
    {
        "id": 957,
        "name": "ITVBe+1"
    },
    {
        "id": 958,
        "name": "ITVBe HD"
    },
    {
        "id": 962,
        "name": "Virgin Media Three"
    },
    {
        "id": 964,
        "name": "5Spike"
    },
    {
        "id": 965,
        "name": "&TV"
    },
    {
        "id": 967,
        "name": "BT Sport 3"
    },
    {
        "id": 968,
        "name": "BT Sport 3 HD"
    },
    {
        "id": 973,
        "name": "ITV Border Scotland"
    },
    {
        "id": 979,
        "name": "Talking Pictures TV"
    },
    {
        "id": 984,
        "name": "AMC"
    },
    {
        "id": 991,
        "name": "YourTV"
    },
    {
        "id": 993,
        "name": "Sony Movies Christmas"
    },
    {
        "id": 996,
        "name": "Notts TV"
    },
    {
        "id": 1004,
        "name": "TVC News"
    },
    {
        "id": 1011,
        "name": "Sony MAX"
    },
    {
        "id": 1012,
        "name": "Vice"
    },
    {
        "id": 1013,
        "name": "Blaze"
    },
    {
        "id": 1014,
        "name": "Quest Red"
    },
    {
        "id": 1032,
        "name": "BoxNation"
    },
    {
        "id": 1036,
        "name": "BoxNation Live HD"
    },
    {
        "id": 1094,
        "name": "Sky Sports NFL"
    },
    {
        "id": 1095,
        "name": "Sky Sports NFL HD"
    },
    {
        "id": 1096,
        "name": "Sky Sports Darts"
    },
    {
        "id": 1097,
        "name": "Sky Sports Darts HD"
    },
    {
        "id": 1098,
        "name": "Sky Sports Cricket"
    },
    {
        "id": 1099,
        "name": "Sky Sports Cricket HD"
    },
    {
        "id": 1100,
        "name": "Sky Sports F1"
    },
    {
        "id": 1101,
        "name": "Sky Sports F1 HD"
    },
    {
        "id": 1102,
        "name": "Sky Sports Football"
    },
    {
        "id": 1103,
        "name": "Sky Sports Football HD"
    },
    {
        "id": 1104,
        "name": "Sky Sports Main Event"
    },
    {
        "id": 1105,
        "name": "Sky Sports Main Event HD"
    },
    {
        "id": 1106,
        "name": "Sky Sports Mix"
    },
    {
        "id": 1107,
        "name": "Sky Sports Mix HD"
    },
    {
        "id": 1108,
        "name": "Sky Sports News"
    },
    {
        "id": 1109,
        "name": "Sky Sports News HD"
    },
    {
        "id": 1110,
        "name": "Sky Sports Premier League"
    },
    {
        "id": 1111,
        "name": "Sky Sports Premier League HD"
    },
    {
        "id": 1112,
        "name": "Sky Sports Golf"
    },
    {
        "id": 1113,
        "name": "Sky Sports Golf HD"
    },
    {
        "id": 1114,
        "name": "Sony MAX 2"
    },
    {
        "id": 1115,
        "name": "B4U Music"
    },
    {
        "id": 1116,
        "name": "Living Foodz"
    },
    {
        "id": 1117,
        "name": "Pop Max +1"
    },
    {
        "id": 1118,
        "name": "Quest +1 Freeview"
    },
    {
        "id": 1120,
        "name": "102.2 Smooth Radio"
    },
    {
        "id": 1121,
        "name": "5Spike +1"
    },
    {
        "id": 1122,
        "name": "95.8 Capital FM"
    },
    {
        "id": 1123,
        "name": "96-106 Capital FM"
    },
    {
        "id": 1124,
        "name": "B4U Plus"
    },
    {
        "id": 1125,
        "name": "Absolute Radio"
    },
    {
        "id": 1126,
        "name": "AMC HD"
    },
    {
        "id": 1127,
        "name": "Arirang HD"
    },
    {
        "id": 1128,
        "name": "BBC Asian Network"
    },
    {
        "id": 1129,
        "name": "BBC Radio 1"
    },
    {
        "id": 1130,
        "name": "BBC Radio 1Xtra"
    },
    {
        "id": 1131,
        "name": "BBC Radio 2"
    },
    {
        "id": 1132,
        "name": "BBC Radio 3"
    },
    {
        "id": 1133,
        "name": "BBC Radio 4 Extra"
    },
    {
        "id": 1134,
        "name": "BBC Radio 4 FM"
    },
    {
        "id": 1135,
        "name": "BBC Radio 4 LW"
    },
    {
        "id": 1136,
        "name": "BBC Radio 5 live"
    },
    {
        "id": 1137,
        "name": "BBC Radio 5 live sports extra"
    },
    {
        "id": 1138,
        "name": "BBC Radio 6 Music"
    },
    {
        "id": 1139,
        "name": "BBC Radio Cymru"
    },
    {
        "id": 1140,
        "name": "BBC Radio Cymru 2"
    },
    {
        "id": 1141,
        "name": "BBC Radio Foyle"
    },
    {
        "id": 1142,
        "name": "BBC Radio London"
    },
    {
        "id": 1143,
        "name": "BBC Radio Nan G\u00e0idheal"
    },
    {
        "id": 1144,
        "name": "BBC Radio Scotland FM"
    },
    {
        "id": 1145,
        "name": "BBC Radio Ulster"
    },
    {
        "id": 1146,
        "name": "BBC Radio Wales"
    },
    {
        "id": 1147,
        "name": "BBC Scotland"
    },
    {
        "id": 1148,
        "name": "BBC Scotland HD"
    },
    {
        "id": 1149,
        "name": "BBC Two Northern Ireland HD"
    },
    {
        "id": 1150,
        "name": "BBC Two Wales HD"
    },
    {
        "id": 1151,
        "name": "BBC WM DAB"
    },
    {
        "id": 1152,
        "name": "BBC WM FM"
    },
    {
        "id": 1153,
        "name": "BBC World Service"
    },
    {
        "id": 1154,
        "name": "Birmingham TV"
    },
    {
        "id": 1155,
        "name": "Blaze Freeview +1"
    },
    {
        "id": 1156,
        "name": "Bloomberg HD"
    },
    {
        "id": 1157,
        "name": "Bristol TV"
    },
    {
        "id": 1158,
        "name": "BT Sport Ultimate"
    },
    {
        "id": 1159,
        "name": "BT Sport X1"
    },
    {
        "id": 1160,
        "name": "BT Sport X1 HD"
    },
    {
        "id": 1161,
        "name": "BT Sport X2"
    },
    {
        "id": 1162,
        "name": "BT Sport X2 HD"
    },
    {
        "id": 1163,
        "name": "BT Sport X3"
    },
    {
        "id": 1164,
        "name": "BT Sport X3 HD"
    },
    {
        "id": 1165,
        "name": "BT Sport X4"
    },
    {
        "id": 1166,
        "name": "BT Sport X4 HD"
    },
    {
        "id": 1167,
        "name": "BT Sport X5"
    },
    {
        "id": 1168,
        "name": "BT Sport X5 HD"
    },
    {
        "id": 1169,
        "name": "BT Sport X6"
    },
    {
        "id": 1170,
        "name": "BT Sport X6 HD"
    },
    {
        "id": 1171,
        "name": "Cardiff TV"
    },
    {
        "id": 1172,
        "name": "Channel 5 +1 Freeview"
    },
    {
        "id": 1173,
        "name": "Channels 24"
    },
    {
        "id": 1174,
        "name": "Classic FM"
    },
    {
        "id": 1175,
        "name": "CNBC HD"
    },
    {
        "id": 1176,
        "name": "CNN HD"
    },
    {
        "id": 1177,
        "name": "Colors Cineplex"
    },
    {
        "id": 1178,
        "name": "Colors HD"
    },
    {
        "id": 1179,
        "name": "Discovery Turbo +1"
    },
    {
        "id": 1180,
        "name": "eir Sport 1 HD"
    },
    {
        "id": 1181,
        "name": "eir Sport 2 HD"
    },
    {
        "id": 1182,
        "name": "Fascination TV"
    },
    {
        "id": 1183,
        "name": "France 24 HD"
    },
    {
        "id": 1184,
        "name": "FreeSports"
    },
    {
        "id": 1185,
        "name": "FreeSports HD"
    },
    {
        "id": 1186,
        "name": "Frontrunner"
    },
    {
        "id": 1187,
        "name": "GEO Kahani"
    },
    {
        "id": 1188,
        "name": "GEO News"
    },
    {
        "id": 1189,
        "name": "GEO TV"
    },
    {
        "id": 1190,
        "name": "GINX eSports TV"
    },
    {
        "id": 1191,
        "name": "GOLD HD"
    },
    {
        "id": 1192,
        "name": "Heart London"
    },
    {
        "id": 1193,
        "name": "Heat"
    },
    {
        "id": 1194,
        "name": "Sky History 2 HD"
    },
    {
        "id": 1195,
        "name": "Hits Radio"
    },
    {
        "id": 1196,
        "name": "Iran International"
    },
    {
        "id": 1197,
        "name": "ITVBe Freeview +1"
    },
    {
        "id": 1198,
        "name": "ITV HD Anglia"
    },
    {
        "id": 1199,
        "name": "ITV HD Border"
    },
    {
        "id": 1200,
        "name": "ITV HD Tyne Tees"
    },
    {
        "id": 1201,
        "name": "ITV HD Wales"
    },
    {
        "id": 1202,
        "name": "ITV HD West"
    },
    {
        "id": 1203,
        "name": "ITV HD Westcountry"
    },
    {
        "id": 1204,
        "name": "ITV HD Yorkshire"
    },
    {
        "id": 1205,
        "name": "Jazz FM"
    },
    {
        "id": 1206,
        "name": "Spotlight TV"
    },
    {
        "id": 1207,
        "name": "Kerrang!"
    },
    {
        "id": 1208,
        "name": "Kiss 100"
    },
    {
        "id": 1209,
        "name": "LBC"
    },
    {
        "id": 1210,
        "name": "Leeds TV"
    },
    {
        "id": 1211,
        "name": "LFC TV HD"
    },
    {
        "id": 1212,
        "name": "Liverpool TV"
    },
    {
        "id": 1213,
        "name": "Magic 105.4"
    },
    {
        "id": 1214,
        "name": "MTV Beats"
    },
    {
        "id": 1215,
        "name": "MTV Ireland"
    },
    {
        "id": 1216,
        "name": "MTV Music +1"
    },
    {
        "id": 1217,
        "name": "NDTV 24x7"
    },
    {
        "id": 1218,
        "name": "New Vision"
    },
    {
        "id": 1219,
        "name": "News18"
    },
    {
        "id": 1220,
        "name": "Newstalk 106-108 FM"
    },
    {
        "id": 1221,
        "name": "Nick Jr HD"
    },
    {
        "id": 1222,
        "name": "NOW 80s"
    },
    {
        "id": 1223,
        "name": "NOW 90s"
    },
    {
        "id": 1224,
        "name": "Oireachtas TV"
    },
    {
        "id": 1225,
        "name": "Paramount Network"
    },
    {
        "id": 1226,
        "name": "Planet Rock"
    },
    {
        "id": 1227,
        "name": "Pop Max Freeview"
    },
    {
        "id": 1228,
        "name": "Premier Christian Radio"
    },
    {
        "id": 1229,
        "name": "Premier Sports 2"
    },
    {
        "id": 1230,
        "name": "Quest HD"
    },
    {
        "id": 1231,
        "name": "Quest Red +1"
    },
    {
        "id": 1232,
        "name": "Racing TV HD"
    },
    {
        "id": 1233,
        "name": "Radio X"
    },
    {
        "id": 1234,
        "name": "RTE 2FM"
    },
    {
        "id": 1235,
        "name": "RT\u00c9 lyric fm"
    },
    {
        "id": 1236,
        "name": "RT\u00c9 Radio 1 FM"
    },
    {
        "id": 1237,
        "name": "RT\u00c9 Raidi\u00f3 na Gaeltachta"
    },
    {
        "id": 1238,
        "name": "S4C HD"
    },
    {
        "id": 1239,
        "name": "Sanskar"
    },
    {
        "id": 1240,
        "name": "Sky Sports Extra"
    },
    {
        "id": 1241,
        "name": "Sky Sports Extra HD"
    },
    {
        "id": 1242,
        "name": "Sky Sports Premier League ROI HD"
    },
    {
        "id": 1243,
        "name": "Smithsonian"
    },
    {
        "id": 1244,
        "name": "Smithsonian HD"
    },
    {
        "id": 1245,
        "name": "Sony Entertainment TV Asia HD"
    },
    {
        "id": 1246,
        "name": "Sony MAX HD"
    },
    {
        "id": 1247,
        "name": "Star Gold HD"
    },
    {
        "id": 1248,
        "name": "talkSPORT"
    },
    {
        "id": 1249,
        "name": "talkSPORT DAB"
    },
    {
        "id": 1250,
        "name": "Tiny Pop"
    },
    {
        "id": 1251,
        "name": "NOW 70s"
    },
    {
        "id": 1252,
        "name": "Travelxp"
    },
    {
        "id": 1253,
        "name": "TRT World"
    },
    {
        "id": 1254,
        "name": "TRT World HD"
    },
    {
        "id": 1255,
        "name": "Tyne & Wear TV"
    },
    {
        "id": 1256,
        "name": "U105"
    },
    {
        "id": 1257,
        "name": "Vice HD"
    },
    {
        "id": 1258,
        "name": "Virgin Media One +1"
    },
    {
        "id": 1259,
        "name": "Virgin Media One HD"
    },
    {
        "id": 1260,
        "name": "Virgin Media Two HD"
    },
    {
        "id": 1261,
        "name": "Virgin Radio"
    },
    {
        "id": 1262,
        "name": "Zee TV HD"
    },
    {
        "id": 1263,
        "name": "ABN TV"
    },
    {
        "id": 1264,
        "name": "AIT International"
    },
    {
        "id": 1265,
        "name": "B4U Movies"
    },
    {
        "id": 1266,
        "name": "BET"
    },
    {
        "id": 1267,
        "name": "Boomerang HD"
    },
    {
        "id": 1268,
        "name": "Chelsea TV HD"
    },
    {
        "id": 1269,
        "name": "Clubland TV"
    },
    {
        "id": 1270,
        "name": "NHK World HD"
    },
    {
        "id": 1271,
        "name": "Showcase"
    },
    {
        "id": 1272,
        "name": "Starz"
    },
    {
        "id": 1273,
        "name": "Trace Vault"
    },
    {
        "id": 1274,
        "name": "Sony Channel +1"
    },
    {
        "id": 1275,
        "name": "Zee Cinema"
    },
    {
        "id": 1276,
        "name": "CGTN"
    },
    {
        "id": 1277,
        "name": "CGTN HD"
    },
    {
        "id": 1278,
        "name": "eir Sport 1"
    },
    {
        "id": 1279,
        "name": "Sky Sports Premier League ROI"
    },
    {
        "id": 1280,
        "name": "Sky Atlantic VIP"
    },
    {
        "id": 1281,
        "name": "Sky Atlantic VIP HD"
    },
    {
        "id": 1282,
        "name": "BT Sport Box Office"
    },
    {
        "id": 1283,
        "name": "Sky Sports Box Office"
    },
    {
        "id": 1284,
        "name": "Sky Sports Box Office HD"
    },
    {
        "id": 1285,
        "name": "ITV Box Office HD"
    },
    {
        "id": 1286,
        "name": "Yanga!"
    },
    {
        "id": 1287,
        "name": "BT Sport Box Office 2"
    },
    {
        "id": 1288,
        "name": "CBS Justice +1"
    },
    {
        "id": 1289,
        "name": "Drama +1"
    },
    {
        "id": 1290,
        "name": "Foodxp"
    },
    {
        "id": 1291,
        "name": "Sky History"
    },
    {
        "id": 1292,
        "name": "Sky History +1"
    },
    {
        "id": 1293,
        "name": "Sky History 2"
    },
    {
        "id": 1294,
        "name": "Sky History 2 HD"
    },
    {
        "id": 1295,
        "name": "La Liga TV HD"
    },
    {
        "id": 1296,
        "name": "MTV Live HD"
    },
    {
        "id": 1297,
        "name": "Paramount Network +1"
    },
    {
        "id": 1298,
        "name": "Paramount Network HD"
    },
    {
        "id": 1299,
        "name": "PBS America +1"
    },
    {
        "id": 1300,
        "name": "Premier Sports 1 HD ROI"
    },
    {
        "id": 1301,
        "name": "Premier Sports 2 HD"
    },
    {
        "id": 1302,
        "name": "Premier Sports 2 HD ROI"
    },
    {
        "id": 1303,
        "name": "Republic Bharat"
    },
    {
        "id": 1304,
        "name": "RTE News"
    },
    {
        "id": 1305,
        "name": "RT\u00c9 One"
    },
    {
        "id": 1306,
        "name": "RT\u00c9 One +1"
    },
    {
        "id": 1307,
        "name": "RT\u00c9 One HD"
    },
    {
        "id": 1308,
        "name": "Sky Cinema Action"
    },
    {
        "id": 1309,
        "name": "Sky Cinema Action HD"
    },
    {
        "id": 1310,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1311,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1312,
        "name": "Sky Cinema Family"
    },
    {
        "id": 1313,
        "name": "Sky Cinema Family HD"
    },
    {
        "id": 1314,
        "name": "Sky Cinema Musicals"
    },
    {
        "id": 1315,
        "name": "Sky Cinema Musicals HD"
    },
    {
        "id": 1316,
        "name": "Sky Cinema Sci-fi/Horror"
    },
    {
        "id": 1317,
        "name": "Sky Cinema Sci-fi/Horror HD"
    },
    {
        "id": 1318,
        "name": "Sky Comedy"
    },
    {
        "id": 1319,
        "name": "Sky Comedy HD"
    },
    {
        "id": 1320,
        "name": "Sky Crime HD"
    },
    {
        "id": 1321,
        "name": "Sky Sports Racing HD"
    },
    {
        "id": 1322,
        "name": "Together TV +1"
    },
    {
        "id": 1323,
        "name": "Virgin Media Sport HD"
    },
    {
        "id": 1324,
        "name": "Zee Cinema HD"
    },
    {
        "id": 1325,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1326,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1327,
        "name": "Sky Cinema Musicals"
    },
    {
        "id": 1328,
        "name": "Sky Cinema Musicals HD"
    },
    {
        "id": 1329,
        "name": "Sky History 2"
    },
    {
        "id": 1330,
        "name": "Sky History 2 HD"
    },
    {
        "id": 1331,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1332,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1333,
        "name": "Sky Cinema Musicals"
    },
    {
        "id": 1334,
        "name": "Sky Cinema Musicals HD"
    },
    {
        "id": 1335,
        "name": "Sky Cinema Action"
    },
    {
        "id": 1336,
        "name": "Sky Cinema Action HD"
    },
    {
        "id": 1337,
        "name": "Sky History"
    },
    {
        "id": 1338,
        "name": "Sky History +1"
    },
    {
        "id": 1339,
        "name": "Sky History 2"
    },
    {
        "id": 1340,
        "name": "Sky History 2 HD"
    },
    {
        "id": 1341,
        "name": "Sky Cinema Musicals"
    },
    {
        "id": 1342,
        "name": "Sky Cinema Musicals HD"
    },
    {
        "id": 1343,
        "name": "Sky Cinema Action"
    },
    {
        "id": 1344,
        "name": "Sky Cinema Action HD"
    },
    {
        "id": 1345,
        "name": "Sky Cinema Action"
    },
    {
        "id": 1346,
        "name": "Sky Cinema Action HD"
    },
    {
        "id": 1347,
        "name": "Sky Cinema Family"
    },
    {
        "id": 1348,
        "name": "Sky Cinema Family HD"
    },
    {
        "id": 1349,
        "name": "Sky Cinema Action"
    },
    {
        "id": 1350,
        "name": "Sky Cinema Action HD"
    },
    {
        "id": 1351,
        "name": "Sky Cinema Family"
    },
    {
        "id": 1352,
        "name": "Sky Cinema Family HD"
    },
    {
        "id": 1353,
        "name": "Sky Cinema Family"
    },
    {
        "id": 1354,
        "name": "Sky Cinema Family HD"
    },
    {
        "id": 1355,
        "name": "RT\u00c9 One HD"
    },
    {
        "id": 1356,
        "name": "CCX TV"
    },
    {
        "id": 1357,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1358,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1359,
        "name": "Yesterday Freeview +1"
    },
    {
        "id": 1360,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1361,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1362,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1363,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1364,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1365,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1366,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1367,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1368,
        "name": "MTV Pride"
    },
    {
        "id": 1369,
        "name": "Sky Documentaries"
    },
    {
        "id": 1370,
        "name": "Sky Documentaries HD"
    },
    {
        "id": 1371,
        "name": "Sky Nature"
    },
    {
        "id": 1372,
        "name": "Sky Nature HD"
    },
    {
        "id": 1373,
        "name": "Sky History 2"
    },
    {
        "id": 1374,
        "name": "Sky History 2 HD"
    },
    {
        "id": 1375,
        "name": "MTV Pride"
    },
    {
        "id": 1376,
        "name": "Sky History 2"
    },
    {
        "id": 1377,
        "name": "Sky History 2 HD"
    },
    {
        "id": 1378,
        "name": "Sky History"
    },
    {
        "id": 1379,
        "name": "Sky History +1"
    },
    {
        "id": 1380,
        "name": "Sky History HD"
    },
    {
        "id": 1381,
        "name": "Sky History 2"
    },
    {
        "id": 1382,
        "name": "Sky History 2 HD"
    },
    {
        "id": 1383,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1384,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1385,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1386,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1387,
        "name": "MTV Pride"
    },
    {
        "id": 1388,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1389,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1390,
        "name": "Pick UK"
    },
    {
        "id": 1391,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1392,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1393,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1394,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1395,
        "name": "BET"
    },
    {
        "id": 1396,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1397,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1398,
        "name": "Sky Cinema Animation HD"
    },
    {
        "id": 1399,
        "name": "Merit"
    },
    {
        "id": 1400,
        "name": "Sky Cinema Animation"
    },
    {
        "id": 1401,
        "name": "Sky Cinema Musicals"
    },
    {
        "id": 1402,
        "name": "Sky Cinema Musicals HD"
    },
    {
        "id": 1403,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1404,
        "name": "Sky Cinema Musicals"
    },
    {
        "id": 1405,
        "name": "Sky Cinema Musicals HD"
    },
    {
        "id": 1406,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1407,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1408,
        "name": "Sky Cinema Musicals"
    },
    {
        "id": 1409,
        "name": "Sky Cinema Musicals HD"
    },
    {
        "id": 1410,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1411,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1412,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1413,
        "name": "Sky Cinema Musicals"
    },
    {
        "id": 1414,
        "name": "Sky Cinema Musicals HD"
    },
    {
        "id": 1415,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1416,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1417,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1418,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1419,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1420,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1421,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1422,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1423,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1424,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1425,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1426,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1427,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1428,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1429,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1430,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1431,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1432,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1433,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1434,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1435,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1436,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1437,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1438,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1439,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1440,
        "name": "eir Sport 2 HD for Sky"
    },
    {
        "id": 1441,
        "name": "eir Sport 2 HD for Sky"
    },
    {
        "id": 1442,
        "name": "eir Sport 2 HD for Sky"
    },
    {
        "id": 1443,
        "name": "Sky Cinema Family"
    },
    {
        "id": 1444,
        "name": "Sky Cinema Family HD"
    },
    {
        "id": 1445,
        "name": "Christmas 24"
    },
    {
        "id": 1446,
        "name": "Christmas 24+"
    },
    {
        "id": 1447,
        "name": "Sky Cinema Family"
    },
    {
        "id": 1448,
        "name": "Sky Cinema Family HD"
    },
    {
        "id": 1449,
        "name": "Nick Jr Paw Patrol"
    },
    {
        "id": 1450,
        "name": "Sky Cinema Sci-fi/Horror"
    },
    {
        "id": 1451,
        "name": "Sky Cinema Sci-fi/Horror HD"
    },
    {
        "id": 1452,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1453,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1454,
        "name": "PrimeVideo HD"
    },
    {
        "id": 1455,
        "name": "Sky Cinema Sci-fi/Horror"
    },
    {
        "id": 1456,
        "name": "Sky Cinema Sci-fi/Horror HD"
    },
    {
        "id": 1457,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1458,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1459,
        "name": "Sky Cinema Family"
    },
    {
        "id": 1460,
        "name": "Sky Cinema Family HD"
    },
    {
        "id": 1461,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1462,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1463,
        "name": "Sky Cinema Family"
    },
    {
        "id": 1464,
        "name": "Sky Cinema Family HD"
    },
    {
        "id": 1465,
        "name": "Sky Cinema Sci-fi/Horror"
    },
    {
        "id": 1466,
        "name": "Sky Cinema Sci-fi/Horror HD"
    },
    {
        "id": 1467,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1468,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1469,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1470,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1471,
        "name": "Sky Cinema Best of 2020"
    },
    {
        "id": 1472,
        "name": "Sky Cinema Best of 2020 HD"
    },
    {
        "id": 1473,
        "name": "Sky Cinema Musicals"
    },
    {
        "id": 1474,
        "name": "Sky Cinema Musicals HD"
    },
    {
        "id": 1475,
        "name": "Sky Cinema Musicals"
    },
    {
        "id": 1476,
        "name": "Sky Cinema Musicals HD"
    },
    {
        "id": 1477,
        "name": "Sky Cinema Musicals"
    },
    {
        "id": 1478,
        "name": "Sky Cinema Musicals HD"
    },
    {
        "id": 1479,
        "name": "Sky Cinema Musicals"
    },
    {
        "id": 1480,
        "name": "Sky Cinema Musicals HD"
    },
    {
        "id": 1481,
        "name": "Sky Cinema Greats"
    },
    {
        "id": 1482,
        "name": "Sky Cinema Greats HD"
    }
]
