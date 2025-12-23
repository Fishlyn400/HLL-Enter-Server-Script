# 基于Steam命令行的《人间地狱》一键启动并连接到指定服务器的脚本

### _**仅适用于Steam平台的HLL**_

-------------------------------

## 部署：
### Step 1. 打包
```powershell
pip install -r requirements.txt
pip install pyinstaller
pyinstaller -n <YourServerName> hll_enter_server_script\main.py --hidden-import=game_manager --hidden-import=constants
```
（将 `<YourServerName>` 替换成你的服务器简称）

### Step 2. 将 `address.txt` 放入打包生成的 `dist/YourServerName` 文件夹下
`address.txt` 文件内容为你的服务器游戏端口的套接字地址，形如 ``xx.xx.xx.xx:xxxx``，不应有其他字符。
文件夹结构如下
```text
dist/
└── circle_3/
    ├── _internal/
    ├── circle_3.exe
    └── address.txt
```
### Step 3. 将 `<YourServerName>` 文件夹放到目标机器上即可。双击exe即可运行

### 另外地，需确保一下文件在目标机器上至少存在一个：
```text
C:\Users\Fish\Desktop\Steam.lnk
C:\Users\Public\Desktop\Steam.lnk
C:\Steam.lnk
```
即在桌面上或C盘根目录里至少存在一个Steam的快捷方式

--------------------------------

_**你可以自行对文件夹里的exe文件创建快捷方式**_

--------------------------------








