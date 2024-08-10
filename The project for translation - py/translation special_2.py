def replace(string,dictionary):
    words = list(dictionary.keys())
    ##words.sort()
    chap='Chapter '
    #print('len string:',len(string))
    nstring=''
    flag = 0
    if string == '\n' or string == '':
        return None
    i = 0
    while i < len(string):
        #print('checking string,',str(string[i:i+2]),'now')
        if str(string[i:i+2]) == '  ':
            #print('match found at i =',i)
            nstring = ''.join((nstring,' '))
            j = i
            while j in range(len(string)):
                if string[j] == ' ':
                    j += 1
                    continue
                else:
                    break
            #print(j-i,'spaces found and moving to position of',string[j:j+2])
            i = j
        else:
            nstring = ''.join((nstring,str(string[i])))
            i += 1
    string = nstring
    nstring=''
    if chap in string:
        stsw = 0
        i = 0
        while i < len(string):
            #print('i started as',i)
            if string[i] == chap[stsw]:
                #print('match found at',i)
                started = i
                while stsw < len(chap):
                    if chap[stsw] == string[i]:
                        i += 1
                        stsw += 1
                    else:
                        #print('continued only till',i)
                        ended = i
                        stsw = 0
                        break
                if stsw != 0:
                    #print('match success and ended at',i-1)
                    #print('chapter string:',string[started:started+12])
                    nstring = ''.join((nstring,'\n\n'+str(string[started:(started+12)])+'\n\n'))
                    #print(nstring)
                    stsw = 0
                    i += 4
                    flag = 1
                else:
                    nstring = ''.join((nstring,str(string[started:ended+1])))
            else:
                nstring = ''.join((nstring,str(string[i])))
            i += 1
            string = nstring
            if flag == 1:
                break
            
    for word in words:
        nstring=''
        #print('checking word',word,'in string',string)
        if word in string:
            stsw = 0
            i = 0
            while i < len(string):
                if string[i] == word[stsw]:
                    #print('match found at',i)
                    started = i
                    while stsw < len(word):
                        if word[stsw] == string[i]:
                            i += 1
                            stsw += 1
                        else:
                            #print('continued only till',i)
                            ended = i
                            stsw = 0
                            break
                    if stsw != 0:
                        #print('match success and ended at',i-1)
                        nstring = ''.join((nstring,dictionary[word]))
                        stsw = 0
                        i -= 1
                    else:
                        nstring = ''.join((nstring,string[started:ended+1]))
                else:
                    nstring = ''.join((nstring,str(string[i])))
                i += 1
            string = nstring
    #print('returning string',string)
    return string


#doubts ,"Xiantian":"Celestial(?)", "Fu yi":"(?)", "Ma De":"Wow!", "Shenlong island":"", ,"Tongtian":"Golden(?)"
##(” with ")

#  IMP : replace (” with ") in NOTEPAD! the character ” isn't mapped in the decoding somehow

#     "":"",
#names = {"land of the Yaozu seal":"Sealed Beast land","Yaozu Sealed Land":"Sealed Beast Land","wind and turbulence":"Luca guy","wind and waves":"Luca guy","Baofeng":"Storm","Province of the Day":"Province of Sun","Province of Day":"Province of Sun","mountain wind":"Darryl","wind wave":"silly guy","Wangcheng":"Wangche","Ya Lena":"Yalena","Qilin":"Unicorn beast","Dong Shen":"Kevin","Dongshen":"Kevin","Okuyama":"Yama","Lenghuo":"cold flames","Tian Yi":"Terry","Leng Feng":"Leni","McWee":"Mcway","Guangming":"Light","Guangwu":"Raymond","Crescent":"New moon","Fu Zheng":"Ray","Ren Guang":"Eric","Tianzhao":"Amatera","metropolitan":"Sigh(?)..","Hongshang":"Tina","Hong Shang":"Tina","Hong Chang":"Tina","air- conditioning":"cold air","air-conditioning":"cold air","Zhan Chao":"Bill","Fengtao":"Luca Moonlight","Mingyue":"Moonlight","Hu Mingyue":"Luca Moonlight","Feng Tao":"Danny","Manxiong":"Barbarian","Man Xiong":"Barbarian", "one-eyed":"Cyclop","one eyed":"Cyclop","Sky Open Axe":"Sky-Breaking Axe", "Heavenly Axe":"Sky-Breaking Axe","Qianshui":"Repulse", "Duchy":"Province","duchy":"Province", "Ma De":"Huh(?)","sky-Opening":"Sky-Breaking","Tongshen":"heaven cult","Heaven-Opening":"Sky-Breaking","Deng":"Bang!","Long Qianying":"Alice","Nanyun":"South cloud","Earth Round":"Earth","Earth-Round":"Earth","Dasheng":"Dax","Nan Yun":"South cloud","Ouyang":"Carter","Amaterasu":"Amatera","Wen liang":"Wengi","Wen Liang":"Wengi","Yuefeng":"Darryl","Xiang'er":"Elen","Xianger":"Elen","Tianmen":"Elysium gate","Xiandi":"Shandy","Hades":"King of the Dead","Fei Yu ":"Birds ","Feiyu":"Birds","Gui Guzi":"Ghost Valley sage","Guiguzi":"Ghost valley sage","Guigu":"Ghost valley sage","Tianque Lingyan":"Vermillion Bird Spirit Fire","Tian Que Ling Yan":"Vermillion Bird Spirit Fire","Lingyan":"Spirit fire","Grand Sage Sun":"Brother Dax","Xuansheng":"Nine Heaven's Profound saint","Qinlong":"Azure Dragon","Bai Qi Shen Array":"Bai Qi Divine Formation","Yi Rong San":"Transformation powder","Jiuzhou":"Universe","eight saints":"eight oracles","Quang Binh":"New world","Tiandaomeng":"Heavenly alliance","Heavenly Dao":"Heavenly","Tiandao":"Heavenly","Nine Heavens Saintess":"Nine oracles","Pluto":"King of the Dead","Daoge":"Doug","Fang Tian's painting":"Heavenly","Venerable":"Marshal","Fang Tian painted":"Heavenly","Pluto's":"Evil","Mae Wei":"Mcway","Maddie":"Mcgrady","Fang Tian's painted":"Heavenly","Made!":"Fuck(?)","inner alchemy":"internal energy","Bai Lian":"White lily","Bailian":"White lily","dantian":"Qi","Dantian":"Qi","Eileen":"Irene","Aileen":"Irene","principalities":"Provinces","call!":"Sigh!","Call!":"Sigh!","Princicipality":"Province","Ai Lin":"Irene","Yanhong":"Bonnie","Kyushu":"World Universe","Provinces":"Mainlands","military master":"Sect master","Nima":"Fuck!","Miao Ying":"Yuri","Miaoying":"Yuri"," Array":" Formation","array":"Formation","Yan Hong":"Bonnie","Heavenly Gate":"Elysium gate(?)","Feng Zi":"brother","Fengzi":"brother","Bing Yao":"Ileana","Bai Xioatian" : "Ewan","Ch6ang'e" : "Empress Chang Er","Changqing" : "Princess Evergreen","Chen Yue" : "Yumi","Co-Workers" : "Gonggong","Duan Feng" : "Zephyr","Duan Yu" : "Donogue","Emperor Tianqi" : "New World Emperor","Erqing" : "Irene","Fang Shixian" : "Robert Box","Fang Ting" : "Tiffany","Fang Zhiqiu" : "Ashley","Gou Shi" : "New World Secretary","Han Aora" : "Aurora","Han Bing" : "Eira","Hu Sanyang" : "Leroy","Ji Linglonog" : "Lindsay","Jiang Shan" : "Susan","King of Guangping" : "Lord Kenny","king of Guangping" : "Lord Kenny","King Guangping" : "Lord Kenny","Quang Bih" : "Lord Kenny","Li Nan" : "Nancy","Li Ruoning" : "Lily's master","Ling XiaoXiao" : "Sonya","Liu Xion" : "Lily","Laona":"Launa","Luo Rita":"Lolita","entourage":"apprentice","Xi Ya":"Thea","Liu Xuan" : "Lily(?)","Jiaolong":"Flood Dragon","great saint Shi":"Dax","Maiwei":"Mcway","Liu Zhi" : "William","Long Qianyu" : "Quincy","Overlord Hammer":"Tyrant Hammer","Long Qian":"Long Quincy","Lu Jiechen" : "Matteo","Lu Lingshan" : "Laura","Meihui" : "Sara","Miaoyuan" : "Serendipity","Mu Xixi" : "Celine","Nangong Jue" : "Sword Devil","Ouyang Jingwen" : "Rachel","Ouyang Zhennan" : "Zoran","Peng Kai" : "Paul","Rei Feifei" : "Ophelia","Ren Yingying" : "Yvette","Yingying":"Yvette","Shen Man" : "Samantha","Shennong" : "Divine Farmer","Sikong Yaran" : "Sister scope","Song Qian" : "Queenie","Sun Dasheng" : "Dax","Yan Chao":"Commodore","Head Sun" : "Dax","Su Qingyan" : "Debra","Zhongzhou":"Donghai(?)","Qingyan" : "Debra","Twelve God Guards" : "Twelve Royal Guards","Qin Shousheng" : "Justin Quin","Xue Peng":"Doni","Nepal Ma!":"fuck!","Ka Lun":"Karen","Xue Mier":"Michelle","Xue Mi'er":"Michelle","Xue Shan":"Douglas","Sheng":"victory","Quin Ronying" : "Monica","Wen Chou Chou" : "Chester","Wen Chouchou" : "Chester","Wen Xiaoyu" : "Neil","Call..":"Sigh..","call..":"Sigh..","Xiaoyu" : "Neil","Wen ":"Chester ","Yan Xiong" : "Sawyer","Yue Chen" : "Florian","Shiqingsan":"Light-weight","Shi Qingsan":"Light-weight stones","Linna":"Olena","Feng Yue":"Darryl","Yue Feng" : "Darryl","Sang Biao":"Judy","Yue Tianlong" : "Drake Darby","Yue Wuya" : "Ambrose","Yue":"Darryl","Xiao Xi" : "Jewel","Xiao Yuruo" : "Yvonne","Xiao Qiongqi's" : "Darryl's Rocky","Xing yao" : "Sloan","Xu Qingyi" : "Shentel Xion","Xue Li" : "Shelly","Ye ziyi" : "Yuanli","Zhang Jiao" : "Zhang Jue"," Wen ":" Chester "," Wen,":" Chester,","Nine Dragons Ascend to Heaven":"Nine dragons heaven ascension","Zhao Lu" : "Jade","Chen Shishi":"Emily","Xia Yinzong":"Xhia Yinzong","Chaos Yangzhu":"Chaotic Yang bead","Chaos Yang Pearl":"Chaotic Yang bead","Chaos Sun Pearl":"Chaotic Yang bead","Zheng Chunqiu" : "Andy","Zhuo Quin" : "Megan"," Xia,":" Thea,","Xia,":"Thea,"," Xia ":" Thea ","Mi'er":"Michelle","Lingfeng":"Pheonix","Qicai":"colorful","Qi Cai":"colorful"}
names={"Daying":"Camp","• ":"-","Co-Working":"Gonggong","Guang Ping Wang":"Lord Kenny","Anthony":"Senior Yutong","Ye Xingjun":"Monarch Yaori","Mccarthy":"Monarch Yaori","Irma":"Ileana","Edward":"Bai Yunfei","Jiuzhou":"Universe","Yutiangong":"Nine Heavens God","Yutian Palace":"Heavenly Palace","Sun Dax":"Dax","King Quang Ping":"Lord Kenny","Weather Palace":"New World Palace","imperial forest troops":"Imperial army troops","Girl Ren":"Girl Debra","How to do?":"What to do?","Princess Tanglin":"Princess Dong Ling","Jiutian God":"Nine Heavens God","God Jiutian":"Nine Heavens God","Kaitian Axe":"Sky-breaking Axe","Liuli Jingshui":"Liuli Purified water","Mu Qingyue":"Diana","Faye Wong":"Fanny Witcham","Heaven and Dao League":"Heavely alliance","Heavenly Dao League":"Heavely alliance","Jianghu Sect":"Main sects","Liu Qingping":"Donna","Fang Qifo":"Fang Mao","pure sun":"Pure yang","victoryzong":"Holy sect","Tang Qingyun":"Watson Tucker","Meng Lang":"Alaric","Meng Ao":"Amastan","Darryl Devil Mountain":"Feng Devil Mountain","Xie liuyun":"Alan","Zhang Na":"Tina(H)","Hai Ling":"heather","Hua Ling":"Lilian Willis","Bai Li":"Clara","Ye Meng":"Melody Yoel","Great Sage":"Dax","great Sage":"Dax","The win d":"Darryl ","the wind ":"Darryl ","Great Breakthrough Technique":"Grand Destruction Art","Yuyao":"Jade","Profound Ye":"Mistlorten","West Cang":"Westrington","Ye Ziyi":"Parker","Dragon! Ascend! Heaven!" : "Ascension of the Nine Dragons","Hellfire":"Hell Flame","Yuan Shen":"Primordial Spirit","Yuanshen":"Primordial Spirit","Ice Soul Cold Needle" : "Ice Needles","Tiangang Swordmanship" : "Celestial Swordmanship","Profound Yin Magic" : "Mysterious Godly Scripture","Xuan Yin Magic" : "Mysterious Godly Scripture","Yin-Yang Qiankun Bag" : "Yin Yang Heaven and Earth Bag","Zixiao Divine Fire" : "Purple Cloud Enchanted Flame","Cuixian Flute":"Jade flute","Bai Yun Frisbee":"Bai Yunfei","land of the Yaozu seal":"Sealed Beast land","Yaozu Sealed Land":"Sealed Beast Land","wind and turbulence":"Luca guy","wind and waves":"Luca guy","Baofeng":"Storm","Province of the Day":"Province of Sun","Province of Day":"Province of Sun","mountain wind":"Darryl","Tianzun":"Luo jue","built ethnic group":"Ancient building","Yulin Army":"New World Army","wind wave":"silly guy","Wangcheng":"Wangche","Ya Lena":"Yalena","Qilin":"Unicorn beast","Dong Shen":"Kevin","Dongshen":"Kevin","Okuyama":"Yama","Lenghuo":"cold flames","Leng Feng":"Leni","McWee":"Mcway","Guangming":"Light","Guangwu":"Raymond","Crescent":"New moon","Fu Zheng":"Ray","Ren Guang":"Eric","Tianzhao":"Amatera","metropolitan":"Sigh..","Haotian Shenjun":"Haotian Sovereign Lord","Hongshang":"Tina","Hong Shang":"Tina","rivers and lakes":"Land and rivers","Hongchang":"Tina","Hong Chang":"Tina","air- conditioning":"cold air","Girl Rhea":"Girl Liya","air-conditioning":"cold air","Zhan Chao":"Bill","Fengtao":"Luca Moonlight","Feng Tao":"Luca Moonlight","Mingyue":"Moonlight","Hu Mingyue":"Luca Moonlight","Feng Tao":"Danny","Manxiong":"Barbarian","Man Xiong":"Barbarian", "one-eyed":"Cyclop","one eyed":"Cyclop","Sky Open Axe":"Sky-Breaking Axe", "Heavenly Axe":"Sky-Breaking Axe","Qianshui":"Repulse", "Duchy":"Province","duchy":"Province", "Ma De":"Huh?","sky-Opening":"Sky-Breaking","Tongshen":"heaven cult","Heaven-Opening":"Sky-Breaking","Deng":"Bang!","Long Qianying":"Alice","Nanyun":"South cloud","Earth Round":"Earth","Earth-Round":"Earth","Sun Dasheng":"Dax","Dasheng":"Dax","Nan Yun":"South cloud","Ouyang":"Carter","Amaterasu":"Amatera","Wen liang":"Wengi","Wen Liang":"Wengi","Yuefeng":"Darryl","Long Xiang'er":"Sheryl","Long Xianger":"Sheryl","Tianmen":"Elysium gate","Xiandi":"Shandy","Hades":"King of the Dead","Fei Yu ":"Birds ","Feiyu":"Birds","Gui Guzi":"Ghost Valley sage","Guiguzi":"Ghost valley sage","Guigu":"Ghost valley sage","Tianque Lingyan":"Vermillion Bird Spirit Fire","Tian Que Ling Yan":"Vermillion Bird Spirit Fire","Lingyan":"Spirit fire","Grand Sage Sun":"Brother Dax","Xuansheng":"Profound saint","Saints of Nine Heavens":"Nine oracles","Saintess of Nine Heavens":"Nine oracles","Nine Heavens Saint":"Nine Oracles","Qinlong":"Azure Dragon","Bai Qi Shen Array":"Bai Qi Divine Formation","Yi Rong San":"Transformation powder","Jiuzhou":"Universe","eight saints":"eight oracles","Quang Binh":"New world","Tiandaomeng":"Heavenly alliance","Heavenly Dao":"Heavenly","Tiandao":"Heavenly","Nine Heavens Saintess":"Nine oracles","Pluto":"King of the Dead","Daoge":"Doug","Fang Tian's painting":"Heavenly","Venerable":"Lord","Fang Tian painted":"Heavenly","Pluto's":"Evil","Mae Wei":"Mcway","Maddie":"Mcgrady","Fang Tian's painted":"Heavenly","Made!":"Fuck(?)","inner alchemy":"internal energy","Bai Lian":"White lily","Bailian":"White lily","dantian":"Spiritual Energy","Dantian":"Spiritual Energy","Eileen":"Irene","Aileen":"Irene","principalities":"Provinces","call!":"Sigh!","Call!":"Sigh!","Princicipality":"Province","Ai Lin":"Irene","Yanhong":"Bonnie","Provinces":"Mainlands","military master":"Sect master","Nima":"Fuck!","Miao Ying":"Yuri","Miaoying":"Yuri"," Array":" Formation","array":"Formation","Yan Hong":"Bonnie","Heavenly Gate":"Elysium gate","Feng Zi":"brother","Fengzi":"brother","Bingyao":"Ileana","Bing Yao":"Ileana","Demon Zun Gone":"Demon Lord","Feng Mo Jing":"Magical mirror","Bai Feng":"White Phoenix","Wudu Sect":"Five Poisons Sect", "Feng Demon Jiang":"Demon Lord","Bai Xioatian" : "Ewan","Chang'e" : "Empress Chang Er","Changqing" : "Princess Evergreen","Chen Yue" : "Yumi","Co-Workers" : "Gonggong","Duan Feng" : "Zephyr","Duan Yu" : "Donogue","Emperor Tianqi" : "New World Emperor","Tianqi" : "New World","Erqing" : "Irene","Fang Shixian" : "Robert Box","Fang Ting" : "Tiffany","Fang Zhiqiu" : "Ashley","Gou Shi" : "New World Secretary","Han Aora" : "Aurora","Han Bing" : "Eira","Hu Sanyang" : "Leroy","Ji Linglonog" : "Lindsay","Li Ruoning":"Celetste Trone","Li Heihu":"Felix","Li Nan":"Nancy","Jiang Shan" : "Susan","Quang Bih":"Lord Kenny","Quang Binh":"Lord Kenny","King of Guangping" : "Lord Kenny","king of Guangping" : "Lord Kenny","Emperor of Tianqi":"Emperor of New world","King Guangping" : "Lord Kenny","Guangping King" : "Lord Kenny","Imperial Forest Army":"Royal new world Army","Royal Forest Army":"Royal new world Army","Quang Bih" : "Lord Kenny","Li Nan" : "Nancy","Li Ruoning" : "Lily's master","Ling XiaoXiao" : "Sonya","Liu Xion" : "Lily","Laona":"Launa","Luo Rita":"Lolita","entourage":"apprentice","Xi Ya":"Thea","Liu Xuan" : "Lily(?)","Jiaolong":"Flood Dragon","great saint Shi":"Dax","Maiwei":"Mcway","Liu Zhi" : "William","Long Qianyu" : "Quincy","Magic Talisman":"Wonder Travel Amulet","Palong Jing":"Dragon Essence","All Thoughts are Ashamed":"Thousand Calamities","Big Ice Dragon Palm":"Icy Dragon Punch","Ling long Pagoda":"Seven Treasures Exquisite Pagoda","Naha King Hammer":"Tyrant Hammer","Overlord's Hammer":"Tyrant Hammer","Overlord Hammer":"Tyrant Hammer","Long Qian":"Long Quincy","Lu Jiechen" : "Matteo","Lu Lingshan" : "Laura","Meihui" : "Sara","Miaoyuan" : "Serendipity","Mu Xixi" : "Celine","Nangong Jue" : "Sword Devil","Ouyang Jingwen" : "Rachel","Ouyang Zhennan" : "Zoran","Peng Kai" : "Paul","Nangong Jue":"Ford","Rei Feifei" : "Ophelia","Ren Yingying" : "Yvette","Yingying":"Yvette","Shen Man" : "Samantha","Shennong" : "Divine Farmer","Sikong Yaran" : "Sister scope","Song Qian" : "Queenie","Sun Dasheng" : "Dax","Yan Chao":"Commodore","Head Sun" : "Dax","Meng Yaxiu":"Mengya","Yaozu's subordinates":"Monster clan subordinates","Miss Ren":"Miss Debra","Bai Tiger":"White Tiger","Yaozu men":"Monster clan men","Yaozu":"Monster","Qingmu Formation":"Wooden Formation","Su Qingyan" : "Debra","Qianyan":"Debra","Zhongzhou":"Donghai(?)","Qingyan" : "Debra","Twelve God Guards" : "Twelve Royal Guards","Shenzong":"Holy Sect altar","Qin Shousheng" : "Justin Quin","Xue Peng":"Doni","Nepal Ma!":"fuck!","Ka Lun":"Karen","Xue Mier":"Michelle","Xue Mi'er":"Michelle","Xue Shan":"Douglas","Sheng":"victory","Quin Ronying" : "Monica","Wen Chou Chou" : "Chester","Wen Chouchou" : "Chester","Wen Xiaoyu" : "Neil","Xiao Yu" : "Neil","Call..":"Sigh..","call..":"Sigh..","Xiaoyu" : "Neil","Wen ":"Chester ","Yan Xiong" : "Sawyer","Yue Chen" : "Florian","Shiqingsan":"Light-weight","Shi Qingsan":"Light-weight stones","Linna":"Olena","Feng Yue":"Darryl","Yue Feng" : "Darryl","Sang Biao":"Judy","Ye Zhixin":"Zoey jehn","Yue Wudi":"Indomitable Darby","Yue Tianlong" : "Drake Darby","Yue Wuya" : "Ambrose","Sun Ting":"Tanya Sunders","Yue,":"Darryl,","Yu Wenyan":"Jackie Yale","Yu Wenyi":"Jasmine Yale","Xiao Xi" : "Jewel","Xiao Yuruo" : "Yvonne","Xiao Qiongqi's" : "Darryl's Rocky","Xing yao" : "Sloan","Xu Qingyi" : "Shentel Xion","SanDuan":"Level 3","SiDan":"Level 4","Wuduan":"Level 5","WuHuang":"Martial Emperor","Crossing the Tribulation Catastrophe":"Heaven Ascension","Apocalyptic World":"New World","Apocalypse Continent":"New World Continent","apocalyptic":"New World","Kwong King Ping":"Lord Kenny","Beiying":"North Moana","North Ying":"North Moana","Bei Ying":"North Moana","Dongao":"Great East","Diyuan":"World Universe","Hall of Longevity":"Eternal Life Sect","longevity hall":"Eternal Life Sect","Huaguosahn":"Flower Mountain Sect","mainland of Kyushu":"Nine Mainlands","Kyushu":"Mainlands","Lingyin Pavilion":"Assassin Sect","Lingyin":"Assassin","Mingjiao":"Incandescent Sect","Tianmen Sect":"Elysium Gate","Cang Shiyue":"Clarice","WIld and Sly Territory":"Deserted realm","Tongtian":"Heaven Cult","Xicang":"Westrington","Xuanye":"Mistloren","Xue Li" : "Shelly","Zi Yan":"Xenia","Ziyan":"Xenia","Ye ziyi" : "Yuanli","Zhang Jiao" : "Zhang Jue"," Wen ":" Chester "," Wen,":" Chester,","Nine Dragons Ascend to Heaven":"Nine dragons heaven ascension","Zhao Lu" : "Jade","Huanxiang":"Yennie","Chen Shishi":"Emily","Xia Yinzong":"Xhia Yinzong","Chaos Yangzhu":"Chaotic Yang bead","Chaos Yang Pearl":"Chaotic Yang bead","Chaos Sun Pearl":"Chaotic Yang bead","Zheng Chunqiu" : "Andy","Zhuo Quin" : "Megan"," Xia,":" Thea,","Xia,":"Thea,","Mi'er":"Michelle","Moroye":"Monl Rama","Lingfeng":"Pheonix","Qicai":"colorful","Qi Cai":"colorful","Bai Ma":"White Horse"," Mona ":" Natalie ","Mona ":"Natalie ","Long Zang":"Hidden Dragon"," Jed":" Jake","Xianyuan":"Immortal garden","Brother Wen":"Brother Chester","Gudong":"Gulp","Pure Sun":"Pure Yang","Demon Zun Gone":"Demon Lord","Demon Zun Goni":"Demon Lord","Jiutian":"Nine heavens","Jiu Tian":"Nine heavens","Tanglin ":"Dong Ling ","The horse":"Prince Consort","the horse":"Prince Consort","Wenzong":"Artemis Sect","Jade Dragon Cohort":"Prince Consort","Meng Yatian":"Mengya","Guangping":"Lord Kenny","Baihu King":"Beast king","King Baihu":"Beast king","I go!":"What?1","Seven-Colored Lingfeng":"Colorful phoenix","Baihu King":"Beast king","Princess Sally":"Princess Dong Ling","Rodolf":"Gong Ao","Baihu clan":"Beast clan","Jade Dragon Manhorse":"Jade Dragon consort","Baihu Wang":"Beast King","Snapped!":"Snap!","Yutong Xianweng":"Senior Yutong","cal l":"Sigh"}

while 1==1:
    file_name = input("\nEnter the name of the file without .txt : ")
    g = open(file_name+'_.txt',"w+")
    with open(file_name+'.txt') as f:
        contents = f.readlines()
    for content in contents:
        #print(content)
##        for i in range(len(content)):
##            if content[i]==' ':
##                continue
##            else:
##                content=content[i:len(content)]
##                break
        content=content[15:len(content)]
        if replace(content,names) is not None: g.write('\n' + replace(content,names))
        
    
    g.close()
    f.close()
    
    print('translation finished')


##string = 'Adhil has  a   goat and     cat .'
##print(replace(string,names))
      

  
