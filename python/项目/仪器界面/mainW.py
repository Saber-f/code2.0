from tkinter import *

# 主窗口即图片
if True:
    window = Tk()
    window.title('DS-80计程仪')
    window.geometry('1200x670')
    photo = PhotoImage(file='面板.gif')
    p_pwr = PhotoImage(file='pwr.gif')
    p_xing = PhotoImage(file='xing.gif')
    p_disp= PhotoImage(file='disp.gif')
    p_menu = PhotoImage(file='menu.gif')
    p_dim = PhotoImage(file='dim.gif')
    p_ent = PhotoImage(file='ent.gif')
    p_u = PhotoImage(file='u.gif')
    p_l = PhotoImage(file='l.gif')
    p_r = PhotoImage(file='r.gif')
    p_d = PhotoImage(file='d.gif')
    cl_p = '#%02x%02x%2x'%(174,178,157)         # 屏幕颜色

# 全局状态变量
if True:
    
    S = IntVar()           
    '''
    全局状态
    0->关机
    1->开机界面
    2->1按disp后的界面
    3->1按menu后的界面
    '''
    s_menu = IntVar()
    '''
    0->主菜单选中第一项
    1->主菜单选中第二项
    2->主菜单选中第三项
    3->主菜单选中第四项
    '''
    s_menu1 = IntVar()          # 状态(主菜单确定后的界面状态记录)

    # 主菜单第一项的值
    s_m11 = IntVar()         
    s_m11_ = IntVar(value=1)
    s_m12 = IntVar()        
    s_m12_ = IntVar()
    if True:
        s_m131 = IntVar()
        s_m131_ = IntVar()
        s_m132 = IntVar()
        s_m132_ = IntVar()
        s_m133 = IntVar()
        s_m133_ = IntVar()
        s_m134 = IntVar()
        s_m134_ = IntVar()
        s_m135 = IntVar()
        s_m135_ = IntVar()
        s_m136 = IntVar()
        s_m136_ = IntVar()
        s_m137 = IntVar()
        s_m137_ = IntVar()
        s_m138 = IntVar()
        s_m138_ = IntVar()
    
    # 主菜单第二项的值
    if True:
        s_m211 = IntVar()
        s_m212 = IntVar(value=1)
        s_m213 = IntVar()
        s_m214 = IntVar()
        s_m211_ = IntVar()
        s_m212_ = IntVar(value=1)
        s_m213_ = IntVar()
        s_m214_ = IntVar()
        s_m22 = IntVar()

    # 主菜单第三项的值
    if True:
        s_m31 = IntVar(value=2)
        s_m321 = IntVar()
        s_m322 = IntVar()
        s_m323 = IntVar()
        s_m324 = IntVar()
        s_m321_ = IntVar()
        s_m322_ = IntVar()
        s_m323_ = IntVar()
        s_m324_ = IntVar()

        s_m331 = IntVar(value=2)
        s_m332 = IntVar()
        s_m331_ = IntVar(value=2)
        s_m332_ = IntVar()

        s_m341 = IntVar()
        s_m342 = IntVar()
        s_m343 = IntVar()
        s_m341_ = IntVar()
        s_m342_ = IntVar()
        s_m343_ = IntVar()
        s_m35 = IntVar(value=1)

    # 主菜单第四项的值
    s_m42 = IntVar()
    s_m43 = IntVar()

# 显示隐藏界面
def dis_1():
    l_sim['text'] = 'SIM |'
    l_speed_num['font'] = "Verdana 80 bold"
    l_kn['font'] = "Verdana 30 bold"
    l_speed.place(x=150,y=120)                  # 显示label
    l_distance.place(x=150,y=330)
    l_sim.place(x=600,y=120)
    l_speed_num.place(x=300,y=190)
    l_kn.place(x=700,y=250)
    l_distance_num.place(x=460,y=370)
    l_nm.place(x=700,y=490)
    S.set(1)
def hid_1():
    l_speed.place_forget()          # 隐藏label
    l_distance.place_forget()
    l_sim.place_forget()
    l_speed_num.place_forget()
    l_kn.place_forget()
    l_distance_num.place_forget()
    l_nm.place_forget()
def dis_3():
    l_menu.place(x=150,y=120)
    l_line.place(x=150,y=180)
    l_m_distance_run_display.place(x=150,y=190)
    l_m_sim.place(x=150,y=250)
    l_m_system_menu.place(x=150,y=310)
    l_m_system_menu2.place(x=150,y=370)
    l_m_ent_set.place(x=550,y=490)
    S.set(3)
def hid_3():
    l_menu.place_forget()
    l_line.place_forget()
    l_m_distance_run_display.place_forget()
    l_m_sim.place_forget()
    l_m_system_menu.place_forget()
    l_m_system_menu2.place_forget()
    l_m_ent_set.place_forget()
def update_31():
    if s_m11.get() == 0:
        l_m1_data_display_val['text'] = 'CONTACT CLOSURE'
    elif s_m11.get() == 1:
        l_m1_data_display_val['text'] = 'IEC61162(VLW)'

    if s_m12_.get() == 0:
        l_m1_reset_val['text'] = 'OFF'
    elif s_m12.get() == 1:
        l_m1_reset_val['text'] = 'NO'

    l_m_31_31['text'] = str(s_m131.get())
    l_m_31_32['text'] = str(s_m132.get())
    l_m_31_33['text'] = str(s_m133.get())
    l_m_31_34['text'] = str(s_m134.get())
    l_m_31_35['text'] = str(s_m135.get())
    l_m_31_36['text'] = str(s_m136.get())
    l_m_31_37['text'] = str(s_m137.get())
    l_m_31_38['text'] = str(s_m138.get())
def dis_31():
    l_m1_distance_run_displa.place(x=150,y=120)
    l_line.place(x=150,y=180)
    l_m1_data_display.place(x=150,y=190)
    l_m1_data_display_val.place(x=310,y=250)
    l_m1_reset.place(x=150,y=310)
    l_m1_reset_val.place(x=670,y=310)
    l_m1_set.place(x=150,y=370)
    l_m1_set_nm.place(x=580,y=430)
    l_m_ent_set.place(x=550,y=490)

    l_m1_data_display_val['bg'] = 'black'
    l_m1_data_display_val['fg'] = cl_p
    l_m1_reset_val['bg'] = cl_p
    l_m1_reset_val['fg'] = 'black'
    l_m1_set_nm['bg'] = cl_p
    l_m1_set_nm['fg'] = 'black'
    dis_3131(0)
    update_31()
    S.set(31)
    s_menu1.set(0)
def hid_31():
    l_m1_distance_run_displa.place_forget()
    l_line.place_forget()
    l_m1_data_display.place_forget()
    l_m1_data_display_val.place_forget()
    l_m1_reset.place_forget()
    l_m1_reset_val.place_forget()
    l_m1_set.place_forget()
    l_m1_set_nm.place_forget()
    hid_311()
    hid_312()
    hid_313()
    l_m_ent_set.place_forget()
def dis_311():
    l_m_31_11.place(x=310,y=310)
    l_m_31_12.place(x=310,y=370)
    if s_m11.get() == 0:
        l_m_31_11['bg'] = cl_p
        l_m_31_11['fg'] = 'black'
        l_m_31_12['fg'] = cl_p
        l_m_31_12['bg'] = 'black'
    elif s_m11.get() == 1:
        l_m_31_11['fg'] = cl_p
        l_m_31_11['bg'] = 'black'
        l_m_31_12['bg'] = cl_p
        l_m_31_12['fg'] = 'black'
    s_menu1.set(3)
def hid_311():
    l_m_31_11.place_forget()
    l_m_31_12.place_forget()
    s_menu1.set(0)
def dis_312():
    l_m_31_21.place(x=670,y=370)
    l_m_31_22.place(x=670,y=430)
    if s_m12.get() == 0:
        l_m_31_21['fg'] = cl_p
        l_m_31_21['bg'] = 'black'
        l_m_31_22['bg'] = cl_p
        l_m_31_22['fg'] = 'black'
    elif s_m12.get() == 1:
        l_m_31_21['bg'] = cl_p
        l_m_31_21['fg'] = 'black'
        l_m_31_22['fg'] = cl_p
        l_m_31_22['bg'] = 'black'
    s_menu1.set(4)
def hid_312():
    l_m_31_21.place_forget()
    l_m_31_22.place_forget()
    s_menu1.set(1)
def dis_3131(s):
    f = False

    if s_m131.get() != 0:
        f = True
    if f:
        l_m_31_31.place(x=385,y=430)  
        
    if s_m132.get() != 0:
        f = True
    if f:
        l_m_31_32.place(x=420,y=430)  

    if s_m133.get() != 0:
        f = True
    if f:
        l_m_31_33.place(x=455,y=430)  

    if s_m134.get() != 0:
        f = True
    if f:
        l_m_31_34.place(x=490,y=430)  

    if s_m135.get() != 0:
        f = True
    if f:
        l_m_31_35.place(x=525,y=430)  


    l_m_31_36.place(x=560,y=430)    
    l_m_31_37.place(x=605,y=430)
    l_m_31_38.place(x=640,y=430)
    if s == 0:
        l_m1_set_nm['bg'] = cl_p
        l_m1_set_nm['fg'] = 'black'
        l_m_31_31['bg'] = cl_p
        l_m_31_31['fg'] = 'black'
        l_m_31_32['bg'] = cl_p
        l_m_31_32['fg'] = 'black'
        l_m_31_33['bg'] = cl_p
        l_m_31_33['fg'] = 'black'
        l_m_31_34['bg'] = cl_p
        l_m_31_34['fg'] = 'black'
        l_m_31_35['bg'] = cl_p
        l_m_31_35['fg'] = 'black'
        l_m_31_36['bg'] = cl_p
        l_m_31_36['fg'] = 'black'
        l_m_31_37['bg'] = cl_p
        l_m_31_37['fg'] = 'black'
        l_m_31_38['bg'] = cl_p
        l_m_31_38['fg'] = 'black'
    elif s == 1:
        l_m1_set_nm['fg'] = cl_p
        l_m1_set_nm['bg'] = 'black'
        l_m_31_31['fg'] = cl_p
        l_m_31_31['bg'] = 'black'
        l_m_31_32['fg'] = cl_p
        l_m_31_32['bg'] = 'black'
        l_m_31_33['fg'] = cl_p
        l_m_31_33['bg'] = 'black'
        l_m_31_34['fg'] = cl_p
        l_m_31_34['bg'] = 'black'
        l_m_31_35['fg'] = cl_p
        l_m_31_35['bg'] = 'black'
        l_m_31_36['fg'] = cl_p
        l_m_31_36['bg'] = 'black'
        l_m_31_37['fg'] = cl_p
        l_m_31_37['bg'] = 'black'
        l_m_31_38['fg'] = cl_p
        l_m_31_38['bg'] = 'black'
def hid_313(): 
    l_m_31_31.place_forget()
    l_m_31_32.place_forget()
    l_m_31_33.place_forget()
    l_m_31_34.place_forget()
    l_m_31_35.place_forget()
    l_m_31_36.place_forget()
    l_m_31_37.place_forget()
    l_m_31_38.place_forget()
    s_menu1.set(2)
def dis_3132():
    l_m_31_31.place(x=385,y=430)  
    l_m_31_32.place(x=420,y=430)  
    l_m_31_33.place(x=455,y=430)  
    l_m_31_34.place(x=490,y=430)  
    l_m_31_35.place(x=525,y=430)  
    l_m_31_36.place(x=560,y=430)    
    l_m_31_37.place(x=605,y=430)
    l_m_31_38.place(x=640,y=430)
    l_m1_set_nm['bg'] = cl_p
    l_m1_set_nm['fg'] = 'black'
    l_m_31_31['fg'] = cl_p
    l_m_31_31['bg'] = 'black'
    l_m_31_32['bg'] = cl_p
    l_m_31_32['fg'] = 'black'
    l_m_31_33['bg'] = cl_p
    l_m_31_33['fg'] = 'black'
    l_m_31_34['bg'] = cl_p
    l_m_31_34['fg'] = 'black'
    l_m_31_35['bg'] = cl_p
    l_m_31_35['fg'] = 'black'
    l_m_31_36['bg'] = cl_p
    l_m_31_36['fg'] = 'black'
    l_m_31_37['bg'] = cl_p
    l_m_31_37['fg'] = 'black'
    l_m_31_38['bg'] = cl_p
    l_m_31_38['fg'] = 'black'
    s_menu1.set(51)
def update_32():
    if s_m211.get() == 0:
        l_m_32_11['text'] = '+'
    elif s_m211.get() == 1:
        l_m_32_11['text'] = '-'
    l_m_32_12['text'] = str((s_m212.get()))
    l_m_32_13['text'] = str((s_m213.get()))
    l_m_32_14['text'] = str((s_m214.get()))
def dis_32():
    l_m2_sim.place(x=150,y=120)
    l_line.place(x=150,y=180)
    l_m2_speed.place(x=150,y=190)
    l_m_32_11.place(x=540,y=250)    
    l_m_32_12.place(x=575,y=250)
    l_m_32_13.place(x=630,y=250)
    l_m_32_14.place(x=665,y=250)
    l_m2_speed_kn.place(x=610,y=250)
    l_m2_data_display.place(x=150,y=310)
    l_m2_data_display_val.place(x=670,y=310)
    l_m_ent_set.place(x=550,y=490)

    l_m_32_11['bg'] = 'black'
    l_m_32_12['bg'] = 'black'
    l_m_32_13['bg'] = 'black'
    l_m_32_14['bg'] = 'black'
    l_m_32_11['fg'] = cl_p
    l_m_32_12['fg'] = cl_p
    l_m_32_13['fg'] = cl_p
    l_m_32_14['fg'] = cl_p
    l_m2_speed_kn['bg'] = 'black'
    l_m2_speed_kn['fg'] = cl_p
    l_m2_data_display_val['bg'] = cl_p
    l_m2_data_display_val['fg'] = 'black'
    S.set(32)
    s_menu1.set(1)
def hid_32():
    l_m2_sim.place_forget()
    l_line.place_forget()
    l_m2_speed.place_forget()
    l_m2_speed_kn.place_forget()
    l_m_32_11.place_forget()
    l_m_32_12.place_forget()
    l_m_32_13.place_forget()
    l_m_32_14.place_forget()
    l_m2_data_display.place_forget()
    l_m2_data_display_val.place_forget()
    l_m_ent_set.place_forget()
def dis_322():
    l_m_32_21.place(x=670,y=370)
    l_m_32_22.place(x=670,y=430)
    if s_m22.get() == 0:
        l_m_32_21['bg'] = 'black'
        l_m_32_21['fg'] = cl_p
        l_m_32_22['fg'] = 'black'
        l_m_32_22['bg'] = cl_p
    elif s_m22.get() == 1:
        l_m_32_21['fg'] = 'black'
        l_m_32_21['bg'] = cl_p
        l_m_32_22['bg'] = 'black'
        l_m_32_22['fg'] = cl_p
def hid_322():
    l_m_32_21.place_forget()
    l_m_32_22.place_forget()
def update_33():
    if s_m321.get() == 0:
        l_m_33_21['text'] = '+'
    elif s_m321.get() == 1:
        l_m_33_21['text'] = '-'
    l_m_33_22['text'] = str((s_m322.get()))
    l_m_33_23['text'] = str((s_m323.get()))
    l_m_33_24['text'] = str((s_m324.get()))

    l_m_33_31['text'] = str((s_m331.get()))
    l_m_33_32['text'] = str((s_m332.get()))

    if s_m341.get() == 0:
        l_m_33_41['text'] = '+'
    elif s_m341.get() == 1:
        l_m_33_41['text'] = '-'
    l_m_33_42['text'] = str((s_m342.get()))
    l_m_33_43['text'] = str((s_m343.get()))
def dis_33():
    l_m3_system_menu.place(x=150,y=120)
    l_line.place(x=150,y=180)
    l_m3_ship_spd_avg.place(x=150,y=190)
    l_m3_ship_spd_avg_val.place(x=572,y=190)
    l_m3_speed_offset.place(x=150,y=240)   
    l_m3_speed_offset_b.place(x=635,y=240)  
    l_m3_track_depth.place(x=150,y=290)
    l_m3_track_depth_m.place(x=630,y=290)
    l_m3_xdr_offset.place(x=150,y=340)
    l_m3_xdr_offset_d.place(x=700,y=340)
    l_m3_spd_data_select.place(x=150,y=390)
    l_m3_spd_data_select_val.place(x=550,y=440)
    l_m_ent_set.place(x=550,y=490)
    l_m3_ship_spd_avg_val['bg'] = 'black'
    l_m3_ship_spd_avg_val['fg'] = cl_p
    l_m3_spd_data_select_val['bg'] = cl_p
    l_m3_spd_data_select_val['fg'] = 'black'
    l_m3_speed_offset_b['bg'] = cl_p
    l_m3_speed_offset_b['fg'] = 'black'
    l_m3_track_depth_m['bg'] = cl_p
    l_m3_track_depth_m['fg'] = 'black'
    l_m3_xdr_offset_d['bg'] = cl_p
    l_m3_xdr_offset_d['fg'] = 'black'

    l_m_33_21['bg'] = cl_p
    l_m_33_22['bg'] = cl_p
    l_m_33_23['bg'] = cl_p
    l_m_33_24['bg'] = cl_p
    l_m_33_31['bg'] = cl_p
    l_m_33_32['bg'] = cl_p
    l_m_33_41['bg'] = cl_p
    l_m_33_42['bg'] = cl_p
    l_m_33_43['bg'] = cl_p
    
    l_m_33_21['fg'] = 'black'
    l_m_33_22['fg'] = 'black'
    l_m_33_23['fg'] = 'black'
    l_m_33_24['fg'] = 'black'
    l_m_33_31['fg'] = 'black'
    l_m_33_32['fg'] = 'black'
    l_m_33_41['fg'] = 'black'
    l_m_33_42['fg'] = 'black'
    l_m_33_43['fg'] = 'black'

    l_m_33_21.place(x=548,y=240)
    l_m_33_22.place(x=578,y=240)
    l_m_33_23.place(x=608,y=240)
    l_m_33_24.place(x=658,y=240)
    l_m_33_31.place(x=608,y=290)
    l_m_33_32.place(x=658,y=290)
    l_m_33_41.place(x=610,y=340)
    l_m_33_42.place(x=640,y=340)
    l_m_33_43.place(x=670,y=340)
    S.set(33)
    s_menu1.set(1)
def hid_33():
    l_m3_system_menu.place_forget()
    l_line.place_forget()
    l_m3_ship_spd_avg.place_forget()
    l_m3_ship_spd_avg_val.place_forget()
    l_m3_speed_offset.place_forget()
    l_m3_speed_offset_b.place_forget()  
    l_m3_track_depth.place_forget()
    l_m3_track_depth_m.place_forget()
    l_m3_xdr_offset.place_forget()
    l_m3_xdr_offset_d.place_forget()
    l_m3_spd_data_select.place_forget()
    l_m3_spd_data_select_val.place_forget()
    l_m_ent_set.place_forget()
    l_m_33_21.place_forget()
    l_m_33_22.place_forget()
    l_m_33_23.place_forget()
    l_m_33_24.place_forget()
    l_m_33_31.place_forget()
    l_m_33_32.place_forget()
    l_m_33_41.place_forget()
    l_m_33_42.place_forget()
    l_m_33_43.place_forget()
    hid_331()
    hid_335()
def dis_331():
    l_m_33_11.place(x=572,y=240)
    l_m_33_12.place(x=572,y=290)
    l_m_33_13.place(x=572,y=340)
    l_m_33_14.place(x=572,y=390)
    if s_m31.get() == 1:
        l_m_33_11['fg'] = cl_p
        l_m_33_11['bg'] = 'black'
    else:
        l_m_33_11['bg'] = cl_p
        l_m_33_11['fg'] = 'black'
    if s_m31.get() == 2:    
        l_m_33_12['fg'] = cl_p
        l_m_33_12['bg'] = 'black'
    else:
        l_m_33_12['bg'] = cl_p
        l_m_33_12['fg'] = 'black'
    if s_m31.get() == 3:
        l_m_33_13['fg'] = cl_p
        l_m_33_13['bg'] = 'black'
    else:
        l_m_33_13['bg'] = cl_p
        l_m_33_13['fg'] = 'black'
    if s_m31.get() == 4:
        l_m_33_14['fg'] = cl_p
        l_m_33_14['bg'] = 'black'
    else:
        l_m_33_14['bg'] = cl_p
        l_m_33_14['fg'] = 'black'
    s_menu1.set(10+s_m31.get())
def hid_331():
    l_m_33_11.place_forget()
    l_m_33_12.place_forget()
    l_m_33_13.place_forget()
    l_m_33_14.place_forget()
    s_menu1.set(1)
def dis_335():
    l_m_33_51.place(x=550,y=290)
    l_m_33_52.place(x=550,y=340)
    l_m_33_53.place(x=550,y=390)
    if s_m35.get() == 1:
        l_m_33_51['fg'] = cl_p
        l_m_33_51['bg'] = 'black'
    else:
        l_m_33_51['bg'] = cl_p
        l_m_33_51['fg'] = 'black'
    if s_m35.get() == 2:    
        l_m_33_52['fg'] = cl_p
        l_m_33_52['bg'] = 'black'
    else:
        l_m_33_52['bg'] = cl_p
        l_m_33_52['fg'] = 'black'
    if s_m35.get() == 3:
        l_m_33_53['fg'] = cl_p
        l_m_33_53['bg'] = 'black'
    else:
        l_m_33_53['bg'] = cl_p
        l_m_33_53['fg'] = 'black'
    s_menu1.set(50+s_m35.get())
def hid_335():
    l_m_33_51.place_forget()
    l_m_33_52.place_forget()
    l_m_33_53.place_forget()
    s_menu1.set(5)
def dis_34():
    l_m4_system_menu2.place(x=150,y=120)
    l_line.place(x=150,y=180)
    l_m4_test.place(x=150,y=190)
    l_m4_dimmer.place(x=150,y=250)
    l_m4_dimmer_val.place(x=510,y=250)
    l_m4_lang.place(x=150,y=310)
    l_m4_lang_val.place(x=540,y=310)
    l_m_ent_set.place(x=550,y=490)
    l_m4_test['bg'] = 'black'
    l_m4_test['fg'] = cl_p
    l_m4_dimmer_val['fg'] = 'black'
    l_m4_dimmer_val['bg'] = cl_p
    l_m4_lang_val['fg'] = 'black'
    l_m4_lang_val['bg'] = cl_p
    S.set(34)
    s_menu1.set(1)
def hid_34():
    l_m4_system_menu2.place_forget()
    l_line.place_forget()
    l_m4_test.place_forget()
    l_m4_dimmer.place_forget()
    l_m4_dimmer_val.place_forget()
    l_m4_lang.place_forget()
    l_m4_lang_val.place_forget()
    l_m_ent_set.place_forget()
    hid_341()
    hid_342()
    hid_343()
    hid_test()
def dis_341():
    l_m_34_11.place(x=220,y=250)
    l_m_34_12.place(x=370,y=425)
    l_m_34_13.place(x=470,y=425)
    l_m_34_12['bg'] = 'black'
    l_m_34_12['fg'] = cl_p
    l_m_34_13['fg'] = 'black'
    l_m_34_13['bg'] = cl_p
    s_menu1.set(111)
def hid_341():
    l_m_34_11.place_forget()
    l_m_34_12.place_forget()
    l_m_34_13.place_forget()
    s_menu1.set(1)
def dis_test():
    l_t_test.place(x=150,y=120)
    l_line.place(x=150,y=180)
    l_t_rs.place(x=150,y=190)
    l_t_pk.place(x=150,y=350)
    l_t_o.place(x=150,y=410)
    s_menu1.set(12)
def hid_test():
    l_t_test.place_forget()
    l_line.place_forget()
    l_t_rs.place_forget()
    l_t_pk.place_forget()
    l_t_o.place_forget()
def dis_342():
    l_m_34_21.place(x=510,y=310)
    l_m_34_22.place(x=510,y=370)
    if s_m42.get() == 0:
        l_m_34_21['bg'] = 'black'
        l_m_34_21['fg'] = cl_p
        l_m_34_22['fg'] = 'black'
        l_m_34_22['bg'] = cl_p
    elif s_m42.get() == 1:
        l_m_34_21['fg'] = 'black'
        l_m_34_21['bg'] = cl_p
        l_m_34_22['bg'] = 'black'
        l_m_34_22['fg'] = cl_p
def hid_342():
    l_m_34_21.place_forget()
    l_m_34_22.place_forget()
def dis_343():
    l_m_34_31.place(x=540,y=370)
    l_m_34_32.place(x=540,y=430)
    if s_m43.get() == 0:
        l_m_34_31['bg'] = 'black'
        l_m_34_31['fg'] = cl_p
        l_m_34_32['fg'] = 'black'
        l_m_34_32['bg'] = cl_p
    elif s_m43.get() == 1:
        l_m_34_31['fg'] = 'black'
        l_m_34_31['bg'] = cl_p
        l_m_34_32['bg'] = 'black'
        l_m_34_32['fg'] = cl_p
def hid_343():
    l_m_34_31.place_forget()
    l_m_34_32.place_forget()

# 按钮函数
def on_of():
    if S.get() == 0:     
        dis_1()
    else:
        hid_1()
        hid_3()
        hid_31()
        hid_32()
        hid_33()
        hid_34()
        hid_test()
        S.set(0)
def disp():
    if S.get() == 1:
        l_sim['text'] = 'SIM \\'
        l_speed_num['font'] = "Verdana 140 bold"
        l_kn['font'] = "Verdana 60 bold"

        l_distance.place_forget()
        l_distance_num.place_forget()
        l_nm.place_forget()
        l_speed_num.place(x=130,y=220)
        l_kn.place(x=660,y=450)
        S.set(2)
def menu():
    if S.get() == 1:
        hid_1()
        s_menu.set(0)
        l_m_distance_run_display['bg'] = 'black'
        l_m_distance_run_display['fg'] = cl_p
        l_m_sim['fg'] = 'black'
        l_m_sim['bg'] = cl_p
        l_m_system_menu['fg'] = 'black'
        l_m_system_menu['bg'] = cl_p
        l_m_system_menu2['fg'] = 'black'
        l_m_system_menu2['bg'] = cl_p
        dis_3()
    elif S.get() == 2:
        l_sim['text'] = 'SIM |'
        l_speed_num['font'] = "Verdana 80 bold"
        l_kn['font'] = "Verdana 30 bold"
        l_distance.place(x=150,y=330)
        l_speed_num.place(x=300,y=190)
        l_kn.place(x=700,y=250)
        l_distance_num.place(x=460,y=370)
        l_nm.place(x=700,y=490)
        S.set(1)
    elif S.get() == 3:
        hid_3()
        dis_1()
    elif S.get() == 31:
        if s_menu1.get() < 3:
            hid_31()
            dis_3()
        elif s_menu1.get() == 3:
            s_m11_.set(s_m11.get())
            hid_311()
        elif s_menu1.get() == 4:
            s_m12_.set(s_m12.get())
            hid_312()
        elif s_menu1.get() >= 51 and s_menu1.get() <= 58:
            s_m131_.set(s_m131.get())
            s_m132_.set(s_m132.get())
            s_m133_.set(s_m133.get())
            s_m134_.set(s_m134.get())
            s_m135_.set(s_m135.get())
            s_m136_.set(s_m136.get())
            s_m137_.set(s_m137.get())
            s_m138_.set(s_m138.get())
            hid_313()
            update_31()
            dis_3131(1)
    elif S.get() == 32:
        if s_menu1.get() >= 1 and s_menu1.get() <= 3:
            hid_32()
            dis_3()
        elif s_menu1.get() >= 11 and s_menu1.get() <= 14:
            s_m211_.set(s_m211.get())
            s_m212_.set(s_m212.get())
            s_m213_.set(s_m213.get())
            s_m214_.set(s_m214.get())
            update_32()
            dis_32()
        elif s_menu1.get() == 21 or s_menu1.get() == 22:
            hid_322()
            s_menu1.set(2)
    elif S.get() == 33:
        if s_menu1.get() >= 1 and s_menu1.get() <= 5:
            hid_33()
            dis_3()
        elif s_menu1.get() >= 11 and s_menu1.get() <= 14:
            hid_331()
        elif s_menu1.get() >= 21 and s_menu1.get() <= 24:
            s_m321_.set(s_m321.get())
            s_m322_.set(s_m322.get())
            s_m323_.set(s_m323.get())
            s_m324_.set(s_m324.get())
            l_m3_speed_offset_b['bg'] = 'black'
            l_m_33_21['bg'] = 'black'
            l_m_33_22['bg'] = 'black'
            l_m_33_23['bg'] = 'black'
            l_m_33_24['bg'] = 'black'
            l_m3_speed_offset_b['fg'] = cl_p
            l_m_33_21['fg'] = cl_p
            l_m_33_22['fg'] = cl_p
            l_m_33_23['fg'] = cl_p
            l_m_33_24['fg'] = cl_p
            update_33()
            s_menu1.set(2)
        elif s_menu1.get() >= 31 and s_menu1.get() <= 32:
            s_m331_.set(s_m331.get())
            s_m332_.set(s_m332.get())
            l_m3_track_depth_m['bg'] = 'black'
            l_m_33_31['bg'] = 'black'
            l_m_33_32['bg'] = 'black'
            l_m3_track_depth_m['fg'] = cl_p
            l_m_33_31['fg'] = cl_p
            l_m_33_32['fg'] = cl_p
            update_33()
            s_menu1.set(3)
        elif s_menu1.get() >= 41 and s_menu1.get() <= 43:
            s_m341_.set(s_m341.get())
            s_m342_.set(s_m342.get())
            s_m343_.set(s_m343.get())
            l_m3_xdr_offset_d['bg'] = 'black'
            l_m_33_41['bg'] = 'black'
            l_m_33_42['bg'] = 'black'
            l_m_33_43['bg'] = 'black'
            l_m3_xdr_offset_d['fg'] = cl_p
            l_m_33_41['fg'] = cl_p
            l_m_33_42['fg'] = cl_p
            l_m_33_43['fg'] = cl_p
            update_33()
            s_menu1.set(4)
        elif s_menu1.get() >= 51 and s_menu1.get() <= 53:
            hid_335()
    elif S.get() == 34:
        if s_menu1.get() >= 1 and s_menu1.get() <= 3:
            hid_34()
            dis_3()
        elif s_menu1.get() == 111 or s_menu1.get() == 112:
            hid_341()
        elif s_menu1.get() == 113:
            hid_test()
            dis_34()
        elif s_menu1.get() == 21 or s_menu1.get() == 22:
            hid_342()
            s_menu1.set(2)
        elif s_menu1.get() == 31 or s_menu1.get() == 32:
            hid_343()
            s_menu1.set(3)
def up():
    if S.get() == 3:
        if s_menu.get() == 0:
            l_m_distance_run_display['bg'] = cl_p
            l_m_distance_run_display['fg'] = 'black'
            l_m_system_menu2['bg'] = 'black'  
            l_m_system_menu2['fg'] = cl_p
            s_menu.set(3)
        elif s_menu.get() == 1:
            l_m_distance_run_display['bg'] = 'black'
            l_m_distance_run_display['fg'] = cl_p
            l_m_sim['bg'] = cl_p
            l_m_sim['fg'] = 'black'
            s_menu.set(0)
        elif s_menu.get() == 2:
            l_m_sim['bg'] = 'black'
            l_m_sim['fg'] = cl_p
            l_m_system_menu['bg'] = cl_p
            l_m_system_menu['fg'] = 'black'
            s_menu.set(1)
        elif s_menu.get() == 3:
            l_m_system_menu['bg'] = 'black'
            l_m_system_menu['fg'] = cl_p
            l_m_system_menu2['bg'] = cl_p
            l_m_system_menu2['fg'] = 'black'  
            s_menu.set(2)
    elif S.get() == 31:
        if s_menu1.get() == 0:
            l_m1_data_display_val['fg'] = 'black'
            l_m1_data_display_val['bg'] = cl_p
            dis_3131(1)
            s_menu1.set(2)
        elif s_menu1.get() == 1:
            l_m1_data_display_val['bg'] = 'black'
            l_m1_data_display_val['fg'] = cl_p
            l_m1_reset_val['bg'] = cl_p
            l_m1_reset_val['fg'] = 'black'
            s_menu1.set(0)
        elif s_menu1.get() == 2:
            l_m1_reset_val['fg'] = cl_p
            l_m1_reset_val['bg'] = 'black'
            dis_3131(0)
            s_menu1.set(1)
        elif s_menu1.get() == 3:
            if s_m11_.get() == 1:
                l_m_31_11['bg'] = cl_p
                l_m_31_11['fg'] = 'black'
                l_m_31_12['fg'] = cl_p
                l_m_31_12['bg'] = 'black'
                s_m11_.set(0)
            elif s_m11_.get() == 0:
                l_m_31_11['fg'] = cl_p
                l_m_31_11['bg'] = 'black'
                l_m_31_12['bg'] = cl_p
                l_m_31_12['fg'] = 'black'
                s_m11_.set(1)
        elif s_menu1.get() == 4:
            if s_m12_.get() == 0:
                l_m_31_21['bg'] = cl_p
                l_m_31_21['fg'] = 'black'
                l_m_31_22['fg'] = cl_p
                l_m_31_22['bg'] = 'black'
                s_m12_.set(1)
            elif s_m12_.get() == 1:
                l_m_31_21['fg'] = cl_p
                l_m_31_21['bg'] = 'black'
                l_m_31_22['bg'] = cl_p
                l_m_31_22['fg'] = 'black'
                s_m12_.set(0)
        elif s_menu1.get() == 51:
            s_m131_.set((s_m131_.get()+1)%10)
            l_m_31_31['text'] = str(s_m131_.get())
        elif s_menu1.get() == 52:
            s_m132_.set((s_m132_.get()+1)%10)
            l_m_31_32['text'] = str(s_m132_.get())
        elif s_menu1.get() == 53:
            s_m133_.set((s_m133_.get()+1)%10)
            l_m_31_33['text'] = str(s_m133_.get())
        elif s_menu1.get() == 54:
            s_m134_.set((s_m134_.get()+1)%10)
            l_m_31_34['text'] = str(s_m134_.get())
        elif s_menu1.get() == 55:
            s_m135_.set((s_m135_.get()+1)%10)
            l_m_31_35['text'] = str(s_m135_.get())
        elif s_menu1.get() == 56:
            s_m136_.set((s_m136_.get()+1)%10)
            l_m_31_36['text'] = str(s_m136_.get())
        elif s_menu1.get() == 57:
            s_m137_.set((s_m137_.get()+1)%10)
            l_m_31_37['text'] = str(s_m137_.get())
        elif s_menu1.get() == 58:
            s_m138_.set((s_m138_.get()+1)%10)
            l_m_31_38['text'] = str(s_m138_.get())
    elif S.get() == 32:
        if s_menu1.get() == 1:
            l_m_32_11['bg'] = cl_p   
            l_m_32_12['bg'] = cl_p   
            l_m_32_13['bg'] = cl_p   
            l_m_32_14['bg'] = cl_p   
            l_m2_speed_kn['bg'] = cl_p   
            l_m_32_11['fg'] = 'black'  
            l_m_32_12['fg'] = 'black'   
            l_m_32_13['fg'] = 'black'    
            l_m_32_14['fg'] = 'black'    
            l_m2_speed_kn['fg'] = 'black'     
            l_m2_data_display_val['bg'] = 'black'
            l_m2_data_display_val['fg'] = cl_p
            s_menu1.set(2)
        elif s_menu1.get() == 11:
            s_m211_.set((s_m211_.get()+1)%2)
            if s_m211_.get() == 0:
                l_m_32_11['text'] = '+'
            elif s_m211_.get() == 1:
                l_m_32_11['text'] = '-'
        elif s_menu1.get() == 12:
            s_m212_.set((s_m212_.get()+1)%10)
            l_m_32_12['text'] = str(s_m212_.get())
        elif s_menu1.get() == 13:
            s_m213_.set((s_m213_.get()+1)%10)
            l_m_32_13['text'] = str(s_m213_.get())
        elif s_menu1.get() == 14:
            s_m214_.set((s_m214_.get()+1)%10)
            l_m_32_14['text'] = str(s_m214_.get())
        elif s_menu1.get() == 2:
            l_m_32_11['fg'] = cl_p   
            l_m_32_12['fg'] = cl_p   
            l_m_32_13['fg'] = cl_p   
            l_m_32_14['fg'] = cl_p   
            l_m2_speed_kn['fg'] = cl_p   
            l_m_32_11['bg'] = 'black'  
            l_m_32_12['bg'] = 'black'   
            l_m_32_13['bg'] = 'black'    
            l_m_32_14['bg'] = 'black'    
            l_m2_speed_kn['bg'] = 'black'     
            l_m2_data_display_val['bg'] = cl_p
            l_m2_data_display_val['fg'] = 'black'
            s_menu1.set(1)
        elif s_menu1.get() == 21:
            l_m_32_21['fg'] = 'black'
            l_m_32_21['bg'] = cl_p
            l_m_32_22['bg'] = 'black'
            l_m_32_22['fg'] = cl_p
            s_menu1.set(22)
        elif s_menu1.get() == 22:
            l_m_32_21['bg'] = 'black'
            l_m_32_21['fg'] = cl_p
            l_m_32_22['fg'] = 'black'
            l_m_32_22['bg'] = cl_p
            s_menu1.set(21)
    elif S.get() == 33:
        if s_menu1.get() == 1:
            l_m3_ship_spd_avg_val['fg'] = 'black'
            l_m3_ship_spd_avg_val['bg'] = cl_p
            l_m3_spd_data_select_val['bg'] = 'black'
            l_m3_spd_data_select_val['fg'] = cl_p
            s_menu1.set(5)
        elif s_menu1.get() == 11:
            l_m_33_11['bg'] = cl_p
            l_m_33_11['fg'] = 'black'
            l_m_33_14['fg'] = cl_p
            l_m_33_14['bg'] = 'black'
            s_menu1.set(14)
        elif s_menu1.get() == 12:
            l_m_33_12['bg'] = cl_p
            l_m_33_12['fg'] = 'black'
            l_m_33_11['fg'] = cl_p
            l_m_33_11['bg'] = 'black'
            s_menu1.set(11)
        elif s_menu1.get() == 13:
            l_m_33_13['bg'] = cl_p
            l_m_33_13['fg'] = 'black'
            l_m_33_12['fg'] = cl_p
            l_m_33_12['bg'] = 'black'
            s_menu1.set(12)
        elif s_menu1.get() == 14:
            l_m_33_14['bg'] = cl_p
            l_m_33_14['fg'] = 'black'
            l_m_33_13['fg'] = cl_p
            l_m_33_13['bg'] = 'black'
            s_menu1.set(13)
        elif s_menu1.get() == 2:
            l_m3_speed_offset_b['fg'] = 'black'
            l_m_33_21['fg'] = 'black'
            l_m_33_22['fg'] = 'black'
            l_m_33_23['fg'] = 'black'
            l_m_33_24['fg'] = 'black'
            l_m3_speed_offset_b['bg'] = cl_p
            l_m_33_21['bg'] = cl_p
            l_m_33_22['bg'] = cl_p
            l_m_33_23['bg'] = cl_p
            l_m_33_24['bg'] = cl_p
            l_m3_ship_spd_avg_val['bg'] = 'black'
            l_m3_ship_spd_avg_val['fg'] = cl_p
            s_menu1.set(1)
        elif s_menu1.get() == 3:
            l_m3_track_depth_m['fg'] = 'black'
            l_m_33_31['fg'] = 'black'
            l_m_33_32['fg'] = 'black'
            l_m3_track_depth_m['bg'] = cl_p
            l_m_33_31['bg'] = cl_p
            l_m_33_32['bg'] = cl_p
            l_m3_speed_offset_b['bg'] = 'black'
            l_m_33_21['bg'] = 'black'
            l_m_33_22['bg'] = 'black'
            l_m_33_23['bg'] = 'black'
            l_m_33_24['bg'] = 'black'
            l_m3_speed_offset_b['fg'] = cl_p
            l_m_33_21['fg'] = cl_p
            l_m_33_22['fg'] = cl_p
            l_m_33_23['fg'] = cl_p
            l_m_33_24['fg'] = cl_p
            s_menu1.set(2)
        elif s_menu1.get() == 4:
            l_m3_xdr_offset_d['fg'] = 'black'
            l_m_33_41['fg'] = 'black'
            l_m_33_42['fg'] = 'black'
            l_m_33_43['fg'] = 'black'
            l_m3_xdr_offset_d['bg'] = cl_p
            l_m_33_41['bg'] = cl_p
            l_m_33_42['bg'] = cl_p
            l_m_33_43['bg'] = cl_p
            l_m3_track_depth_m['bg'] = 'black'
            l_m_33_31['bg'] = 'black'
            l_m_33_32['bg'] = 'black'
            l_m3_track_depth_m['fg'] = cl_p
            l_m_33_31['fg'] = cl_p
            l_m_33_32['fg'] = cl_p
            s_menu1.set(3)
        elif s_menu1.get() == 5:
            l_m3_spd_data_select_val['fg'] = 'black'
            l_m3_spd_data_select_val['bg'] = cl_p
            l_m3_xdr_offset_d['bg'] = 'black'
            l_m_33_41['bg'] = 'black'
            l_m_33_42['bg'] = 'black'
            l_m_33_43['bg'] = 'black'
            l_m3_xdr_offset_d['fg'] = cl_p
            l_m_33_41['fg'] = cl_p
            l_m_33_42['fg'] = cl_p
            l_m_33_43['fg'] = cl_p
            s_menu1.set(4)
        elif s_menu1.get() == 21:
            s_m321_.set((s_m321_.get()+1)%2)
            if s_m321_.get() == 0:
                l_m_33_21['text'] = '+'
            elif s_m321_.get() == 1:
                l_m_33_21['text'] = '-'
        elif s_menu1.get() == 22:
            s_m322_.set((s_m322_.get()+1)%10)
            l_m_33_22['text'] = str(s_m322_.get())
        elif s_menu1.get() == 23:
            s_m323_.set((s_m323_.get()+1)%10)
            l_m_33_23['text'] = str(s_m323_.get())
        elif s_menu1.get() == 24:
            s_m324_.set((s_m324_.get()+1)%10)
            l_m_33_24['text'] = str(s_m324_.get())
        elif s_menu1.get() == 31:
            s_m331_.set((s_m331_.get()+1)%10)
            l_m_33_31['text'] = str(s_m331_.get())
        elif s_menu1.get() == 32:
            s_m332_.set((s_m332_.get()+1)%10)
            l_m_33_32['text'] = str(s_m332_.get())
        elif s_menu1.get() == 41:
            s_m341_.set((s_m341_.get()+1)%2)
            if s_m341_.get() == 0:
                l_m_33_41['text'] = '+'
            elif s_m341_.get() == 1:
                l_m_33_41['text'] = '-'
        elif s_menu1.get() == 42:
            s_m342_.set((s_m342_.get()+1)%10)
            l_m_33_42['text'] = str(s_m342_.get())
        elif s_menu1.get() == 43:
            s_m343_.set((s_m343_.get()+1)%10)
            l_m_33_43['text'] = str(s_m343_.get())
        elif s_menu1.get() == 51:
            l_m_33_51['bg'] = cl_p
            l_m_33_51['fg'] = 'black'
            l_m_33_53['fg'] = cl_p
            l_m_33_53['bg'] = 'black'
            s_menu1.set(53)
        elif s_menu1.get() == 52:
            l_m_33_52['bg'] = cl_p
            l_m_33_52['fg'] = 'black'
            l_m_33_51['fg'] = cl_p
            l_m_33_51['bg'] = 'black'
            s_menu1.set(51)
        elif s_menu1.get() == 53:
            l_m_33_53['bg'] = cl_p
            l_m_33_53['fg'] = 'black'
            l_m_33_52['fg'] = cl_p
            l_m_33_52['bg'] = 'black'
            s_menu1.set(52)
    elif S.get() == 34:
        if s_menu1.get() == 1:
            l_m4_test['fg'] = 'black'
            l_m4_test['bg'] = cl_p
            l_m4_lang_val['bg'] = 'black'
            l_m4_lang_val['fg'] =cl_p
            s_menu1.set(3)
        elif s_menu1.get() == 2:
            l_m4_dimmer_val['fg'] = 'black'
            l_m4_dimmer_val['bg'] = cl_p
            l_m4_test['bg'] = 'black'
            l_m4_test['fg'] = cl_p
            s_menu1.set(1)
        elif s_menu1.get() == 3:
            l_m4_lang_val['fg'] = 'black'
            l_m4_lang_val['bg'] =cl_p
            l_m4_dimmer_val['bg'] = 'black'
            l_m4_dimmer_val['fg'] = cl_p
            s_menu1.set(2)
        elif s_menu1.get() == 21:
            l_m_34_21['fg'] = 'black'
            l_m_34_21['bg'] = cl_p
            l_m_34_22['bg'] = 'black'
            l_m_34_22['fg'] = cl_p
            s_menu1.set(22)
        elif s_menu1.get() == 22:
            l_m_34_21['bg'] = 'black'
            l_m_34_21['fg'] = cl_p
            l_m_34_22['fg'] = 'black'
            l_m_34_22['bg'] = cl_p
            s_menu1.set(21)
        elif s_menu1.get() == 31:
            l_m_34_31['fg'] = 'black'
            l_m_34_31['bg'] = cl_p
            l_m_34_32['bg'] = 'black'
            l_m_34_32['fg'] = cl_p
            s_menu1.set(32)
        elif s_menu1.get() == 32:
            l_m_34_31['bg'] = 'black'
            l_m_34_31['fg'] = cl_p
            l_m_34_32['fg'] = 'black'
            l_m_34_32['bg'] = cl_p
            s_menu1.set(31)
def down():
    if S.get() == 3:
        if s_menu.get() == 0:
            l_m_distance_run_display['bg'] = cl_p
            l_m_distance_run_display['fg'] = 'black'
            l_m_sim['bg'] = 'black'
            l_m_sim['fg'] = cl_p
            s_menu.set(1)
        elif s_menu.get() == 1:
            l_m_sim['bg'] = cl_p
            l_m_sim['fg'] = 'black'
            l_m_system_menu['bg'] = 'black'
            l_m_system_menu['fg'] = cl_p
            s_menu.set(2)
        elif s_menu.get() == 2:
            l_m_sim['fg'] = 'black'
            l_m_system_menu['bg'] = cl_p
            l_m_system_menu['fg'] = 'black'
            l_m_system_menu2['bg'] = 'black'
            l_m_system_menu2['fg'] = cl_p  
            s_menu.set(3)
        elif s_menu.get() == 3:
            l_m_distance_run_display['bg'] = 'black'
            l_m_distance_run_display['fg'] = cl_p
            l_m_system_menu2['bg'] = cl_p
            l_m_system_menu2['fg'] = 'black'  
            s_menu.set(0)
    elif S.get() == 31:
        if s_menu1.get() == 0:
            l_m1_data_display_val['fg'] = 'black'
            l_m1_data_display_val['bg'] = cl_p
            l_m1_reset_val['fg'] = cl_p
            l_m1_reset_val['bg'] = 'black'
            s_menu1.set(1)
        elif s_menu1.get() == 1:
            l_m1_reset_val['bg'] = cl_p
            l_m1_reset_val['fg'] = 'black'
            dis_3131(1)
            s_menu1.set(2)
        elif s_menu1.get() == 2:
            l_m1_data_display_val['bg'] = 'black'
            l_m1_data_display_val['fg'] = cl_p
            dis_3131(0)
            s_menu1.set(0)
        elif s_menu1.get() == 3:
            if s_m11_.get() == 1:
                l_m_31_11['bg'] = cl_p
                l_m_31_11['fg'] = 'black'
                l_m_31_12['fg'] = cl_p
                l_m_31_12['bg'] = 'black'
                s_m11_.set(0)
            elif s_m11_.get() == 0:
                l_m_31_11['fg'] = cl_p
                l_m_31_11['bg'] = 'black'
                l_m_31_12['bg'] = cl_p
                l_m_31_12['fg'] = 'black'
                s_m11_.set(1)
        elif s_menu1.get() == 4:
            if s_m12_.get() == 0:
                l_m_31_21['bg'] = cl_p
                l_m_31_21['fg'] = 'black'
                l_m_31_22['fg'] = cl_p
                l_m_31_22['bg'] = 'black'
                s_m12_.set(1)
            elif s_m12_.get() == 1:
                l_m_31_21['fg'] = cl_p
                l_m_31_21['bg'] = 'black'
                l_m_31_22['bg'] = cl_p
                l_m_31_22['fg'] = 'black'
                s_m12_.set(0)
        elif s_menu1.get() == 51:
            s_m131_.set((s_m131_.get()-1)%10)
            l_m_31_31['text'] = str(s_m131_.get())
        elif s_menu1.get() == 52:
            s_m132_.set((s_m132_.get()-1)%10)
            l_m_31_32['text'] = str(s_m132_.get())
        elif s_menu1.get() == 53:
            s_m133_.set((s_m133_.get()-1)%10)
            l_m_31_33['text'] = str(s_m133_.get())
        elif s_menu1.get() == 54:
            s_m134_.set((s_m134_.get()-1)%10)
            l_m_31_34['text'] = str(s_m134_.get())
        elif s_menu1.get() == 55:
            s_m135_.set((s_m135_.get()-1)%10)
            l_m_31_35['text'] = str(s_m135_.get())
        elif s_menu1.get() == 56:
            s_m136_.set((s_m136_.get()-1)%10)
            l_m_31_36['text'] = str(s_m136_.get())
        elif s_menu1.get() == 57:
            s_m137_.set((s_m137_.get()-1)%10)
            l_m_31_37['text'] = str(s_m137_.get())
        elif s_menu1.get() == 58:
            s_m138_.set((s_m138_.get()-1)%10)
            l_m_31_38['text'] = str(s_m138_.get())
    elif S.get() == 32:
        if s_menu1.get() == 1:
            l_m_32_11['bg'] = cl_p   
            l_m_32_12['bg'] = cl_p   
            l_m_32_13['bg'] = cl_p   
            l_m_32_14['bg'] = cl_p   
            l_m2_speed_kn['bg'] = cl_p   
            l_m_32_11['fg'] = 'black'  
            l_m_32_12['fg'] = 'black'   
            l_m_32_13['fg'] = 'black'    
            l_m_32_14['fg'] = 'black'    
            l_m2_speed_kn['fg'] = 'black'     
            l_m2_data_display_val['bg'] = 'black'
            l_m2_data_display_val['fg'] = cl_p
            s_menu1.set(2)
        elif s_menu1.get() == 2:
            l_m_32_11['fg'] = cl_p   
            l_m_32_12['fg'] = cl_p   
            l_m_32_13['fg'] = cl_p   
            l_m_32_14['fg'] = cl_p   
            l_m2_speed_kn['fg'] = cl_p   
            l_m_32_11['bg'] = 'black'  
            l_m_32_12['bg'] = 'black'   
            l_m_32_13['bg'] = 'black'    
            l_m_32_14['bg'] = 'black'    
            l_m2_speed_kn['bg'] = 'black'     
            l_m2_data_display_val['bg'] = cl_p
            l_m2_data_display_val['fg'] = 'black'
            s_menu1.set(1)
        elif s_menu1.get() == 11:
            s_m211_.set((s_m211_.get()-1)%2)
            if s_m211_.get() == 0:
                l_m_32_11['text'] = '+'
            elif s_m211_.get() == 1:
                l_m_32_11['text'] = '-'
        elif s_menu1.get() == 12:
            s_m212_.set((s_m212_.get()-1)%10)
            l_m_32_12['text'] = str(s_m212_.get())
        elif s_menu1.get() == 13:
            s_m213_.set((s_m213_.get()-1)%10)
            l_m_32_13['text'] = str(s_m213_.get())
        elif s_menu1.get() == 14:
            s_m214_.set((s_m214_.get()-1)%10)
            l_m_32_14['text'] = str(s_m214_.get())
        elif s_menu1.get() == 21:
            l_m_32_21['fg'] = 'black'
            l_m_32_21['bg'] = cl_p
            l_m_32_22['bg'] = 'black'
            l_m_32_22['fg'] = cl_p
            s_menu1.set(22)
        elif s_menu1.get() == 22:
            l_m_32_21['bg'] = 'black'
            l_m_32_21['fg'] = cl_p
            l_m_32_22['fg'] = 'black'
            l_m_32_22['bg'] = cl_p
            s_menu1.set(21)
    elif S.get() == 33:
        if s_menu1.get() == 1:
            l_m3_ship_spd_avg_val['fg'] = 'black'
            l_m3_ship_spd_avg_val['bg'] = cl_p
            l_m3_speed_offset_b['bg'] = 'black'
            l_m_33_21['bg'] = 'black'
            l_m_33_22['bg'] = 'black'
            l_m_33_23['bg'] = 'black'
            l_m_33_24['bg'] = 'black'
            l_m3_speed_offset_b['fg'] = cl_p
            l_m_33_21['fg'] = cl_p
            l_m_33_22['fg'] = cl_p
            l_m_33_23['fg'] = cl_p
            l_m_33_24['fg'] = cl_p
            s_menu1.set(2)
        elif s_menu1.get() == 11:
            l_m_33_11['bg'] = cl_p
            l_m_33_11['fg'] = 'black'
            l_m_33_12['fg'] = cl_p
            l_m_33_12['bg'] = 'black'
            s_menu1.set(12)
        elif s_menu1.get() == 12:
            l_m_33_12['bg'] = cl_p
            l_m_33_12['fg'] = 'black'
            l_m_33_13['fg'] = cl_p
            l_m_33_13['bg'] = 'black'
            s_menu1.set(13)
        elif s_menu1.get() == 13:
            l_m_33_13['bg'] = cl_p
            l_m_33_13['fg'] = 'black'
            l_m_33_14['fg'] = cl_p
            l_m_33_14['bg'] = 'black'
            s_menu1.set(14)
        elif s_menu1.get() == 14:
            l_m_33_14['bg'] = cl_p
            l_m_33_14['fg'] = 'black'
            l_m_33_11['fg'] = cl_p
            l_m_33_11['bg'] = 'black'
            s_menu1.set(11)
        elif s_menu1.get() == 2:
            l_m3_speed_offset_b['fg'] = 'black'
            l_m_33_21['fg'] = 'black'
            l_m_33_22['fg'] = 'black'
            l_m_33_23['fg'] = 'black'
            l_m_33_24['fg'] = 'black'
            l_m3_speed_offset_b['bg'] = cl_p
            l_m_33_21['bg'] = cl_p
            l_m_33_22['bg'] = cl_p
            l_m_33_23['bg'] = cl_p
            l_m_33_24['bg'] = cl_p
            l_m3_track_depth_m['bg'] = 'black'
            l_m_33_31['bg'] = 'black'
            l_m_33_32['bg'] = 'black'
            l_m3_track_depth_m['fg'] = cl_p
            l_m_33_31['fg'] = cl_p
            l_m_33_32['fg'] = cl_p
            s_menu1.set(3)
        elif s_menu1.get() == 3:
            l_m3_track_depth_m['fg'] = 'black'
            l_m_33_31['fg'] = 'black'
            l_m_33_32['fg'] = 'black'
            l_m3_track_depth_m['bg'] = cl_p
            l_m_33_31['bg'] = cl_p
            l_m_33_32['bg'] = cl_p
            l_m3_xdr_offset_d['bg'] = 'black'
            l_m_33_41['bg'] = 'black'
            l_m_33_42['bg'] = 'black'
            l_m_33_43['bg'] = 'black'
            l_m3_xdr_offset_d['fg'] = cl_p
            l_m_33_41['fg'] = cl_p
            l_m_33_42['fg'] = cl_p
            l_m_33_43['fg'] = cl_p
            s_menu1.set(4)
        elif s_menu1.get() == 4:
            l_m3_xdr_offset_d['fg'] = 'black'
            l_m_33_41['fg'] = 'black'
            l_m_33_42['fg'] = 'black'
            l_m_33_43['fg'] = 'black'
            l_m3_xdr_offset_d['bg'] = cl_p
            l_m_33_41['bg'] = cl_p
            l_m_33_42['bg'] = cl_p
            l_m_33_43['bg'] = cl_p
            l_m3_spd_data_select_val['bg'] = 'black'
            l_m3_spd_data_select_val['fg'] = cl_p
            s_menu1.set(5)
        elif s_menu1.get() == 5:
            l_m3_spd_data_select_val['fg'] = 'black'
            l_m3_spd_data_select_val['bg'] = cl_p
            l_m3_ship_spd_avg_val['bg'] = 'black'
            l_m3_ship_spd_avg_val['fg'] = cl_p
            s_menu1.set(1)
        elif s_menu1.get() == 21:
            s_m321_.set((s_m321_.get()-1)%2)
            if s_m321_.get() == 0:
                l_m_33_21['text'] = '+'
            elif s_m321_.get() == 1:
                l_m_33_21['text'] = '-'
        elif s_menu1.get() == 22:
            s_m322_.set((s_m322_.get()-1)%10)
            l_m_33_22['text'] = str(s_m322_.get())
        elif s_menu1.get() == 23:
            s_m323_.set((s_m323_.get()-1)%10)
            l_m_33_23['text'] = str(s_m323_.get())
        elif s_menu1.get() == 24:
            s_m324_.set((s_m324_.get()-1)%10)
            l_m_33_24['text'] = str(s_m324_.get())
        elif s_menu1.get() == 31:
            s_m331_.set((s_m331_.get()-1)%10)
            l_m_33_31['text'] = str(s_m331_.get())
        elif s_menu1.get() == 32:
            s_m332_.set((s_m332_.get()-1)%10)
            l_m_33_32['text'] = str(s_m332_.get())
        elif s_menu1.get() == 41:
            s_m341_.set((s_m341_.get()-1)%2)
            if s_m341_.get() == 0:
                l_m_33_41['text'] = '+'
            elif s_m341_.get() == 1:
                l_m_33_41['text'] = '-'
        elif s_menu1.get() == 42:
            s_m342_.set((s_m342_.get()-1)%10)
            l_m_33_42['text'] = str(s_m342_.get())
        elif s_menu1.get() == 43:
            s_m343_.set((s_m343_.get()-1)%10)
            l_m_33_43['text'] = str(s_m343_.get())
        elif s_menu1.get() == 51:
            l_m_33_51['bg'] = cl_p
            l_m_33_51['fg'] = 'black'
            l_m_33_52['fg'] = cl_p
            l_m_33_52['bg'] = 'black'
            s_menu1.set(52)
        elif s_menu1.get() == 52:
            l_m_33_52['bg'] = cl_p
            l_m_33_52['fg'] = 'black'
            l_m_33_53['fg'] = cl_p
            l_m_33_53['bg'] = 'black'
            s_menu1.set(53)
        elif s_menu1.get() == 53:
            l_m_33_53['bg'] = cl_p
            l_m_33_53['fg'] = 'black'
            l_m_33_51['fg'] = cl_p
            l_m_33_51['bg'] = 'black'
            s_menu1.set(51)
    elif S.get() == 34:
        if s_menu1.get() == 1:
            l_m4_test['fg'] = 'black'
            l_m4_test['bg'] = cl_p
            l_m4_dimmer_val['bg'] = 'black'
            l_m4_dimmer_val['fg'] = cl_p
            s_menu1.set(2)
        elif s_menu1.get() == 2:
            l_m4_dimmer_val['fg'] = 'black'
            l_m4_dimmer_val['bg'] = cl_p
            l_m4_lang_val['bg'] = 'black'
            l_m4_lang_val['fg'] = cl_p
            s_menu1.set(3)
        elif s_menu1.get() == 3:
            l_m4_lang_val['fg'] = 'black'
            l_m4_lang_val['bg'] =cl_p
            l_m4_test['bg'] = 'black'
            l_m4_test['fg'] = cl_p
            s_menu1.set(1)
        elif s_menu1.get() == 21:
            l_m_34_21['fg'] = 'black'
            l_m_34_21['bg'] = cl_p
            l_m_34_22['bg'] = 'black'
            l_m_34_22['fg'] = cl_p
            s_menu1.set(22)
        elif s_menu1.get() == 22:
            l_m_34_21['bg'] = 'black'
            l_m_34_21['fg'] = cl_p
            l_m_34_22['fg'] = 'black'
            l_m_34_22['bg'] = cl_p
            s_menu1.set(21)
        elif s_menu1.get() == 31:
            l_m_34_31['fg'] = 'black'
            l_m_34_31['bg'] = cl_p
            l_m_34_32['bg'] = 'black'
            l_m_34_32['fg'] = cl_p
            s_menu1.set(32)
        elif s_menu1.get() == 32:
            l_m_34_31['bg'] = 'black'
            l_m_34_31['fg'] = cl_p
            l_m_34_32['fg'] = 'black'
            l_m_34_32['bg'] = cl_p
            s_menu1.set(31)
def left():
    if S.get() == 31:
        if s_menu1.get() == 51:
            l_m_31_31['bg'] = cl_p
            l_m_31_31['fg'] = 'black'
            l_m_31_38['fg'] = cl_p
            l_m_31_38['bg'] = 'black'
            s_menu1.set(58)
        elif s_menu1.get() == 52:
            l_m_31_32['bg'] = cl_p
            l_m_31_32['fg'] = 'black'
            l_m_31_31['fg'] = cl_p
            l_m_31_31['bg'] = 'black'
            s_menu1.set(51)
        elif s_menu1.get() == 53:
            l_m_31_33['bg'] = cl_p
            l_m_31_33['fg'] = 'black'
            l_m_31_32['fg'] = cl_p
            l_m_31_32['bg'] = 'black'
            s_menu1.set(52)
        elif s_menu1.get() == 54:
            l_m_31_34['bg'] = cl_p
            l_m_31_34['fg'] = 'black'
            l_m_31_33['fg'] = cl_p
            l_m_31_33['bg'] = 'black'
            s_menu1.set(53)
        elif s_menu1.get() == 55:
            l_m_31_35['bg'] = cl_p
            l_m_31_35['fg'] = 'black'
            l_m_31_34['fg'] = cl_p
            l_m_31_34['bg'] = 'black'
            s_menu1.set(54)
        elif s_menu1.get() == 56:
            l_m_31_36['bg'] = cl_p
            l_m_31_36['fg'] = 'black'
            l_m_31_35['fg'] = cl_p
            l_m_31_35['bg'] = 'black'
            s_menu1.set(55)
        elif s_menu1.get() == 57:
            l_m_31_37['bg'] = cl_p
            l_m_31_37['fg'] = 'black'
            l_m_31_36['fg'] = cl_p
            l_m_31_36['bg'] = 'black'
            s_menu1.set(56)
        elif s_menu1.get() == 58:
            l_m_31_38['bg'] = cl_p
            l_m_31_38['fg'] = 'black'
            l_m_31_37['fg'] = cl_p
            l_m_31_37['bg'] = 'black'
            s_menu1.set(57)
    elif S.get() == 32:
        if s_menu1.get() == 11:
            l_m_32_11['fg'] = 'black'
            l_m_32_14['bg'] = 'black'
            l_m_32_11['bg'] = cl_p
            l_m_32_14['fg'] = cl_p
            s_menu1.set(14)
        elif s_menu1.get() == 12:
            l_m_32_11['bg'] = 'black'
            l_m_32_12['fg'] = 'black'
            l_m_32_11['fg'] = cl_p
            l_m_32_12['bg'] = cl_p
            s_menu1.set(11)
        elif s_menu1.get() == 13:
            l_m_32_12['bg'] = 'black'
            l_m_32_13['fg'] = 'black'
            l_m_32_12['fg'] = cl_p
            l_m_32_13['bg'] = cl_p
            s_menu1.set(12)
        elif s_menu1.get() == 14:
            l_m_32_13['bg'] = 'black'
            l_m_32_14['fg'] = 'black'
            l_m_32_13['fg'] = cl_p
            l_m_32_14['bg'] = cl_p
            s_menu1.set(13)
    elif S.get() == 33:
        if s_menu1.get() == 21:
            l_m_33_21['fg'] = 'black'
            l_m_33_24['bg'] = 'black'
            l_m_33_21['bg'] = cl_p
            l_m_33_24['fg'] = cl_p
            s_menu1.set(24)
        elif s_menu1.get() == 22:
            l_m_33_21['bg'] = 'black'
            l_m_33_22['fg'] = 'black'
            l_m_33_21['fg'] = cl_p
            l_m_33_22['bg'] = cl_p
            s_menu1.set(21)
        elif s_menu1.get() == 23:
            l_m_33_22['bg'] = 'black'
            l_m_33_23['fg'] = 'black'
            l_m_33_22['fg'] = cl_p
            l_m_33_23['bg'] = cl_p
            s_menu1.set(22)
        elif s_menu1.get() == 24:
            l_m_33_23['bg'] = 'black'
            l_m_33_24['fg'] = 'black'
            l_m_33_23['fg'] = cl_p
            l_m_33_24['bg'] = cl_p
            s_menu1.set(23)
        if s_menu1.get() == 31:
            l_m_33_31['fg'] = 'black'
            l_m_33_32['bg'] = 'black'
            l_m_33_31['bg'] = cl_p
            l_m_33_32['fg'] = cl_p
            s_menu1.set(32)
        elif s_menu1.get() == 32:
            l_m_33_31['bg'] = 'black'
            l_m_33_32['fg'] = 'black'
            l_m_33_31['fg'] = cl_p
            l_m_33_32['bg'] = cl_p
            s_menu1.set(31)
        if s_menu1.get() == 41:
            l_m_33_41['fg'] = 'black'
            l_m_33_43['bg'] = 'black'
            l_m_33_41['bg'] = cl_p
            l_m_33_43['fg'] = cl_p
            s_menu1.set(43)
        elif s_menu1.get() == 42:
            l_m_33_41['bg'] = 'black'
            l_m_33_42['fg'] = 'black'
            l_m_33_41['fg'] = cl_p
            l_m_33_42['bg'] = cl_p
            s_menu1.set(41)
        elif s_menu1.get() == 43:
            l_m_33_42['bg'] = 'black'
            l_m_33_43['fg'] = 'black'
            l_m_33_42['fg'] = cl_p
            l_m_33_43['bg'] = cl_p
            s_menu1.set(42)
    elif S.get() == 34:
        if s_menu1.get() == 111:
            l_m_34_12['bg'] = 'black'
            l_m_34_12['fg'] = cl_p
            l_m_34_13['fg'] = 'black'
            l_m_34_13['bg'] = cl_p
            s_menu1.set(112)
        elif s_menu1.get() == 112:
            l_m_34_12['fg'] = 'black'
            l_m_34_12['bg'] = cl_p
            l_m_34_13['bg'] = 'black'
            l_m_34_13['fg'] = cl_p
            s_menu1.set(111)
def right():
    if S.get() == 31:
        if s_menu1.get() == 51:
            l_m_31_31['bg'] = cl_p
            l_m_31_31['fg'] = 'black'
            l_m_31_32['fg'] = cl_p
            l_m_31_32['bg'] = 'black'
            s_menu1.set(52)
        elif s_menu1.get() == 52:
            l_m_31_32['bg'] = cl_p
            l_m_31_32['fg'] = 'black'
            l_m_31_33['fg'] = cl_p
            l_m_31_33['bg'] = 'black'
            s_menu1.set(53)
        elif s_menu1.get() == 53:
            l_m_31_33['bg'] = cl_p
            l_m_31_33['fg'] = 'black'
            l_m_31_34['fg'] = cl_p
            l_m_31_34['bg'] = 'black'
            s_menu1.set(54)
        elif s_menu1.get() == 54:
            l_m_31_34['bg'] = cl_p
            l_m_31_34['fg'] = 'black'
            l_m_31_35['fg'] = cl_p
            l_m_31_35['bg'] = 'black'
            s_menu1.set(55)
        elif s_menu1.get() == 55:
            l_m_31_35['bg'] = cl_p
            l_m_31_35['fg'] = 'black'
            l_m_31_36['fg'] = cl_p
            l_m_31_36['bg'] = 'black'
            s_menu1.set(56)
        elif s_menu1.get() == 56:
            l_m_31_36['bg'] = cl_p
            l_m_31_36['fg'] = 'black'
            l_m_31_37['fg'] = cl_p
            l_m_31_37['bg'] = 'black'
            s_menu1.set(57)
        elif s_menu1.get() == 57:
            l_m_31_37['bg'] = cl_p
            l_m_31_37['fg'] = 'black'
            l_m_31_38['fg'] = cl_p
            l_m_31_38['bg'] = 'black'
            s_menu1.set(58)
        elif s_menu1.get() == 58:
            l_m_31_38['bg'] = cl_p
            l_m_31_38['fg'] = 'black'
            l_m_31_31['fg'] = cl_p
            l_m_31_31['bg'] = 'black'
            s_menu1.set(51)
    elif S.get() == 32:
        if s_menu1.get() == 11:
            l_m_32_11['fg'] = 'black'
            l_m_32_12['bg'] = 'black'
            l_m_32_11['bg'] = cl_p
            l_m_32_12['fg'] = cl_p
            s_menu1.set(12) 
        elif s_menu1.get() == 12:
            l_m_32_12['fg'] = 'black'
            l_m_32_13['bg'] = 'black'
            l_m_32_12['bg'] = cl_p
            l_m_32_13['fg'] = cl_p
            s_menu1.set(13) 
        elif s_menu1.get() == 13:
            l_m_32_13['fg'] = 'black'
            l_m_32_14['bg'] = 'black'
            l_m_32_13['bg'] = cl_p
            l_m_32_14['fg'] = cl_p
            s_menu1.set(14) 
        elif s_menu1.get() == 14:
            l_m_32_11['bg'] = 'black'
            l_m_32_14['fg'] = 'black'
            l_m_32_11['fg'] = cl_p
            l_m_32_14['bg'] = cl_p
            s_menu1.set(11) 
    elif S.get() == 33:
        if s_menu1.get() == 21:
            l_m_33_21['fg'] = 'black'
            l_m_33_22['bg'] = 'black'
            l_m_33_21['bg'] = cl_p
            l_m_33_22['fg'] = cl_p
            s_menu1.set(22)
        elif s_menu1.get() == 22:
            l_m_33_23['bg'] = 'black'
            l_m_33_22['fg'] = 'black'
            l_m_33_23['fg'] = cl_p
            l_m_33_22['bg'] = cl_p
            s_menu1.set(23)
        elif s_menu1.get() == 23:
            l_m_33_24['bg'] = 'black'
            l_m_33_23['fg'] = 'black'
            l_m_33_24['fg'] = cl_p
            l_m_33_23['bg'] = cl_p
            s_menu1.set(24)
        elif s_menu1.get() == 24:
            l_m_33_21['bg'] = 'black'
            l_m_33_24['fg'] = 'black'
            l_m_33_21['fg'] = cl_p
            l_m_33_24['bg'] = cl_p
            s_menu1.set(21)
        if s_menu1.get() == 31:
            l_m_33_31['fg'] = 'black'
            l_m_33_32['bg'] = 'black'
            l_m_33_31['bg'] = cl_p
            l_m_33_32['fg'] = cl_p
            s_menu1.set(32)
        elif s_menu1.get() == 32:
            l_m_33_31['bg'] = 'black'
            l_m_33_32['fg'] = 'black'
            l_m_33_31['fg'] = cl_p
            l_m_33_32['bg'] = cl_p
            s_menu1.set(31)
        if s_menu1.get() == 41:
            l_m_33_41['fg'] = 'black'
            l_m_33_42['bg'] = 'black'
            l_m_33_41['bg'] = cl_p
            l_m_33_42['fg'] = cl_p
            s_menu1.set(42)
        elif s_menu1.get() == 42:
            l_m_33_43['bg'] = 'black'
            l_m_33_42['fg'] = 'black'
            l_m_33_43['fg'] = cl_p
            l_m_33_42['bg'] = cl_p
            s_menu1.set(43)
        elif s_menu1.get() == 43:
            l_m_33_41['bg'] = 'black'
            l_m_33_43['fg'] = 'black'
            l_m_33_41['fg'] = cl_p
            l_m_33_43['bg'] = cl_p
            s_menu1.set(41)
    elif S.get() == 34:
        if s_menu1.get() == 111:
            l_m_34_12['fg'] = 'black'
            l_m_34_12['bg'] = cl_p
            l_m_34_13['bg'] = 'black'
            l_m_34_13['fg'] = cl_p
            s_menu1.set(112)
        elif s_menu1.get() == 112:
            l_m_34_12['bg'] = 'black'
            l_m_34_12['fg'] = cl_p
            l_m_34_13['fg'] = 'black'
            l_m_34_13['bg'] = cl_p
            s_menu1.set(111)
def ent():
    if S.get() == 3:
        hid_3()
        if s_menu.get() == 0:
            dis_31()
        elif s_menu.get() == 1:
            dis_32()
        elif s_menu.get() == 2:
            dis_33()
        elif s_menu.get() == 3:
            dis_34()
    elif S.get() == 31:
        if s_menu1.get() == 0:
            dis_311()
        elif s_menu1.get() == 1:
            dis_312()
        elif s_menu1.get() == 2:
            dis_3132()
        elif s_menu1.get() == 3:
            s_m11.set(s_m11_.get())
            hid_311()
            update_31()
        elif s_menu1.get() == 4:
            s_m12.set(s_m12_.get())
            hid_312()
            update_31()
        elif s_menu1.get() >= 51 and s_menu1.get() <= 58:
            s_m131.set(s_m131_.get())
            s_m132.set(s_m132_.get())
            s_m133.set(s_m133_.get())
            s_m134.set(s_m134_.get())
            s_m135.set(s_m135_.get())
            s_m136.set(s_m136_.get())
            s_m137.set(s_m137_.get())
            s_m138.set(s_m138_.get())
            hid_313()
            update_31()
            dis_3131(1)
    elif S.get() == 32:
        if s_menu1.get() == 1:
            l_m_32_12['bg'] = cl_p
            l_m_32_13['bg'] = cl_p
            l_m_32_14['bg'] = cl_p
            l_m2_speed_kn['bg'] = cl_p
            l_m_32_12['fg'] = 'black'
            l_m_32_13['fg'] = 'black'
            l_m_32_14['fg'] = 'black'
            l_m2_speed_kn['fg'] = 'black'
            s_menu1.set(11) 
        elif s_menu1.get() >= 11 and s_menu1.get() <= 14:
            s_m211.set(s_m211_.get())
            s_m212.set(s_m212_.get())
            s_m213.set(s_m213_.get())
            s_m214.set(s_m214_.get())
            update_32()
            dis_32()
        elif s_menu1.get() == 2:
            dis_322()
            s_menu1.set(21+s_m22.get())
        elif s_menu1.get() == 21 or s_menu1.get() == 22:
            hid_322()
            s_m22.set(s_menu1.get()-21)
            s_menu1.set(2)
            if s_m22.get() == 0:
                l_m2_data_display_val['text'] = 'N0'
            elif s_m22.get() == 1:
                l_m2_data_display_val['text'] = 'OFF'
    elif S.get() == 33:
        if s_menu1.get() == 1:
            dis_331()
        elif s_menu1.get() >= 11 and s_menu1.get() <= 14:
            s_m31.set(s_menu1.get()-10)
            if s_m31.get() == 1:
                l_m3_ship_spd_avg_val['text'] = '15 SEC'
            elif s_m31.get() == 2:
                l_m3_ship_spd_avg_val['text'] = '30 SEC'
            elif s_m31.get() == 3:
                l_m3_ship_spd_avg_val['text'] = '45 SEC'
            elif s_m31.get() == 4:
                l_m3_ship_spd_avg_val['text'] = '60 SEC'
            hid_331()
        elif s_menu1.get() == 2:
            l_m_33_22['bg'] = cl_p
            l_m_33_23['bg'] = cl_p
            l_m_33_24['bg'] = cl_p
            l_m3_speed_offset_b['bg'] = cl_p
            l_m_33_22['fg'] = 'black'
            l_m_33_23['fg'] = 'black'
            l_m_33_24['fg'] = 'black'
            l_m3_speed_offset_b['fg'] = 'black'
            s_menu1.set(21)
        elif s_menu1.get() == 3:
            l_m_33_32['bg'] = cl_p
            l_m3_track_depth_m['bg'] = cl_p
            l_m_33_32['fg'] = 'black'
            l_m3_track_depth_m['fg'] = 'black'
            s_menu1.set(31)
        elif s_menu1.get() == 4:
            l_m_33_42['bg'] = cl_p
            l_m_33_43['bg'] = cl_p
            l_m3_xdr_offset_d['bg'] = cl_p
            l_m_33_42['fg'] = 'black'
            l_m_33_43['fg'] = 'black'
            l_m3_xdr_offset_d['fg'] = 'black'
            s_menu1.set(41)
        elif s_menu1.get() == 5:
            dis_335()
        elif s_menu1.get() >= 21 and s_menu1.get() <= 24:
            s_m321.set(s_m321_.get())
            s_m322.set(s_m322_.get())
            s_m323.set(s_m323_.get())
            s_m324.set(s_m324_.get())
            l_m3_speed_offset_b['bg'] = 'black'
            l_m_33_21['bg'] = 'black'
            l_m_33_22['bg'] = 'black'
            l_m_33_23['bg'] = 'black'
            l_m_33_24['bg'] = 'black'
            l_m3_speed_offset_b['fg'] = cl_p
            l_m_33_21['fg'] = cl_p
            l_m_33_22['fg'] = cl_p
            l_m_33_23['fg'] = cl_p
            l_m_33_24['fg'] = cl_p
            update_33()
            s_menu1.set(2)
        elif s_menu1.get() >= 31 and s_menu1.get() <= 32:
            s_m331.set(s_m331_.get())
            s_m332.set(s_m332_.get())
            l_m3_track_depth_m['bg'] = 'black'
            l_m_33_31['bg'] = 'black'
            l_m_33_32['bg'] = 'black'
            l_m3_track_depth_m['fg'] = cl_p
            l_m_33_31['fg'] = cl_p
            l_m_33_32['fg'] = cl_p
            update_33()
            s_menu1.set(3)
        elif s_menu1.get() >= 41 and s_menu1.get() <= 43:
            s_m341.set(s_m341_.get())
            s_m342.set(s_m342_.get())
            s_m343.set(s_m343_.get())
            l_m3_xdr_offset_d['bg'] = 'black'
            l_m_33_41['bg'] = 'black'
            l_m_33_42['bg'] = 'black'
            l_m_33_43['bg'] = 'black'
            l_m3_xdr_offset_d['fg'] = cl_p
            l_m_33_41['fg'] = cl_p
            l_m_33_42['fg'] = cl_p
            l_m_33_43['fg'] = cl_p
            update_33()
            s_menu1.set(4)
        elif s_menu1.get() >= 51 and s_menu1.get() <= 53:
            s_m35.set(s_menu1.get()-50)
            if s_m35.get() == 1:
                l_m3_spd_data_select_val['text'] = 'GPS'
            elif s_m35.get() == 2:
                l_m3_spd_data_select_val['text'] = 'DOPPLER'
            elif s_m35.get() == 3:
                l_m3_spd_data_select_val['text'] = 'AUTO'
            hid_335()
    elif S.get() == 34:
        if s_menu1.get() == 1:
            dis_341()
        elif s_menu1.get() == 2:
            dis_342()
            s_menu1.set(21+s_m42.get())
        elif s_menu1.get() == 3:
            dis_343()
            s_menu1.set(31+s_m43.get())
        elif s_menu1.get() == 111:
            hid_34()
            dis_test()
            s_menu1.set(113)
        elif s_menu1.get() == 112:
            hid_341()
        elif s_menu1.get() == 21 or s_menu1.get() == 22:
            hid_342()
            s_m42.set(s_menu1.get()-21)
            s_menu1.set(2)
            if s_m42.get() == 0:
                l_m4_dimmer_val['text'] = 'INTERNAL'
            elif s_m42.get() == 1:
                l_m4_dimmer_val['text'] = 'EXTERNAL'
        elif s_menu1.get() == 31 or s_menu1.get() == 32:
            hid_343()
            s_m43.set(s_menu1.get()-31)
            if s_m43.get() == 0:
                l_m4_lang_val['text'] = 'ENGLISH'
            elif s_m43.get() == 1:
                l_m4_lang_val['text'] = 'にほんご'
            s_menu1.set(3)
            
## 按钮
if True:
    img_label = Label(window, imag=photo)
    img_label.pack()

    b_u = Button(window,imag=p_u,bd=0,width=49,height=49,command=up).place(x=1002,y=68)               
    b_d = Button(window,imag=p_d,bd=0,width=49,height=49,command=down).place(x=1003,y=162)             
    b_l = Button(window,imag=p_l,bd=0,width=49,height=49,command=left).place(x=941,y=113)
    b_r = Button(window,imag=p_r,bd=0,width=49,height=49,command=right).place(x=1061,y=115)

    b_menu = Button(window,imag=p_menu,bd=0,width=81,height=55,command=menu).place(x=924,y=259)
    b_ent = Button(window,imag=p_ent,bd=0,width=81,height=55,command=ent).place(x=1044,y=260)
    b_disp = Button(window,imag=p_disp,bd=0,width=81,height=55,command=disp).place(x=924,y=344)
    b_dim = Button(window,imag=p_dim,bd=0,width=81,height=55).place(x=1043,y=344)

    b_xing = Button(window,imag=p_xing,bd=0,width=110,height=57).place(x=971,y=425)
    b_pwr= Button(window,imag=p_pwr,bd=0,width=95,height=75,command=on_of).place(x=1038,y=534)

## Label(初始页+disp页)
if True:
    l_speed = Label(window,text='SPEED',bg=cl_p,font = "Verdana 40 bold",width=5,height=1)
    l_distance = Label(window,text='DISTANCE',bg=cl_p,font = "Verdana 40 bold",width=8,height=1)
    l_sim = Label(window,text='',bg=cl_p,font = "Verdana 40 bold",width=5,height=1)
    l_speed_num = Label(window,text='▲ 10.0',bg=cl_p,width=5,height=1)
    l_kn = Label(window,text='kn',bg=cl_p,width=2,height=1)
    l_distance_num = Label(window,text='0.30',bg=cl_p,font = "Verdana 80 bold",width=4,height=1)
    l_nm = Label(window,text='NM',bg=cl_p,font = "Verdana 40 bold",width=2,height=1)

## Label(MENU页)
if True:
    l_menu = Label(window,text='MENU',bg=cl_p,font = "Verdana 33 bold",width=5,height=1)
    l_line = Label(window,text='',bg='black',font = "Verdana 1 bold",width=620,height=1)
    l_m_distance_run_display = Label(window,text='DISTANCE RUN DISPLAY',font = "Verdana 33 bold",width=20,height=1)             # 主菜单第一项
    l_m_sim = Label(window,text='SIM',bg=cl_p,font = "Verdana 33 bold",width=4,height=1)                                        # 主菜单第二项
    l_m_system_menu = Label(window,text='SYSTEM MENU',bg=cl_p,font = "Verdana 33 bold",width=12,height=1)                       # 主菜单第三项
    l_m_system_menu2 = Label(window,text='SYSTEM MENU2',bg=cl_p,font = "Verdana 33 bold",width=13,height=1)                     # 主菜单第四项
    l_m_ent_set = Label(window,text='ENT:SET',bg=cl_p,font = "Verdana 33 bold",width=7,height=1)

## Label(MENU_1页)
if True:
    l_m1_distance_run_displa = Label(window,text='DISTANCE RUN DISPLAY',bg=cl_p,font = "Verdana 33 bold",width=20,height=1)
    l_m1_data_display = Label(window,text='DATA DISPLAY',bg=cl_p,font = "Verdana 33 bold",width=12,height=1)            # 主菜单_1第一项
    l_m1_data_display_val = Label(window,font = "Verdana 33 bold",width=15,height=1)                                    # 主菜单_1第一项值
    l_m1_reset = Label(window,text='RESET',bg=cl_p,font = "Verdana 33 bold",width=5,height=1)                           # 主菜单_1第二项
    l_m1_reset_val = Label(window,text='OFF',font = "Verdana 33 bold",width=3,height=1)                                 # 主菜单_1第二项值
    l_m1_set = Label(window,text='SET',bg=cl_p,font = "Verdana 33 bold",width=3,height=1)                               # 主菜单_1第三项
    l_m1_set_nm = Label(window,text='.     NM',font = "Verdana 33 bold",width=6,height=1)            

    l_m_31_31 = Label(window,text='',font = "Verdana 33 bold",width=1,height=1) 
    l_m_31_32 = Label(window,text='',font = "Verdana 33 bold",width=1,height=1) 
    l_m_31_33 = Label(window,text='',font = "Verdana 33 bold",width=1,height=1) 
    l_m_31_34 = Label(window,text='',font = "Verdana 33 bold",width=1,height=1) 
    l_m_31_35 = Label(window,text='',font = "Verdana 33 bold",width=1,height=1) 
    l_m_31_36 = Label(window,text='',font = "Verdana 33 bold",width=1,height=1) 
    l_m_31_37 = Label(window,text='',font = "Verdana 33 bold",width=1,height=1) 
    l_m_31_38 = Label(window,text='',font = "Verdana 33 bold",width=1,height=1) 

    l_m_31_11 = Label(window,text='IEC61162(VLW)',font = "Verdana 33 bold",width=15,height=1)
    l_m_31_12 = Label(window,text='CONTACT CLOSURE',font = "Verdana 33 bold",width=15,height=1)

    l_m_31_21 = Label(window,text='OFF',font = "Verdana 33 bold",width=3,height=1)
    l_m_31_22 = Label(window,text='ON',font = "Verdana 33 bold",width=3,height=1)

## Label(MENU_2页)
if True:
    l_m2_sim = Label(window,text='SIM',bg=cl_p,font = "Verdana 33 bold",width=3,height=1)
    l_m2_speed = Label(window,text='SPEED',bg=cl_p,font = "Verdana 33 bold",width=5,height=1)                   # 主菜单_2第一项
    l_m2_speed_kn = Label(window,text='.     kn',font = "Verdana 33 bold",width=5,height=1)                       # 主菜单_2第一项值
    l_m2_data_display = Label(window,text='DATA DISPLAY',bg=cl_p,font = "Verdana 33 bold",width=12,height=1)    # 主菜单_2第二项
    l_m2_data_display_val = Label(window,text='NO',font = "Verdana 33 bold",width=3,height=1)                  # 主菜单_2第二项值

    l_m_32_11 = Label(window,text='+',font = "Verdana 33 bold",width=1,height=1) 
    l_m_32_12 = Label(window,text='1',font = "Verdana 33 bold",width=1,height=1) 
    l_m_32_13 = Label(window,text='0',font = "Verdana 33 bold",width=1,height=1) 
    l_m_32_14 = Label(window,text='0',font = "Verdana 33 bold",width=1,height=1) 
    l_m_32_21 = Label(window,text='ON',font = "Verdana 33 bold",width=3,height=1) 
    l_m_32_22 = Label(window,text='OFF',font = "Verdana 33 bold",width=3,height=1) 

## Label(MENU_3页)
if True:
    l_m3_system_menu = Label(window,text='SYSTEM MENU',bg=cl_p,font = "Verdana 28 bold",width=12,height=1)
    l_m3_ship_spd_avg = Label(window,text='SHP SPD AVG',bg=cl_p,font = "Verdana 28 bold",width=12,height=1)
    l_m3_ship_spd_avg_val = Label(window,text='30 SEC',bg=cl_p,font = "Verdana 28 bold",width=6,height=1)
    l_m3_speed_offset = Label(window,text='SPEED OFFSET',bg=cl_p,font = "Verdana 28 bold",width=12,height=1)
    l_m3_speed_offset_b = Label(window,text='.   %',bg=cl_p,font = "Verdana 28 bold",width=4,height=1)
    l_m3_track_depth = Label(window,text='TRACK DEPTH',bg=cl_p,font = "Verdana 28 bold",width=11,height=1)
    l_m3_track_depth_m = Label(window,text='.   m',bg=cl_p,font = "Verdana 28 bold",width=4,height=1)
    l_m3_xdr_offset = Label(window,text='XDR OFFSET',bg=cl_p,font = "Verdana 28 bold",width=10,height=1)
    l_m3_xdr_offset_d = Label(window,text='°',bg=cl_p,font = "Verdana 28 bold",width=1,height=1)
    l_m3_spd_data_select = Label(window,text='SPD DATA SELCET',bg=cl_p,font = "Verdana 28 bold",width=14,height=1)
    l_m3_spd_data_select_val = Label(window,text='GPS',bg=cl_p,font = "Verdana 28 bold",width=8,height=1)
    
    l_m_33_21 = Label(window,text='+',bg=cl_p,font = "Verdana 28 bold",width=1,height=1) 
    l_m_33_22 = Label(window,text='0',bg=cl_p,font = "Verdana 28 bold",width=1,height=1) 
    l_m_33_23 = Label(window,text='0',bg=cl_p,font = "Verdana 28 bold",width=1,height=1) 
    l_m_33_24 = Label(window,text='0',bg=cl_p,font = "Verdana 28 bold",width=1,height=1) 

    l_m_33_31 = Label(window,text='2',bg=cl_p,font = "Verdana 28 bold",width=1,height=1) 
    l_m_33_32 = Label(window,text='0',bg=cl_p,font = "Verdana 28 bold",width=1,height=1) 

    l_m_33_41 = Label(window,text='+',bg=cl_p,font = "Verdana 28 bold",width=1,height=1) 
    l_m_33_42 = Label(window,text='0',bg=cl_p,font = "Verdana 28 bold",width=1,height=1) 
    l_m_33_43 = Label(window,text='0',bg=cl_p,font = "Verdana 28 bold",width=1,height=1) 

    l_m_33_11 = Label(window,text='15 SEC',font = "Verdana 28 bold",width=6,height=1) 
    l_m_33_12 = Label(window,text='30 SEC',font = "Verdana 28 bold",width=6,height=1) 
    l_m_33_13 = Label(window,text='45 SEC',font = "Verdana 28 bold",width=6,height=1) 
    l_m_33_14 = Label(window,text='60 SEC',font = "Verdana 28 bold",width=6,height=1) 

    l_m_33_51 = Label(window,text='GPS',bg=cl_p,font = "Verdana 28 bold",width=8,height=1) 
    l_m_33_52 = Label(window,text='DOPPLER',bg=cl_p,font = "Verdana 28 bold",width=8,height=1) 
    l_m_33_53 = Label(window,text='AUTO',bg=cl_p,font = "Verdana 28 bold",width=8,height=1) 

## Label(MENU_4页)
if True:
    l_m4_system_menu2 = Label(window,text='SYSTEM MENU2',bg=cl_p,font = "Verdana 33 bold",width=13,height=1)
    l_m4_test = Label(window,text='TEST',bg=cl_p,font = "Verdana 33 bold",width=5,height=1)
    l_m4_dimmer = Label(window,text='DIMMER',bg=cl_p,font = "Verdana 33 bold",width=7,height=1)
    l_m4_dimmer_val = Label(window,text='INTERNAL',bg=cl_p,font = "Verdana 33 bold",width=9,height=1)
    l_m4_lang = Label(window,text='言語/LANG',bg=cl_p,font = "Verdana 33 bold",width=8,height=1)
    l_m4_lang_val = Label(window,text='ENGLISH',bg=cl_p,font = "Verdana 33 bold",width=8,height=1)

    l_m_34_11 = Label(window,text='TEST START ?\n(STOP: PWR OFF)\nare you sure?',bg=cl_p,font = "Verdana 33 bold",width=16,height=3)
    l_m_34_12 = Label(window,text='YES',font = "Verdana 33 bold",width=3,height=1)
    l_m_34_13 = Label(window,text='NO',font = "Verdana 33 bold",width=3,height=1)
    l_m_34_21 = Label(window,text='INTERNAL',font = "Verdana 33 bold",width=9,height=1)
    l_m_34_22 = Label(window,text='EXTERNAL',font = "Verdana 33 bold",width=9,height=1)
    l_m_34_31 = Label(window,text='ENGLISH',font = "Verdana 33 bold",width=8,height=1)
    l_m_34_32 = Label(window,text='にほんご',font = "Verdana 33 bold",width=8,height=1)

## Lablel(test页)
if True:
    l_t_test = Label(window,text='TEST',bg=cl_p,font = "Verdana 33 bold",width=4,height=1)
    l_t_rs = Label(window,text='ROM             :OK   80.4C  x  \nRAM             :OK                  \nSIO              :OK                  ',bg=cl_p,font = "Verdana 30 bold",width=23,height=3)
    l_t_pk = Label(window,text='PUSH KEY',bg='black',fg=cl_p,font = "Verdana 30 bold",width=9,height=1)
    l_t_o = Label(window,text='  (STOP:PWR OFF)  65501010061 \n\t               6550101003J\nCMT\t               6550101004k',bg=cl_p,font = "Verdana 25 bold",width=26,height=3)

window.mainloop()