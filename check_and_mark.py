import os, glob, datetime
report_path='D:\\USB_ERROR_REPORT.txt'
logs=glob.glob('D:\\opencore-*.txt')
valid=[l for l in logs if len(open(l,'rb').read())>500]
valid.sort(key=os.path.getmtime)
log_file=valid[-1] if valid else (sorted(logs,key=os.path.getmtime)[-1] if logs else '')
with open(log_file,'rb') as f: data=f.read()
text=data.decode('latin1',errors='ignore')
lines=text.splitlines()
last=lines[-10:] if len(lines)>=10 else lines
hang='EXITBS:START' if any('EXITBS:START' in l for l in last) else ('Early UI/Config error' if len(lines)<10 else 'Unknown')
content=f'Newest substantial log: {os.path.basename(log_file)} (lines={len(lines)})\nLast lines:\n'+'\n'.join(last[-5:])+f'\nHang: {hang}\nVerdict: Still frozen after fixes (DevirtualiseMmio=False, SSDT-RHUB=True). Stop rebooting blindly.\n'
with open(report_path,'w') as f:
    f.write('USB BOOT AUTO-MARKER\nTime: '+str(datetime.datetime.now())+'\n'+content)
print('Updated',report_path)
print('Log:',os.path.basename(log_file),'lines=',len(lines),'hang=',hang)
