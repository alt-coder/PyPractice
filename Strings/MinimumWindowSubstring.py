def minWindow(s,p):
            allchar = {i for i in p}
            if(len(s)<len(p)): return ""
            dubilicate = allchar
            rd = []
            mp = [0]*256
            dt={}
            for i in p:
                # if mp[ord(i)] == 0:
                    mp[ord(i)] += 1
                    if i not in dt:
                        dt[i]=1
                    else : dt[i]+=1
            ct = 0
            l,r = 0,0
            minl,minr = -1,len(s)-1
            while(r<len(s)):
                if(mp[ord(s[r])] > 0):
                    ct += 1
                    mp[ord(s[r])]-=1
                rd.append(s[r])

                if(ct == len(p)):
                    pd = rd[1:]
                    dpt={}
                    for ch in pd:
                        if ch not in dpt:
                            dpt[ch] = 1
                        else:
                            dpt[ch]+=1
                while(ct == len(p)):
                    pd = rd[1:]
                    if s[l] not in allchar or (s[l] in pd and dpt[s[l]] >= dt[s[l]]):
                        l+=1
                        dpt[pd[0]]-=1
                        rd = pd
                        continue
                    else:
                        if r-l < minr-minl:
                            minl = l
                            minr = r
                        mp[ord(s[l])]=1
                        l+=1
                        ct-=1
                        rd = pd
                r+=1
            if minl == -1 : return ""
            return s[minl:minr+1]

print(minWindow("this is a test string","tist"))