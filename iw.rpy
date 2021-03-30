label start_iw:
    $ prolog_time()
    $ persistent.sprite_time = "day"
    scene bg black with dissolve
    
    ### дляТЕСТОВ
    
        
    
    ### /дляТЕСТОВ
    
    $ set_mode_nvl()
    "{i}Существует теория, что Вселенная бесконечна,{/i}"
    "{i}а потому в ней должны быть копии нашей планеты.{/i}"
    "{i}Вы только представьте: летел космический корабль{/i}"
    "{i}миллионы световых лет в поисках другой цивилизации…{/i}"
    "{i}и уткнулся в Мытищи.{/i}"
    window hide
    $ day_time()
    $ backdrop = "days"
    $ new_chapter(1, u"Прибытие")
    play music music_list["no_tresspassing"]
    scene bg ext_bus with flash
    $ set_mode_adv()
    window show
    "Я вышел из автобуса и осмотрелся."
    
    "Небо здесь было низкое и какое-то твёрдое, без этой легкомысленной прозрачности, намекающей на бездонность космоса — настоящая библейская твердь, гладкая и непроницаемая."
    "И твердь эта несомненно опиралась на могучие плечи местного Атланта."

    "Воздух был горячий и густой, пахло пылью, старым железом, раздавленной зеленью, жизнью."
    "Трава была по пояс, неподалёку темнели заросли кустарника, торчали кое-как унылые кривоватые деревья."

    "Автобус стоял на дне огромной котловины с пологими склонами; местность вокруг заметно поднималась к размытому неясному горизонту, и это было странно, потому что где-то рядом текла река, большая и спокойная, текла на запад, вверх по склону котловины."

    sv "Мало того, что из зимы попал в лето, так и местность ещё странная"

    window hide    
    scene bg ext_camp_entrance_day with dissolve2
    window show
    sv "И что это за пионерлагерь “Совёнок”?{w} Откуда здесь пережиток далёких социалистических времён?{w} И ведь не скажешь, что заброшен"

    window hide
    play ambience ambience_camp_entrance_day
    play sound sfx_suspence_bang
    show dv_s normal pioneer at center with hpunch
    stop music
    window show
    dvp "Привет!{w} Ты, наверное, новенький?"
    
    "Я недолго постоял в раздумьях и решился-таки осторожно перейти к контакту четвёртой степени:"

    me "Ну… наверное."

    sv "Мало ли, куда меня занесло. Может, уже и планета совсем другая, и я тут общаюсь с некоей кремнийорганической формой жизни"

    "Впрочем, внешне девушка ничем не отличалась от обыкновенных людей."

    show dv_s smile with dissolve
    dvp "О! Это замечательно! Добро пожаловать в пионерлагерь «Совёнок»."
    dvp "От лица всего нашего дружного коллектива ребят, вожатых и обслуживающего персонала приветствую тебя!"
    
    show dv_s grin with dissolve
    dvp "Надеюсь, тебе у нас понравится!{w} Моё имя Славяна! Но все меня Славя зовут. И ты тоже зови."

    me "Хорошо. Буду звать."

    show dv_s normal with dissolve
    sv "Надеюсь, вскоре я проснусь, и никого звать уже не понадобится. Как там в Винни-Пухе: как позвать Слонопотама? Идёт ли он на свист и если идёт, то зачем?"

    me "Э-э-э… да… А меня Семён зовут. И ты тоже зови… Если понадоблюсь."
    
    show dv_s smile with dissolve

    "Я почесал затылок."

    sv "Абсурдная ситуация, абсурдные мысли. Какой-то лагерь, пионеры, Славяны…"

    show sl_e4 serious pioneer at right with hpunch
    show dv_s shocked:
        ease 1 xpos 0.2
        
    slp "Алиса? Что ты тут делаешь?"

    show dv_s surprise with dissolve
    dvp "Не слушай её! Она перепутала! Я — Славяна!"

    show sl_e4 surprise with dissolve
    slp "Что значит ты — Славяна? А я тогда кто?"
    
    show dv_s normal:
        ease 0.5 xpos 0.3    
    play music music_list["eat_some_trouble"] fadein 2
    slf "Откуда я знаю? Возможно, ты — Лена."
    
    show dv_s laugh with dissolve
    slf "И вообще, кто первый, тот и Славяна!"

    show sl_e4 serious with dissolve
    sls "Не обращай внимания, Алиса шутит. Она у нас выдумщица и хулиганка."
    "Обратилась Славя Номер Два уже ко мне."
    
    show dv_s normal with dissolve
    
    show sl_e4 shy close:
        ease 1 xpos 0.6
    "Она подхватила меня под руку и прижалась так, что я почувствовал мягкость её груди."
    sls "И лучше держись от неё подальше. От таких, сам понимаешь, ничего хорошего не жди."

    show sl_e4 smile pioneer at cright with ease
    
    "Потом немного отстранилась и продолжила уже громче:"
    sls "Сейчас я провожу тебя к вожатой.{w} Как доехал?"

    sv "Что здесь творится?"

    show dv_s normal:
        ease 0.5 xpos 0.4    
    "Славя Номер Один схватила меня за другую руку и потянула к себе."
    slf "Нет, я провожу!"

    show sl_e4 serious:
        ease 0.5 xpos 0.6
    sls "..."
    
    window hide
    show dv_s normal:
        ease 0.7 xpos 0.2
    show sl_e4 serious with hpunch:
        ease 0.7 xpos 0.5
    $ renpy.pause(0.5, hard=True)
    
    show sl_e4 serious:
        ease 0.7 xpos 0.8
    show dv_s normal with hpunch:
        ease 0.7 xpos 0.5
    $ renpy.pause(0.5, hard=True)
    
    show dv_s angry:
        ease 0.7 xpos 0.2
    show sl_e4 serious with hpunch:
        ease 0.7 xpos 0.5
    $ renpy.pause(0.5, hard=True)
    
    show sl_e4 angry:
        ease 0.6 xpos 0.8
    show dv_s angry with hpunch:
        ease 0.6 xpos 0.5
    $ renpy.pause(0.5, hard=True)
    
    show dv_s angry:
        ease 0.6 xpos 0.2
    show sl_e4 angry with hpunch:
        ease 0.6 xpos 0.5
    $ renpy.pause(0.5, hard=True)
    
    show sl_e4 angry:
        ease 0.5 xpos 0.8
    show dv_s rage with hpunch:
        ease 0.5 xpos 0.5
    $ renpy.pause(0.5, hard=True)
    
    show dv_s rage:
        ease 0.5 xpos 0.2
    show sl_e4 rage with hpunch:
        ease 0.5 xpos 0.5
    $ renpy.pause(0.5, hard=True)
    
    show sl_e4 rage:
        ease 0.4 xpos 0.8
    show dv_s rage with hpunch:
        ease 0.4 xpos 0.5
    $ renpy.pause(0.5, hard=True)

    show dv_s angry at left with ease
    show sl_e4 angry at right with ease

    window show
    #"Некоторое время продолжалось молчаливое силовое противостояние, заключавшееся в перетягивании Семёна."
    
    "Наконец поняв, что грубой силой тут ничего не решить, соперницы оставили меня в покое и перешли к переговорам."

    show sl_e4 angry at cright with ease
    sls "Ты что творишь? Совсем сбрендила или это уже белая горячка?"

    show dv_s angry at cleft with ease
    slf "Да сколько можно одно и то же снова и снова. Всё, надоело! Хочу быть доброй, ласковой и милой."

    show sl_e4 surprise at right with ease
    sls "Чего-о-о?"

    show dv_s normal with dissolve
    slf "Того!{w} Теперь твоя очередь в одиночестве бренчать на гитаре по вечерам, устраивать пакости Панамке и держать в страхе весь лагерь."
    slf "Ещё быть колючей, гордой и неприступной, но с большим, любящим сердцем. Не забудь."

    show sl_e4 serious with dissolve
    sls "Вот ещё.{w} С каких это пор…"

    slf "А вот с таких. Теперь только так и никак иначе. Твоё место занято.{w} Смирись."

    show sl_e4 angry with dissolve
    sls "Знаешь, что?"
    "Славя Номер Два кипела от негодования не в силах подобрать слова."

    slf "Что?"

    sls "Это уже переходит всякие границы. Совсем распоясалась!{w} Придётся взяться и за твоё воспитание."

    show dv_s grin with dissolve
    slf "Ну, попробуй…"

    scene bg ext_road_day with wipeleft
    "Я под шумок стал озираться в поисках путей отступления, чтобы просто по-тихому незаметно удалиться."

    stop music fadeout 2
    unv "Ой, девочки, м-может, не надо?"
    "Раздался сзади чей-то жалобный голосок."

    window hide
    scene bg ext_camp_entrance_day with wiperight
    show un sad sport far at center with dissolve
    $ renpy.pause(2, hard=True)
    window show

    sv "Кажется, я окружён и бежать некуда"

    show sl_e4 serious pioneer at fleft with hpunch
    sls "Лена!"
    
    show dv_s normal pioneer at fright with vpunch
    slf "Вот только тебя здесь не хватало. Чего пришла?{w} Скройся с глаз, а то я за себя не ручаюсь!"

    show un sad sport at center with dissolve
    un "Алиса… Но ведь так нельзя…"

    show dv_s angry with dissolve
    slf "Было нельзя, а теперь можно! Беру власть в свои руки!"

    usp "Вся власть советам!"
    show us laugh sport far at cright behind un with hpunch    
    usp "То есть мне!"

    "Сцена обогатилась ещё одним персонажем: маленькой рыжей девочкой лет двенадцати."
    "Она быстро подбежала к Славянам и встала между ними живым барьером."
    
    show un angry2 at cleft with ease
    show us normal sport at center with ease
    
    sls "Ульяна, ты очень вовремя!{w} Держи свою подругу на поводке и намордник на неё надень, а то покусает ещё." 
    show sl_e4 angry with dissolve
    sls "Бешеная."

    show dv_s rage with dissolve
    slf "Щас я кого-то укушу — мало не покажется!"
    show us surp1 with dissolve
    stop ambience
    play sound sfx_angry_ulyana
    $ renpy.pause(2, hard=True)
    show us surp2 with dissolve
    $ renpy.pause(2, hard=True)
    #window hide
    scene bg black
    play music music_list["that_s_our_madhouse"]
    
    play sound sfx_face_slap 
    with hpunch
    $ renpy.pause(0.1, hard=True)
    play sound sfx_lena_hits_alisa 
    with vpunch
    $ renpy.pause(0.1, hard=True)
    play sound sfx_pat_shoulder_hard 
    with hpunch
    $ renpy.pause(0.75, hard=True)
    play sound sfx_drop_alisa_bag 
    with hpunch
    $ renpy.pause(0.75, hard=True)
    play sound sfx_punch_medium 
    with hpunch
    $ renpy.pause(0.75, hard=True)
    play sound sfx_broken_dish 
    with vpunch
    $ renpy.pause(0.75, hard=True)
    play sound sfx_armature_swish 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_piano_head_bump 
    with vpunch
    $ renpy.pause(1.5, hard=True)
    play sound sfx_body_bump 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_break_flashlight_alisa
    with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_punch_washstand 
    with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_break_cupboard 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_bodyfall_1 
    with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_punch_medium 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_bush_body_fall 
    with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_armature_swish 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_boat_impact 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_face_slap 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_energy_door_bus 
    with vpunch
    $ renpy.pause(2, hard=True)
    play sound sfx_drop_pipe 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_punch_washstand 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_fall_grass 
    with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_fall_wood_floor 
    with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_alisa_falls 
    with hpunch
    $ renpy.pause(2, hard=True)
    stop music fadeout 2
    stop sound
    play ambience ambience_ext_road_day

    scene bg ext_camp_entrance_day with dissolve
    show dv_s cry pioneer at fleft with dissolve 
    show sl_e4 dontlike pioneer at fright with dissolve
    show us angry sport at left with dissolve
    show un angry sport at right with dissolve
    
    #window show
    "Довольно быстро всё кончилось."
    "Славя Номер Один лежала на земле, и её держала каким-то хитрым захватом маленькая Ульяна, а Славю Номер Два держала Лена, выглядевшая теперь отнюдь не безобидно."

    us "Ну, и что тут происходит? Что я пропустила интересного?"

    show un angry2 at cright with ease
    show sl_e4 sad with dissolve
    sls "Эта ненормальная утверждает, что теперь она Славяна."
    "Славя Номер Два кивнула на поверженную Славю Номер Один."

    show us sad at cleft with ease
    us "Алиска, поясни!"

    show dv_s sad with dissolve
    sls "Да чего пояснять? Хочу побыть колхозницей.{w} Надоело, знаешь ли, каждый раз одно и то же.{w} Разнообразие, все дела."

    show us smile with dissolve
    us "А что, идея мне нравится. Должно быть весело. Может, правда попробуем?"

    mtp "И правда, почему бы не попробовать?"

    window hide
    show mt normal panama pioneer at center with dspr
    show us surp2 sport at left with ease
    show un surprise sport at right with ease
    show dv_s surprise with dissolve 
    show sl_e4 surprise pioneer at fright with dissolve
    
    window show
    chor "Ольга Дмитриевна?"

    mt "Да-да, она самая. Не ждали?"
    mt "Ну и что вы тут устроили? Совсем кукухой поехали."
    
    show mt sad close with dissolve
    mt "Лена, давай его на новый виток. А этих бракованных в расход, и сама не забудь ликвидироваться."
    
    window hide
    show us fear
    show un scared
    show dv_s scared
    show sl_e4 scared
    show mt smile with dissolve
    
    window show
    mt "Отдохну наконец от вас хотя бы недельку.{w} В конце концов, должен же и у меня быть отпуск…"

    window hide
    stop ambience
    hide mt with dissolve
    $ renpy.pause(1, hard=True)
    hide dv_s with dissolve
    $ renpy.pause(1, hard=True)
    hide sl_e4 with dissolve
    $ renpy.pause(1, hard=True)
    hide un with dissolve
    $ renpy.pause(1, hard=True)
    hide us with dissolve
    play music music_list["orchid"]
    $ renpy.pause(2, hard=True)
    
    scene bg ext_camp_entrance_evening with dissolve2
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    show un sad sport far at center with dissolve
    window show
    un "Прости, Семён…"

    "Девушка Лена зашагала ко мне, не сводя с меня грустного взгляда."
    "В её руке блеснул угрожающего вида кухонный нож."
    "Наверняка очень острый."
    "Впрочем, проверять его остроту на себе мне не хотелось, и я стал медленно пятиться, не выпуская из виду всю чудную компанию, собравшуюся на стоянке перед воротами пионерского лагеря «Совёнок»."

    play sound sfx_punch_medium
    with vpunch
    "Спина встретилась с твёрдой холодной преградой."
    "Я несколько раз толкнулся в неё не оборачиваясь, но безрезультатно."
    
    window hide
    hide un with dissolve2
    show un cry sport at center with dissolve2
    
    window show
    "Лена тем временем подходила всё ближе и становилась всё печальнее."
    "Но несмотря ни на что, её решимость огорчить меня до невозможности ничуть не поколебалась."

    me "Сходил за хлебушком, называется…"

    window hide
    scene bg ext_camp_entrance_night with dissolve2
    $ persistent.sprite_time = "night"
    $ night_time()
    show un cry_smile sport close at center with dissolve2
    window show
    
    play sound_loop sfx_head_heartbeat
    un "Не бойся."
    "Успокоила меня Лена и занесла нож для удара."
    
    un "Я как раз недавно смотрела в библиотеке анатомический атлас, и теперь знаю, куда бить, чтобы всё прошло быстро."
    window hide
    $ renpy.pause(1, hard=True)
    play sound sfx_scary_sting
    show un evil_smile
    $ renpy.pause(1, hard=True)
    play sound sfx_ghost_children_laugh

    scene bg black with dissolve2
    stop sound_loop
    play ambience ambience_old_camp_outside
    stop music fadeout 3
    pause