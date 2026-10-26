import wrap
from wrap_py import sprite

wrap.world.create_world(1000,600)
wrap.sprite.add('battle_city_items',100,565,'base_defend_brick')
wrap.sprite.add('battle_city_items',300,565,'base_defend_brick')
wrap.sprite.add('battle_city_items',500,565,'base_defend_brick')
wrap.sprite.add('battle_city_items',700,565,'base_defend_brick')
wrap.sprite.set_angle(0,270)
wrap.sprite.set_angle(1,270)
wrap.sprite.set_angle(2,270)
wrap.sprite.set_angle(3,270)

wrap.sprite.add('mario-1-big',200,340,'stand')

wrap.actions.set_size(4,192,384,5000)

wrap.sprite.add_text('где же принцеса!!!!!!!!!!!!!!!!!???????????',400,120,text_color=[100,200,100])

wrap.sprite.add('mario-princess',600,340,'toad')

wrap.actions.set_size(6,192,384,5000)

wrap.sprite.add_text('я её сьел!!!!!!!!',420,200,text_color=[250,60,250])




































