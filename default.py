# import the XBMC libraries so we can use the controls and functions of XBMC
import xbmc, xbmcgui ,random, serial, threading, time,struct



#KEY_POWER_POWER   =        49
#KEY_1_COMPANYINFO =        206
#KEY_2_PRODUCTINFO =        205
#KEY_3_MUTEBUZZER  =        192
#KEY_TVAV_CHARTUSB =        7
#KEY_4_ISHIHARA    =        203
#KEY_5_ANIMAL      =        202
#KEY_6_CARTOON     =        201
#KEY_SLEEP_SC1     =        204
#KEY_7_SC2         =        200
#KEY_8_SC3         =        199
#KEY_9_SC4         =        198
#KEY_VSM_ASTIGFAN  =         22
#KEY_DISP_CROSSBAR =        248
#KEY_0_DOT         =        207
#KEY_FAV_MADDOX    =        213
#KEY_SCAN_PERIPERAL=        209
#KEY_UP_NEXT       =        166
#KEY_ZOOM_REDGREEN =        208
#KEY_LEFT_EDUCATIONAL=      169
#KEY_MENU_OK         =       11
#KEY_RIGHT_MENU      =      168
#KEY_SWAP_LANGUAGE1  =      247
#KEY_DOWN_PREV       =      167
#KEY_MUTE_LANGUAGE2  =      195
#KEY_MAGIC_LANDLOT   =      223
#KEY_SWAPTIMER_THUMLINGSE = 216
#KEY_CHILDTIMER_APLHARAND = 0
#KEY_PICMUTE_NUMERICRAND  = 221
#KEY_COLORTONE_PAEDIATRIC = 226
#KEY_PBASS_CONTRAST       = 230
#KEY_SURR_LOGMAR          = 224
#KEY_SSM_SNELLAN          = 227

KEY_POWER_POWER   =        0x30
KEY_1_COMPANYINFO =        0x31
KEY_2_PRODUCTINFO =        0x32
KEY_3_MUTEBUZZER  =        0x33
KEY_TVAV_CHARTUSB =        0x34
KEY_4_ISHIHARA    =        0x35
KEY_5_ANIMAL      =        0x36
KEY_6_CARTOON     =        0x37
KEY_SLEEP_SC1     =        0x38
KEY_7_SC2         =        0x39
KEY_8_SC3         =        0x3A
KEY_9_SC4         =        0x3B
KEY_VSM_ASTIGFAN  =        0x3C
KEY_DISP_CROSSBAR =        0x3D
KEY_0_DOT         =        0x3E
KEY_FAV_MADDOX    =        0x3F
KEY_SCAN_PERIPERAL=        0x40
KEY_UP_NEXT       =        0x41
KEY_ZOOM_REDGREEN =        0x42
KEY_LEFT_EDUCATIONAL=      0x43
KEY_MENU_OK         =      0x44
KEY_RIGHT_MENU      =      0x45
KEY_SWAP_LANGUAGE1  =      0x46
KEY_DOWN_PREV       =      0x47
KEY_MUTE_LANGUAGE2  =      0x48
KEY_MAGIC_LANDLOT   =      0x49
KEY_SWAPTIMER_THUMLINGSE = 0x4A
KEY_CHILDTIMER_APLHARAND = 0x4B
KEY_PICMUTE_NUMERICRAND  = 0x4C
KEY_COLORTONE_PAEDIATRIC = 0x4D
KEY_PBASS_CONTRAST       = 0x4E
KEY_SURR_LOGMAR          = 0x4F
KEY_SSM_SNELLAN          = 0x50


#AB6 Modes
MODE_WELCOME =           0
MODE_CHART   =           1
MODE_CHART_DIST_MENU =   2
MODE_CHART_GROUP_MENU =  3
MODE_USB_MENU         =  4
MODE_USB_PLAY         =  5
MODE_STANDBY          =  6

#distance macros
DIST_6  = 0
DIST_8  = 1
DIST_10 = 2
DIST_12 = 3
DIST_15 = 4
DIST_20 = 5
DIST_MIR= 6

#file type
JPG=0
BMP=1

#Languages
LANG_ARABIC    = 0
LANG_BENGALI   = 1
LANG_GUJARATHI = 2
LANG_HINDI     = 3
LANG_KANNADA   = 4
LANG_MALAYALAM = 5
LANG_ORIYA     = 6
LANG_PUNJABI   = 7
LANG_TAMIL     = 8
LANG_TELUGU    = 9
LANG_URDU      =10

LANG_MAX = LANG_URDU
LANG_MIN = LANG_ARABIC
DIST_MAX = DIST_MIR
DIST_MIN = DIST_6
GROUP_MIN = 0
GROUP_MAX = 5

#chart type  definitions
#No distance dependeancy & no sub folder
CHART_COMPANY_INFO = 0
CHART_PROD_INFO    = 1
CHART_ANIMAL       = 2
CHART_CARTOON      = 3
CHART_ISHIHARA     = 4

#No distance dependeancy & has sub folders
CHART_EDUCATION    = 5

#has distance dependancy and no sub folders no random no language dependancy
CHART_ACC       = 6
CHART_ASTIG_FAN = 7
CHART_CONTRAST  = 8
CHART_DOTS      = 9
CHART_LANDLOT   = 10
CHART_LOGMAR    = 11
CHART_MADDOX    = 12
CHART_PEADIATRIC= 13
CHART_PERIPERALS= 14
CHART_RED_GREEN = 15
CHART_SC1       = 16
CHART_SC2       = 17
CHART_SC3       = 18
CHART_SC4       = 19
CHART_THUMLINGE = 20

#has distance dependancy and random generation no language dependancy
CHART_ALPHABETS = 21
CHART_NUMERIC   = 22

#has distance dependancy and language dependancy no rtandom
CHART_LANGUAGE1 =  23
CHART_LANGUAGE2 =  24
CHART_SNELLAN   =  25

keycode_to_charttype={KEY_POWER_POWER:-1,
                      KEY_1_COMPANYINFO:CHART_COMPANY_INFO,
                      KEY_2_PRODUCTINFO:CHART_PROD_INFO,
                      KEY_3_MUTEBUZZER:-2,
                      KEY_TVAV_CHARTUSB:-3,
                      KEY_4_ISHIHARA:CHART_ISHIHARA,
                      KEY_5_ANIMAL:CHART_ANIMAL,
                      KEY_6_CARTOON:CHART_CARTOON,
                      KEY_SLEEP_SC1:CHART_SC1,
                      KEY_7_SC2:CHART_SC2,
                      KEY_8_SC3:CHART_SC3,
                      KEY_9_SC4:CHART_SC4,
                      KEY_VSM_ASTIGFAN:CHART_ASTIG_FAN,
                      KEY_DISP_CROSSBAR:CHART_ACC,
                      KEY_0_DOT:CHART_DOTS,
                      KEY_FAV_MADDOX:CHART_MADDOX,
                      KEY_SCAN_PERIPERAL:CHART_PERIPERALS,
                      KEY_UP_NEXT:-4,
                      KEY_ZOOM_REDGREEN:CHART_RED_GREEN,
                      KEY_LEFT_EDUCATIONAL:-5,
                      KEY_MENU_OK:-6,
                      KEY_RIGHT_MENU:-7,
                      KEY_SWAP_LANGUAGE1:CHART_LANGUAGE1,
                      KEY_DOWN_PREV:-8,
                      KEY_MUTE_LANGUAGE2:CHART_LANGUAGE2,
                      KEY_MAGIC_LANDLOT:CHART_LANDLOT,
                      KEY_SWAPTIMER_THUMLINGSE:CHART_THUMLINGE,
                      KEY_CHILDTIMER_APLHARAND:CHART_ALPHABETS,
                      KEY_PICMUTE_NUMERICRAND:CHART_NUMERIC,
                      KEY_COLORTONE_PAEDIATRIC:CHART_PEADIATRIC,
                      KEY_PBASS_CONTRAST:CHART_CONTRAST,
                      KEY_SURR_LOGMAR:CHART_LOGMAR,
                      KEY_SSM_SNELLAN:CHART_SNELLAN  }

#chart property : 0- Distance dependancy; 1- Subfolder; 2- Language; 3 - Random; 4 - File type 0-jpg 1- bmp
#-------------------------------------------------------
chart_property=[ [0,0,0,0,1],   #Company info
                 [0,0,0,0,1],   #Product info
                 [0,0,0,0,0],   #Animal
                 [0,0,0,0,0],   #Cartoon,
                 [0,0,0,0,0],   #Isihara
                 [0,1,0,0,0],   #Education
                 [1,0,0,0,0],   #Acc
                 [1,0,0,0,0],   #Astig Fan
                 [1,0,0,0,0],   #Contrast
                 [1,0,0,0,0],   #Dots
                 [1,0,0,0,0],   # Landlot
                 [1,0,0,0,0],   # Logmar
                 [1,0,0,0,1],   # MAddox
                 [1,0,0,0,0],   # Peadiatric
                 [1,0,0,0,0],   # Periperals
                 [1,0,0,0,1],   # Red Green Chartsa
                 [1,0,0,0,0],   # SC1
                 [1,0,0,0,0],   # SC2
                 [1,0,0,0,0],   # SC3
                 [1,0,0,0,0],   # SC4
                 [1,0,0,0,0],   # ThumlingsE
                 [1,0,0,1,0],   # Aplphabets
                 [1,0,0,1,0],   # Numerics
                 [1,0,1,0,0],   # Language 1
                 [1,0,1,0,0],   # Laguage 2
                 [1,0,1,0,0] ]    # Snellan


dir_distance=["/COMMON",
              "/6FEET",
              "/8FEET",
              "/10FEET",
              "/12FEET",
              "/15FEET",
              "/20FEET",
              "/MIRROR" ];

dir_chart_type=[ "/CO_INFO",
                 "/PROD_INFO",
                 "/ANIMAL",
                 "/CARTOON",
                 "/ISHIHARA",
                 "/EDUCATION",
                 "/ACC",
                 "/ASTIGFAN",
                 "/CONTRAST",
                 "/DOTS",
                 "/LANDLOT",
                 "/LOGMAR",
                 "/MADDOX",
                 "/PEDIATRIC",
                 "/PERIPERALS",
                 "/REDGREEN",
                 "/SC1",
                 "/SC2",
                 "/SC3",
                 "/SC4",
                 "/THUMLINGSE",
                 "/ALPHABETS",
                 "/NUMERICS",
                 "/LANGUAGE",
                 "/LANGUAGE",
                 "/SNELLAN"]

#Max number of charts or sub folder for each chart type and for each distance
max_chart=[[1,1,1,1,1,1,1],   #Company info
           [1,1,1,1,1,1,1],   #Product info
           [6,6,6,6,6,6,6],   #Animal
           [9,9,9,9,9,9,9],   #Cartoon,
           [9,9,9,9,9,9,9],   #Isihara
           [6,6,6,6,6,6,6],   #Education
           [4,4,4,4,4,4,4],   #Acc
           [18,18,18,18,18,18,18], #Astig Fan
           [16,16,16,16,16,16,16],        #Contrast
           [8,8,8,8,8,8,8],   #Dots
           [8,8,8,8,8,8,8],   #Landlot
           [6,6,6,6,10,10,10],#Logmar
           [5,5,5,5,5,5,5],   # MAddox
           [7,7,7,7,7,4,4],   # Peadiatric
           [1,1,1,1,1,1,1],   # Periperals
           [6,6,6,6,5,6,6],   # Red Green Chartsa
           [1,1,1,1,1,1,1],   # SC1
           [1,1,1,1,1,1,1],   # SC2
           [1,1,1,1,1,1,1],   # SC3
           [1,1,1,1,1,1,1],   # SC4
           [8,8,8,8,8,8,8],   # ThumlingsE
           [3,3,3,3,3,3,3],   # Aplphabets
           [3,3,3,3,3,3,3],   # Numerics
           [11,11,11,11,11,11,11],   # Language 1
           [11,11,11,11,11,11,11],   # Laguage 2
           [11,11,11,11,11,11,11]]   # Snellan

dir_sub_chart=[ "/CATRACT", #0
                "/RETINA",  #1
                "/CORNEA",  #2
                "/GLAUCOMA",#3
                "/LASIK",   #4
                "/CONTACTLENS", #5
                "/ALPHABETS1", #6
                "/ALPHABETS2", #7
                "/ALPHABETS3", #8
                "/NUMERIC1",   #9
                "/NUMERIC2",   #10
                "/NUMERIC3",   #11
                "/ARABIC",     #12 //for LANGUAGE1 and 2
                "/BENGALI",    #13
                "/GUJARATHI",  #14
                "/HINDI",      #15
                "/KANNADA",    #16
                "/MALAYALAM",  #17
                "/ORIYA",      #18
                "/PUNJABI",    #19
                "/TAMIL",      #20
                "/TELUGU",     #21
                "/URDU",       #22
                "/ARABIC",     #23  for SNELLAN
                "/BENGALI",    #24
                "/GUJARATHI",  #14
                "/HINDI",      #15
                "/KANNADA",    #16
                "/MALAYALAM",  #17
                "/ORIYA",      #18
                "/PUNJABI",    #19
                "/TAMIL",      #20
                "/TELUGU",     #21
                "/URDU" ]      #22



# index used to access the sub_dir string in the dir_sub_chart array
sub_index=[[0,0,0,0,0,0,0],   #Company info
                  [0,0,0,0,0,0,0],   #Product info
                  [0,0,0,0,0,0,0],   #Animal
                  [0,0,0,0,0,0,0],   #Cartoon, 0
                  [0,0,0,0,0,0,0],   #Isihara
                  [0,0,0,0,0,0,0],   #Education
                  [0,0,0,0,0,0,0],   #Acc
                  [0,0,0,0,0,0,0],   #Astig Fan
                  [0,0,0,0,0,0,0],   #Contrast
                  [0,0,0,0,0,0,0],   #Dots
                  [0,0,0,0,0,0,0],   # Landlot
                  [0,0,0,0,0,0,0],   # LogmaR
                  [0,0,0,0,0,0,0],   # MAddox
                  [0,0,0,0,0,0,0],   # Peadiatric
                  [0,0,0,0,0,0,0],   # Periperals
                  [0,0,0,0,0,0,0],   # Red Green Chartsa
                  [0,0,0,0,0,0,0],   # SC1
                  [0,0,0,0,0,0,0],   # SC2
                  [0,0,0,0,0,0,0],   # SC3
                  [0,0,0,0,0,0,0],   # SC4
                  [0,0,0,0,0,0,0],   # ThumlingsE
                  [6,6,6,6,6,6,6],   # Aplphabets
                  [9,9,9,9,9,9,9],   # Numerics
                  [12,12,12,12,12,12,12],   # Language 1
                  [12,12,12,12,12,12,12],   # Laguage 2
                  [23,23,23,23,23,23,23]]   # Snellan

max_sub_chart=[[33,33,33,33,33,33,33],	#CATRACT, //0
                   [26,26,26,26,26,26,26],	#RETINA,  //1
                   [9,9, 9, 9, 9, 9,9],     #CORNEA,    //2
                   [7,7, 7, 7, 7, 7,7],		#GLAUCOMA,  //3
                   [9,9, 9, 9, 9, 9,9],     #LASIK,    //4
                   [5,5, 5, 5, 5, 5,5],     #CONTACTLENS, //5
                   [8,8, 8, 8, 8, 8,8], 	#ALPHABETS1, //6
                   [8,8, 8, 8, 8, 8,8],		#ALPHABETS2,  //7
                   [8,8, 8, 8, 8, 8,8],		#ALPHABETS3, //8
                   [8,8, 8, 8, 8, 8,8],		#NUMERIC1,   //9
                   [8,8, 8, 8, 8, 8,8],		#NUMERIC2,   //10
                   [8,8, 8, 8, 8, 8,8],		#NUMERIC3,   //11
                   [8,8, 8, 8, 8, 8,8],  #for Language1&2  //ARABIC,//12
                   [8,8, 8, 8, 8, 8,8],     #BENGALI,    //13
                   [8,8, 8, 8, 8, 8,8],     #GUJARATHI,  //14
                   [8,8, 8, 8, 8, 8,8],    	#HINDI,      //15
                   [8,8, 8, 8, 8, 8,8],    	#KANNADA,    //16
                   [8,8, 8, 8, 8, 8,8],     #MALAYALAM,  //17
                   [8,8, 8, 8, 8, 8,8],     #ORIYA,      //18
                   [8,8, 8, 8, 8, 8,8],     #PUNJABI,    //19
                   [8,8, 8, 8, 8, 8,8],   	#TAMIL,      //20
                   [8,8, 8, 8, 8, 8,8],     #TELUGU,     //21
                   [8,8, 8, 8, 8, 8,8],     #URDU        //22
                   [4,4, 4, 4, 8, 8,8],  # for SNELLAN   //ARABIC,//23
                   [4,4, 4, 4, 8, 8,8],     #BENGALI,    //24
                   [4,4, 4, 4, 8, 8,8],     #GUJARATHI,  //25
                   [4,4, 4, 4, 8, 8,8],     #HINDI,      //26
                   [4,4, 4, 4, 8, 8,8],     #KANNADA,    //27
                   [4,4, 4, 4, 8, 8,8],     #MALAYALAM,  //28
                   [4,4, 4, 4, 8, 8,8],     #ORIYA,      //29
                   [4,4, 4, 4, 8, 8,8],     #PUNJABI,    //30
                   [4,4, 4, 4, 8, 8,8],     #TAMIL,      //31
                   [4,4, 4, 4, 8, 8,8],     #TELUGU,     //32
                   [4,4, 4, 4, 8, 8,8] ]  	#URDU        //33



# Table of CRC values for high-order byte
table_crc_hi = [ 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0,
        0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
        0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0,
        0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
        0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1,
        0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41,
        0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1,
        0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
        0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0,
        0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40,
        0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1,
        0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
        0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0,
        0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40,
        0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0,
        0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
        0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0,
        0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
        0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0,
        0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
        0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0,
        0x80, 0x41, 0x00, 0xC1, 0x81, 0x40, 0x00, 0xC1, 0x81, 0x40,
        0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1,
        0x81, 0x40, 0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
        0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41, 0x01, 0xC0,
        0x80, 0x41, 0x00, 0xC1, 0x81, 0x40 ]

# Table of CRC values for low-order byte
table_crc_lo = [ 0x00, 0xC0, 0xC1, 0x01, 0xC3, 0x03, 0x02, 0xC2, 0xC6, 0x06,
        0x07, 0xC7, 0x05, 0xC5, 0xC4, 0x04, 0xCC, 0x0C, 0x0D, 0xCD,
        0x0F, 0xCF, 0xCE, 0x0E, 0x0A, 0xCA, 0xCB, 0x0B, 0xC9, 0x09,
        0x08, 0xC8, 0xD8, 0x18, 0x19, 0xD9, 0x1B, 0xDB, 0xDA, 0x1A,
        0x1E, 0xDE, 0xDF, 0x1F, 0xDD, 0x1D, 0x1C, 0xDC, 0x14, 0xD4,
        0xD5, 0x15, 0xD7, 0x17, 0x16, 0xD6, 0xD2, 0x12, 0x13, 0xD3,
        0x11, 0xD1, 0xD0, 0x10, 0xF0, 0x30, 0x31, 0xF1, 0x33, 0xF3,
        0xF2, 0x32, 0x36, 0xF6, 0xF7, 0x37, 0xF5, 0x35, 0x34, 0xF4,
        0x3C, 0xFC, 0xFD, 0x3D, 0xFF, 0x3F, 0x3E, 0xFE, 0xFA, 0x3A,
        0x3B, 0xFB, 0x39, 0xF9, 0xF8, 0x38, 0x28, 0xE8, 0xE9, 0x29,
        0xEB, 0x2B, 0x2A, 0xEA, 0xEE, 0x2E, 0x2F, 0xEF, 0x2D, 0xED,
        0xEC, 0x2C, 0xE4, 0x24, 0x25, 0xE5, 0x27, 0xE7, 0xE6, 0x26,
        0x22, 0xE2, 0xE3, 0x23, 0xE1, 0x21, 0x20, 0xE0, 0xA0, 0x60,
        0x61, 0xA1, 0x63, 0xA3, 0xA2, 0x62, 0x66, 0xA6, 0xA7, 0x67,
        0xA5, 0x65, 0x64, 0xA4, 0x6C, 0xAC, 0xAD, 0x6D, 0xAF, 0x6F,
        0x6E, 0xAE, 0xAA, 0x6A, 0x6B, 0xAB, 0x69, 0xA9, 0xA8, 0x68,
        0x78, 0xB8, 0xB9, 0x79, 0xBB, 0x7B, 0x7A, 0xBA, 0xBE, 0x7E,
        0x7F, 0xBF, 0x7D, 0xBD, 0xBC, 0x7C, 0xB4, 0x74, 0x75, 0xB5,
        0x77, 0xB7, 0xB6, 0x76, 0x72, 0xB2, 0xB3, 0x73, 0xB1, 0x71,
        0x70, 0xB0, 0x50, 0x90, 0x91, 0x51, 0x93, 0x53, 0x52, 0x92,
        0x96, 0x56, 0x57, 0x97, 0x55, 0x95, 0x94, 0x54, 0x9C, 0x5C,
        0x5D, 0x9D, 0x5F, 0x9F, 0x9E, 0x5E, 0x5A, 0x9A, 0x9B, 0x5B,
        0x99, 0x59, 0x58, 0x98, 0x88, 0x48, 0x49, 0x89, 0x4B, 0x8B,
        0x8A, 0x4A, 0x4E, 0x8E, 0x8F, 0x4F, 0x8D, 0x4D, 0x4C, 0x8C,
        0x44, 0x84, 0x85, 0x45, 0x87, 0x47, 0x46, 0x86, 0x82, 0x42,
        0x43, 0x83, 0x41, 0x81, 0x80, 0x40 ]

distance_names=["6 FEET",
                "8 FEET",
                "10 FEET",
                "12 FEET",
                "15 FEET",
                "20 FEET",
                "MIRROR CHART"]

language_names=[" ARABIC  ",
                " BENGALI ",
                "GUJARATHI",
                "  HINDI  ",
                " KANNADA ",
                "MALAYALAM",
                "  ORIYA  ",
                " PUNJABI ",
                "  TAMIL  ",
                " TELUGU  ",
                "  URDU   " ]
#variables for AB6

ab6_mode = MODE_WELCOME
ab6_distance = DIST_10
ab6_distance_temp = DIST_10
ab6_language = LANG_TAMIL
ab6_language1 = LANG_TAMIL
ab6_language2 = LANG_HINDI
ab6_random_number = 1
ab6_base_dir ="/AB6"
ab6_file_name = "MyFileName"
ab6_file_type = BMP
ab6_chart_no = 1
ab6_chart_type = CHART_COMPANY_INFO
ab6_ctype = CHART_COMPANY_INFO
ab6_prev_ctype = CHART_COMPANY_INFO
ab6_flag=0

AB6_VIDEO= 0
AB6_PICTURE=1
AB6_MUSIC=2
AB6_CANCEL=3

ab6_media_type = AB6_VIDEO
#ab6_usb_status=0
ab6_group_no = 0
ab6_buzzer_enable =1
button_code=0

#s="0123456"
out_buff=bytearray(7)
in_buff=bytearray(7)

rnd_code1=0x00
rnd_code2=0x00
crc_lo =0x00
crc_hi =0x00
fontsize1='font14'

running =1
screen_saver_flag=0
screen_saver_min=0
screen_saver_sec=0



ser=serial.Serial('/dev/ttyAMA0',115200, timeout=0.1)

image_file='/storage/.kodi/addons/script.example/resource/19/COMMON/CO_INFO/1.bmp'
image_screen =xbmcgui.ControlImage(0,0,1280,720,image_file)
image_tick =xbmcgui.ControlImage(0,0,85,50,'/storage/.kodi/addons/script.example/resource/19/COMMON/SYSTEM/tick.bmp')

txt_distance=xbmcgui.ControlLabel(20,580,500,50,"Distance",font=fontsize1, textColor="0xFFFF0000")
txt_language1=xbmcgui.ControlLabel(20,610,500,30,"Language 1",font=fontsize1, textColor="0xFFFF0000")
txt_language2=xbmcgui.ControlLabel(20,640,500,30,"Language 2",font=fontsize1,textColor="0xFFFF0000")
txt_language_msg=xbmcgui.ControlLabel(470,620,700,20,"TAMIL set for key L1",font=fontsize1,textColor="0xFFFF0000")
txt_language_name=xbmcgui.ControlLabel(0,0,500,75,"TAMIL ",font=fontsize1,textColor="0xff040404")
txt_screen_saver=xbmcgui.ControlLabel(0,0,500,75,"Screen Saver",font=fontsize1,textColor="0xFFFF0000")

#thread.start_new_thread(serial_thread,('',))

class MyWindow(xbmcgui.Window):
    global image_file
    global button_code
    global image_screen
    global ab6_flag

    def __init__(self):
        self.addControl(image_screen)
        self.addControl(image_tick)
        self.addControl(txt_distance)
        self.addControl(txt_language1)
        self.addControl(txt_language2)
        self.addControl(txt_language_msg)
        self.addControl(txt_language_name)
        self.addControl(txt_screen_saver)

        image_tick.setVisible(False)
        txt_distance.setVisible(False)
        txt_distance.setVisible(False)
        txt_language1.setVisible(False)
        txt_language2.setVisible(False)
        txt_language_msg.setVisible(False)
        txt_language_name.setVisible(False)
        txt_screen_saver.setVisible(False)

        #ser.write('Starting Vision Chart Script')
        self.Init_config()
        self.operate_buzzer(1)
        self.serial_thread()
        self.display_routine()
#       thread.start_new_thread(self.serial_thread,('sass',2))
####################################################################
    def onAction(self,action):
        global ab6_mode

#       xbmcgui.Dialog().ok("On Focusw"," "," "," ")
        if ab6_mode==MODE_USB_PLAY:
           xbmc.executebuiltin("PlayerControl(Stop)")
           ab6_mode=MODE_USB_MENU

####################################################################
# handle an event sent by the GUI
    def MyonAction(self,action):
         global ab6_mode
         global ab6_distance
         global ab6_distance_temp
         global ab6_language
         global ab6_language1
         global ab6_language2
         global ab6_random_number
         global ab6_base_dir
         global ab6_file_name
         global ab6_file_type
         global ab6_chart_no
         global ab6_chart_type
         global ab6_ctype
         global ab6_prev_ctype
         global ab6_group_no
         global ab6_buzzer_enable
         global button_code
         global ab6_flag
         global ab6_media_type

         command= 0
         buzzer = 0
         call_display = 0
#         command=action
         button_code=action #.getButtonCode(self)
#         xbmcgui.Dialog().ok("Button Code",str(button_code)," "," ")

         if(ab6_buzzer_enable==1):
             self.operate_buzzer(1)

         if button_code == KEY_3_MUTEBUZZER:
            #enable/disable buzzer
             if ab6_buzzer_enable == 1:
	         ab6_buzzer_enable=0
	     else:
	         ab6_buzzer_enable=1
         elif ab6_mode == MODE_STANDBY:
             ab6_mode = MODE_WELCOME
             ab6_chart_type = CHART_COMPANY_INFO
             call_display=1

         elif (ab6_mode == MODE_WELCOME or ab6_mode == MODE_CHART):
            if button_code == KEY_1_COMPANYINFO:
                ab6_mode=MODE_WELCOME
            call_display=self.ksr_welcome_chart(button_code)

    	 elif ab6_mode == MODE_CHART_DIST_MENU:
             if button_code == KEY_DOWN_PREV:
                 if ab6_distance_temp >= DIST_MAX:
                     ab6_distance_temp=DIST_MIN
                 else:
                     ab6_distance_temp+=1
             if button_code == KEY_MENU_OK:
                ab6_distance=ab6_distance_temp
                time.sleep(0.2)
                #self.write_eeprom_data(1,ab6_distance)
		#########################################################################################
		file_one = open("/storage/.kodi/distance.txt","w")
                data_distance = str(ab6_distance)
                file_one.write(data_distance)
                file_one.close()
		#########################################################################################
                time.sleep(0.2)
                #SDL_Delay(400)
                ab6_mode=MODE_CHART
                ab6_chart_no=1
                image_tick.setVisible(False)
             if button_code == KEY_UP_NEXT:
                if ab6_distance_temp<=DIST_MIN:
                    ab6_distance_temp=DIST_MAX
                else:
                    ab6_distance_temp-=1
             call_display=1
         elif ab6_mode == MODE_CHART_GROUP_MENU:
             if button_code == KEY_DOWN_PREV:
                 if ab6_group_no>=GROUP_MAX:
               	     ab6_group_no=GROUP_MIN
                 else:
              	     ab6_group_no+=1
                 call_display=1
             elif button_code == KEY_MENU_OK:
                  ab6_chart_type=CHART_EDUCATION
                  ab6_mode=MODE_CHART
                  ab6_chart_no=1
                  image_tick.setVisible(False)
                  call_display=1
             elif button_code == KEY_LEFT_EDUCATIONAL:
                  ab6_chart_type=CHART_EDUCATION
                  ab6_mode=MODE_CHART
                  image_tick.setVisible(False)
                  ab6_chart_no=1
                  call_display=1
             elif  button_code ==KEY_UP_NEXT:
                 if ab6_group_no <= GROUP_MIN:
             	     ab6_group_no=GROUP_MAX
                 else:
                     ab6_group_no-=1
                 call_display=1
             elif button_code==KEY_TVAV_CHARTUSB:
                 call_display=0
             else:
                 ab6_mode=MODE_CHART
                 image_tick.setVisible(False)
                 call_display=self.ksr_welcome_chart(button_code)

         elif ab6_mode==MODE_USB_MENU:
             if button_code == KEY_LEFT_EDUCATIONAL:
                 if ab6_media_type==AB6_VIDEO:
                    ab6_media_type=AB6_MUSIC
                 else:
                    ab6_media_type-=1
                 call_display=1
             elif button_code==KEY_RIGHT_MENU:
                 if ab6_media_type==AB6_MUSIC:
                    ab6_media_type=AB6_VIDEO
                 else:
                    ab6_media_type+=1
                 call_display=1
             elif  button_code ==KEY_UP_NEXT:
                 ab6_media_type=AB6_VIDEO
                 call_display=1
             elif button_code == KEY_DOWN_PREV:
                 ab6_media_type=AB6_CANCEL
                 call_display=1
             elif button_code==KEY_MENU_OK:
                 if ab6_media_type==AB6_VIDEO:
                      xbmc.executebuiltin("ActivateWindow(Videos)")
                      ab6_mode=MODE_USB_PLAY
                 elif ab6_media_type==AB6_PICTURE:
                      xbmc.executebuiltin("ActivateWindow(Pictures)")
                      ab6_mode=MODE_USB_PLAY
                 elif ab6_media_type==AB6_MUSIC:
                      xbmc.executebuiltin("ActivateWindow(Music)")
                      ab6_mode=MODE_USB_PLAY
                 elif ab6_media_type==AB6_CANCEL:
                      ab6_mode=MODE_CHART
                 call_display=1
             elif button_code == KEY_TVAV_CHARTUSB:
                 ab6_mode=MODE_CHART
                 call_display=1


         if call_display <> 0 :
             self.display_routine()
	 else:
             time.sleep(0.3)
             if(ab6_buzzer_enable==1):
                  self.operate_buzzer(0)
#         xbmcgui.Dialog().ok("ab6_flag@handler",str(ab6_flag)," "," ")
         ab6_flag=0

#############################################################################

    def ksr_welcome_chart(self, key):
        global ab6_mode
        global ab6_distance
        global ab6_distance_temp
        global ab6_language
        global ab6_language1
        global ab6_language2
        global ab6_random_number
        global ab6_base_dir
        global ab6_file_name
        global ab6_file_type
        global ab6_chart_no
        global ab6_chart_type
        global ab6_ctype
        global ab6_prev_ctype
        global ab6_group_no
        global ab6_buzzer_enable
        global ab6_media_type
        global screen_saver_min
        max_chart_no=0
        sindex=0

        ab6_prev_ctype = ab6_ctype
        ab6_ctype = keycode_to_charttype[key]

        if ab6_ctype < 0 : # key has special function in this mode
            if key == KEY_POWER_POWER:
                ab6_mode=MODE_STANDBY
                #running=0
                #time.sleep(0.3)
                #ser.close()
                #xbmc.executebuiltin("Action(Back)")
                #self.close()
                #ab6_mode=MODE_STANDBY
                #time.sleep(1)
            elif key == KEY_TVAV_CHARTUSB:
                ab6_mode=MODE_USB_MENU
                ab6_media_type=AB6_VIDEO

            elif key == KEY_UP_NEXT:
                sindex=sub_index[ab6_chart_type][ab6_distance]
                if chart_property[ab6_chart_type][1] ==1:  # sub group for educationl chart
                    sindex+=ab6_group_no;
                    max_chart_no=max_sub_chart[sindex][ab6_distance]
                 # to check Language dependancy of chart type
 		elif chart_property[ab6_chart_type][2]==1 :
                    sindex+=ab6_language;
                    max_chart_no=max_sub_chart[sindex][ab6_distance]
                # to check random dependancy of chart type
                elif chart_property[ab6_chart_type][3]==1:
                   #ab6_random_number=random.randint(1,3)
                    sindex+=ab6_random_number
                    max_chart_no=max_sub_chart[sindex][ab6_distance]
                else:
                    max_chart_no=max_chart[ab6_chart_type][ab6_distance]
                if ab6_chart_no<max_chart_no:
                    ab6_chart_no+=1
                   # xbmc.executebuiltin("Action(NextPicture)")
                else:
                    return 0
#                return 0
            elif key == KEY_DOWN_PREV:
                if ab6_chart_no>1 :
                    ab6_chart_no-=1
                   # xbmc.executebuiltin("Action(PreviousPicture)")
                else:
                    return 0
#                return 0
            elif key == KEY_LEFT_EDUCATIONAL:
                ab6_mode=MODE_CHART_GROUP_MENU
            elif key == KEY_RIGHT_MENU:
                if ab6_chart_type==CHART_COMPANY_INFO: # if the chart type is welcome screen you can change the distance
                    ab6_mode=MODE_CHART_DIST_MENU
                    ab6_distance_temp=ab6_distance
                elif (ab6_chart_type==CHART_LANGUAGE1 or ab6_chart_type==CHART_LANGUAGE2) :
                    # in other chart modes the key works for language selection
                    if ab6_language >= LANG_MAX:
                        ab6_language=LANG_MIN
                    else:
                        ab6_language+=1
            elif key == KEY_MENU_OK:
                # to strore the language numbers for L1 and L2 if the previous key was L1 or L2
                if ab6_chart_type==CHART_LANGUAGE1:
                    txt_language_msg.setLabel(' L1 key assigned with ' + language_names[ab6_language])
                    txt_language_msg.setVisible(True)
                    time.sleep(0.6)
                    if ab6_language1!=ab6_language:
                        ab6_language1=ab6_language
                        #self.write_eeprom_data(2,ab6_language1)

			#############################################################################
			file_two = open("/storage/.kodi/language_one.txt","w")
			data_language_one = str(ab6_language1)
			file_two.write(data_language_one)
			file_two.close()
		#############################################################################
                    time.sleep(0.6)
                    txt_language_msg.setVisible(False)
                    #strcpy(temp,language_names[ab6_language]);
                    #   sprintf(var," L1 key assigned with ");
                    #   strcat(var,temp);
                    #   printf_SDL_TTF(100,650,var,0);
                    #	SDL_Delay(1400);

                if ab6_chart_type==CHART_LANGUAGE2:
                    txt_language_msg.setLabel(' L2 key assigned with ' + language_names[ab6_language])
                    txt_language_msg.setVisible(True)
                    time.sleep(0.6)
                    if ab6_language2!=ab6_language:
                        ab6_language2=ab6_language
             	        #self.write_eeprom_data(3,ab6_language2)


			############################################################################################
			file_three = open("/storage/.kodi/language_two.txt","w")
                        data_language_two = str(ab6_language2)
                        file_three.write(data_language_two)
                        file_three.close()
		##################################################################################################
                    time.sleep(0.6)
                    txt_language_msg.setVisible(False)
                    #strcpy(temp,language_names[ab6_ xbmcgui.Dialog().ok("Serial Thread",str(n),str(ord(in_buff[0])) ,"")language]);
                    #sprintf(var," L2 key assigned with ");
                    #strcat(var,temp);
                    #printf_SDL_TTF(100,650,var,0);
                    #SDL_Delay(1400);
                if ab6_chart_type==CHART_PROD_INFO:
                    screen_saver_min=30


        else:  # key has chart function in this mode
           ab6_chart_no=1;
           ab6_chart_type=ab6_ctype;
           #check if the L! key is pressed consecutively
           #if yes increase language
           if ab6_chart_type==CHART_LANGUAGE1:
               ab6_language=ab6_language1
           # for L2
           if ab6_chart_type==CHART_LANGUAGE2:
                ab6_language=ab6_language2
        return 1
 ########################################################################

    def display_routine(self):
        global ab6_mode
        global ab6_distance
        global ab6_distance_temp
        global ab6_language
        global ab6_language1
        global ab6_language2
        global ab6_random_number
        global ab6_base_dir
        global ab6_file_name
        global ab6_file_type
        global ab6_chart_no
        global ab6_chart_type
        global ab6_ctype
        global ab6_prev_ctype
        global ab6_group_no
        global ab6_buzzer_enable
        global image_file
        global image_screen
        global ab6_media_type

        base_dir_buff='/storage/.kodi/addons/script.example/resource/19'
        dist_dir_buff ="COMMON" #/COMMON,/8FEEt
        chart_type_buff="EDUCATION" #// /EDUCATION , /SNELLLAN
        sub_dir_buff="CATARACT"#  //  /CATARACT     /TAMIL
        file_name_buff="1" # // 1 , 2
        file_ext_buff=".jpg" #; //.jpg , .bmp
        temp='/storage/.kodi/addons/script_example/resources/'
        #char str1[25]="";
        #char str2[25]="";
 	sub_chart=0
        #int  max_chart_no;
        #int sindex;
        #int count,x,y;

        txt_language_name.setVisible(False)
        txt_distance.setVisible(False)
        txt_language1.setVisible(False)
        txt_language2.setVisible(False)


        if (ab6_mode == MODE_WELCOME or  ab6_mode == MODE_CHART):
            if chart_property[ab6_chart_type][0]==1:
                dist_dir_buff=dir_distance[ab6_distance+1] # adds DISTANCE string
            else:
                dist_dir_buff=dir_distance[0] # adds "COMMON" or DISTANCE string

            chart_type_buff=dir_chart_type[ab6_chart_type]  # adds chart type folder name

            #to check the sub folder prperty and add the sub folder to dir string
            if chart_property[ab6_chart_type][1]==1: #group in educational chart
                sub_chart= (sub_index[ab6_chart_type][ab6_distance])+ab6_group_no
                sub_dir_buff=dir_sub_chart[sub_chart]
            #to check Language dependancy of chart type
 	    elif chart_property[ab6_chart_type][2]==1:
                sub_chart= (sub_index[ab6_chart_type][ab6_distance])+ab6_language
                sub_dir_buff=dir_sub_chart[sub_chart]
            #to check random dependancy of chart type
            elif chart_property[ab6_chart_type][3]==1:
                ab6_random_number=random.randint(0,2)
                sub_chart= (sub_index[ab6_chart_type][ab6_distance])+ab6_random_number
                sub_dir_buff=dir_sub_chart[sub_chart]
            else:
                sub_dir_buff=''

            #to add chart number to string
            file_name_buff=str(ab6_chart_no)

            #to get the chart type
            ab6_file_type = chart_property[ab6_chart_type][4]
            if ab6_file_type==JPG:
                file_ext_buff=".jpg"
            else:
                file_ext_buff=".bmp"

            image_file=base_dir_buff+dist_dir_buff+chart_type_buff+sub_dir_buff+'/'+file_name_buff+file_ext_buff
            image_dir=base_dir_buff+dist_dir_buff+chart_type_buff+sub_dir_buff+'/'
            #DisplayImageFile(2,temp);

            image_screen.setImage(image_file)

            if  ab6_chart_type==CHART_LANGUAGE1 or ab6_chart_type==CHART_LANGUAGE2 :
                txt_language_name.setLabel(language_names[ab6_language])
                txt_language_name.setPosition(560,680)
                txt_language_name.setVisible(True)
            	#strcpy(str1,language_names[ab6_language]);
            	#printf_SDL_TTF(500,680,str1,3)
            else:
                txt_language_name.setVisible(False)

            if ab6_chart_type==CHART_COMPANY_INFO:
                txt_distance.setLabel("Distance   : " + distance_names[ab6_distance])
                txt_distance.setVisible(True)
                #strcpy(str1,distance_names[ab6_distance]);
                #sprintf(str2,"Distance   : ");
                #strcat(str2,str1);
                #printf_SDL_TTF(10,640,str2,0);

                txt_language1.setLabel('Language 1:' + language_names[ab6_language1])
                txt_language1.setVisible(True)
                #strcpy(str1,language_names[ab6_language1]);
                #sprintf(str2,"Language 1: ");
                #strcat(str2,str1);
                #printf_SDL_TTF(10,680,str2,0);

                txt_language2.setLabel('Language 2:' + language_names[ab6_language2])
                txt_language2.setVisible(True)
                #strcpy(str1,language_names[ab6_language2]);
                #sprintf(str2,"Language 2: ");
                #strcat(str2,str1);
                #printf_SDL_TTF(10,720,str2,0);
                #break ;
            else:
                txt_distance.setVisible(False)
                txt_language1.setVisible(False)
                txt_language2.setVisible(False)


        elif ab6_mode== MODE_CHART_DIST_MENU :
            image_file='/storage/.kodi/addons/script.example/resource/19/COMMON/SYSTEM/dist_menu.jpg'
            image_screen.setImage(image_file)
            image_tick.setPosition(920,140+(ab6_distance_temp*84))
            image_tick.setVisible(True)
        elif ab6_mode == MODE_CHART_GROUP_MENU :
            image_file='/storage/.kodi/addons/script.example/resource/19/COMMON/SYSTEM/group_menu.jpg'
            image_screen.setImage(image_file)
            image_tick.setPosition(907,163+(ab6_group_no*84))
            image_tick.setVisible(True)
            #DisplayImageFile(2,"/AB6/COMMON/SYSTEM/group_menu.jpg");
            #LoadBmp("/COMMON/SYSTEM/tick.bmp",726,163+(ab6_group_no*84));
        elif ab6_mode == MODE_STANDBY:
            image_file='/storage/.kodi/addons/script.example/resource/19/COMMON/SYSTEM/blankscreen.bmp'
            #DisplayImageFile(2,"/AB6/COMMON/SYSTEM/blank_screen.jpg");
            image_screen.setImage(image_file)
        elif ab6_mode==MODE_USB_MENU:
 #           xbmc.executebuiltin("PlayerControl(Stop)")
            if ab6_media_type==AB6_VIDEO:
                image_file='/storage/.kodi/addons/script.example/resource/19/COMMON/SYSTEM/video_select.jpg'
            elif ab6_media_type==AB6_PICTURE:
                image_file='/storage/.kodi/addons/script.example/resource/19/COMMON/SYSTEM/picture_select.jpg'
            elif ab6_media_type==AB6_MUSIC:
                image_file='/storage/.kodi/addons/script.example/resource/19/COMMON/SYSTEM/music_select.jpg'
            elif ab6_media_type==AB6_CANCEL:
                image_file='/storage/.kodi/addons/script.example/resource/19/COMMON/SYSTEM/cancel_select.jpg'
            image_screen.setImage(image_file)

        #xbmcgui.Dialog().ok("Button Code",str(ab6_chart_type),str(ab6_random_number),sub_dir_buff)

######################################################################

    def read_eeprom_data(self,  address):
       	ret =0
	n=0
	global out_buff
	global in_buff
        global rnd_code1
        global rnd_code2
        global crc_lo
        global crc_hi

	out_buff[0]=0x5A
        out_buff[1]=rnd_code1
	out_buff[2]=0x02  # read command
	out_buff[3]=address   # address of data
	out_buff[4]=0x00
	out_buff[5]=rnd_code2
	out_buff[6]=0xA5

	ser.flushInput()
        ret = ser.write(out_buff)

	time.sleep(0.3)
	#read back data
	in_buff = ser.read(7)
        n=len(in_buff)


	if (n==7 and ord(in_buff[0])==0x5A and ord(in_buff[6])==0xA5 and ord(in_buff[2])==0x62):
	     ret= ord(in_buff[4])
             return ret
	return 0xff

################################################################
    def write_eeprom_data(self,address, data):
        ret =0
	n=0
	global out_buff
        global in_buff

	out_buff[0]=0x5A
	out_buff[1]=rnd_code1
	out_buff[2]=0x03 # Write command
	out_buff[3]=address # address of data
	out_buff[4]=data
	out_buff[5]=rnd_code2
	out_buff[6]=0xA5

	ser.flushInput()
	ret = ser.write(out_buff)

	time.sleep(0.5)
	#read back data
	in_buff = ser.read(7)

	if (n==7 and ord(in_buff[0])==0x5A and ord(in_buff[6])==0xA5 and ord(in_buff[2])==0x63 and ord(in_buff[4])==data):
#	# check crc values of the received bytes
             return 0
	return 0xff
##############################################################################
    def operate_buzzer(self,  duration): # duration 0-Short beep 1-Long beep
        ret =0
        n=0
        global out_buff
        global in_buff
        global rnd_code1
        global rnd_code2

        out_buff[0]=0x5A
        out_buff[1]=rnd_code1
        if duration==1:
            out_buff[2]=0x04  # read command
        else:
            out_buff[2]=0x05
        out_buff[3]=duration   # address of data
        out_buff[4]=0x00
        out_buff[5]=rnd_code2
        out_buff[6]=0xA5

        ret = ser.write(out_buff)
#########################################################################

    def Init_config(self):
	ret =0
	n=0
	global out_buff
        global in_buff
	read_data=0
        global rnd_code1
        global rnd_code2
        global ab6_distance
        global ab6_language1
        global ab6_language2
	
#	read_data=self.read_eeprom_data(1)
	
#	read_distance = open('/storage/.kodi/distance.txt',r')
#	read_distance_data = read_distance.read(1)
#	read_data = read_distance_data
	#read_distance.close()
#        if (read_data>=DIST_MIN and read_data <=DIST_MAX):
 #           ab6_distance=read_data
#
 #       read_data=self.read_eeprom_data(2)
  #      if(read_data>=LANG_MIN and read_data <=LANG_MAX):
   #         ab6_language1=read_data

    #    read_data=self.read_eeprom_data(3)
     #   if(read_data>=LANG_MIN and read_data <=LANG_MAX):
      #      ab6_language2=read_data

       # ab6_language=ab6_language1

# for initalisation and validation of remote board
        rnd_code1=random.randint(0,255)
        rnd_code2=random.randint(0,255)
#Initialise out buffer with init data
	out_buff[0]=0x5A
	out_buff[1]=rnd_code1
	out_buff[2]=0x01
	out_buff[3]=rnd_code1
	out_buff[4]=rnd_code2
	out_buff[5]=rnd_code2
	out_buff[6]=0xA5


        ser.flushInput()

	ret = ser.write(out_buff)
	time.sleep(0.3)

	in_buff = ser.read(7)
#	time.sleep(0.1)
	n=len(in_buff)
        if n==7:
            rnd_code1=in_buff[0]
            rnd_code2=in_buff[6]

            if ord(in_buff[0])!=0x5A or ord(in_buff[6])!=0xA5 or ord(in_buff[2])!=0x61:
		print "hello"
                #xbmc.executebuiltin("Powerdown")
              #  xbmc.executebuiltin("PlayerControl('Stop')")
        else:
	    print "world"
           # xbmc.executebuiltin("Powerdown")

#	read_data=self.read_eeprom_data(1)

	read_distance = open("/storage/.kodi/distance.txt","r")
	read_distance_data = read_distance.read()
	distance_final = int(read_distance_data)
	if (distance_final>=DIST_MIN and distance_final <=DIST_MAX):
	    ab6_distance=distance_final
	
#	read_data=self.read_eeprom_data(2)
	
	read_language_one = open("/storage/.kodi/language_one.txt","r")
        read_language_one_data = read_language_one.read()
	language_one_final = int(read_language_one_data)
	if(language_one_final>=LANG_MIN and language_one_final <=LANG_MAX):
	    ab6_language1=language_one_final

#	read_data=self.read_eeprom_data(3)
	
	read_language_two = open("/storage/.kodi/language_two.txt","r")
        read_language_two_data = read_language_two.read()
	language_two_final = int(read_language_two_data)
	if(language_two_final>=LANG_MIN and language_two_final <=LANG_MAX):
           ab6_language2=language_two_final

	ab6_language=ab6_language1
	return 0

####################################################################

    def _serial_thread(self):
        global in_buff
        global screen_saver_flag
        global screen_saver_min
        global screen_saver_sec
        command = 0
        global image_file
        global image_screen
        global running
        global ab6_flag
        n=0
        x=0
        y=0

       # xbmcgui.Dialog().ok("Serial Thread1","","","")
        while running==1:
            in_buff = ser.read(1)
            n=len(in_buff)
            #xbmcgui.Dialog().ok("Serial Thread2","","" ,"")
	    if n>0 and ord(in_buff[0])>=0x30 and ord(in_buff[0])<=0x50 :
                #xbmcgui.Dialog().ok("Serial Thread3","","" ,"")
	        if screen_saver_flag==1: # exit the screen saver
	            screen_saver_flag=0
	            screen_saver_min=0
                    txt_screen_saver.setVisible(False)
	            self.display_routine()

	        else:
                    screen_saver_min=0
                    screen_saver_sec=0
                    command=ord(in_buff[0])
                    #xbmcgui.Dialog().ok("ab6_flag@sthread",str(ab6_flag)," "," ")
                    if ab6_flag==0 and ab6_mode!=MODE_USB_PLAY:
                       ab6_flag=1
                       self.MyonAction(command)
	        time.sleep(0.2)
	        ser.flushInput()
	        #stop_buzzer()
	    else:
                #xbmcgui.Dialog().ok("Serial Thread3","","" ,"")
	        time.sleep(0.1)
	        screen_saver_sec+=1
	        if screen_saver_sec>300:

	            screen_saver_min+=1
		    screen_saver_sec=0
	        if screen_saver_min>29:
		    screen_saver_flag=1
		    screen_saver_min=29
                    image_file='/storage/.kodi/addons/script.example/resource/19/COMMON/SYSTEM/blankscreen.bmp'
                    image_screen.setImage(image_file)
                    x=random.randint(0,800)
                    y=random.randint(0,700)
                    txt_screen_saver.setPosition(x,y)
                    txt_screen_saver.setLabel(screen_saver_text)
                    txt_screen_saver.setVisible(True)




    def serial_thread(self):
        threading.Thread(target=self._serial_thread).start()

# store our window as a short variable for easy of use
W = MyWindow()
#thread.start_new_thread(serial_thread,('sass',2))
# run our window we created with our background jpeg image
W.doModal()
# after the window is closed, Destroy it.
del W
