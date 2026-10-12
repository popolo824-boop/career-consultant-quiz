# input: json list of [base, [chunk_plain_text,...]]; writes base.wav and base.json (chunk start times)
import sys,json,os,warnings; warnings.filterwarnings("ignore")
import numpy as np, soundfile as sf
from kokoro import KPipeline
p=KPipeline(lang_code='j'); SR=24000; GAP=0.06
for base,chunks in json.load(open(sys.argv[1])):
    if os.path.exists(base+".json"): continue
    parts=[];starts=[];t=0.12
    parts.append(np.zeros(int(SR*0.12),dtype=np.float32))
    for c in chunks:
        a=np.concatenate([x.audio.numpy() for x in p(c,voice='jf_alpha',speed=1.3)])
        starts.append(t); parts.append(a); parts.append(np.zeros(int(SR*GAP),dtype=np.float32)); t+=len(a)/SR+GAP
    sf.write(base+".wav",np.concatenate(parts),SR)
    json.dump(starts,open(base+".json","w")); print(base,round(t,2),flush=True)
