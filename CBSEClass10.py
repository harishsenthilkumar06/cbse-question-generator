from flask import Flask, render_template, request, redirect
import math
import random

app = Flask(__name__)

#Definitions
def HCF():
    i = 0
    factors = []
    y = 0
    while y <= 6:
        r = random.randint(1,200)
        t = random.randint(1,200)
        y = math.gcd(r,t)
    return(r,t,y)

def pf():
  o = []
  while len(o) < 6:
    o = []
    p = random.randint(1,200)
    u = p
    i = 2
    while i <= u:
      if u % i == 0:
        o.append(str(i))
        u = u/i
        i = 2
      else:
        i += 1
  a = "x"
  o = a.join(o)
  return(p,o)

def LCM():
  s,d,f = HCF()
  LCM = int(s*d/f)
  return(s,d,LCM,f,s*d)

def lcm_finder(x, y, z):
  gcd2 = math.gcd(y, z)
  gcd3 = math.gcd(x, gcd2)
  lcm2 = y*z // gcd2
  lcm3 = int(x*lcm2 // math.gcd(x, lcm2))
  return(lcm3)

def LCM_HCF_3():
  l = z = x = c = 0
  factors = []
  while (z != l != x and max(factors) != 1) == 0:
    l = random.randint(1,50)
    z = random.randint(1,50)
    x = random.randint(1,100)
    if z < l and z < x :
      for i in range(1,z+1):
        if l%i == 0 and x%i ==0 and z%i ==0:
          factors.append(i)
    if l < z and l < x :
      for i in range(1,l+1):
        if z%i == 0 and x%i ==0 and l%i ==0:
          factors.append(i)
    if x < l and x < z :
      for i in range(1,x+1):
        if z%i == 0 and x%i ==0 and l%i ==0:
          factors.append(i)
  c = lcm_finder(l,x,z)
  return(l,z,x,c,max(factors))

def term_or_non_term():
  v = random.choice((1,2))
  if v == 1:
    b = random.choice((10, 16, 32, 128, 8, 20, 40, 50, 80, 160, 400, 500))
    m = "y"
  else:
    b = random.choice((13,41,48,23,48,12,60,660,90,445))
    m = "n"
  n = random.randint(1,300)
  b = "{}/{}".format(n,b)
  return(b,m)

def poly_roots():
  b_w = random.choice((-2-1,1,2,3,4,5,6))
  b_e = random.randint(-50,50)
  b_r = random.randint(-50,240)
  if b_e < 0:
    if b_r < 0:
      b_q = "{}x²{}x{}.".format(b_w,b_e,b_r)
    elif b_r == 0:
      b_q = "{}x²{}x".format(b_w,b_e)
    else:
      b_q = "{}x²{}x+{}".format(b_w,b_e,b_r)
  if b_e == 0:
    if b_r < 0:
      b_q = "{}x²{}".format(b_w,b_r)
    elif b_r == 0:
      b_q = "{}x²".format(b_w)
    else:
      b_q = "{}x²+{}".format(b_w,b_r)
  if b_e > 0:
    if b_r < 0:
      b_q = "{}x²+{}x{}".format(b_w,b_e,b_r)
    elif b_r == 0:
      b_q = "{}x²+{}x".format(b_w,b_e)
    else:
      b_q = "{}x²+{}x+{}".format(b_w,b_e,b_r)
  if ((b_e)**2 - 4*b_w*b_r) > 0:
    b_t = 2
  elif ((b_e)**2 - 4*b_w*b_r) == 0:
    b_t = 1
  else:
    b_t = 0
  b_q = "The no. of zeroes in the polynomial {} is _______".format(b_q)
  return(b_q,b_t)

def poly_roots_fr():
  b_y = random.randint(-16,16) #root 1
  b_u = random.randint(-16,16)  #root 2
  b_i = random.choice((-3,-2,-1,1,2,3))  #a
  b_o = -(b_i*(b_y+b_u))  #b
  b_p = b_i*b_y*b_u #c
  b_q = ""
  if b_i == -1:
    if b_o < 0:
      if b_p < 0:
        b_q = "-x²{}x{}.".format(b_o,b_p)
      elif b_p == 0:
        b_q = "-x²{}x".format(b_o)
      else:
        b_q = "-x²{}x+{}".format(b_o,b_p)
    if b_o == 0:
      if b_p < 0:
        b_q = "-x²{}".format(b_p)
      elif b_p == 0:
        b_q = "-x²".format(b_i)
      else:
        b_q = "-x²+{}".format(b_p)
    if b_o > 0:
      if b_p < 0:
        b_q = "-x²+{}x{}".format(b_o,b_p)
      elif b_p == 0:
        b_q = "-x²+{}x".format(b_o)
      else:
        b_q = "-x²+{}x+{}".format(b_o,b_p)
  elif b_i == 1:
    if b_o < 0:
      if b_p < 0:
        b_q = "x²{}x{}.".format(b_o,b_p)
      elif b_p == 0:
        b_q = "x²{}x".format(b_o)
      else:
        b_q = "x²{}x+{}".format(b_o,b_p)
    if b_o == 0:
      if b_p < 0:
        b_q = "x²{}".format(b_p)
      elif b_p == 0:
        b_q = "x²".format(b_i)
      else:
        b_q = "x²+{}".format(b_p)
    if b_o > 0:
      if b_p < 0:
        b_q = "x²+{}x{}".format(b_o,b_p)
      elif b_p == 0:
        b_q = "x²+{}x".format(b_o)
      else:
        b_q = "x²+{}x+{}".format(b_o,b_p)
  elif b_o < 0:
    if b_p < 0:
      b_q = "{}x²{}x{}.".format(b_i,b_o,b_p)
    elif b_p == 0:
      b_q = "{}x²{}x".format(b_i,b_o)
    else:
      b_q = "{}x²{}x+{}".format(b_i,b_o,b_p)
  elif b_o == 0:
    if b_p < 0:
      b_q = "{}x²{}".format(b_i,b_p)
    elif b_p == 0:
      b_q = "{}x²".format(b_i)
    else:
      b_q = "{}x²+{}".format(b_i,b_p)
  elif b_o > 0:
    if b_p < 0:
      b_q = "{}x²+{}x{}".format(b_i,b_o,b_p)
    elif b_p == 0:
      b_q = "{}x²+{}x".format(b_i,b_o)
    else:
      b_q = "{}x²+{}x+{}".format(b_i,b_o,b_p)
  if b_u < b_y:
    temp = b_y
    b_y = b_u
    b_u = temp
  return("The zeroes of the quadratic {} in ascending order are _______. (Format: <root>,<root>)".format(b_q),"{},{}".format(b_y,b_u))

def poly_roots_thingamajig():
  b_y = random.randint(-16,16) #root 1
  b_u = random.randint(-16,16)  #root 2
  b_i = random.choice((-3,-2,-1,1,2,3))  #a
  b_o = -(b_i*(b_y+b_u))  #b
  b_p = b_i*b_y*b_u #c
  b_q = ""
  if b_i == -1:
    if b_o < 0:
      if b_p < 0:
        b_q = "-x2{}x{}.".format(b_o,b_p)
      elif b_p == 0:
        b_q = "-x2{}x".format(b_o)
      else:
        b_q = "-x2{}x+{}".format(b_o,b_p)
    if b_o == 0:
      if b_p < 0:
        b_q = "-x2{}".format(b_p)
      elif b_p == 0:
        b_q = "-x2".format(b_i)
      else:
        b_q = "-x2+{}".format(b_p)
    if b_o > 0:
      if b_p < 0:
        b_q = "-x2+{}x{}".format(b_o,b_p)
      elif b_p == 0:
        b_q = "-x2+{}x".format(b_o)
      else:
        b_q = "-x2+{}x+{}".format(b_o,b_p)
  elif b_i == 1:
    if b_o < 0:
      if b_p < 0:
        b_q = "x2{}x{}.".format(b_o,b_p)
      elif b_p == 0:
        b_q = "x2{}x".format(b_o)
      else:
        b_q = "x2{}x+{}".format(b_o,b_p)
    if b_o == 0:
      if b_p < 0:
        b_q = "x2{}".format(b_p)
      elif b_p == 0:
        b_q = "x2".format(b_i)
      else:
        b_q = "x2+{}".format(b_p)
    if b_o > 0:
      if b_p < 0:
        b_q = "x2+{}x{}".format(b_o,b_p)
      elif b_p == 0:
        b_q = "x2+{}x".format(b_o)
      else:
        b_q = "x2+{}x+{}".format(b_o,b_p)
  elif b_o < 0:
    if b_p < 0:
      b_q = "{}x2{}x{}.".format(b_i,b_o,b_p)
    elif b_p == 0:
      b_q = "{}x2{}x".format(b_i,b_o)
    else:
      b_q = "{}x2{}x+{}".format(b_i,b_o,b_p)
  elif b_o == 0:
    if b_p < 0:
      b_q = "{}x2{}".format(b_i,b_p)
    elif b_p == 0:
      b_q = "{}x2".format(b_i)
    else:
      b_q = "{}x2+{}".format(b_i,b_p)
  elif b_o > 0:
    if b_p < 0:
      b_q = "{}x2+{}x{}".format(b_i,b_o,b_p)
    elif b_p == 0:
      b_q = "{}x2+{}x".format(b_i,b_o)
    else:
      b_q = "{}x2+{}x+{}".format(b_i,b_o,b_p)
  b_d = b_y + b_u
  b_f = b_y*b_u
  return("Find the quadratic whose sum and product are {} and {} respectively. (Format: ( /-)ax2(+/-)bx(+/-)c)".format(b_d,b_f),str(b_q))

def big_boy_polynomial():
  b_y = random.randint(-16,16) #root 1
  b_u = random.randint(-16,16) #root 2
  b_i = random.choice((-3,2))  #a
  b_o = -(b_i*(b_y+b_u))  #b
  b_p = b_i*b_y*b_u #c
  b_g = (list(range(-10,10)))
  b_g.remove(0)
  b_g = random.choice(b_g) #d
  bwahaha = random.randint(0,1)
  if bwahaha == 0:
    if b_i == -1:
      if b_o < 0:
        if b_p < 0:
          b_q = "-x2{}x{}".format(b_o,b_p)
        elif b_p == 0:
          b_q = "-x2{}x".format(b_o)
        else:
          b_q = "-x2{}x+{}".format(b_o,b_p)
      if b_o == 0:
        if b_p < 0:
          b_q = "-x2{}".format(b_p)
        elif b_p == 0:
          b_q = "-x2".format(b_i)
        else:
          b_q = "-x2+{}".format(b_p)
      if b_o > 0:
        if b_p < 0:
          b_q = "-x2+{}x{}".format(b_o,b_p)
        elif b_p == 0:
          b_q = "-x2+{}x".format(b_o)
        else:
          b_q = "-x2+{}x+{}".format(b_o,b_p)
    elif b_i == 1:
      if b_o < 0:
        if b_p < 0:
          b_q = "x2{}x{}".format(b_o,b_p)
        elif b_p == 0:
          b_q = "x2{}x".format(b_o)
        else:
          b_q = "x2{}x+{}".format(b_o,b_p)
      if b_o == 0:
        if b_p < 0:
          b_q = "x2{}".format(b_p)
        elif b_p == 0:
          b_q = "x2".format(b_i)
        else:
          b_q = "x2+{}".format(b_p)
      if b_o > 0:
        if b_p < 0:
          b_q = "x2+{}x{}".format(b_o,b_p)
        elif b_p == 0:
          b_q = "x2+{}x".format(b_o)
        else:
          b_q = "x2+{}x+{}".format(b_o,b_p)
    elif b_o < 0:
      if b_p < 0:
        b_q = "{}x2{}x{}".format(b_i,b_o,b_p)
      elif b_p == 0:
        b_q = "{}x2{}x".format(b_i,b_o)
      else:
        b_q = "{}x2{}x+{}".format(b_i,b_o,b_p)
    elif b_o == 0:
      if b_p < 0:
        b_q = "{}x2{}".format(b_i,b_p)
      elif b_p == 0:
        b_q = "{}x2".format(b_i)
      else:
        b_q = "{}x2+{}".format(b_i,b_p)
    elif b_o > 0:
      if b_p < 0:
        b_q = "{}x2+{}x{}".format(b_i,b_o,b_p)
      elif b_p == 0:
        b_q = "{}x2+{}x".format(b_i,b_o)
      else:
        b_q = "{}x2+{}x+{}".format(b_i,b_o,b_p)
    b_w = b_o+(b_i*b_g) #(ax^2+bx+c)(x+d)= ax^3+(b+ad)x^2+(c+bd)x+cd => b_i = a; b_o = b; b_p = c; b_g = d;
    b_e = b_p+(b_o*b_g)
    b_r = b_p*b_g
    b_h = ""
    if b_w < 0:
      if b_e < 0:
        if b_r < 0:
          b_h = "{}x³{}x²{}x{}".format(b_i,b_w,b_e,b_r)
        elif b_r == 0:
          b_h = "{}x³{}x²{}x".format(b_i,b_w,b_e)
        else:
          b_h = "{}x³{}x²{}x+{}".format(b_i,b_w,b_e,b_r)
      if b_e == 0:
        if b_r < 0:
          b_h = "{}x³{}x²{}".format(b_i,b_w,b_r)
        elif b_r == 0:
          b_h = "{}x³{}x²".format(b_i,b_w)
        else:
          b_h = "{}x³{}x²+{}".format(b_i,b_w,b_r)
      if b_e > 0:
        if b_r < 0:
          b_h = "{}x³{}x²+{}x{}".format(b_i,b_w,b_e,b_r)
        elif b_r == 0:
          b_h = "{}x³{}x²+{}x".format(b_i,b_w,b_e)
        else:
          b_h = "{}x³{}x²+{}x+{}".format(b_i,b_w,b_e,b_r)
    if b_w > 0:
      if b_e < 0:
        if b_r < 0:
          b_h = "{}x³+{}x²{}x{}".format(b_i,b_w,b_e,b_r)
        elif b_r == 0:
          b_h = "{}x³+{}x²{}x".format(b_i,b_w,b_e)
        else:
          b_h = "{}x³+{}x²{}x+{}".format(b_i,b_w,b_e,b_r)
      if b_e == 0:
        if b_r < 0:
          b_h = "{}x³+{}x²{}".format(b_i,b_w,b_r)
        elif b_r == 0:
          b_h = "{}x³+{}x²".format(b_i,b_w)
        else:
          b_h = "{}x³+{}x²+{}".format(b_i,b_w,b_r)
      if b_e > 0:
        if b_r < 0:
          b_h = "{}x³+{}x²+{}x{}".format(b_i,b_w,b_e,b_r)
        elif b_r == 0:
          b_h = "{}x³+{}x²+{}x".format(b_i,b_w,b_e)
        else:
          b_h = "{}x³+{}x²+{}x+{}".format(b_i,b_w,b_e,b_r)
    if b_g > 0:
      b_j = "x+{}".format(b_g)
    else:
      b_j = "x{}".format(b_g)
    b_h = "Divide the polynomial {} by {}. (Format: ( /-)ax2(+/-)bx(+/-)c)".format(b_h,b_j)
    return(b_h,b_q)
  else:
    b_y = random.randint(-16,16) #root 1
    b_u = random.randint(-16,16)  #root 2
    b_i = random.choice((-1,1,))  #a
    b_o = -(b_i*(b_y+b_u))  #b
    b_p = b_i*b_y*b_u #c
    b_q = ""
    if b_i == -1:
      if b_o < 0:
        if b_p < 0:
          b_q = "-x²{}x{}".format(b_o,b_p)
        elif b_p == 0:
          b_q = "-x²{}x".format(b_o)
        else:
          b_q = "-x²{}x+{}".format(b_o,b_p)
      if b_o == 0:
        if b_p < 0:
          b_q = "-x²{}".format(b_p)
        elif b_p == 0:
          b_q = "-x²".format(b_i)
        else:
          b_q = "-x²+{}".format(b_p)
      if b_o > 0:
        if b_p < 0:
          b_q = "-x²+{}x{}".format(b_o,b_p)
        elif b_p == 0:
          b_q = "-x²+{}x".format(b_o)
        else:
          b_q = "-x²+{}x+{}".format(b_o,b_p)
    elif b_i == 1:
      if b_o < 0:
        if b_p < 0:
          b_q = "x²{}x{}".format(b_o,b_p)
        elif b_p == 0:
          b_q = "x²{}x".format(b_o)
        else:
          b_q = "x²{}x+{}".format(b_o,b_p)
      if b_o == 0:
        if b_p < 0:
          b_q = "x²{}".format(b_p)
        elif b_p == 0:
          b_q = "x²".format(b_i)
        else:
          b_q = "x²+{}".format(b_p)
      if b_o > 0:
        if b_p < 0:
          b_q = "x²+{}x{}".format(b_o,b_p)
        elif b_p == 0:
          b_q = "x²+{}x".format(b_o)
        else:
          b_q = "x²+{}x+{}".format(b_o,b_p)
    elif b_o < 0:
      if b_p < 0:
        b_q = "{}x²{}x{}".format(b_i,b_o,b_p)
      elif b_p == 0:
        b_q = "{}x²{}x".format(b_i,b_o)
      else:
        b_q = "{}x²{}x+{}".format(b_i,b_o,b_p)
    elif b_o == 0:
      if b_p < 0:
        b_q = "{}x²{}".format(b_i,b_p)
      elif b_p == 0:
        b_q = "{}x²".format(b_i)
      else:
        b_q = "{}x²+{}".format(b_i,b_p)
    elif b_o > 0:
      if b_p < 0:
        b_q = "{}x²+{}x{}".format(b_i,b_o,b_p)
      elif b_p == 0:
        b_q = "{}x²+{}x".format(b_i,b_o)
      else:
        b_q = "{}x²+{}x+{}".format(b_i,b_o,b_p)
    if b_y < 0:
      b_y = "x+{}".format(int(math.fabs(b_y)))
    else:
      b_y = "x-{}".format(b_y)
    if b_u < 0:
      b_u = "x+{}".format(int(math.fabs(b_u)))
    else:
      b_u = "x-{}".format(b_u)
    b_h = "Divide the polynomial {} by {}. (Format: x(+/-)a)".format(b_q,b_y)
    return(b_h,b_u)
import random

def l_e_2v():
  c_l = list(range(-15,15))
  c_l.remove(-1)
  c_l.remove(1)
  c_l.remove(0)
  c_a1 = random.choice(c_l)
  c_b1 = random.choice(c_l)
  c_a2 = random.choice(c_l)
  c_b2 = random.choice(c_l)
  c_sol_x = random.choice(c_l)
  c_sol_y = random.choice(c_l)
  c_c1 = -((c_a1*c_sol_x)+(c_b1*c_sol_y)) #ax+by+c = 0 >>> ax +by = -c
  c_c2 = -((c_a2*c_sol_x)+(c_b2*c_sol_y))
  if c_b1 > 0:
    if c_c1 > 0:
      c_eq1 = "{}x+{}y+{}".format(c_a1,c_b1,c_c1)
    if c_c1 < 0:
      c_eq1 = "{}x+{}y{}".format(c_a1,c_b1,c_c1)
  if c_b1 < 0:
    if c_c1 > 0:
      c_eq1 = "{}x{}y+{}".format(c_a1,c_b1,c_c1)
    if c_c1 < 0:
      c_eq1 = "{}x{}y{}".format(c_a1,c_b1,c_c1)
  if c_b2 > 0:
    if c_c2 > 0:
      c_eq2 = "{}x+{}y+{}".format(c_a2,c_b2,c_c2)
    if c_c2 < 0:
      c_eq2 = "{}x+{}y{}".format(c_a2,c_b2,c_c2)
  if c_b2 < 0:
    if c_c2 > 0:
      c_eq2 = "{}x{}y+{}".format(c_a2,c_b2,c_c2)
    if c_c2 < 0:
      c_eq2 = "{}x{}y{}".format(c_a2,c_b2,c_c2)
  return(c_eq1,c_eq2,c_sol_x,c_sol_y)

def l_e_1():
  c_eq1,c_eq2,c_sol_x,c_sol_y = l_e_2v()
  c_q1 = "Solve the given equations(Format: x,y):{}, {}".format(c_eq1,c_eq2)
  c_ans1 = "{},{}".format(c_sol_x,c_sol_y)
  return(c_q1,c_ans1)

def l_e_2():
  c_eq1,c_eq2,c_sol_x,c_sol_y = l_e_2v()
  c_q2 = "Solve the give equations and find the value of y = mx + 3: {}, {}. Format: (p/q)".format(c_eq1,c_eq2)
  c_ans2 = "{}/{}".format(c_sol_y-3,c_sol_x)
  return(c_q2,c_ans2)

def l_e_3():
  c_eq1,c_eq2,c_sol_x,c_sol_y = l_e_2v()
  c_q3 = "Solve the give equations using cross-multiplication method:{}, {}".format(c_eq1,c_eq2)
  c_ans3 = "{},{}".format(c_sol_x,c_sol_y)
  return(c_q3,c_ans3)

def l_e_4():
  c_eq1,c_eq2,c_sol_x,c_sol_y = l_e_2v()
  c_q4 = "Solve the give equations using substitution method:{}, {}".format(c_eq1,c_eq2)
  c_ans4 = "{},{}".format(c_sol_x,c_sol_y)
  return(c_q4,c_ans4)

def l_e_5():
  c_eq1,c_eq2,c_sol_x,c_sol_y = l_e_2v()
  c_q5 = "Solve the give equations using elimination method:{}, {}".format(c_eq1,c_eq2)
  c_ans5 = "{},{}".format(c_sol_x,c_sol_y)
  return(c_q5,c_ans5)

def quad_roots_fr():
  b_y = random.randint(-16,16) #root 1
  b_u = random.randint(-16,16)  #root 2
  b_i = random.choice((-3,-2,-1,1,2,3))  #a
  b_o = -(b_i*(b_y+b_u))  #b
  b_p = b_i*b_y*b_u #c
  b_q = ""
  if b_i == -1:
    if b_o < 0:
      if b_p < 0:
        b_q = "-x²{}x{}.".format(b_o,b_p)
      elif b_p == 0:
        b_q = "-x²{}x".format(b_o)
      else:
        b_q = "-x²{}x+{}".format(b_o,b_p)
    if b_o == 0:
      if b_p < 0:
        b_q = "-x²{}".format(b_p)
      elif b_p == 0:
        b_q = "-x²".format(b_i)
      else:
        b_q = "-x²+{}".format(b_p)
    if b_o > 0:
      if b_p < 0:
        b_q = "-x²+{}x{}".format(b_o,b_p)
      elif b_p == 0:
        b_q = "-x²+{}x".format(b_o)
      else:
        b_q = "-x²+{}x+{}".format(b_o,b_p)
  elif b_i == 1:
    if b_o < 0:
      if b_p < 0:
        b_q = "x²{}x{}.".format(b_o,b_p)
      elif b_p == 0:
        b_q = "x²{}x".format(b_o)
      else:
        b_q = "x²{}x+{}".format(b_o,b_p)
    if b_o == 0:
      if b_p < 0:
        b_q = "x²{}".format(b_p)
      elif b_p == 0:
        b_q = "x²".format(b_i)
      else:
        b_q = "x²+{}".format(b_p)
    if b_o > 0:
      if b_p < 0:
        b_q = "x²+{}x{}".format(b_o,b_p)
      elif b_p == 0:
        b_q = "x²+{}x".format(b_o)
      else:
        b_q = "x²+{}x+{}".format(b_o,b_p)
  elif b_o < 0:
    if b_p < 0:
      b_q = "{}x²{}x{}.".format(b_i,b_o,b_p)
    elif b_p == 0:
      b_q = "{}x²{}x".format(b_i,b_o)
    else:
      b_q = "{}x²{}x+{}".format(b_i,b_o,b_p)
  elif b_o == 0:
    if b_p < 0:
      b_q = "{}x²{}".format(b_i,b_p)
    elif b_p == 0:
      b_q = "{}x²".format(b_i)
    else:
      b_q = "{}x²+{}".format(b_i,b_p)
  elif b_o > 0:
    if b_p < 0:
      b_q = "{}x²+{}x{}".format(b_i,b_o,b_p)
    elif b_p == 0:
      b_q = "{}x²+{}x".format(b_i,b_o)
    else:
      b_q = "{}x²+{}x+{}".format(b_i,b_o,b_p)
  if b_u < b_y:
    temp = b_y
    b_y = b_u
    b_u = temp
  return("Find zeroes of the quadratic {} using factorisation or quadratic formula. Write them in ascending order. (Format: <root1>,<root2>)".format(b_q),"{},{}".format(b_y,b_u))

def quad_3():
  d_l = list(range(-32,32,4))
  d_l.remove(0)
  d_b = random.choice(d_l)
  d_c = int((d_b**2)/4) #b^2 - 4c = 0 >>> c = b**2/4
  if d_b > 0:
    d_q = "x²+{}x+k".format(d_b)
  if d_b < 0:
    d_q = "x²{}x+k".format(d_b)
  d_q = "Find k such that the roots of {} are real and equal.".format(d_q)
  return(d_q,str(d_c))

def ap():
  e_a = random.randint(-100,100)
  e_d = random.choice((-10,-9,-8,-7,-6,-5,-4,-3,-2,2,3,4,5,6,7,8,9,10))
  e_ap = []
  for i in range(20):
    e_ap.append(e_a+(i*e_d))
  return(e_ap,e_a,e_d)

def e_1():
  e_ap,e_a,e_d = ap()
  e1 = "Write the first 5 terms of the AP: a = {}; d = {}".format(e_a,e_d)
  e1a = "{},{},{},{},{}".format(e_ap[0],e_ap[1],e_ap[2],e_ap[3],e_ap[4])
  return(e1,e1a)

def e_2():
  e_ap,e_a,e_d = ap()
  e_b = random.randint(4,20)
  e2 = "Find the {}th term of the AP: a = {}; d = {}".format(e_b,e_a,e_d)
  e2a = str(e_ap[e_b])
  return(e2,e2a)

def e_3():
  e_ap,e_a,e_d = ap()
  e_b = random.randint(8,20)
  e3 = "Which term of the AP, {},{},{}... is {}".format(e_ap[0],e_ap[1],e_ap[2],e_ap[e_b])
  e3a = str(e_b)
  return(e3,e3a)

def e_4():
  e_w = random.randint(1,2)
  e_ap,e_a,e_d = ap()
  e_b = random.randint(8,20)
  if e_w == 1:
    e_b = e_ap[e_b]
    e4a = "y"
  else:
    e4a = "n"
  e4 = "Is {} a term of the AP {},{},{}...? (y/n)".format(e_b,e_ap[0],e_ap[1],e_ap[2])
  return(e4,e4a)

def e_5():
  e_ap,e_a,e_d = ap()
  e_b = random.choice(range(8,20,2))
  e5 = "Find the sum of {} terms of the AP {},{},{}...".format(e_b,e_ap[0],e_ap[1],e_ap[2])
  e5a = str(int((e_b/2)*((2*e_a)+((e_b-1)*e_d))))
  return(e5,e5a)

def e_6():
  e_ap,e_a,e_d = ap()
  e_b = random.choice(range(8,20,2))
  e6 = "How many terms of the AP {},{},{}... add up to {}".format(e_ap[0],e_ap[1],e_ap[2],int((e_b/2)*((2*e_a)+((e_b-1)*e_d))))
  e6a = str(e_b)
  return(e6,e6a)

def f_1():
  f_dec = random.randint(1,2)
  if f_dec == 1:
    f_a = random.randint(3,9)
    f_b = random.randint(3,9)
    f_c = math.sqrt(f_a**2 + f_b**2)
    f1a = "y"
  if f_dec == 2:
    f_a = random.randint(3,9)
    f_b = random.randint(3,9)
    f_c = random.randint(3,12)
    f1a = "n"
  f1 = "Check if the triangle formed with sides {},{},{} is right angled. (y/n)".format(f_a,f_c,f_b)
  return(f1,f1a)

def distance_pts():
  m = random.randint(1,15)
  n = random.randint(1,15)
  p = random.randint(-10,10)
  q = random.randint(-10,10) #d= int >>> d^2 = x-p^2 + y-q^2 >>>
  x = (m**2) - (n**2) + p
  y = 2*m*n + q  #(y-q)^2 = (m^2-1)^2 >>> y = m^2 + q - 1
  d = m**2 + n**2
  return(x,y,p,q,d)

def g_1():
  x,y,p,q,d = distance_pts()
  g1 = "Find the distance between the points ({},{}) and ({},{})".format(x,y,p,q)
  g1a = str(d)
  return(g1,g1a)

def g_2():
  g_dec = random.randint(1,2)
  if g_dec == 1:
    x1, y1 = random.randint(-15, 15), random.randint(-15, 15)
    m = random.randint(-15, 15)
    c = y1 - m * x1
    x2 = random.randint(-15, 15)
    y2 = m * x2 + c
    x3 = random.randint(-15, 15)
    y3 = m * x3 + c
    g2a = "y"
  elif g_dec == 2:
    x1,y1 = random.randint(-15, 15), random.randint(-15, 15)
    x2,y2 = random.randint(-15, 15), random.randint(-15, 15)
    x3,y3 = random.randint(-15, 15), random.randint(-15, 15)
    g2a = "n"

  g2 = "Check if the points ({},{}),({},{}) and ({},{}) are collinear or not. (y/n)".format(x1,y1,x2,y2,x3,y3)
  return(g2,g2a)

def g_3():
  g_dec = random.randint(1,2)
  if g_dec == 1:
    x1,y1 = random.randint(-15,15),random.randint(-15,15)
    x2,y2 = random.randint(-15,15),random.randint(-15,15)
    x3,y3 = random.randint(-15,15),random.randint(-15,15)
    x4,y4 = random.randint(-15,15),random.randint(-15,15)
    g3a = "n"
  elif g_dec == 2:
    x1,y1 = random.randint(-15,15),random.randint(-15,15)
    a = random.randint(-5,5)
    x2,y2 = (x1+a),y1
    x3,y3 = x1,(y1+a)
    x4,y4 = x1 + a, y1 + a
    g3a = "y"
  g3 = "Check whether the following points form a square: ({},{}), ({},{}), ({},{}), ({},{}). (y/n)".format(x1,y1,x2,y2,x3,y3,x4,y4)
  return(g3,g3a)

def g_4():
  x1,y1 = random.randint(-15,15),random.randint(-15,15)
  x2,y2 = random.randint(-15,15),random.randint(-15,15)
  x3,y3 = int(((y2**2)-(y1**2)+(x2**2)-(x1**2))/(2*(x2-x1))),0
  g4 = "Find the point on the x-axis equidistant from ({},{}),({},{}). Format:(x,y)".format(x1,y1,x2,y2)
  g4a = "({},{})".format(x3,y3)
  return(g4,g4a)

def g_5():
  x1,y1 = random.randint(-15,15),random.randint(-15,15)
  x2,y2 = random.randint(-15,15),random.randint(-15,15)
  m = random.randint(1,6)
  n = random.randint(1,5)
  x3,y3 = int((m*x2 + n*x1)/(m+n)),int((m*y2 + n*y1)/(m+n))
  g5 = "Find the ration in which ({},{}) divides the line joining the points ({},{}),({},{}).Format: m:n".format(x3,y3,x1,y1,x2,y2)
  g5a = "{}:{}".format(m,n)
  return(g5,g5a)

def g_6():
  x1,y1 = random.randint(-15,15),random.randint(-15,15)
  x2,y2 = random.randint(-15,15),random.randint(-15,15)
  x3,y3 = random.randint(-15,15),random.randint(-15,15)
  g6 = "Find the area of the triangle whose vertices are ({},{}),({},{}),({},{})".format(x1,y1,x2,y2,x3,y3)
  g6a = str(int((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2))
  return(g6,g6a)

def g_7():
  x1,y1 = random.randint(-15,15),random.randint(-15,15)
  x2,y2 = random.randint(-15,15),random.randint(-15,15)
  x3,y3 = random.randint(-15,15),random.randint(-15,15)
  x4,y4 = random.randint(-15,15),random.randint(-15,15)
  g7 = "Find the area of the quadrilateral whose vertices are ({},{}),({},{}),({},{}),({},{})".format(x1,y1,x2,y2,x3,y3,x4,y4)
  g7a = str(int((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)+int((x1*(y4-y3)+x4*(y3-y1)+x3*(y1-y4))/2))
  return(g7,g7a)

def i_1():
  m = random.randint(3,8)
  x = 2*m
  y = m**2 - 1
  z = m**2 + 1
  i1 = "A tangent PQ of length {} is drawn from the point P on a circle of radius {} to an external point Q. Find the length OQ, where O is the centre of the cirle.".format(y,x)
  i1a = str(z)
  return(i1,i1a)

def i_2():
  m = random.randint(3,8)
  x = 2*m
  y = m**2 - 1
  z = m**2 + 1
  i2 = "A pair of tangents are drawn from a point P {} cm away from the centre of a circle of radius {} cm. Find the length of the tangents.".format(z,x)
  i2a = str(y)
  return(i2,i2a)

def i_3():
  m = random.choice((30, 45, 60))
  x = random.randint(1,7)
  y = x*(math.sin(math.radians(m)))
  i3 = "A pair of tangents is drawn from a point P {} cm away from the centre of a circle subtending {} degrees at the centre. Find the length of the tangents.".format(x,2*m)
  i3a = str(y)
  return(i3,i3a)

def j_1():
  r = random.choice((0.7,1.4,2.1,3.5,4.9,7,7.7,14))
  i = random.choice(("pizza","circular table","coaster","plate"))
  j1 = "Find the area of a {} of radius {}.".format(i,r)
  j1a = 22*r*r/7
  return(j1,j1a)

def j_2():
  r = random.choice((7,14))
  y = random.randint(3,6)
  p = random.randint(2,y)
  j2 = "Find the area of the {}th ring of a bullseye that has {} rings and a total radius of {}".format(p,y,y*r)
  j2a = str(int((22*p*r*p*r)/7)-((22*(p-1)*(p-1)*r*r)/7))
  return(j2,j2a)

def j_3():
  r = random.choice((4.9,7,7.7,14))
  s = random.choice((4,5,6,8,9))
  j3 = "Find the area of a {} degree slice of a pizza of radius {}.".format(int(360/s),r)
  j3a = str(int((22*r*r)/(7*s)))
  return(j3,j3a)

def k_1():
  k_a = random.randint(1,12)
  k_vol = 4*(k_a**3)
  k_tsa = 18*(k_a**2)
  k1 = "Find the TSA and volume of 3 cubes of side {} joined to the mutually perpendicular sides of another cube also of side {}.".format(k_a,k_a)
  k1a = "{},{}".format(k_tsa,k_vol)
  return(k1,k1a)

def k_2():
  k_r = random.choice((4.9,5.6,7,7.7,14))
  k_a = 2*k_r
  k_vol = (k_a**3) - ((2*22*k_r*k_r*k_r)/(3*7))
  k_tsa = 6*(k_a**2) + (22*k_r*k_r/7)
  k2 = "Find the TSA and volume of a cube with a side of {}, having a hemisphere of radius {} cut out of it.".format(k_a,k_r)
  k2a = "{},{}".format(k_tsa,k_vol)
  return(k2,k2a)

def k_3():
  k_r = random.choice((4.9,5.6,7,7.7,14))
  k_a = 2*k_r
  k_vol = (k_a**3) + ((4*22*k_r*k_r*k_r)/(3*7))
  k_tsa = 6*(k_a**2) + 2*(22*k_r*k_r/7)
  k3 = "Find the TSA and volume of a cube with a side of {}, having a hemisphere of radius {} attatched to each end of it.".format(k_a,k_r)
  k3a = "{},{}".format(k_tsa,k_vol)
  return(k3,k3a)

def k_4():
  k_r = random.choice((4.9,5.6,7,7.7,14))
  k_h = random.randint(1,16)
  k_vol = (22*k_r*k_r*k_h/21)+(44*k_r*k_r/21)
  k4 = "Calculate the volume of a cone of radius {} and height {}, having a hemisphere attatched to the bottom of it".format(k_r,k_h)
  k4a = str(k_vol)
  return(k4,k4a)

correct_answer = 0
prev_q_no = 0
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
counter_6 = 0
counter_7 = 0
counter_8 = 0
counter_9 = 0
counter_10 = 0
counter_11 = 0
counter_12 = 0
counter_13 = 0
counter_quadratics = 0
counter_linears = 0
practice_score = 0
score = 0
re_temp = {}
nonre_temp = {}

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/page1', methods=['GET'])
def page1():
    return render_template('page1.html')
    
@app.route('/page2')
def page2():
    global practice_score
    return render_template('page2.html', practice_score = practice_score)

@app.route('/reset', methods = ['GET'])
def reset():
    
    global counter_1
    global counter_2
    global counter_3
    global counter_4
    global counter_5
    global counter_6
    global counter_7
    global counter_8
    global counter_9
    global counter_10
    global counter_11
    global counter_12
    global counter_13 
    global score
    global re_temp
    global nonre_temp
    global correct_answer
    global prev_q_no
    global practice_score

    correct_answer = counter_1 = counter_2 = counter_3 = counter_4 = counter_5 = counter_6 = counter_7 = counter_8 = counter_9 = counter_10 = counter_11 = counter_12 = counter_13 = score = practice_score = prev_q_no = 0
    re_temp = nonre_temp = {}

    return "Filler"

@app.route('/chapter1', methods=['GET','POST'])
def chapter1():
    
    global counter_1  
    global score
    global re_temp
    global nonre_temp
    global correct_answer
    global prev_q_no

    output = "Result"

    user_answer = request.form.get('user_answer')
    q_no = prev_q_no

    if counter_1 == 10000:
        correct_answer = 0
        prev_q_no = 0
        counter = 0
        score = 0
        re_temp = {}
        nonre_temp = {}
        return redirect("/page1")

    if counter_1 != 0:
    
        if user_answer == correct_answer:
            output = "Well done. "+ correct_answer + " is the right answer!"
            score += 5
            
        else:
            output = "That was either an invalid response or an incorrect one. It's okay, you'll get it next time!"
            score -= 1
        
    if counter_1 == 0:
        score = 0
        re_temp = {}
        for i in (1,6,11):
            r,t,y = HCF()
            p,o = pf()
            s,d,lcm,hcf,prdct = LCM()
            l,z,x,c,v = LCM_HCF_3()
            b,m = term_or_non_term()
            a_reusable = {i:["Using Euclid's Division Algorithm, find the HCF of {} and {}.".format(r,t),str(y)],i+1:["Express {} as the product of it's prime factors.".format(p),o],i+2:["Find the LCM and HCF of {} and {} and verify that LCM x HCF is equal to the product of the numbers. ( Format: LCMxHCF=Product )".format(s,d),"{}x{}={}".format(lcm,hcf,prdct)],i+3:["Find the LCM and HCF of {}, {} and {}. (Format : LCM,HCF)".format(l,z,x),"{},{}".format(c,v)],i+4:["Check whether {} is a terminating or non-terminating decimal. (Format : y/n)".format(b),m]}
            re_temp.update(a_reusable)
        a_nonre = {1:["Given that HCF (306, 657) = 9, find LCM (306, 657)","22338"],2:["Use Euclid’s division algorithm to find the HCF of :135 and 225","45"],3:["An army contingent of 616 members is to march behind an army band of 32 members in a parade. The two groups are to march in the same number of columns. What is the maximum number of columns in which they can march?","8"],4:["There is a circular path around a sports field. Sonia takes 18 minutes to drive one round of the field, while Ravi takes 12 minutes for the same. Suppose they both start at the same point and at the same time, and go in the same direction. After how many minutes will they meet again at the starting point?","36"],5:["Use Euclid’s division algorithm to find the HCF of :196 and 38220","196"]}
        nonre_temp = a_nonre.copy()

    if len(re_temp) > 0 and len(nonre_temp) > 0:
        
        re_or_nonre = random.randint(0,1) #Determining whether to use a reusable(generative) question or a non-reusable NCERT question       #{{{CHANGE LATER TO RANDINT}}} CRITICAL
        if re_or_nonre == 0: #Reusable questions
            q_no = random.choice(list(re_temp.keys()))
            question = re_temp[q_no][0]
            answer = re_temp[q_no][1]
            del re_temp[q_no]

        if re_or_nonre == 1: #Non reusable questions
            q_no = random.choice(list(nonre_temp.keys()))
            question = nonre_temp[q_no][0]
            answer = nonre_temp[q_no][1]
            del nonre_temp[q_no]
            
    elif len(re_temp) > 0:
        q_no = random.choice(list(re_temp.keys()))
        question = re_temp[q_no][0]
        answer = re_temp[q_no][1]
        del re_temp[q_no]

    elif len(nonre_temp) > 0:
        q_no = random.choice(list(nonre_temp.keys()))
        question = nonre_temp[q_no][0]
        answer = nonre_temp[q_no][1]
        del nonre_temp[q_no]

    else:
        output = "Well done, bro! You finished this chapter's questions"
        question = "{}/100".format(score)
        counter_1 = 10000
        
    if output != "Well done, bro! You finished this chapter's questions":             
        prev_q_no = q_no
        correct_answer = answer
        print(answer)
        counter_1 += 1
        
    return render_template('chapter1.html',question = question, score = score, output = output)

@app.route('/chapter2', methods=['GET','POST'])
def chapter2():

    global counter_2  
    global score
    global re_temp
    global nonre_temp
    global correct_answer
    global prev_q_no

    output = "Result"

    user_answer = request.form.get('user_answer')
    q_no = prev_q_no

    if counter_2 == 10000:
        correct_answer = 0
        prev_q_no = 0
        counter_2 = 0
        score = 0
        re_temp = {}
        nonre_temp = {}
        return redirect("/page1")

    if counter_2 != 0:
    
        if user_answer == correct_answer:
            output = "Well done. "+ correct_answer + " is the right answer!"
            score += 5
            
        else:
            output = "That was either an invalid response or an incorrect one. It's okay, you'll get it next time!"
            score -= 1
        
    if counter_2 == 0:
        score = 0
        re_temp = {}
        i = None
        for i in (1,5,9):
            b_q,b_t = poly_roots()
            b_a,b_s = poly_roots_fr()
            b_d,b_f = poly_roots_thingamajig()
            b_k,b_l = big_boy_polynomial()
            b_reusable = {i:[b_q,str(b_t)],i+1:[b_a,b_s],i+2:[b_d,b_f],i+3:[b_k,b_l]}
            re_temp.update(b_reusable)
        b_nonre = {1:["Find the zeroes of the following quadratic polynomials and verify the relationship between the zeroes and the coefficients:x² – 2x – 8.[Format:smaller,greater]","-2,4"],2:["Find the zeroes of the following quadratic polynomials and verify the relationship between the zeroes and the coefficients:4u² + 8u.[Format:smaller,greater]","-2,0"],3:["Obtain all other zeroes of 3x⁴ + 6x³ – 2x² – 10x – 5, if two of its zeroes are √(5/3) and –√(5/3).[Format:smaller,greater]","-1,-1"],4:["If two zeroes of the polynomial x⁴ – 6x³ – 26x² + 138x – 35 are ± 2√(3), find other zeroes.[Format:smaller,greater]","-5,7"]}
        nonre_temp = b_nonre.copy()

    if len(re_temp) > 0 and len(nonre_temp) > 0:
        
        re_or_nonre = random.randint(0,1) #Determining whether to use a reusable(generative) question or a non-reusable NCERT question       #{{{CHANGE LATER TO RANDINT}}} CRITICAL
        if re_or_nonre == 0: #Reusable questions
            q_no = random.choice(list(re_temp.keys()))
            question = re_temp[q_no][0]
            answer = re_temp[q_no][1]
            del re_temp[q_no]

        if re_or_nonre == 1: #Non reusable questions
            q_no = random.choice(list(nonre_temp.keys()))
            question = nonre_temp[q_no][0]
            answer = nonre_temp[q_no][1]
            del nonre_temp[q_no]
            
    elif len(re_temp) > 0:
        q_no = random.choice(list(re_temp.keys()))
        question = re_temp[q_no][0]
        answer = re_temp[q_no][1]
        del re_temp[q_no]

    elif len(nonre_temp) > 0:
        q_no = random.choice(list(nonre_temp.keys()))
        question = nonre_temp[q_no][0]
        answer = nonre_temp[q_no][1]
        del nonre_temp[q_no]

    else:
        output = "Well done, bro! You finished this chapter's questions"
        question = "{}/80".format(score)
        counter_2 = 10000
        
    if output != "Well done, bro! You finished this chapter's questions":             
        prev_q_no = q_no
        correct_answer = answer
        print(answer)
        counter_2 += 1
        
    return render_template('chapter2.html',question = question, score = score, output = output)
    
@app.route('/chapter3', methods=['GET','POST'])
def chapter3():
    
    global counter_3 
    global score
    global re_temp
    global nonre_temp
    global correct_answer
    global prev_q_no

    output = "Result"

    user_answer = request.form.get('user_answer')
    q_no = prev_q_no

    if counter_3 == 10000:
        correct_answer = 0
        prev_q_no = 0
        counter_3 = 0
        score = 0
        re_temp = {}
        nonre_temp = {}
        return redirect("/page1")

    if counter_3 != 0:
    
        if user_answer == correct_answer:
            output = "Well done. "+ correct_answer + " is the right answer!"
            score += 5
            
        else:
            output = "That was either an invalid response or an incorrect one. It's okay, you'll get it next time!"
            score -= 1
        
    if counter_3 == 0:
        score = 0
        re_temp = {}
        i = None
        for i in (1,6,11):
            c1,c1a = l_e_1()
            c2,c2a = l_e_2()
            c3,c3a = l_e_3()
            c4,c4a = l_e_4()
            c5,c5a = l_e_5()
            c_reusable = {i:[c1,c1a],i+1:[c2,c2a],i+2:[c3,c3a],i+3:[c4,c4a],i+4:[c5,c5a]}
            re_temp.update(c_reusable)
        c_nonre = {1:["Half the perimeter of a rectangular garden, whose length is 4 m more than its width, is 36 m. Find the dimensions of the garden.(Format:length,breadth)","20,16"],2:["The students of a class are made to stand in rows. If 3 students are extra in a row, there would be 1 row less. If 3 students are less in a row, there would be 2 rows more. Find the number of students in the class.","36"],3:["Solve the following pair of linear equations by the substitution method:s – t = 3.(Format:s,t)","9,6"],4:[" A train covered a certain distance at a uniform speed. If the train would have been 10 km/h faster, it would have taken 2 hours less than the scheduled time. And, if the train were slower by 10 km/h; it would have taken 3 hours more than the scheduled time. Find the distance covered by the train.","600"],5:["Solve the following pair of linear equations by the elimination method and the substitution method:3x + 4y = 10 and 2x – 2y = 2","2,1"]}
        nonre_temp = c_nonre.copy()

    if len(re_temp) > 0 and len(nonre_temp) > 0:
        
        re_or_nonre = random.randint(0,1) #Determining whether to use a reusable(generative) question or a non-reusable NCERT question       #{{{CHANGE LATER TO RANDINT}}} CRITICAL
        if re_or_nonre == 0: #Reusable questions
            q_no = random.choice(list(re_temp.keys()))
            question = re_temp[q_no][0]
            answer = re_temp[q_no][1]
            del re_temp[q_no]

        if re_or_nonre == 1: #Non reusable questions
            q_no = random.choice(list(nonre_temp.keys()))
            question = nonre_temp[q_no][0]
            answer = nonre_temp[q_no][1]
            del nonre_temp[q_no]
            
    elif len(re_temp) > 0:
        q_no = random.choice(list(re_temp.keys()))
        question = re_temp[q_no][0]
        answer = re_temp[q_no][1]
        del re_temp[q_no]

    elif len(nonre_temp) > 0:
        q_no = random.choice(list(nonre_temp.keys()))
        question = nonre_temp[q_no][0]
        answer = nonre_temp[q_no][1]
        del nonre_temp[q_no]

    else:
        output = "Well done, bro! You finished this chapter's questions"
        question = "{}/100".format(score)
        counter_3 = 10000
        
    if output != "Well done, bro! You finished this chapter's questions":             
        prev_q_no = q_no
        correct_answer = answer
        print(answer)
        counter_3 += 1
        
    return render_template('chapter3.html',question = question, score = score, output = output)    
    
@app.route('/chapter4', methods=['GET','POST'])
def chapter4():
    
    global counter_4 
    global score
    global re_temp
    global nonre_temp
    global correct_answer
    global prev_q_no

    output = "Result"

    user_answer = request.form.get('user_answer')
    q_no = prev_q_no

    if counter_4 == 10000:
        correct_answer = 0
        prev_q_no = 0
        counter_4 = 0
        score = 0
        re_temp = {}
        nonre_temp = {}
        return redirect("/page1")

    if counter_4 != 0:
    
        if user_answer == correct_answer:
            output = "Well done. "+ correct_answer + " is the right answer!"
            score += 5
            
        else:
            output = "That was either an invalid response or an incorrect one. It's okay, you'll get it next time!"
            score -= 1
        
    if counter_4 == 0:
        score = 0
        re_temp = {}
        i = None
        for i in (1,4,7,10,13):
            d1,d1a = quad_roots_fr()
            d2,d2a = poly_roots()
            d3,d3a = quad_3()
            d_reusable = {i:[d1,d1a],i+1:[d2,d2a],i+2:[d3,d3a]}
            re_temp.update(d_reusable)
            
    if len(re_temp) > 0:
        q_no = random.choice(list(re_temp.keys()))
        question = re_temp[q_no][0]
        answer = re_temp[q_no][1]
        del re_temp[q_no]

    else:
        output = "Well done, bro! You finished this chapter's questions"
        question = "{}/75".format(score)
        counter_4 = 10000
        
    if output != "Well done, bro! You finished this chapter's questions":             
        prev_q_no = q_no
        correct_answer = answer
        print(answer)
        counter_4 += 1
        
    return render_template('chapter4.html',question = question, score = score, output = output)    


@app.route('/chapter5', methods=['GET','POST'])
def chapter5():
        
    global counter_5 
    global score
    global re_temp
    global nonre_temp
    global correct_answer
    global prev_q_no

    output = "Result"

    user_answer = request.form.get('user_answer')
    q_no = prev_q_no

    if counter_5 == 10000:
        correct_answer = 0
        prev_q_no = 0
        counter_5 = 0
        score = 0
        re_temp = {}
        nonre_temp = {}
        return redirect("/page1")

    if counter_5 != 0:
    
        if user_answer == correct_answer:
            output = "Well done. "+ correct_answer + " is the right answer!"
            score += 5
            
        else:
            output = "That was either an invalid response or an incorrect one. It's okay, you'll get it next time!"
            score -= 1
        
    if counter_5 == 0:
        score = 0
        re_temp = {}
        i = None
        for i in (1,7,13):
            e1,e1a = e_1()
            e2,e2a = e_2()
            e3,e3a = e_3()
            e4,e4a = e_4()
            e5,e5a = e_5()
            e6,e6a = e_6()
            e_reusable = {i:[e1,e1a],i+1:[e2,e2a],i+2:[e3,e3a],i+3:[e4,e4a],i+4:[e5,e5a],i+5:[e6,e6a]}
            re_temp.update(e_reusable)

    if len(re_temp) > 0:
        q_no = random.choice(list(re_temp.keys()))
        question = re_temp[q_no][0]
        answer = re_temp[q_no][1]
        del re_temp[q_no]
        
    else:
        output = "Well done, bro! You finished this chapter's questions"
        question = "{}/90".format(score)
        counter_5 = 10000
        
    if output != "Well done, bro! You finished this chapter's questions":             
        prev_q_no = q_no
        correct_answer = answer
        print(answer)
        counter_5 += 1
        
    return render_template('chapter5.html',question = question, score = score, output = output)    

@app.route('/chapter6', methods=['GET','POST'])
def chapter6():
    
    global counter_6 
    global score
    global re_temp
    global nonre_temp
    global correct_answer
    global prev_q_no

    output = "Result"

    user_answer = request.form.get('user_answer')
    q_no = prev_q_no

    if counter_6 == 10000:
        correct_answer = 0
        prev_q_no = 0
        counter_6 = 0
        score = 0
        re_temp = {}
        nonre_temp = {}
        return redirect("/page1")

    if counter_6 != 0:
    
        if user_answer == correct_answer:
            output = "Well done. "+ correct_answer + " is the right answer!"
            score += 5
            
        else:
            output = "That was either an invalid response or an incorrect one. It's okay, you'll get it next time!"
            score -= 1
        
    if counter_6 == 0:
        score = 0
        re_temp = {}
        i = None
        for i in range(1,21):
            f1,f1a = f_1()
            f_reusable = {i:[f1,f1a]}
            re_temp.update(f_reusable)

    if len(re_temp) > 0:
        q_no = random.choice(list(re_temp.keys()))
        question = re_temp[q_no][0]
        answer = re_temp[q_no][1]
        del re_temp[q_no]

    else:
        output = "Well done, bro! You finished this chapter's questions"
        question = "{}/100".format(score)
        counter_6 = 10000
        
    if output != "Well done, bro! You finished this chapter's questions":             
        prev_q_no = q_no
        correct_answer = answer
        print(answer)
        counter_6 += 1
        
    return render_template('chapter6.html',question = question, score = score, output = output)    

@app.route('/chapter7', methods=['GET','POST'])
def chapter7():
    
    global counter_7 
    global score
    global re_temp
    global nonre_temp
    global correct_answer
    global prev_q_no

    output = "Result"

    user_answer = request.form.get('user_answer')
    q_no = prev_q_no

    if counter_7 == 10000:
        correct_answer = 0
        prev_q_no = 0
        counter_7 = 0
        score = 0
        re_temp = {}
        nonre_temp = {}
        return redirect("/page1")

    if counter_7 != 0:
    
        if user_answer == correct_answer:
            output = "Well done. "+ correct_answer + " is the right answer!"
            score += 5
            
        else:
            output = "That was either an invalid response or an incorrect one. It's okay, you'll get it next time!"
            score -= 1
        
    if counter_7 == 0:
        score = 0
        re_temp = {}
        i = None
        for i in (1,8,15):
            g1,g1a = g_1()
            g2,g2a = g_2()
            g3,g3a = g_3()
            g4,g4a = g_4()
            g5,g5a = g_5()
            g6,g6a = g_6()
            g7,g7a = g_7()
            g_reusable = {i:[g1,g1a],i+1:[g2,g2a],i+2:[g3,g3a],i+3:[g4,g4a],i+4:[g5,g5a],i+5:[g6,g6a],i+6:[g7,g7a]}
            re_temp.update(g_reusable)
            
    if len(re_temp) > 0:
        q_no = random.choice(list(re_temp.keys()))
        question = re_temp[q_no][0]
        answer = re_temp[q_no][1]
        del re_temp[q_no]

    else:
        output = "Well done, bro! You finished this chapter's questions"
        question = "{}/105".format(score)
        counter_7 = 10000
        
    if output != "Well done, bro! You finished this chapter's questions":             
        prev_q_no = q_no
        correct_answer = answer
        print(answer)
        counter_7 += 1
        
    return render_template('chapter7.html',question = question, score = score, output = output)    

    
@app.route('/chapter8', methods=['GET','POST'])
def chapter8():
    return redirect("/page1")

@app.route('/chapter9', methods=['GET','POST'])
def chapter9():
    
    global counter_9 
    global score
    global re_temp
    global nonre_temp
    global correct_answer
    global prev_q_no

    output = "Result"

    user_answer = request.form.get('user_answer')
    q_no = prev_q_no

    if counter_9 == 10000:
        correct_answer = 0
        prev_q_no = 0
        counter_9 = 0
        score = 0
        re_temp = {}
        nonre_temp = {}
        return redirect("/page1")

    if counter_9 != 0:
    
        if user_answer == correct_answer:
            output = "Well done. "+ correct_answer + " is the right answer!"
            score += 5
            
        else:
            output = "That was either an invalid response or an incorrect one. It's okay, you'll get it next time!"
            score -= 1
        
    if counter_9 == 0:
        score = 0
        re_temp = {}
        i = None
        for i in (1,4,7,10,13):
            i1,i1a = i_1()
            i2,i2a = i_2()
            i3,i3a = i_3()
            i_reusable = {i:[i1,i1a],i+1:[i2,i2a],i+2:[i3,i3a]}
            re_temp.update(i_reusable)

    if len(re_temp) > 0 and len(nonre_temp) > 0:
        
        re_or_nonre = random.randint(0,1) #Determining whether to use a reusable(generative) question or a non-reusable NCERT question       #{{{CHANGE LATER TO RANDINT}}} CRITICAL
        if re_or_nonre == 0: #Reusable questions
            q_no = random.choice(list(re_temp.keys()))
            question = re_temp[q_no][0]
            answer = re_temp[q_no][1]
            del re_temp[q_no]

        if re_or_nonre == 1: #Non reusable questions
            q_no = random.choice(list(nonre_temp.keys()))
            question = nonre_temp[q_no][0]
            answer = nonre_temp[q_no][1]
            del nonre_temp[q_no]
            
    elif len(re_temp) > 0:
        q_no = random.choice(list(re_temp.keys()))
        question = re_temp[q_no][0]
        answer = re_temp[q_no][1]
        del re_temp[q_no]

    elif len(nonre_temp) > 0:
        q_no = random.choice(list(nonre_temp.keys()))
        question = nonre_temp[q_no][0]
        answer = nonre_temp[q_no][1]
        del nonre_temp[q_no]

    else:
        output = "Well done, bro! You finished this chapter's questions"
        question = "{}/75".format(score)
        counter_9 = 10000
        
    if output != "Well done, bro! You finished this chapter's questions":             
        prev_q_no = q_no
        correct_answer = answer
        print(answer)
        counter_9 += 1
        
    return render_template('chapter9.html',question = question, score = score, output = output)    

    
@app.route('/chapter10', methods=['GET','POST'])
def chapter10():
    
    global counter_10 
    global score
    global re_temp
    global nonre_temp
    global correct_answer
    global prev_q_no

    output = "Result"

    user_answer = request.form.get('user_answer')
    q_no = prev_q_no

    if counter_10 == 10000:
        correct_answer = 0
        prev_q_no = 0
        counter_10 = 0
        score = 0
        re_temp = {}
        nonre_temp = {}
        return redirect("/page1")

    if counter_10 != 0:
    
        if user_answer == correct_answer:
            output = "Well done. "+ correct_answer + " is the right answer!"
            score += 5
            
        else:
            output = "That was either an invalid response or an incorrect one. It's okay, you'll get it next time!"
            score -= 1
        
    if counter_10 == 0:
        score = 0
        re_temp = {}
        i = None
        for i in (1,4,7,10,13):
            j1,j1a = j_1()
            j2,j2a = j_2()
            j3,j3a = j_3()
            j_reusable = {i:[j1,j1a],i+1:[j2,j2a],i+2:[j3,j3a]}
            re_temp.update(j_reusable)
           
    if len(re_temp) > 0:
        q_no = random.choice(list(re_temp.keys()))
        question = re_temp[q_no][0]
        answer = re_temp[q_no][1]
        del re_temp[q_no]

    else:
        output = "Well done, bro! You finished this chapter's questions"
        question = "{}/75".format(score)
        counter_10 = 10000
        
    if output != "Well done, bro! You finished this chapter's questions":             
        prev_q_no = q_no
        correct_answer = answer
        print(answer)
        counter_10 += 1
        
    return render_template('chapter10.html',question = question, score = score, output = output)    
    
@app.route('/chapter11', methods=['GET','POST'])
def chapter11():
    
    global counter_11 
    global score
    global re_temp
    global nonre_temp
    global correct_answer
    global prev_q_no

    output = "Result"

    user_answer = request.form.get('user_answer')
    q_no = prev_q_no

    if counter_11 == 10000:
        correct_answer = 0
        prev_q_no = 0
        counter_11 = 0
        score = 0
        re_temp = {}
        nonre_temp = {}
        return redirect("/page1")

    if counter_11 != 0:
    
        if user_answer == correct_answer:
            output = "Well done. "+ correct_answer + " is the right answer!"
            score += 5
            
        else:
            output = "That was either an invalid response or an incorrect one. It's okay, you'll get it next time!"
            score -= 1
        
    if counter_11 == 0:
        score = 0
        re_temp = {}
        i = None
        for i in (1,5,9,13):
            k1,k1a = k_1()
            k2,k2a = k_2()
            k3,k3a = k_3()
            k4,k4a = k_4()
            k_reusable = {i:[k1,k1a],i+1:[k2,k2a],i+2:[k3,k3a],i+3:[k4,k4a]}
            re_temp.update(k_reusable)
            
    if len(re_temp) > 0:
        q_no = random.choice(list(re_temp.keys()))
        question = re_temp[q_no][0]
        answer = re_temp[q_no][1]
        del re_temp[q_no]

    else:
        output = "Well done, bro! You finished this chapter's questions"
        question = "{}/80".format(score)
        counter_11 = 10000
        
    if output != "Well done, bro! You finished this chapter's questions":             
        prev_q_no = q_no
        correct_answer = answer
        print(answer)
        counter_11 += 1
        
    return render_template('chapter11.html',question = question, score = score, output = output)    

@app.route('/chapter12', methods=['GET','POST'])
def chapter12():
    return redirect("/page1")
   
@app.route('/chapter13', methods=['GET','POST'])
def chapter13():
    return redirect("/page1")

@app.route('/quadratics', methods=['GET','POST'])
def quadratics():

    global practice_score
    global correct_answer
    global counter_quadratics
    
    output = "Solve Solve Solve!"
    user_answer = request.form.get('user_answer')

    if counter_quadratics != 0:
        
        if user_answer == correct_answer:
            output = "Well done. "+ correct_answer + " is the right answer!"
            practice_score += 5

        else:
            output = "That was either an invalid response or an incorrect one. The right answer was "+correct_answer+". It's okay, you'll get it next time!"
            practice_score -= 1

    if practice_score >= 100:
        counter_quadratics = 0
        return render_template("cat.html")

    question, answer = poly_roots_fr()
    counter_quadratics += 1
    correct_answer = answer
        
    return render_template('quadratics.html', score = practice_score, question = question, output = output)

@app.route('/linears', methods=['GET','POST'])
def linears():

    global practice_score
    global correct_answer
    global counter_linears
    
    output = "Solve Solve Solve!"
    user_answer = request.form.get('user_answer')

    if counter_linears != 0:
        
        if user_answer == correct_answer:
            output = "Well done. "+ correct_answer + " is the right answer!"
            practice_score += 5

        else:
            output = "That was either an invalid response or an incorrect one. It's okay, you'll get it next time!"
            practice_score -= 1

    if practice_score >= 100:
        counter_quadratics = 0
        return render_template("cat.html")

    question, answer = l_e_1()
    counter_linears += 1
    correct_answer = answer
        
    return render_template('linears.html', score = practice_score, question = question, output = output)

@app.route('/credits', methods=['POST','GET'])
def credits():
    return render_template('credits.html')

if __name__ == '__main__':
    app.run()
