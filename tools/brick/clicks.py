import numpy as np, soundfile as sf
SR=48000; FPS=30; N=392; START=12; DROP=10; END=489
rng=np.random.default_rng(7)
out=np.zeros(int(SR*END/FPS)+SR)
def click(pitch):
    t=np.arange(int(SR*0.06))/SR
    tone=np.sin(2*np.pi*pitch*t)*np.exp(-t*90)
    noise=rng.standard_normal(len(t))*np.exp(-t*220)
    knock=np.sin(2*np.pi*(pitch*0.35)*t)*np.exp(-t*60)
    return 0.35*tone+0.25*noise+0.4*knock
for i in range(N):
    land=(START+i+DROP*0.55)/FPS
    s=int(land*SR); c=click(rng.uniform(1800,2600))*rng.uniform(0.6,1.0)
    out[s:s+len(c)]+=c
# final "done" chime when last brick lands
t=np.arange(int(SR*1.2))/SR
chime=sum(np.sin(2*np.pi*f*t)*np.exp(-t*3) for f in (1046.5,1318.5,1568.0))/3
s=int((START+N+DROP)/FPS*SR); out[s:s+len(chime)]+=0.6*chime
out=out/np.max(np.abs(out))*0.8
sf.write("clicks.wav",out[:int(SR*END/FPS)],SR); print("ok",len(out)/SR)
