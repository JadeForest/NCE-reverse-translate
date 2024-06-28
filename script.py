import os

DIR = '新概念英语2'
os.chdir(os.getcwd()+f'\\{DIR}')

jscript = '''
<script type="text/javascript">
	function display(id){  
		var target=document.getElementById(id);  
		if(target.style.display=="none"){  
			target.style.display="";  
		}else{  
			target.style.display="none";  
		}  
	}  
</script>
'''

with open('titles.txt','r',encoding='utf-8') as f:
    titles = f.readlines()

with open('lesson.txt','r',encoding='GBK') as f:
    raw = f.read()
    
titles = [s.strip('\n') for s in titles]
lessons = raw.split('$课文')
lessons = [s for s in lessons if s]

for title, lesson in zip(titles, lessons):
    lines = lesson.split('\n')
    lines = [s.strip() for s in lines[1:] if s]
    with open(title+'.html','w',encoding='UTF-8') as html_file:
        for i, (en, zh) in enumerate(zip(lines[::2], lines[1::2])):
            en = en.lstrip('0123456789.')
            html = (f'<div>{zh}</div>'
                    +'<input type="text" size=200><br>'
                    +'<div><input type="submit" value="答案" onclick="display(\'{}\')">'.format(i)
                    +f'<span id="{i}" style="display:none">{en}</span></div><br>')

            html_file.write(html+'\n')
            
        html_file.write(jscript)