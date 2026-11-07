import wrap
ss=1000
vp=600
vv=1030
ps2=600
ps3=900
vv=1030
wrap.world.create_world(ss,vv)
wrap.sprite.add('mario-items',50,vp,'cloud_platform')
wrap.sprite.add('mario-items',ps2,vp,'cloud_platform')
wrap.sprite.add('mario-items',ps3,vp,'cloud_platform')
wrap.sprite.add('mario-items',ss-50,vp,'cloud_platform')


wrap.add_sprite_dir('sklad')
wrap.sprite.add('sklad2',50,vp-50,'sn2',False)
wrap.sprite.set_size(4,100,100)
wrap.sprite.add('mario-enemies',400,500)
wrap.sprite.show(4)
r=(ps2-50)/2+50
wrap.actions.move_to(4,r,vp-150)


wrap.actions.move_to(4,ps2,vp-50)
o=(ps3-ps2)/2+ps2
wrap.actions.move_to(4,o,vp-150)

wrap.actions.move_to(4,ps3,vp-50)
w=(ss-50-ps3)/2+ps3
wrap.actions.move_to(4,w,vp-150)

wrap.actions.move_to(4,ss-50,vp-50)




























































































































































































