#!/usr/bin/env python3

# ---------------------------------------------------------------------------- #
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import sys
import math
import time
import glob
import os

# ---------------------------------------------------------------------------- #
def specialkeys(key, x, y):
    global xrot
    global yrot
    global zrot
    global scale
    global start_xrot
    global start_yrot
    global start_zrot
    global start_scale
    global end_xrot
    global end_yrot
    global end_zrot
    global end_scale
    global l_ambi
    global t_help
    global t_menu
    global t_osdinfo
    global menu_sel_item
    global line_width
    global color_line_i
    global color_line_i_max
    global color_line_a
    global sel_mol
    global max_mol
    global animation_time
    global animation_frame
    global animation_procces
    global animation_loop
    global animation_count
    global animation_rec

    if key == GLUT_KEY_UP:
        if not t_menu:
            xrot -= 2.0
        else:
            menu_sel_item -= 1
            if menu_sel_item < 0:
                menu_sel_item = menu_max_item

    if key == GLUT_KEY_DOWN:
        if not t_menu:
            xrot += 2.0
        else:
            menu_sel_item += 1
            if menu_sel_item > menu_max_item:
                menu_sel_item = 0

    if key == GLUT_KEY_LEFT:
        if not t_menu:
            yrot -= 2.0
        else:
            if menu_sel_item == 0:
                sel_mol -= 1
                if sel_mol < 0:
                    sel_mol = max_mol
            elif menu_sel_item == 1:
                xrot -= 2.0
            elif menu_sel_item == 2:
                yrot -= 2.0
            elif menu_sel_item == 3:
                zrot -= 2.0
            elif menu_sel_item == 4:
                scale -= 0.05
            elif menu_sel_item == 5:
                l_ambi -= 0.02
                if l_ambi < 0.02:
                    l_ambi = 0.02
            elif menu_sel_item == 6:
                line_width -= 0.1
                if line_width < 0.0:
                    line_width = 0.0
            elif menu_sel_item == 7:
                color_line_i -= 1
                if color_line_i < 0:
                    color_line_i = color_line_i_max
            elif menu_sel_item == 8:
                color_line_a -= 0.05
                if color_line_a < 0.0:
                    color_line_a = 0.0
            elif menu_sel_item == 9:
                start_xrot -= 2.0
                xrot = start_xrot
            elif menu_sel_item == 10:
                start_yrot -= 2.0
                yrot = start_yrot
            elif menu_sel_item == 11:
                start_zrot -= 2.0
                zrot = start_zrot
            elif menu_sel_item == 12:
                start_scale -= 0.05
                scale = start_scale
            elif menu_sel_item == 13:
                end_xrot -= 2.0
                xrot = end_xrot
            elif menu_sel_item == 14:
                end_yrot -= 2.0
                yrot = end_yrot
            elif menu_sel_item == 15:
                end_zrot -= 2.0
                zrot = end_zrot
            elif menu_sel_item == 16:
                end_scale -= 0.05
                scale = end_scale
            elif menu_sel_item == 17:
                animation_time -= 2
                if animation_time < 10:
                    animation_time = 10
            elif menu_sel_item == 18:
                animation_frame -= 1
                if animation_frame < 1:
                    animation_frame = 1

    if key == GLUT_KEY_RIGHT:
        if not t_menu:
            yrot += 2.0
        else:
            if menu_sel_item == 0:
                sel_mol += 1
                if sel_mol > max_mol:
                    sel_mol = 0
            elif menu_sel_item == 1:
                xrot += 2.0
            elif menu_sel_item == 2:
                yrot += 2.0
            elif menu_sel_item == 3:
                zrot += 2.0
            elif menu_sel_item == 4:
                scale += 0.05
            elif menu_sel_item == 5:
                l_ambi += 0.02
                if l_ambi > 1.00:
                    l_ambi = 1.00
            elif menu_sel_item == 6:
                line_width += 0.1
                if line_width > 40.0:
                    line_width = 40.0
            elif menu_sel_item == 7:
                color_line_i += 1
                if color_line_i > color_line_i_max:
                    color_line_i = 0
            elif menu_sel_item == 8:
                color_line_a += 0.05
                if color_line_a > 1.0:
                    color_line_a = 1.0
            elif menu_sel_item == 9:
                start_xrot += 2.0
                xrot = start_xrot
            elif menu_sel_item == 10:
                start_yrot += 2.0
                yrot = start_yrot
            elif menu_sel_item == 11:
                start_zrot += 2.0
                zrot = start_zrot
            elif menu_sel_item == 12:
                start_scale += 0.05
                scale = start_scale
            elif menu_sel_item == 13:
                end_xrot += 2.0
                xrot = end_xrot
            elif menu_sel_item == 14:
                end_yrot += 2.0
                yrot = end_yrot
            elif menu_sel_item == 15:
                end_zrot += 2.0
                zrot = end_zrot
            elif menu_sel_item == 16:
                end_scale += 0.05
                scale = end_scale
            elif menu_sel_item == 17:
                animation_time += 2
            elif menu_sel_item == 18:
                animation_frame += 1

    if key == GLUT_KEY_PAGE_UP:
        if not t_menu:
            zrot += 2.0

    if key == GLUT_KEY_PAGE_DOWN:
        if not t_menu:
            zrot -= 2.0

    if key == GLUT_KEY_INSERT:
        if not t_menu:
            xrot = 0.0
            yrot = 0.0
            zrot = 0.0

    if key == GLUT_KEY_HOME:
        if not t_menu:
            scale -= 0.05

    if key == GLUT_KEY_END:
        if not t_menu:
            scale += 0.05

    if key == GLUT_KEY_F1:
        t_help = not t_help
        t_menu = 0
        t_osdinfo = 0

    if key == GLUT_KEY_F2:
        t_help = 0
        t_menu = not t_menu
        t_osdinfo = 0

    if key == GLUT_KEY_F3:
        t_help = 0
        t_menu = 0
        t_osdinfo = not t_osdinfo

    if key == GLUT_KEY_F5:
        t_help = 0
        t_menu = 0
        animation_procces = 1
        animation_loop = 0
        animation_count = 0
        start_animation()

    if key == GLUT_KEY_F8:
        t_help = 0
        t_menu = 0
        animation_procces = 1
        animation_loop = 0
        animation_count = 0
        animation_rec = 1
        start_animation()

    if key == GLUT_KEY_F12:
        exit()


    reshape(win_width, win_height)
    glutPostRedisplay()

# ---------------------------------------------------------------------------- #
def reshape(w, h):
    global win_width
    global win_height
    win_width = w
    win_height = h
    light_mat_specular = (1,1,1,1)
    light0_diffuse = (l_ambi, l_ambi, l_ambi, 1.0) 
    light0_direction = (0.0, 0.0, 1.0, 0.0) 
    glClearColor(color_clear[0], color_clear[1], color_clear[2], color_clear[3])
    glShadeModel(GL_FLAT);
    glViewport(0, 0, win_width, win_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
    glEnable(GL_LINE_SMOOTH)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_NORMALIZE)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0);
    glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, light_mat_specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 128.0)
    glEnable(GL_LIGHT0) 
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light0_diffuse) 
    glLightfv(GL_LIGHT0, GL_POSITION, light0_direction)



# ---------------------------------------------------------------------------- #
def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glScalef(scale, scale, scale)
    glPushMatrix()
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glRotatef(zrot, 0.0, 0.0, 1.0)

    # lines
    l = line_width * scale
    if l > 0 and color_line_a > 0.01:
        la = color_line_a * color_line_a
        glColor4f(color_line[color_line_i][0],
                  color_line[color_line_i][1],
                  color_line[color_line_i][2],
                  la)
        glLineWidth(l)
        for i in mol[sel_mol][1]:
            for j in i[5]:
                glDisable(GL_LIGHTING)
                glBegin(GL_LINES)
                k = int(j)
                glVertex3f(i[1], i[2], i[3])
                glVertex3f(mol[sel_mol][1][k][1],
                           mol[sel_mol][1][k][2],
                           mol[sel_mol][1][k][3])
                glEnd()
                glEnable(GL_LIGHTING)

    # spheres
    for i in mol[sel_mol][1]:
        glColor4f(color_line[int(i[4])][0],
                  color_line[int(i[4])][1], 
                  color_line[int(i[4])][2],  
                  1.0)
        glTranslatef(i[1], i[2], i[3])
        glutSolidSphere(0.1, 100, 100)
        glTranslatef(0.0 - i[1], 0.0 -  i[2], 0.0 -  i[3])
    glPopMatrix()

    # Text
    if t_help:
        glEnter2D()
        glColor3f(color_t_help[0],color_t_help[1],color_t_help[2])
        i = 20
        glWrite(12, i, "F1            : Help");                   i += 12
        glWrite(12, i, "F2            : Menu");                   i += 12
        glWrite(12, i, "F3            : OSD Info");               i += 12
        glWrite(12, i, "F5            : Animation");              i += 12
        #glWrite(12, i, "F6            : Animation (loop)");       i += 12
        #glWrite(12, i, "F7            : Animation stop");         i += 12
        glWrite(12, i, "F8            : Record animation");       i += 12
        glWrite(12, i, "UP,DOWN       : Axis X");                 i += 12
        glWrite(12, i, "LEFT,RIGHT    : Axis Y");                 i += 12
        glWrite(12, i, "PG_UP,PG_DOWN : Axis Z");                 i += 12
        glWrite(12, i, "INSERT        : Reset Axis XYZ");         i += 12
        glWrite(12, i, "HOME,END      : Zoom");                   i += 12
        glWrite(12, i, "F12           : Exit")

        glLeave2D()

    elif t_menu:
        glEnter2D()

        i = 20
        if menu_sel_item == 0:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Structure:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d > < %s >" % (sel_mol, mol[sel_mol][0]))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Structure:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d > < %s >" % (sel_mol, mol[sel_mol][0]))

        i += 20
        if xrot > 0:
            xr = xrot + 0.01
        else:
            xr = xrot - 0.01
        if menu_sel_item == 1:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Axis X:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (xr))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Axis X:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (xr))

        i += 12
        if yrot > 0:
            yr = yrot + 0.01
        else:
            yr = yrot - 0.01
        if menu_sel_item == 2:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Axis Y:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (yr))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Axis Y:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (yr))

        i += 12
        if zrot > 0:
            zr = zrot + 0.01
        else:
            zr = zrot - 0.01
        if menu_sel_item == 3:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Axis Z:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (zr))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Axis Z:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (zr))

        i += 12
        if scale > 0:
            sc = (scale + 0.0001) * 100
        else:
            sc = (scale - 0.0001) * 100
        if menu_sel_item == 4:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Scale:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (sc))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Scale:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (sc))

        i += 20
        lt = l_ambi * 100
        if menu_sel_item == 5:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Light:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (lt))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Light:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (lt))

        i += 12
        lw = line_width * 100
        if menu_sel_item == 6:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Line Width:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (lw))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Line Width:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (lw))

        i += 12
        if menu_sel_item == 7:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Line Color:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (color_line_i))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Line Color:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (color_line_i))

        i += 12
        la = color_line_a * 100
        if menu_sel_item == 8:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Line Trns:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (la))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Line Trns:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (la))


        i += 20
        glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
        glWrite(12, i, "Animation start:")

        i += 20
        if start_xrot > 0:
            xr = start_xrot + 0.01
        else:
            xr = start_xrot - 0.01
        if menu_sel_item == 9:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Axis X:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (xr))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Axis X:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (xr))

        i += 12
        if start_yrot > 0:
            yr = start_yrot + 0.01
        else:
            yr = start_yrot - 0.01
        if menu_sel_item == 10:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Axis Y:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (yr))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Axis Y:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (yr))

        i += 12
        if start_zrot > 0:
            zr = start_zrot + 0.01
        else:
            zr = start_zrot - 0.01
        if menu_sel_item == 11:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Axis Z:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (zr))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Axis Z:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (zr))

        i += 12
        if start_scale > 0:
            sc = (start_scale + 0.0001) * 100
        else:
            sc = (start_scale - 0.0001) * 100
        if menu_sel_item == 12:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Scale:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (sc))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Scale:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (sc))


        i += 20
        glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
        glWrite(12, i, "Animation end:")

        i += 20
        if end_xrot > 0:
            xr = end_xrot + 0.01
        else:
            xr = end_xrot - 0.01
        if menu_sel_item == 13:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Axis X:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (xr))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Axis X:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (xr))

        i += 12
        if end_yrot > 0:
            yr = end_yrot + 0.01
        else:
            yr = end_yrot - 0.01
        if menu_sel_item == 14:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Axis Y:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (yr))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Axis Y:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (yr))

        i += 12
        if end_zrot > 0:
            zr = end_zrot + 0.01
        else:
            zr = end_zrot - 0.01
        if menu_sel_item == 15:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Axis Z:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (zr))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Axis Z:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (zr))

        i += 12
        if end_scale > 0:
            sc = (end_scale + 0.0001) * 100
        else:
            sc = (end_scale - 0.0001) * 100
        if menu_sel_item == 16:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Scale:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (sc))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Scale:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (sc))

        i += 20
        glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
        glWrite(12, i, "Animation parametres:")

        i += 12
        if menu_sel_item == 17:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Time in ms:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (animation_time))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Time in ms:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (animation_time))

        i += 12
        if menu_sel_item == 18:
            glColor3f(color_t_menu_p_a[0],color_t_menu_p_a[1],color_t_menu_p_a[2])
            glWrite(12, i, "Frames:")
            glColor3f(color_t_menu_v_a[0],color_t_menu_v_a[1],color_t_menu_v_a[2])
            glWrite(108, i, "< %4d >" % (animation_frame))
        else:
            glColor3f(color_t_menu_p_n[0],color_t_menu_p_n[1],color_t_menu_p_n[2])
            glWrite(12, i, "Frames:")
            glColor3f(color_t_menu_v_n[0],color_t_menu_v_n[1],color_t_menu_v_n[2])
            glWrite(108, i, "< %4d >" % (animation_frame))

        glLeave2D()

    elif t_osdinfo:
        glEnter2D()

        i = 20
        glColor3f(color_t_osd_p[0],color_t_osd_p[1],color_t_osd_p[2])
        glWrite(12, i, "Structure:")
        glColor3f(color_t_osd_v[0],color_t_osd_v[1],color_t_osd_v[2])
        glWrite(108, i, "%4d %s" % (sel_mol, mol[sel_mol][0]))

        i += 12
        # correction
        if xrot > 0:
            xr = xrot + 0.01
        else:
            xr = xrot - 0.01
        glColor3f(color_t_osd_p[0],color_t_osd_p[1],color_t_osd_p[2])
        glWrite(12, i, "Axis X:")
        glColor3f(color_t_osd_v[0],color_t_osd_v[1],color_t_osd_v[2])
        glWrite(108, i, "%4d" % (xr))

        i += 12
        # correction
        if yrot > 0:
            yr = yrot + 0.01
        else:
            yr = yrot - 0.01
        glColor3f(color_t_osd_p[0],color_t_osd_p[1],color_t_osd_p[2])
        glWrite(12, i, "Axis Y:")
        glColor3f(color_t_osd_v[0],color_t_osd_v[1],color_t_osd_v[2])
        glWrite(108, i, "%4d" % (yr))

        i += 12
        # correction
        if zrot > 0:
            zr = zrot + 0.01
        else:
            zr = zrot - 0.01
        glColor3f(color_t_osd_p[0],color_t_osd_p[1],color_t_osd_p[2])
        glWrite(12, i, "Axis Z:")
        glColor3f(color_t_osd_v[0],color_t_osd_v[1],color_t_osd_v[2])
        glWrite(108, i, "%4d" % (zr))

        i += 12
        # correction
        if scale > 0:
            sc = (scale + 0.0001) * 100
        else:
            sc = (scale - 0.0001) * 100
        glColor3f(color_t_osd_p[0],color_t_osd_p[1],color_t_osd_p[2])
        glWrite(12, i, "Zoom:")
        glColor3f(color_t_osd_v[0],color_t_osd_v[1],color_t_osd_v[2])
        glWrite(108, i, "%4d" % (sc))

        glLeave2D()


    glutSwapBuffers()

#----------------------------------------------------------------------------- #
def snap():
    pixels=[]
    screenshot = glReadPixels(0,0,win_width,win_height,GL_RGBA,GL_UNSIGNED_BYTE)
    snapshot = Image.frombuffer("RGBA", (win_width, win_height),screenshot,"raw","RGBA",0,0)
    s = "/run/tmp/%08dtemp.png" % (animation_count)
    snapshot.save(s)


#----------------------------------------------------------------------------- #
def togif():
    # filepaths
    fp_in = "/run/tmp/*.png"
    fp_out = "/run/tmp/image.gif"
    fw = open(fp_out, "w")
    img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
    img.save(fp=fp_out, 
             format='GIF', 
             append_images=imgs,
             save_all=True, 
             duration=(animation_time*4), 
             loop=0)
    fw.close()
    for f in sorted(glob.glob(fp_in)):
        os.remove(f)
    print("togif done")

# ------------------------------------------------------------------------ #
def start_animation():
    global xrot
    global yrot
    global zrot
    global scale
    global animation_time
    global animation_frame
    global animation_procces
    global animation_loop
    global animation_count
    global animation_rec
    xinc = (end_xrot - start_xrot)   / animation_frame
    yinc = (end_yrot - start_yrot)   / animation_frame
    zinc = (end_zrot - start_zrot)   / animation_frame
    sinc = (end_scale - start_scale) / animation_frame
    xrot = start_xrot
    yrot = start_yrot
    zrot = start_zrot
    scale = start_scale
    i = 0
    while i < animation_frame and animation_procces:
        # --------- #
        xrot  += xinc
        yrot  += yinc
        zrot  += zinc
        scale += sinc
        # --------- #
        draw()
        if animation_rec:
            snap()
        time.sleep(animation_time / 1000.0)
        i += 1
        animation_count += 1
    print("Animation stop")
    if animation_rec:
        togif()
    animation_procces = 0
    animation_count = 0
    animation_rec = 0
    
# ------------------------------------------------------------------------ #
def shift_coords():
    global mol
    for i in mol:
        for j in i[1]:
            j[1] = j[1] - 0.5
            j[2] = j[2] - 0.5
            j[3] = j[3] - 0.5

# ------------------------------------------------------------------------ #
def glEnter2D():
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, win_width, win_height, 0)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glDisable(GL_DEPTH_TEST)
    glDisable(GL_LIGHTING)
 
# ------------------------------------------------------------------------ #
def glLeave2D():
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
 
# ------------------------------------------------------------------------ #
def glWrite(x, y, text):
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_8_BY_13,  ord(ch))

# ---------------------------------------------------------------------------- #
def parse_file(filename):
    global mol
    global sel_mol
    global max_mol
    j = 0
    #mol = [] # store example
    f = open(filename, "r")
    line = f.readline()
    while line:
        if line[0] == 'N' or line[0] == 'D':
            sp = line.split('=')
            sp[0] = sp[0].strip()
            sp[1] = sp[1].strip()
            if   sp[0] == 'Name':
                j += 1
                mol.append([sp[1], []])
            elif sp[0] == 'Data':
                sp[1] = sp[1].split(',')
                d = []
                for i in sp[1]:
                    d.append(i.strip())
                di = []
                di.append(float(d[0]))
                di.append(float(d[1]))
                di.append(float(d[2]))
                di.append(float(d[3]))
                di.append(float(d[4]))
                di.append([])
                for i in d[5:]:
                    if i:
                        di[5].append(float(i))
                mol[j][1].append(di)
        line = f.readline()
    max_mol = j
    sel_mol = 0
    for i in mol:
        print("Find structure: ",i[0])
    
    f.close()

# ---------------------------------------------------------------------------- #
win_width = 600
win_height = 600
win_posx = 100
win_posy = 100
mol = [
    ['Example structure',
     [[0, 0.0, 0.0, 0.0, 0, [1, 3, 4]],
      [1, 1.0, 0.0, 0.0, 0, [2, 5]],
      [2, 1.0, 1.0, 0.0, 0, [3, 6]],
      [3, 0.0, 1.0, 0.0, 0, [7]],
      [4, 0.0, 0.0, 1.0, 0, [5, 7]],
      [5, 1.0, 0.0, 1.0, 0, [6]],
      [6, 1.0, 1.0, 1.0, 0, [7]],
      [7, 0.0, 1.0, 1.0, 0, []],
      [8, 0.5, 0.5, 0.25, 0, [0, 1, 2, 3, 9]],
      [9, 0.5, 0.5, 0.75, 0, [4, 5, 6, 7]]
     ]
    ]
]
sel_mol = 0
max_mol = 0
color_clear = [0.0, 0.0, 0.0, 1.0]
color_line_i = 0
color_line_i_max = 6
color_line_a = 0.4
color_line = [[1.0, 1.0, 1.0],
              [1.0, 0.0, 0.0],
              [1.0, 1.0, 0.0],
              [0.0, 1.0, 0.0],
              [0.0, 1.0, 1.0],
              [0.0, 0.0, 1.0],
              [1.0, 0.0, 1.0]]
xrot = 0.0
yrot = 0.0
zrot = 0.0
scale = 1.9
start_xrot = 0.0
start_yrot = 0.0
start_zrot = 0.0
start_scale = 1.9
end_xrot = 0.0
end_yrot = 0.0
end_zrot = 0.0
end_scale = 1.9
l_ambi = 0.7
line_width = 4.0
t_help = 0
t_menu = 0
t_osdinfo = 0
color_t_help = [0.4, 0.4, 0.4]
color_t_menu_p_a = [0.89, 0.89, 0.89]
color_t_menu_v_a = [0.3, 0.8, 0.3]
color_t_menu_p_n = [0.4, 0.4, 0.4]
color_t_menu_v_n = [0.4, 0.4, 0.4]
menu_sel_item = 0
menu_max_item = 18
color_t_osd_p = [0.4, 0.4, 0.4]
color_t_osd_v = [0.3, 0.8, 0.3]
animation_time = 45
animation_frame = 50
animation_procces = 0
animation_loop = 0
animation_count = 0
animation_rec = 0
#----------------------------------------------------------------------------- #
parse_file("atoms.conf")
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH | GLUT_ALPHA)
glutInitWindowSize(win_width, win_height)
glutInitWindowPosition(win_posx, win_posy)
glutInit(sys.argv)
glutCreateWindow(b"Atoms")
glutDisplayFunc(draw)
glutReshapeFunc(reshape)
glutSpecialFunc(specialkeys)
shift_coords()
reshape(win_width, win_height)
glutMainLoop()
exit()

