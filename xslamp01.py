#!/usr/bin/python3

#Autor: Ondřej Šlampa, xslamp01@stud.fit.vutbr.cz
#Projekt: KRY projekt 1: Eliptické křivky
#Popis: Program vypočítá soukromý klíč k veřejnému klíči.

Fp=0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
a=-3
b=0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
P=(0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
    0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)
public=(0x52910a011565810be90d03a299cb55851bab33236b7459b21db82b9f5c1874fe,               
    0xe3d03339f660528d511c2b1865bcdfd105490ffc4c597233dd2b2504ca42a562)

#Vypočítá inverzní prvek k zadanému.
def inverse(a):
    return pow(a, Fp-2, Fp)

#Sečte dva body na eliptické křivce.
def add(P1, P2):
    (xp,yp)=P1
    (xq,yq)=P2
    l=((yq-yp)*inverse(xq-xp))%Fp
    xr=(l*l-xp-xq)%Fp
    yr=(l*(xp-xr)-yp)%Fp
    return (xr,yr)

#Vynásobí bod na eliptické křivce dvěma.
def double(P):
    (xp,yp)=P
    l=((3*xp*xp+a)*inverse(2*yp))%Fp
    xr=(l*l-2*xp)%Fp
    yr=(l*(xp-xr)-yp)%Fp
    return (xr,yr)

#Nalezne soukromý klíč.
def find_d():
    if(P==public):
        return 1

    i=2
    i_times_P=double(P)

    if(i_times_P==public):
        return i

    while i_times_P!=public and i<100:
        i=i+1
        i_times_P=add(P,i_times_P)
    return i

#Tisk soukromého klíče.
print(find_d())

