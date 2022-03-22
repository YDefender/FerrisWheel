# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define rai = Character("Rai Gamliloi")


# The game starts here.

label start:
    $ player_name = renpy.input("Input Your Character Name down here then press enter")
    $ player_name = player_name.strip()
    
    
    scene bgcloud1
    with fade
    play music "audio/music_happy.mp3" fadein 1.0 volume 0.5
    "Aku berdiri sendirian, melamun sembari memainkan ponsel yang dipenuhi pesan berupa pertanyaan yang tak kunjung terjawab oleh lawan bicara (?)."
    "Sesekali, mataku melirik, mencari-cari sosok yang kunanti di antara kerumunan manusia yang berlalu-lalang. Ia tidak terlambat, hanya aku saja yang tidak sabaran."
    "Pekik sebuah suara familiar terdengar. Bertepatan dengan itu, sesosok manusia bersurai blond dengan streak pelangi itu muncul di hadapanku." 

    scene bg1
    with fade

    show rai basic
    rai "Oh, helloooo!"

label choices:
    rai "Rai ga telat, kan?"
menu:
    "Nggak kok Rai, ini lebih awal dari jam janjian":
        jump choices1_a

    "...":
        jump choices1_b

label choices1_a:
    rai "Yuk, masuk sekarang!"
    jump choices1_common

label choices1_b:
    rai "Gomen-gomen, yuk masuk sekarang!"
    jump choices1_common

label choices1_common:
   "Aku terkekeh kecil, kemudian mengangguk dan berjalan bersamanya memasuki tempat tersebut- Taman bermain."

label continue:
    scene bg2
    with fade

    show rai basic
    "Aku menatap Rai yang celingukan melihat- lihat wahana"
    player_name.strip() "\"Kamu mau main yang mana dulu\""

    rai "Hm? Kamu maunya yang mana?" 
    

label choices2:
    "Dia malah balik bertanya. Aku menatap sekeliling, bergumam seolah-olah berpikir, kemudian menunjuk rel besar yang menjulang di hadapan kami berdua dengan wajah serius."
menu:
    "\"Roller coaster yuk!\"":
        jump choices2_a

    "\"Aku Ngidam Roller coaster!\"":
        jump choices2_b

label choices2_a:
    rai "Eeeeehh-!"
    jump choices2_common

label choices2_b:
    rai "wtf??"
    jump choices2_common

label choices2_common:
   "Aku tertawa kecil melihat wajah Rai yang mendadak berubah ekspresi. Kedua kakinya sudah bersiap mengambil langkah, untuk kabur tentu saja."

label continue2:
    rai "Y-Yakin?"
    player_name.strip() "\"Nggak kok Rai, bercanda. Kalau naik itu nanti lemes kita\"" 
    "Rai menghela napas lega."
    player_name.strip() "\"Kita coba yang santai-santai dulu yuk\"" 
    rai "Tapi yang mana?" 
    "Mataku menatap sekitar, kemudian terpaku pada salah satu stan. "
    player_name.strip() "\"Tembak hadiah mau? Rai kan lumayan jago soal tembak-tembakan,\""
    rai "Oooo, bole bole, hayu!"

    scene bg shoot
    with fade

    show rai basic

    "Sepasang senapan kayu kini ada di tangan kami berdua. Pemuda di sampingku ini langsung membidik, membuatku kelabakan ikut mencari target."
    "\"Rai mau yang mana?\""
    rai "Yang mana aja boleh~ Kamu mau yang mana?"
    "\"Y-Ya terserah sih ....\""
    rai "Hum, kita coba lomba yuk! Siapa yang ga dapet, traktir cola~"
    "Ini mah emang dianya aja pengen cola."
    "..."
    "\"Rai, ke kafe yuk! Sekalian ngadem, panas nih.\""
    rai "Bole bole, hayu!"
        
    scene bg cafe
    with fade

    show rai basic
    
    "Aku dan pemuda bersurai blond ini berjalan menuju salah satu kafe yang tersedia di area taman bermain, dan masuk ke dalamnya"
    "Kami langsung disambut oleh denting bel selamat datang dan nuansa elegan yang memanjakan mata dari kafe tersebut."

    "Suasana di dalamnya terasa begitu sunyi dibandingkan dengan area luar yang begitu riuh dan heboh, mungkin karena memang tidak banyak pengunjung yang mampir ke kafe."

    rai "Mau duduk di mana??"
    "\"Dekat jendela aja gimana? Biar kelihatan pemandangan,\""
    
    "Rai hanya menurut dan mengekori, bersamaaan dengan seorang pelayan yang membawa menu."
    "Setelah memesan, aku memperhatikan Rai, yang terpaku dengan pemandangan di luar jendela. Apa yang ada di dalam pikirannya saat ini? Pekerjaan? Penya, mungkin? Atau teman-temannya?"
    "...Entah"
    "Aku ikut menatap ke luar untuk sesaat. Segala keriuhan yang tak terdengar terasa begitu berbeda jika dilihat dari balik kaca jendela."
    "Semua orang sedang bersenang-senang, menghabiskan waktu bersama orang-orang tersayang."
    "Yah, termasuk aku, bersama Rai di sini."
    
    "\"Rai, habis ini mau ngapain?\""
    rai "Nyoba wahana yang lain,"
    "\"Iya, tapi maksudku mau main yang mana?\""
    rai "Cangkir teh yang muter-muter?"
    "\"Boleh, tapi apa nggak pusing nanti?\""
    rai "Rai gapapa kalau kamu mau, kalau pusing, kita cari yang lain aja, gidu ...."
    
    "Ia menjawab sambil manggut-manggut lucu. Aku tertawa saja, menahan diri yang gemay pengen ngunyel mukanya."
    
    "\"Iya gidu~\""
    
    "Aku menirukan suaranya"
    
    rai "Giduu~" 
    "Dia mengulanginya lagi, membuatku tertawa untuk kesekian kalinya. Duh, kebangetan nih anak lucunya."
    "\"Ya udah, tapi nanti kita lihat-lihat suvenir dulu ya?\""
    rai "Bolee, ada yang mau dibeli kah?" 
    "\"Aku mau beliin Rai bando, pasti lucu.\""
    "Jawabanku sontak membuat ekspresi wajah Rai berubah."
    rai "Eeeeeee- K-Kok jadi Rai .... Kamu aja yang pake,"
    "Aku sok-sok tertawa jahat mendengarnya."
    "\"Tapi aku pengen liat Rai make~\""
    rai "Nooo-!!"
    
    "Aku tertawa kesenangan, bahkan meloncat-loncat kecil saking bahagianya. Isi handphoneku kini penuh dengan berbagai foto sang polisi dari berbagai sudut, sementara Rai hanya diam dengan ekspresi wajah yang sulit dijelaskan."
    "Satu hal yang pasti, dia malu, tentu saja."
    
    "\"Ihhhh, kamu imut bangeet aaaaaa~\""
    rai "EEeeeeEEEeee yamee- Aku mau lepas ajaa-"
    "\"Eh jangan dilepas! Ga usah malu, di sini kan rame yang make bando begini~\""
    "....."
    stop music fadeout 1.0
    play music "audio/music_down.mp3" fadein 1.0 volume 0.5

    "Oh no, dia diem"
    "Ngambek kah?"
    "Dia tidak mau menatap wajahku. Kutarik-tarik lengan bajunya, mengharapkan respons dari Rai, namun dia diam saja."
    "Aku mulai khawatir, mungkin dilepas saja ya? Kasihan juga kalau dipaksa, nanti mainnya jadi enggak seru soalnya kepikiran terus."
    "\"Em, Rai, kalau gamau pake boleh lepas kok, k-kan tadi udah difoto-\""
    rai "Eh- G-Gak apa-apa, kan untuk hari ini aja ...."
    "\"Yakin? Aku gak maksa kok kalau Rai gak mau.\""
    rai "Gak apa-apa sih ... tapi kamu juga harus make."
    
    stop music fadeout 1.0
    play music "audio/music_happy.mp3" fadein 1.0 volume 0.5

    "\"Ohh, jadi gitu toh. Biar ga malu sendirian ya?\""

    "Aku tertawa saja, sembari mengangguk meski Rai belum menatap ke arahku. "
    "\"Iya, aku juga make kok. Rai yang pilihin deh, biar sesuai kemauan Rai.\""
    rai "Boleh~?!"
    "Dia melonjak, senang diperbolehkan memilih, bahkan sorot matanya berbinar sejenak"
    "\"Iyaaa, boleh. Yang jelek-jelek juga gapapa,\""
    rai "Rai bakal pilihin yang lucu!"
    "Kemudian ngacir ke area bando tanpa aba-aba. Aku hanya memperhatikannya dengan senyum yang belum luntur, agak lega dia tidak ngambek."

    "How can someone be this cute..."
    
    scene bg2
    with fade

    "\"Duh kepalaku pusing beneran.\""

    show rai basic
    rai "Mau duduk dulu kaah?"
    "\"Plis duduk dulu aaaa ....\""
    "Setelah keluar dari wahana spinning teacups, aku dan Rai beristirahat di salah satu bangku panjang yang tersedia."
    "Kepalaku berdenyut parah, bahkan aku jalan aja gak bener, padahal tadi muternya gak gila-gila amat."
    "Aku melirik Rai yang duduk di sampingku sambil memijit dahi."
    "Nampaknya dia juga pusing- Ya iyalah, normalnya pasti begitu."
    "Kupejamkan mata sejenak, berharap rasa denyut di kepalaku bisa segera hilang."
    "Kala aku membuka mata, Rai berdiri di hadapanku dengan sebotol minuman dingin, mungkin dia baru kembali dari vending machine"
  
    rai "Kita istirahat dulu sebentar,"
    "Aku hanya mengangguk, sembari mengambil minuman yang diberikan pemuda itu."
    "Sejenak, pikiranku terasa melayang-layang. Sebuah pertanyaan pendek terlintas di kepala, membuatku menatap Rai lamat-lamat tanpa kusadari."
    "Aku menerka-nerka, mengira-ngira, mempertanyakan suatu hal yang mungkin terdengar bodoh-"
    
    scene bgcloud1
    with fade

    "Apakah dia merasa senang menghabiskan waktu bersamaku?"
    "Hari sudah hampir berakhir, dan berbagai macam wahana di taman ini telah kami coba. Melelahkan, namun sangat menyenangkan. "
    "Awalnya, aku berniat mengajak Rai pulang, apalagi melihat matahari yang mulai bersiap untuk pamit dari langit."
    "Namun, melihat Rai yang pandangannya tertuju pada sebuah wahana besar di hadapan, membuatku mengurungkan niat tersebut."
    "Dia bahkan berdiri lama sekali, seolah lupa dengan keadaan sekitar, dan hanya menatap lurus pada benda besar yang berputar itu."

    scene bgplay1
    with fade
    show rai basic
    "Bianglala."

    "\"Rai-\""
    
label choices3:
    rai "Eh, ah, iya? Pulang ya?"
menu:
    "\"Rai, kamu mau naik bianglala?\"":
        jump choices3_a

    "\"Rai? Kenapa bengong begitu?\"":
        jump choices3_b

label choices3_a:
    rai "Mau!"
    jump choices3_common

label choices3_b:
    rai "Gaada apa-apa kok, yuk pulang"
    jump endingscene

label choices3_common:
    "Pemuda itu langsung mengalihkan atensinya padaku, dengan sorot mata berbinar-binar yang tak pernah aku lihat sebelumnya."
    jump continue3


label continue3:
    "Secercah warna pelangi yang ada di iris matanya berkilat bahagia, membuatku terkesiap sejenak."
    "Untuk sepersekian detik, aku bisa melihat pancaran kebahagiaan dari mata indah Rai."
    "Aku bahkan kehilangan kata-kata, tenggelam tanpa sadar dalam warna-warni manik mata pemuda di hadapanku ini."
    "God, my heart."

    scene bginside1
    with fade
    show rai basic

    "\"Whoaaa~~~!!\""
    "Aku dan Rai sama-sama berseru, kala kereta bianglala (?) yang kami naiki mulai bergerak naik ke atas. Pemandangan indah yang terpampang jelas di luar jendela memanjakan mata kami berdua."
    "Meski aku terpesona, pikiranku masih tertuju pada pertanyaan yang sedari tadi mengisi kepala."
    "Mataku kini tertuju pada Rai, yang masih menatap keluar sambil mengoceh-ngoceh riang. Astaga, aku bahkan tidak mendengarkan."
    "\"Rai,\""
    
    stop music fadeout 1.0
    play music "audio/music_down.mp3" fadein 1.0 volume 0.5

    rai "Kenapa~?" 
    "Dia menyahut, tanpa menoleh padaku. Aku menghela napas pendek, mengumpulkan keberanian."
    "\"Aku mau tanya sesuatu boleh?\""
    "dia hanya mengangguk."
    "\"Sebenarnya, menghabiskan waktu bersamaku itu menyenangkan atau nggak?\""
    "Dalam sedetik, pandangan pemuda itu kini tertuju padaku."
    "Sorot matanya bertanya-tanya, membuatku tanpa sadar menggigit bibir, mendadak merasa bodoh."
    "\"Eh, k-kalau Rai gamau jawab juga gapapa, pasti pertanyaanku aneh ya?\""
    rai "He? Enggak kok! Rai bingung aja kenapa tiba-tiba kamu nanya gitu ...."
    "Aku mengangguk saja, bingung harus membalas apa. Dia juga ikut diam, entah memikirkan apa. Jantungku sudah dag-dig-dug (?) tak keruan, dan kini mataku tak menatap wajah Rai"
    rai "Tentu saja menyenangkan."
    "Rai memecahkan keheningan, namun aku tetap menunduk diam."
    rai "Ngabisin waktu sama kamu itu seruuuuu banget, Rai senang!"
    rai "Jarang-jarang Rai bisa keluar dan main-main kayak gini, apalagi sama orang lain."
    "Aku masih senyap, bingung aku harus bilang apa."
    rai "Rai senang sekali kok, apalagi karena kamu mau nemenin Rai. "
    rai "Kita main apa aja kamu ikut, ga protes."
    rai "Ngemil apa aja juga Rai ga dimarahin. "
    rai "Beli ini itu iya-iya aja."
    rai "Menghabiskan waktu sama seseorang, apalagi orang yang sayang sama Rai, itu sesuatu yang pastinya membahagiakan sekali."
    "Entah kenapa, aku merasakan wajahku memanas. Kala aku mendongak, pemuda dengan highlight pelangi itu tersenyum lebar padaku, manis sekali."
    "God, I'm melting."
    rai "Kamu sendiri seneng nggak main sama Rai seharian ini?" 
    "\"Seneng dong! Banget malah!!!!\""
    "seruku spontan tanpa pikir panjang, membuat dia terkejut, kemudian tergelak."
    "Duh malu."
    "\"Bagiku, ngabisin waktu sama Rai itu suatu memori yang penting banget, yang bakal aku treasure sampai kapanpun,\""
    "ucapku, mencoba merangkai kalimat dengan pikiran melayang-layang ga jelas."
    "\"Rai itu sangaaaaat berharga buat aku, soalnya Rai udah membuat aku bahagia,\""
    "lanjutku, sebelum kemudian menghela napas panjang."
    "\"Jadi, seenggaknya, biarpun ga seberapa, aku juga pengen bikin Rai bahagia.\""
    "Sunyi, ekspresi wajah Rai berubah jadi ... kaget? Bingung? Entah, aku tidak tahu bagaimana menjelaskannya."
    "\"Aku ngelihat Rai selalu sibuk, dan agak jarang berinteraksi sama yang lain. Kamu itu kayak Takamama, sibuk dengan pekerjaan, tapi Rai terasa lebih jauh buat ... diraih, gitu,\""
    "\"Aku tahu Rai pasti ngabisin waktu sama anak-anak lain, bahkan mungkin ngobrol tiap hari,\""
    "\"Tapi, gatau kenapa, aku ngerasa Rai agak kesepian, meski ga yakin begitu. Ini cuma perasaan pribadi aja.\""
    "Jeda lagi, aku menarik napas panjang, dan menghembuskannya perlahan. Detak jantungku terasa terlalu cepat dan berisik."
    "\"Jadi, dengan menghabiskan waktu sama Rai di sini, mungkin, aku bisa membuat Rai ngerasa lebih senang, dan lupa hal-hal melelahkan. Aku ingin menjadi orang yang membahagiakan Rai, biarpun sebentar, gitu.\""
    "Aku memainkan jemariku, merasa awkward mengatakan hal2 semacam itu pada Rai."
    "Namun, dia hanya tersenyum, dan tak lama kemudian, tawanya pecah, membuatku merona malu."
    "\"Maaf! Pasti kedengarannya aneh-!\""
    rai "Nggak kok, it's okay! Rai justru senang kamu jujur sama Rai~" 
    rai "Makasih banyak,"
    rai "Rai bahagia banget hari ini, makasih banyak udah mau main sama Rai~"
    "\"Sama-sama .... A-Aku juga bahagia soalnya bisa bareng Rai, makasih ....\""
    "Dia tersenyum lebar, membuat wajahku ikut mengukir kurva bahagia."
    "Beautiful, indeed...."
label endingscene:  
    "..."
    "\"Let's make even more happy memories, shall we?\""


return
