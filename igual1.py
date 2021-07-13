# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:23:31 2021

@author: 48789
"""

lw = ['bl2_S235_111_p1_g',
               'bl2_S235_111_p2_g',
               'bl3_S235_111_p3_g',
               'bl2_S235_111_p4_g',
               'bl8_S235_111_p5_g',
               'bl2_S235_111_p6_g',
               'bl3_S235_111_p7_g',
               'bl2_S235_111_p8_g',
               'bl12_S235_111_p9_g'              
               ]
low = ['bl3_S235_111_p7_g',
               'bl2_S235_111_p8_g',
               'bl12_S235_111_p9_g' ]


ld= ['bl2_S235_111_p8_g.dxf',
               'bl12_S235_111_p9_g.dxf',
               'bl6_S355_12_p6.dxf',
               'bl2_S235_111_p2.dxf'
               ]
emp = []
for i in lw:
    for j in ld:
        print(i,'and',j)
        if i in j:
            txt = 'ld ma '+i
            emp.append(txt)
            

dlw = [ i+'.dxf' for i in lw]

a = [poz for poz in dlw if poz in ld]

