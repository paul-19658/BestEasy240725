import subprocess
def runChrome(port):
    # 似乎独占一个线程，不结束的话，线性的话，后面没法运行
    cmd = r'"C:\Users\BESTEASY\AppData\Local\Google\Chrome\Application\chrome.exe" ' \
          f'--remote-debugging-port={port} '
    subprocess.run(cmd)
runChrome(9222)