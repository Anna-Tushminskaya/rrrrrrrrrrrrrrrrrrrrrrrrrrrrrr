import wrap
wrap.world.create_world(1000,600)
wrap.sprite.add('pacman',500,300,'player2')
x1=300
y1=200
wrap.sprite.add('pacman',x1,y1)
x2=600
y2=400
wrap.sprite.add('pacman',x2,y2)
x3=800
y3=300
wrap.sprite.add('pacman',x3,y3)
wrap.sprite.add('pacman',550,300,'enemy_blue_down2')

wrap.sprite.add_text('tochka1',x1,y1-30,text_color=[255,27,166])
wrap.sprite.add_text('tochka2',x2,y2-30,text_color=[27,255,166])
wrap.sprite.add_text('tochka3',x3,y3-30,text_color=[27,166,255])
wrap.actions.move_to(4,x1,y1)
wrap.sprite.set_costume(4,'enemy_ill_white1')





























