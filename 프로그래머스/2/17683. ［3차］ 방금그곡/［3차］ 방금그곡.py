def trans(music):
    music = music.replace('A#', 'a')
    music = music.replace('C#', 'c')
    music = music.replace('D#', 'd')
    music = music.replace('F#', 'f')
    music = music.replace('G#', 'g')
    
    return music

def hTom(time):
    return int(time[:2])*60 + int(time[3:])
    
def solution(m, musicinfos):
    answer = []
    m = trans(m)
    
    for infos in musicinfos:
        s, e, title, music = infos.split(',')
        time = hTom(e)-hTom(s)
        music = trans(music)
        
        music = music * (time//len(music)) + music[:time%len(music)]
        
        if m in music:
            answer.append((title, time))
            
    if len(answer) >= 1:
        answer.sort(key = lambda x:(-x[1]))
        return answer[0][0]
    else:
        return '(None)'
        