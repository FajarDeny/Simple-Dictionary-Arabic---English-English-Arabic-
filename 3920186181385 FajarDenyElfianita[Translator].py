# Membuat Dictionary

kamus = {
    "harimau"  : "Tiger\nنَمِرٌ",
    "sapi"     : "Cow\nبَقَرَةٌ ",
    "gajah"    : "Elephant\nفِيْلٌ",
    "anjing"   : "Dog\n كَلْبٌ",
    "kelinci"  : "Rabbit\nأَرْنَبٌ",
    "tikus"    : "Mouse\n فَأْرٌ",
    "kucing"   : "Cat\n قِطٌّ",
    "kura-kura": "Turtle\n سُلَحْفَاةٌ",
    "katak"    : "Frog\n ضِفْدَعٌ",
    "kodok"    : "Frog\n ضِفْدَعٌ",
    "kera"     : "Monkey\n القردُ",
    "monyet"   : "Monkey\nالقردُ",
    "ular"     : "Snake\n الثعبانُ",
    "singa"    : "Lion\n الأسدُ",
    "buaya"    : "Crocodile\n تِمساحٌ",
    "dinosaurus": "Dinosaurus\n الديناصور",
    "kanguru"  : "Kangaroo\n الكنغرُ",
    "jerapah"  : "Giraffe\n الزرافة",
    "tupai"    : "Squirrel\n السنجابُ",
    "gurita"   : "Abstetric\n الأخطبوط",
    "unta"     : "Camel\n الجملُ",
    "anak anjing": "Puppy\nجرو",
    "kerbau"   : "Buffalo\nجاموس",
    "kuda"     : "Horse\nالحصان",
    "zebra"    : "Zebra\nحمار الوحش",
    "babi"     : "Pig\nخنزير",
    "kambing"  : "Goat\nالماعز",
    "serigala" : "Wolf\nالذئب",
    "beruang"  : "Bear\nالدب",
    "macan"    : "Tiger\nالنمر",
    "gorila"   : "Gorilla\nغوريلا",
    "landak"   : "Porcupine\nقنفذ",
    "siput"    : "Snail\nحلزون",
    "keledai"  : "Donkey\nحمار",
    "kecoa"    : "Cockroach\nصرصور",
    "kupu-kupu": "Butterfly\nفراشة",
    "serangga" : "Insect\nحشرة",
    "nyamuk"   : "Mosquito\nبعوض",
    "laba-laba": "Spider\nالعناكب",
    "kalajengking": "Scorpion\nعقرب",
    "ulat"     : "Caterpillar\nتراكتور",
    "lebah"    : "Bee\nنحلة",
    "tawon"    : "Bee\nنحلة",
    "kutu"     : "Louse\nقملة",
    "lalat"    : "Fly\nطيران",
    "semut"    : "Ant\nنملة",
    "paus"     : "Whale\nالحوت",
    "udang"    : "Shrimp\nجمبري",
    "ikan"     : "Fish\nالسمكة",
    "lumba-lumba"  : "Dolphin\nالدلفين",
    "apel"         : "Apple\nتفاحة", 
    "anggur"       : "Grape \n نبيذ",
    "belimbing"    : "Starfruit\n نجمة الفاكهة",
    "ceri"         : "Cherry\n الكرز",
    "delima"       : "Pomegranate\n رمان ",
    "durian"       : "Durian\n  دوريان ",
    "jambu air"    : "Water Apple\n  ماء الجوافة ",
    "jambu batu"    : "Guava\n جوافة ",
    "kelengkeng"    : " Longan \n اللونجان ",
    "lemon"        : " Lemon \n ليمون ",
    "mangga"       : " Mango \n مانجو ",
    "manggis"      : " Mangosteen \n مانغوستين ",
    "markisa"      : " Passion Fruit \n فاكهة العاطفة ",
    "melon"    : " Melon \n شمام ",
    "nanas"    :   " Pineapple \n أناناس ",
    "nangka"   : " Jackfruit \n الكاكايا ",
    "naga"     : " Dragon Fruit \n تنين ",
    "pepaya"   : " Papaya \n بابايا ",
    "pir"      : " Pear \n كمثرى ",
    "pisang"     : "Banana\n موز ",
    "rambutan"   : " Rambutan \n الرامبوتان ",
    "semangka"   : " Watermelon \n بطيخ ",
    "sirsak"     : " Soursop \n قشطة شائكة ",
    "stroberi"   : " Strawberry \n فراولة ",

    


}


import datetime
currentDate = datetime.date.today()
currentTime = datetime.datetime.now()


print(currentDate.strftime("How a Beautiful Day Today,\nThanks For Visit Us \nat %A, %B %d %Y"))
print(datetime.datetime.strftime(currentTime, '%H:%M'))
print("                                                                   ")
print("=================Welcome to Amazon Dictionory=======================")

print("____________________________________________________________________")
print("                                                                    ")
print("============ The Best English Translator in this Campus ============")

print("````````````````````````````````````````````````````````````````````")
print("                          ``````````````                            ")
print("                               `````                                ")
nama=input("                  Please enter your name: ")
salam = input(nama.upper() +", Assalamualaikum......\n")
kabar = input("How are you? "+ nama.upper () + "?\n ")

print("````````````````````````````````````````````````````````````````````")
print("Hello, " + nama.upper() + " lets learn with us, you can enter your own words")

print("                    It's All About Fruits and Animals               ")
print("Please Choose Your Translator from Indonesia - English and Arabic, type A or B")
pilihan=input("A. Animals \nB. Fruits\nI Choose : ").lower()
if pilihan =="a":
    kata = "words"
    while kata != "4" : 
        kata=input("Enter The Word [type 'stop' if you finish]  : ").lower()
        if kata == "harimau" :
            print("%s" % kamus ["harimau"])
        elif kata == "sapi" :
            print("%s" % kamus ["sapi"])
        elif kata == "gajah" :
            print("%s" % kamus ["gajah"])
        elif kata == "anjing" :
            print("%s" % kamus ["anjing"]
            )
        elif kata == "kelinci" :
            print("%s" % kamus ["kelinci"])
        elif kata == "tikus" :
            print("%s" % kamus ["tikus"])
        elif kata == "kucing" :
            print("%s" % kamus ["kucing"])
        elif kata == "kura-kura" :
            print("%s" % kamus ["kura-kura"])
        elif kata == "katak" :
            print("%s" % kamus ["katak"])
        elif kata == "kodok" :
            print("%s" % kamus ["kodok"])
        elif kata == "kera" :
            print("%s" % kamus ["kera"])
        elif kata == "monyet" :
            print("%s" % kamus ["monyet"])
        elif kata == "ular" :
            print("%s" % kamus ["ular"])
        elif kata == "singa" :
            print("%s" % kamus ["singa"])
        elif kata == "buaya" :
            print("%s" % kamus ["buaya"])
        elif kata == "dinosaurus" :
            print("%s" % kamus ["dinosaurus"])
        elif kata == "kanguru" :
            print("%s" % kamus ["kanguru"])
        elif kata == "jerapah" :
            print("%s" % kamus ["jerapah"])
        elif kata == "tupai" :
            print("%s" % kamus ["tupai"])
        elif kata == "gurita" :
            print("%s" % kamus ["gurita"])
        elif kata == "unta" :
            print("%s" % kamus ["unta"])
        elif kata == "anak anjing" :
            print("%s" % kamus ["anak anjing"])
        elif kata == "kerbau" :
            print("%s" % kamus ["kerbau"])
        elif kata == "kuda" :
            print("%s" % kamus ["kuda"])
        elif kata == "zebra" :
            print("%s" % kamus ["zebra"])
        elif kata == "babi" :
            print("%s" % kamus ["babi"])
        elif kata == "kambing" :
            print("%s" % kamus ["kambing"])
        elif kata == "serigala" :
            print("%s" % kamus ["serigala"])
        elif kata == "beruang" :
            print("%s" % kamus ["beruang"])
        elif kata == "macan" :
            print("%s" % kamus ["macan"])
        elif kata == "gorila" :
            print("%s" % kamus ["gorila"])
        elif kata == "landak" :
            print("%s" % kamus ["landak"])
        elif kata == "siput" :
            print("%s" % kamus ["siput"])
        elif kata == "keledai" :
            print("%s" % kamus ["keledai"])
        elif kata == "kecoa" :
            print("%s" % kamus ["kecoa"])
        elif kata == "kupu-kupu" :
            print("%s" % kamus ["kupu-kupu"])
        elif kata == "jangkrik" :
            print("%s" % kamus ["jangkrik"])
        elif kata == "serangga" :
            print("%s" % kamus ["serangga"])
        elif kata == "nyamuk" :
            print("%s" % kamus ["nyamuk"])
        elif kata == "laba-laba" :
            print("%s" % kamus ["laba-laba"])
        elif kata == "kalajengking" :
            print("%s" % kamus ["kalajengking"])
        elif kata == "ulat" :
            print("%s" % kamus ["ulat"])
        elif kata == "lebah" :
            print("%s" % kamus ["lebah"])
        elif kata == "tawon" :
            print("%s" % kamus ["tawon"])
        elif kata == "kutu" :
            print("%s" % kamus ["kutu"])
        elif kata == "lalat" :
            print("%s" % kamus ["lalat"])
        elif kata == "semut" :
            print("%s" % kamus ["semut"])
        elif kata == "paus" :
            print("%s" % kamus ["paus"])
        elif kata == "udang" :
            print("%s" % kamus ["udang"])
        elif kata == "lumba-lumba" :
            print("%s" % kamus ["lumba-lumba"])
        elif kata == "ikan" :
            print("%s" % kamus ["ikan"])
        elif kata =="stop" :
            print(" ________________________THANKS FOR YOUR VISITING _______________________")
            break
        else :
            print("================ Sorry, we can't find your Animal ===================  ")
            print("               === Maybe you can see in the Zoo ===                    ")
else :
    words = "kata"
    while words != "4" : 
        words=input("Enter The Word [type 'stop' if you finish]  : ").lower()
        if words == "anggur" :
            print("%s" % kamus ["anggur"])
        elif words == "apel" :
            print("%s" % kamus ["apel"])
        elif words == "belimbing" :
            print("%s" % kamus ["belimbing"])
        elif words == "ceri" :
            print("%s" % kamus ["ceri"]
            )
        elif words == "delima" :
            print("%s" % kamus ["delima"])
        elif words == "durian" :
            print("%s" % kamus ["durian"])
        elif words == "jambu air" :
            print("%s" % kamus ["jambu air"])
        elif words == "jambu batu" :
            print("%s" % kamus ["jambu batu"])
        elif words == "kelengkeng" :
            print("%s" % kamus ["kelengkeng"])
        elif words == "lemon" :
            print("%s" % kamus ["lemon"])
        elif words == "mangga" :
            print("%s" % kamus ["mangga"])
        elif words == "manggis" :
            print("%s" % kamus ["manggis"])
        elif words == "markisa" :
            print("%s" % kamus ["markisa"])
        elif words == "melon" :
            print("%s" % kamus ["melon"])
        elif words == "nanas" :
            print("%s" % kamus ["nanas"])
        elif words == "nangka" :
            print("%s" % kamus ["nangka"])
        elif words == "naga" :
            print("%s" % kamus ["naga"])
        elif words == "pepaya" :
            print("%s" % kamus ["pepaya"])
        elif words == "pir" :
            print("%s" % kamus ["pir"])
        elif words == "pisang" :
            print("%s" % kamus ["pisang"])
        elif words == "rambutan" :
            print("%s" % kamus ["rambutan"])
        elif words == "semangka" :
            print("%s" % kamus ["semangka"])
        elif words == "sirsak" :
            print("%s" % kamus ["sirsak"])
        elif words == "stroberi" :
            print("%s" % kamus ["stroberi"])
        elif words =="stop" :
            print(" ________________________THANKS FOR YOUR VISITING _______________________")
            break
        else :
            print("================ Sorry, we can't find your Fruits ===================  ")
            print("                === maybe you can see in the Market ===                ")





                  
# Mengakses isi dictionary


