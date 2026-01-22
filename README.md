# 火绒病毒库更新日志

本仓库跟踪[火绒安全软件](https://www.huorong.cn/)病毒库的变更，通过读取`pset.db,troj.db,hwl.db,behav.db,crithash.db`自动生成与上一版本相比新增的特征项/报毒名, 黑名单哈希和白名单哈希。

> **免责声明**：本项目非火绒官方出品，仅供学习和技术交流使用。作者不对使用本项目造成的任何后果负责。

## 概览

- **最新版本**: `1769081101` (2026-01-22 11:25:01 UTC)
- **特征项总数**: 66,919
- **关键哈希特征项总数**: 80,764
- **行为特征项总数**: 909
- **黑名单哈希总数**: 150,983
- **白名单哈希总数**: 123,463
- **已跟踪版本数**: 29

## 特征项分类分布

```mermaid
pie showData
    title Top 10
    "Trojan" : 23997
    "TrojanDownloader" : 9795
    "Backdoor" : 6505
    "TrojanSpy" : 6091
    "OMacro" : 3394
    "Virus" : 2820
    "TrojanDropper" : 2724
    "Adware" : 2345
    "VirTool" : 2299
    "Ransom" : 1991
    "Other" : 4958
```


---

## 更新日志

<details>
<summary><b>1769081101</b> - 2026-01-22 11:25:01 UTC</summary>

#### 特征项变更 ([pset.txt](data/1769081101.pset.txt))

<details>
<summary>
新增正式定义: 38 | 移除正式定义: 1
</summary>

```
[+] Backdoor/ASPX.WebShell.m
[+] Backdoor/MSIL.AsyncRAT.ac
[+] HEUR:Backdoor/ASPX.WebShell.n
[+] HEUR:Backdoor/ASPX.WebShell.o
[+] HEUR:Trojan/ProxyChanger.d
[+] HEUR:Trojan/ShellLoader.aib
[+] HVM:Backdoor/W64.Agent.n
[+] HVM:TrojanDownloader/W64.Agent.ct
[+] Trojan/BAT.Loader.l
[+] Trojan/FakeApp.acc
[+] Trojan/FakeApp.acd
[+] Trojan/FakeApp.ace
[+] Trojan/FakeApp.acf
[+] Trojan/FakeApp.acg
[+] Trojan/FakeApp.ach
[+] Trojan/HTML.Agent.br
[+] Trojan/Injector.clp
[+] Trojan/Loader.nb
[+] Trojan/Loader.nc
[+] Trojan/MSIL.Obfuscated.kd
[+] Trojan/MSIL.ShellLoader.am
[+] Trojan/Obfuscated.nw
[+] Trojan/PS.Agent.bt
[+] Trojan/Python.Agent.bt
[+] Trojan/Runner.fo
[+] Trojan/ShellLoader.aib
[+] Trojan/W64.Injector.cc
[+] Trojan/W64.Injector.cd
[+] TrojanDownloader/Agent.bly
[+] TrojanDownloader/JS.Agent.ij
[+] TrojanDownloader/JS.Maloader.as
[+] TrojanDownloader/LNK.Agent.hd
[+] TrojanDownloader/MSIL.Agent.ajl
[+] TrojanDownloader/PS.Agent.fh
[+] TrojanDownloader/PS.Agent.fi
[+] TrojanDownloader/VBS.Agent.kh
[+] TrojanDownloader/VBS.Agent.ki
[+] TrojanSpy/W64.Stealer.aa
[-] Trojan/ShellLoader.ahx
```

</details>

<details>
<summary>
新增遥测定义: 39 | 移除遥测定义: 39
</summary>

```
[+] Backdoor/AsyncRAT.n!submit
[+] Backdoor/MSIL.Crysan.f!submit
[+] Exploit/CVE-2025-32433.a!submit
[+] HEUR:Backdoor/MSIL.Agent.aw!submit
[+] HEUR:Trojan/PS.Runner.v!submit
[+] HVM:Trojan/ShellLoader.ck!submit
[+] HVM:Trojan/ShellLoader.cm!submit
[+] HVM:Trojan/ShellLoader.cn!submit
[+] HVM:Trojan/ShellLoader.co!submit
[+] Trojan/FakeApp.aci!submit
[+] Trojan/FakeApp.acj!submit
[+] Trojan/FakeApp.ack!submit
[+] Trojan/FakeApp.acl!submit
[+] Trojan/FakeApp.acm!submit
[+] Trojan/FakeApp.acn!submit
[+] Trojan/Injector.clq!submit
[+] Trojan/Injector.clr!submit
[+] Trojan/JS.Obfuscated.dj!submit
[+] Trojan/JS.Obfuscated.dk!submit
[+] Trojan/JS.Obfuscated.dl!submit
[+] Trojan/Linux.Mirai.gq!submit
[+] Trojan/Loader.nd!submit
[+] Trojan/Loader.ne!submit
[+] Trojan/Loader.nf!submit
[+] Trojan/Loader.ng!submit
[+] Trojan/MSIL.Obfuscated.ke!submit
[+] Trojan/MSIL.Obfuscated.kf!submit
[+] Trojan/Python.Agent.bu!submit
[+] Trojan/Python.Agent.bv!submit
[+] Trojan/Python.Loader.n!submit
[+] Trojan/ShellLoader.ahf!submit
[+] Trojan/ShellLoader.aic!submit
[+] Trojan/ShellLoader.aid!submit
[+] Trojan/ShellLoader.aie!submit
[+] TrojanDownloader/Agent.blz!submit
[+] TrojanDownloader/JS.Agent.ik!submit
[+] TrojanDownloader/Linux.Agent.ec!submit
[+] TrojanDownloader/MSIL.Agent.ajm!submit
[+] TrojanDropper/Agent.alg!submit
[-] Backdoor/ASPX.WebShell.m!submit
[-] Backdoor/MSIL.AsyncRAT.ac!submit
[-] HEUR:Backdoor/ASPX.WebShell.n!submit
[-] HEUR:Backdoor/ASPX.WebShell.o!submit
[-] HEUR:Trojan/ShellLoader.aib!submit
[-] HVM:Backdoor/W64.Agent.n!submit
[-] HVM:TrojanDownloader/W64.Agent.ct!submit
[-] Trojan/BAT.Loader.l!submit
[-] Trojan/FakeApp.acc!submit
[-] Trojan/FakeApp.acd!submit
[-] Trojan/FakeApp.ace!submit
[-] Trojan/FakeApp.acf!submit
[-] Trojan/FakeApp.acg!submit
[-] Trojan/FakeApp.ach!submit
[-] Trojan/HTML.Agent.br!submit
[-] Trojan/Injector.clp!submit
[-] Trojan/Loader.nb!submit
[-] Trojan/Loader.nc!submit
[-] Trojan/MSIL.Obfuscated.kd!submit
[-] Trojan/MSIL.ShellLoader.am!submit
[-] Trojan/Obfuscated.nw!submit
[-] Trojan/PS.Agent.bt!submit
[-] Trojan/ProxyChanger.i!submit
[-] Trojan/Python.Agent.bt!submit
[-] Trojan/Runner.fo!submit
[-] Trojan/ShellLoader.aib!submit
[-] Trojan/W64.Injector.cc!submit
[-] Trojan/W64.Injector.cd!submit
[-] TrojanDownloader/Agent.bly!submit
[-] TrojanDownloader/JS.Agent.ij!submit
[-] TrojanDownloader/JS.Maloader.as!submit
[-] TrojanDownloader/LNK.Agent.hd!submit
[-] TrojanDownloader/MSIL.Agent.ajl!submit
[-] TrojanDownloader/PS.Agent.fh!submit
[-] TrojanDownloader/PS.Agent.fi!submit
[-] TrojanDownloader/VBS.Agent.fj!submit
[-] TrojanDownloader/VBS.Agent.kh!submit
[-] TrojanDownloader/VBS.Agent.ki!submit
[-] TrojanSpy/W64.Stealer.aa!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1769081101.crithash.txt))

<details>
<summary>
新增正式定义: 18 | 移除正式定义: 1
</summary>

```
[+] HackTool/Linux.PortScan.a!crit
[+] HackTool/Linux.PortScan.b!crit
[+] Ransom/W32.LockFile.rl!crit
[+] Trojan/BAT.Obfuscated.arg!crit
[+] Trojan/HTML.Redirector.a!crit
[+] Trojan/Linux.Mirai.d!crit
[+] Trojan/MSIL.Obfuscated.kd!crit
[+] Trojan/W32.FakeApp.g!crit
[+] Trojan/W32.FakeApp.h!crit
[+] Trojan/W32.ShellLoader.x!crit
[+] Trojan/W32.ShellLoader.y
[+] Trojan/W64.StartPage.ll!crit
[+] TrojanDownloader/HTML.Agent.f!crit
[+] TrojanDownloader/LNK.Agent.g!crit
[+] TrojanDownloader/PS.Agent.bq!crit
[+] TrojanDownloader/PS.Agent.br!crit
[+] TrojanSpy/W64.Stealer.e!crit
[+] TrojanSpy/W64.Stealer.f!crit
[-] TrojanSpy/W64.Stealer.d!crit
```

</details>

<details>
<summary>
新增遥测定义: 29 | 移除遥测定义: 20
</summary>

```
[+] Backdoor/PHP.WebShell.ab!crit!submit
[+] Backdoor/W32.Lotok.ab!crit!submit
[+] Exploit/JS.CVE-2022-1364.a!crit!submit
[+] Joke/BAT.Shutdown.c!crit!submit
[+] Joke/VBS.CrazyWindow.b!crit!submit
[+] Joke/VBS.CrazyWindow.c!crit!submit
[+] Joke/VBS.CrazyWindow.d!crit!submit
[+] Trojan/JS.Redirector.a!crit!submit
[+] Trojan/Linux.DDos.b!crit!submit
[+] Trojan/Linux.Mirai.e!crit!submit
[+] Trojan/Linux.Mirai.f!crit!submit
[+] Trojan/PS.Obfuscator.fs!crit!submit
[+] Trojan/VBS.KillWin.a!crit!submit
[+] Trojan/W32.HiJack.z!crit!submit
[+] Trojan/W64.Agent.gp!crit!submit
[+] Trojan/W64.Agent.gq!crit!submit
[+] TrojanDownloader/BAT.Agent.c!crit!submit
[+] TrojanDownloader/HTML.Agent.g!crit!submit
[+] TrojanDownloader/LNK.Agent.f!crit!submit
[+] TrojanDownloader/PS.Agent.bs!crit!submit
[+] TrojanDownloader/PS.Runner.t!crit!submit
[+] TrojanDownloader/PS.Runner.u!crit!submit
[+] TrojanDownloader/PS.Runner.v!crit!submit
[+] TrojanDownloader/PS.Runner.w!crit!submit
[+] TrojanDownloader/W32.Starter.g!crit!submit
[+] TrojanDownloader/W32.Starter.h!crit!submit
[+] TrojanDropper/W64.Agent.b!crit!submit
[+] TrojanSpy/W32.Shiz.a!crit!submit
[+] TrojanSpy/W32.Shiz.b!crit!submit
[-] HackTool/Linux.PortScan.a!crit!submit
[-] HackTool/Linux.PortScan.b!crit!submit
[-] Ransom/W32.LockFile.rl!crit!submit
[-] Trojan/BAT.Obfuscated.arg!crit!submit
[-] Trojan/HTML.Redirector.a!crit!submit
[-] Trojan/JS.Pdfka.l!crit!submit
[-] Trojan/Linux.Mirai.d!crit!submit
[-] Trojan/MSIL.Obfuscated.kd!crit!submit
[-] Trojan/W32.FakeApp.g!crit!submit
[-] Trojan/W32.FakeApp.h!crit!submit
[-] Trojan/W32.ShellLoader.s!crit!submit
[-] Trojan/W32.ShellLoader.x!crit!submit
[-] Trojan/W32.ShellLoader.y!crit!submit
[-] Trojan/W64.StartPage.ll!crit!submit
[-] TrojanDownloader/HTML.Agent.f!crit!submit
[-] TrojanDownloader/LNK.Agent.g!crit!submit
[-] TrojanDownloader/PS.Agent.bq!crit!submit
[-] TrojanDownloader/PS.Agent.br!crit!submit
[-] TrojanDropper/W32.Agent.f!crit!submit
[-] TrojanSpy/W64.Stealer.f!crit!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1769081101.troj.txt))

新增: 1,563 | 移除: 1

</details>
<details>
<summary><b>1768997183</b> - 2026-01-21 12:06:23 UTC</summary>

#### 特征项变更 ([pset.txt](data/1768997183.pset.txt))

<details>
<summary>
新增正式定义: 53 | 移除正式定义: 2
</summary>

```
[+] Adware/InstallCore.t
[+] Backdoor/Lotok.ol
[+] Exploit/CVE-2022-1364
[+] HEUR:Ransom/LockFile.rj
[+] HEUR:Trojan/FakeApp.av
[+] HEUR:Trojan/ShellLoader.ahy
[+] HVM:Trojan/ShellLoader.cl
[+] HVM:Trojan/W64.ShellLoader.ak
[+] HVM:TrojanSpy/W64.Stealer.aa
[+] HackTool/EDRBlocker
[+] HackTool/MSIL.AppxPotato.a
[+] HackTool/MSIL.BrowserGhost.a
[+] HackTool/MSIL.ListRDP.a
[+] HackTool/MSIL.LsassDumper.b
[+] HackTool/MSIL.SharpClipHistory.a
[+] HackTool/MSIL.SharpElevator.a
[+] HackTool/MSIL.SharpWxDump.a
[+] Ransom/Akira.d
[+] Ransom/LockFile.rj
[+] SVM:TrojanDownloader/JS.MalBehav.gen!H
[+] SVM:TrojanDownloader/JS.MalBehav.gen.G
[+] Trojan/Agent.clt
[+] Trojan/BAT.Pwrsvc.bw
[+] Trojan/CoinMiner.lb
[+] Trojan/FakeApp.abz
[+] Trojan/FakeApp.aca
[+] Trojan/FakeApp.acb
[+] Trojan/Injector.cln
[+] Trojan/Injector.clo
[+] Trojan/Korplug.ak
[+] Trojan/Korplug.al
[+] Trojan/Linux.CoinMiner.dx
[+] Trojan/Linux.DDos.bj
[+] Trojan/Linux.DDos.bk
[+] Trojan/Loader.na
[+] Trojan/MSIL.AddUser.k
[+] Trojan/Python.Loader.m
[+] Trojan/ShellLoader.ahz
[+] Trojan/ShellLoader.aia
[+] Trojan/StartPage.lk
[+] Trojan/W64.Agent.gn
[+] Trojan/W64.Agent.go
[+] Trojan/W64.Loader.al
[+] TrojanDownloader/Linux.Agent.ea
[+] TrojanDownloader/Linux.Agent.eb
[+] TrojanDownloader/PS.Agent.ff
[+] TrojanDownloader/PS.Agent.fg
[+] TrojanDownloader/VBS.Agent.kg
[+] TrojanDownloader/W64.Agent.cs
[+] TrojanDropper/Agent.ale
[+] TrojanDropper/Agent.alf
[+] TrojanDropper/W64.Agent.cb
[+] Virus/Viking.a!dll@viking_kdll
[-] Ransom/Akira.e
[-] SVM:TrojanDownloader/JS.MalBehav.gen.a
```

</details>

<details>
<summary>
新增遥测定义: 45 | 移除遥测定义: 51
</summary>

```
[+] Backdoor/ASPX.WebShell.m!submit
[+] Backdoor/Lotok.nv!submit
[+] Backdoor/MSIL.AsyncRAT.ac!submit
[+] HEUR:Backdoor/ASPX.WebShell.n!submit
[+] HEUR:Backdoor/ASPX.WebShell.o!submit
[+] HEUR:Trojan/ShellLoader.aib!submit
[+] HVM:Backdoor/W64.Agent.n!submit
[+] HVM:TrojanDownloader/W64.Agent.ct!submit
[+] HackTool/MSIL.SchTask.a!submit
[+] HackTool/W64.ProcessHacker.b!submit
[+] Ransom/LockFile.rk!submit
[+] Trojan/BAT.Loader.l!submit
[+] Trojan/DLLHijack.ac!submit
[+] Trojan/FakeApp.acc!submit
[+] Trojan/FakeApp.acd!submit
[+] Trojan/FakeApp.ace!submit
[+] Trojan/FakeApp.acf!submit
[+] Trojan/FakeApp.acg!submit
[+] Trojan/FakeApp.ach!submit
[+] Trojan/HTML.Agent.br!submit
[+] Trojan/Injector.clp!submit
[+] Trojan/Loader.nb!submit
[+] Trojan/Loader.nc!submit
[+] Trojan/MSIL.Obfuscated.kd!submit
[+] Trojan/MSIL.ShellLoader.am!submit
[+] Trojan/Obfuscated.nw!submit
[+] Trojan/PS.Agent.bt!submit
[+] Trojan/ProxyChanger.i!submit
[+] Trojan/Python.Agent.bt!submit
[+] Trojan/Runner.fo!submit
[+] Trojan/ShellLoader.aib!submit
[+] Trojan/W64.Injector.cc!submit
[+] Trojan/W64.Injector.cd!submit
[+] TrojanDownloader/Agent.bly!submit
[+] TrojanDownloader/JS.Agent.ij!submit
[+] TrojanDownloader/JS.Maloader.as!submit
[+] TrojanDownloader/LNK.Agent.hd!submit
[+] TrojanDownloader/MSIL.Agent.ajl!submit
[+] TrojanDownloader/PS.Agent.fh!submit
[+] TrojanDownloader/PS.Agent.fi!submit
[+] TrojanDownloader/VBS.Agent.fj!submit
[+] TrojanDownloader/VBS.Agent.kh!submit
[+] TrojanDownloader/VBS.Agent.ki!submit
[+] TrojanSpy/W64.Stealer.aa!submit
[+] TrojanSpy/W64.Stealer.ab!submit
[-] Adware/InstallCore.t!submit
[-] Backdoor/Lotok.ol!submit
[-] HEUR:Ransom/LockFile.rj!submit
[-] HEUR:Trojan/FakeApp.av!submit
[-] HEUR:Trojan/ShellLoader.ahy!submit
[-] HVM:Trojan/MalBehav.i!submit
[-] HVM:Trojan/ShellLoader.cl!submit
[-] HVM:Trojan/W64.ShellLoader.ak!submit
[-] HVM:TrojanSpy/W64.Stealer.aa!submit
[-] HackTool/AppxPotato.a!submit
[-] HackTool/BrowserGhost.a!submit
[-] HackTool/ListRDP.a!submit
[-] HackTool/LsassDumper.b!submit
[-] HackTool/SchTask.a!submit
[-] HackTool/SharpClipHistory.a!submit
[-] HackTool/SharpElevator.a!submit
[-] HackTool/SharpWxDump.a!submit
[-] Ransom/Akira.d!submit
[-] Ransom/LockFile.rj!submit
[-] SVM:TrojanDownloader/JS.MalBehav.b!submit
[-] Trojan/AddUser.k!submit
[-] Trojan/Agent.clt!submit
[-] Trojan/Agent.clu!submit
[-] Trojan/CoinMiner.lb!submit
[-] Trojan/FakeApp.abz!submit
[-] Trojan/FakeApp.aca!submit
[-] Trojan/FakeApp.acb!submit
[-] Trojan/Injector.cln!submit
[-] Trojan/Injector.clo!submit
[-] Trojan/Korplug.ak!submit
[-] Trojan/Korplug.al!submit
[-] Trojan/Linux.CoinMiner.dx!submit
[-] Trojan/Linux.DDos.bj!submit
[-] Trojan/Linux.DDos.bk!submit
[-] Trojan/Loader.na!submit
[-] Trojan/Python.Loader.m!submit
[-] Trojan/ShellLoader.ahz!submit
[-] Trojan/ShellLoader.aia!submit
[-] Trojan/StartPage.lk!submit
[-] Trojan/W64.Agent.gn!submit
[-] Trojan/W64.Agent.go!submit
[-] Trojan/W64.Loader.al!submit
[-] TrojanDownloader/Linux.Agent.ea!submit
[-] TrojanDownloader/Linux.Agent.eb!submit
[-] TrojanDownloader/PS.Agent.ff!submit
[-] TrojanDownloader/PS.Agent.fg!submit
[-] TrojanDownloader/VBS.Agent.kg!submit
[-] TrojanDownloader/W64.Agent.cs!submit
[-] TrojanDropper/Agent.ale!submit
[-] TrojanDropper/Agent.alf!submit
[-] TrojanDropper/W64.Agent.cb!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1768997183.crithash.txt))

<details>
<summary>
新增正式定义: 7
</summary>

```
[+] Exploit/W32.Vulndriver.b!crit
[+] Exploit/W32.Vulndriver.c!crit
[+] Trojan/HTML.Phishing.ot!crit
[+] Trojan/JS.Obfuscated.dj!crit
[+] Trojan/JS.Obfuscated.dk!crit
[+] Trojan/JS.Obfuscated.dl!crit
[+] Trojan/SCR.ShellCode.m!crit
```

</details>

<details>
<summary>
新增遥测定义: 32 | 移除遥测定义: 12
</summary>

```
[+] Backdoor/PHP.Webshell.aa!crit!submit
[+] Backdoor/PS.ReverseShell.h!crit!submit
[+] Backdoor/PS.ReverseShell.j!crit!submit
[+] HackTool/Linux.PortScan.a!crit!submit
[+] HackTool/Linux.PortScan.b!crit!submit
[+] Ransom/W32.LockFile.d!crit!submit
[+] Ransom/W32.LockFile.e!crit!submit
[+] Ransom/W32.LockFile.rl!crit!submit
[+] Trojan/BAT.Obfuscated.arg!crit!submit
[+] Trojan/HTML.Redirector.a!crit!submit
[+] Trojan/Linux.Mirai.d!crit!submit
[+] Trojan/MSIL.Obfuscated.kd!crit!submit
[+] Trojan/W32.FakeApp.g!crit!submit
[+] Trojan/W32.FakeApp.h!crit!submit
[+] Trojan/W32.KillFile.a!crit!submit
[+] Trojan/W32.ShellLoader.s!crit!submit
[+] Trojan/W32.ShellLoader.x!crit!submit
[+] Trojan/W32.ShellLoader.y!crit!submit
[+] Trojan/W32.Stealer.b!crit!submit
[+] Trojan/W64.StartPage.ll!crit!submit
[+] TrojanDownloader/HTML.Agent.f!crit!submit
[+] TrojanDownloader/LNK.Agent.g!crit!submit
[+] TrojanDownloader/PS.Agent.bq!crit!submit
[+] TrojanDownloader/PS.Agent.br!crit!submit
[+] TrojanDownloader/PS.Runner.s!crit!submit
[+] TrojanDownloader/VBS.Runner.g!crit!submit
[+] TrojanDownloader/VBS.Starter.b!crit!submit
[+] TrojanDropper/W32.Agent.f!crit!submit
[+] TrojanSpy/PS.Keylogger.b!crit!submit
[+] TrojanSpy/PS.Stealer.n!crit!submit
[+] TrojanSpy/W64.Stealer.e!crit!submit
[+] TrojanSpy/W64.Stealer.f!crit!submit
[-] Backdoor/W32.Lotok.aa!crit!submit
[-] Exploit/W32.Vulndriver.b!crit!submit
[-] Exploit/W32.Vulndriver.c!crit!submit
[-] HEUR:Trojan/W32.HiJack.a!crit!submit
[-] Trojan/HTML.Phishing.ot!crit!submit
[-] Trojan/JS.Obfuscated.dj!crit!submit
[-] Trojan/JS.Obfuscated.dk!crit!submit
[-] Trojan/JS.Obfuscated.dl!crit!submit
[-] Trojan/SCR.ShellCode.m!crit!submit
[-] Trojan/W32.ShellLoader.q!crit!submit
[-] Trojan/W32.ShellLoader.r!crit!submit
[-] TrojanDropper/W32.Agent.e!crit!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1768997183.troj.txt))

新增: 31

</details>
<details>
<summary><b>1768907496</b> - 2026-01-20 11:11:36 UTC</summary>

#### 特征项变更 ([pset.txt](data/1768907496.pset.txt))

<details>
<summary>
新增正式定义: 40 | 移除正式定义: 53
</summary>

```
[+] Backdoor/Androm.aj
[+] Backdoor/Lotok.oc
[+] HEUR:Trojan/JS.Injector.t
[+] HVM:Trojan/ShellLoader.ck
[+] OMacro/Thus.n
[+] Ransom/Akira.e
[+] Ransom/Linux.Lockbit.e
[+] Trojan/Agent.cls
[+] Trojan/BAT.Obfuscated.an
[+] Trojan/FakeApp.abr
[+] Trojan/FakeApp.abs
[+] Trojan/FakeApp.abt
[+] Trojan/FakeApp.abu
[+] Trojan/FakeApp.abv
[+] Trojan/FakeApp.abw
[+] Trojan/FakeApp.abx
[+] Trojan/FakeApp.aby
[+] Trojan/Injector.clm
[+] Trojan/JS.Obfuscated.di
[+] Trojan/KillWin.dj
[+] Trojan/Linux.Agent.dh
[+] Trojan/Linux.DDos.bh
[+] Trojan/Linux.DDos.bi
[+] Trojan/Loader.mx
[+] Trojan/Loader.my
[+] Trojan/Loader.mz
[+] Trojan/MSIL.Loader.at
[+] Trojan/MSIL.Obfuscated.kc
[+] Trojan/OSX.Loader.a
[+] Trojan/OSX.Loader.c
[+] Trojan/ShellLoader.ahy
[+] Trojan/W64.Agent.gl
[+] Trojan/W64.Loader.ak
[+] TrojanDownloader/Agent.blx
[+] TrojanDownloader/LNK.Agent.hc
[+] TrojanDownloader/W64.Agent.cr
[+] TrojanDropper/Agent.alb
[+] TrojanDropper/Agent.alc
[+] TrojanDropper/Agent.ald
[+] TrojanDropper/PS.Agent.z
[-] Adware/ExtensionInstaller
[-] Backdoor/XRat
[-] Constructor/CodeLoaderGen
[-] Constructor/ShellGenerate
[-] Exploit/CVE-2020-16902
[-] Exploit/CVE-2022-21882
[-] Exploit/CVE-2025-29824
[-] Exploit/CVE-2025-60710
[-] HackTool/AntSword
[-] HackTool/BloodHound
[-] HackTool/BrowserSpy
[-] HackTool/DSEFix
[-] HackTool/Ddos.d
[-] HackTool/DefenderWrite
[-] HackTool/DumpGuard
[-] HackTool/Gost
[-] HackTool/Inject
[-] HackTool/Launcher
[-] HackTool/Linux.CoinMiner
[-] HackTool/Mimipenguin
[-] HackTool/NoPatchGuard
[-] HackTool/PassStealer
[-] HackTool/Railgun
[-] HackTool/Reaper
[-] HackTool/Remote
[-] HackTool/SilentButDeadly
[-] HackTool/Stowaway
[-] HackTool/Uacme
[-] Hacktool/DisPPL
[-] Joke/Crayzpop
[-] Joke/ScreenMelter
[-] RootKit/Agent
[-] Rootkit/DNSHijack
[-] Rootkit/Inject
[-] Rootkit/Injecter
[-] Rootkit/MiniFilter
[-] Trojan/BSoD
[-] Trojan/FakeChrome
[-] Trojan/JS.Dropper
[-] Trojan/JS.POSCardStealer
[-] Trojan/Lisp.Neyer
[-] Trojan/MSIL.Obfuscated
[-] Trojan/ServStart
[-] Trojan/VB.Agent
[-] Trojan/VBS.Radier
[-] Trojan/Zlader
[-] TrojanDownloader/Qfas
[-] TrojanDownloader/SiMay
[-] TrojanSpy/JS.Credtect
[-] TrojanSpy/Loader
[-] TrojanSpy/MSIL.Steam
[-] Virus/VBS.Agent
[-] Worm/VBS.Padon
```

</details>

<details>
<summary>
新增遥测定义: 52 | 移除遥测定义: 44
</summary>

```
[+] Adware/InstallCore.t!submit
[+] Backdoor/Lotok.ol!submit
[+] HEUR:Ransom/LockFile.rj!submit
[+] HEUR:Trojan/FakeApp.av!submit
[+] HEUR:Trojan/ShellLoader.ahy!submit
[+] HVM:Trojan/MalBehav.i!submit
[+] HVM:Trojan/ShellLoader.cl!submit
[+] HVM:Trojan/W64.ShellLoader.ak!submit
[+] HVM:TrojanSpy/W64.Stealer.aa!submit
[+] HackTool/AppxPotato.a!submit
[+] HackTool/BrowserGhost.a!submit
[+] HackTool/ListRDP.a!submit
[+] HackTool/LsassDumper.b!submit
[+] HackTool/SchTask.a!submit
[+] HackTool/SharpClipHistory.a!submit
[+] HackTool/SharpElevator.a!submit
[+] HackTool/SharpWxDump.a!submit
[+] Ransom/LockFile.rj!submit
[+] SVM:TrojanDownloader/JS.MalBehav.a!submit
[+] SVM:TrojanDownloader/JS.MalBehav.b!submit
[+] Trojan/AddUser.k!submit
[+] Trojan/Agent.clt!submit
[+] Trojan/Agent.clu!submit
[+] Trojan/CoinMiner.lb!submit
[+] Trojan/FakeApp.abz!submit
[+] Trojan/FakeApp.aca!submit
[+] Trojan/FakeApp.acb!submit
[+] Trojan/Injector.cln!submit
[+] Trojan/Injector.clo!submit
[+] Trojan/Korplug.ak!submit
[+] Trojan/Korplug.al!submit
[+] Trojan/Linux.CoinMiner.dx!submit
[+] Trojan/Linux.DDos.bj!submit
[+] Trojan/Linux.DDos.bk!submit
[+] Trojan/Linux.Mirai.gp!submit
[+] Trojan/Loader.na!submit
[+] Trojan/Python.Loader.m!submit
[+] Trojan/ShellLoader.ahz!submit
[+] Trojan/ShellLoader.aia!submit
[+] Trojan/StartPage.lk!submit
[+] Trojan/W64.Agent.gn!submit
[+] Trojan/W64.Agent.go!submit
[+] Trojan/W64.Loader.al!submit
[+] TrojanDownloader/Linux.Agent.ea!submit
[+] TrojanDownloader/Linux.Agent.eb!submit
[+] TrojanDownloader/PS.Agent.ff!submit
[+] TrojanDownloader/PS.Agent.fg!submit
[+] TrojanDownloader/VBS.Agent.kg!submit
[+] TrojanDownloader/W64.Agent.cs!submit
[+] TrojanDropper/Agent.ale!submit
[+] TrojanDropper/Agent.alf!submit
[+] TrojanDropper/W64.Agent.cb!submit
[-] Backdoor/Androm.aj!submit
[-] Backdoor/Lotok.oc!submit
[-] Exploit/Vulndriver!submit
[-] HEUR:Trojan/JS.Injector.t!submit
[-] HVM:Trojan/ShellLoader.ck!submit
[-] HackTool/PetitPotato!submit
[-] OMacro/Thus.n!submit
[-] Ransom/Akira.e!submit
[-] Ransom/Linux.Lockbit.e!submit
[-] RootKit/Agent!submit
[-] Trojan/Agent.cls!submit
[-] Trojan/BAT.Obfuscated.an!submit
[-] Trojan/FakeApp.abb!submit
[-] Trojan/FakeApp.abr!submit
[-] Trojan/FakeApp.abs!submit
[-] Trojan/FakeApp.abt!submit
[-] Trojan/FakeApp.abu!submit
[-] Trojan/FakeApp.abv!submit
[-] Trojan/FakeApp.abw!submit
[-] Trojan/FakeApp.abx!submit
[-] Trojan/FakeApp.aby!submit
[-] Trojan/Injector.clm!submit
[-] Trojan/JS.Obfuscated.di!submit
[-] Trojan/KillWin.dj!submit
[-] Trojan/Linux.Agent.dh!submit
[-] Trojan/Linux.DDos.bh!submit
[-] Trojan/Linux.DDos.bi!submit
[-] Trojan/Loader.mx!submit
[-] Trojan/Loader.my!submit
[-] Trojan/Loader.mz!submit
[-] Trojan/MSIL.Loader.at!submit
[-] Trojan/MSIL.Obfuscated.kc!submit
[-] Trojan/OSX.Loader.a!submit
[-] Trojan/OSX.Loader.c!submit
[-] Trojan/ShellLoader.ahy!submit
[-] Trojan/W64.Agent.gl!submit
[-] Trojan/W64.Loader.ak!submit
[-] TrojanDownloader/Agent.blx!submit
[-] TrojanDownloader/LNK.Agent.hc!submit
[-] TrojanDownloader/W64.Agent.cr!submit
[-] TrojanDropper/Agent.alb!submit
[-] TrojanDropper/Agent.alc!submit
[-] TrojanDropper/Agent.ald!submit
[-] TrojanDropper/PS.Agent.z!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1768907496.crithash.txt))

<details>
<summary>
新增正式定义: 8 | 移除正式定义: 1
</summary>

```
[+] Backdoor/JSP.WebShell.r!crit
[+] Backdoor/Linux.Gafgyt.b!crit
[+] HackTool/W64.Fscan.a!crit
[+] Trojan/Linux.Mirai.c!crit
[+] Trojan/MSIL.Obfuscated.aq!crit
[+] TrojanDownloader/HTML.Agent.e!crit
[+] TrojanDownloader/W32.Agent.blx!crit
[+] TrojanSpy/W64.Stealer.d!crit
[-] Backdoor/JSP.WebShell.r
```

</details>

<details>
<summary>
新增遥测定义: 34 | 移除遥测定义: 11
</summary>

```
[+] Backdoor/BAT.ReverseShell.c!crit!submit
[+] Backdoor/PHP.WebShell.y!crit!submit
[+] Backdoor/PHP.WebShell.z!crit!submit
[+] Backdoor/W32.Lotok.aa!crit!submit
[+] Exploit/W32.Vulndriver.b!crit!submit
[+] Exploit/W32.Vulndriver.c!crit!submit
[+] HEUR:Trojan/W32.HiJack.a!crit!submit
[+] Joke/BAT.CrazyWindow.a!crit!submit
[+] Ransom/VBS.LockFile.b!crit!submit
[+] Ransom/W32.LockFile.b!crit!submit
[+] Trojan/BAT.KillFile.b!crit!submit
[+] Trojan/BAT.KillWin.j!crit!submit
[+] Trojan/BAT.KillWin.k!crit!submit
[+] Trojan/HTML.Phishing.ot!crit!submit
[+] Trojan/JS.Obfuscated.dj!crit!submit
[+] Trojan/JS.Obfuscated.dk!crit!submit
[+] Trojan/JS.Obfuscated.dl!crit!submit
[+] Trojan/SCR.KillWin.b!crit!submit
[+] Trojan/SCR.ShellCode.m!crit!submit
[+] Trojan/VBS.KillAV.c!crit!submit
[+] Trojan/W32.Injector.u!crit!submit
[+] Trojan/W32.Injector.v!crit!submit
[+] Trojan/W32.ShellLoader.q!crit!submit
[+] Trojan/W32.ShellLoader.r!crit!submit
[+] Trojan/W64.ShellLoader.e!crit!submit
[+] TrojanDownloader/W32.Starter.b!crit!submit
[+] TrojanDownloader/W32.Starter.c!crit!submit
[+] TrojanDownloader/W32.Starter.e!crit!submit
[+] TrojanDropper/W32.Agent.e!crit!submit
[+] TrojanDropper/W32.Starter.b!crit!submit
[+] TrojanSpy/BAT.Stealer.i!crit!submit
[+] TrojanSpy/PHP.Phishing.b!crit!submit
[+] TrojanSpy/W32.Stealer.ad!crit!submit
[+] TrojanSpy/W32.Stealer.ae!crit!submit
[-] Backdoor/Linux.Gafgyt.b!crit!submit
[-] Backdoor/W32.Lotok.z!crit!submit
[-] HackTool/W64.Fscan.a!crit!submit
[-] Trojan/Linux.Mirai.c!crit!submit
[-] Trojan/MSIL.Obfuscated.aq!crit!submit
[-] Trojan/W32.Agent.aa!crit!submit
[-] Trojan/W32.Agent.y!crit!submit
[-] Trojan/W32.Agent.z!crit!submit
[-] TrojanDownloader/HTML.Agent.e!crit!submit
[-] TrojanDownloader/W32.Agent.blx!crit!submit
[-] TrojanSpy/W64.Stealer.d!crit!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1768907496.troj.txt))

新增: 304 | 移除: 38,729

#### 白名单哈希变更 ([hwl.txt](data/1768907496.hwl.txt))

移除: 18,410

</details>
<details>
<summary><b>1768821989</b> - 2026-01-19 11:26:29 UTC</summary>

#### 特征项变更 ([pset.txt](data/1768821989.pset.txt))

<details>
<summary>
新增正式定义: 37
</summary>

```
[+] HEUR:TrojanDropper/Agent.ar
[+] HVM:Backdoor/Lotok.cl
[+] Trojan/BAT.Runner.bs
[+] Trojan/BAT.Runner.bt
[+] Trojan/FakeApp.aae
[+] Trojan/FakeApp.abo
[+] Trojan/FakeApp.abp
[+] Trojan/FakeApp.abq
[+] Trojan/FakeApp.zd
[+] Trojan/Loader.mw
[+] Trojan/MSIL.Disabler.e
[+] Trojan/MSIL.Obfuscated.kb
[+] Trojan/PS.Loader.q
[+] Trojan/PS.Loader.r
[+] Trojan/Python.DDos.i
[+] Trojan/Rozena.bf
[+] Trojan/Runner.fn
[+] Trojan/ShellLoader.ahv
[+] Trojan/ShellLoader.ahw
[+] Trojan/ShellLoader.ahx
[+] Trojan/W64.Agent.gm
[+] Trojan/W64.Injector.cb
[+] Trojan/W64.ShellLoader.aj
[+] TrojanDownloader/JS.Agent.ii
[+] TrojanDownloader/PS.Agent.fe
[+] TrojanDownloader/VBS.Agent.kf
[+] TrojanDropper/Agent.akz
[+] TrojanDropper/Agent.ala
[+] TrojanDropper/Android.Agent.ci
[+] TrojanDropper/Android.Agent.cj
[+] TrojanDropper/Android.Agent.ck
[+] TrojanDropper/Android.Agent.cl
[+] TrojanDropper/Android.Agent.cm
[+] TrojanDropper/JS.Agent.cd
[+] TrojanDropper/Python.Loader.a
[+] TrojanSpy/Android.SMSSpy.aq
[+] TrojanSpy/Android.SMSSpy.ar
```

</details>

<details>
<summary>
新增遥测定义: 41 | 移除遥测定义: 38
</summary>

```
[+] Backdoor/Androm.aj!submit
[+] Backdoor/Lotok.oc!submit
[+] HEUR:Trojan/JS.Injector.t!submit
[+] HVM:Trojan/ShellLoader.ck!submit
[+] Ransom/Akira.d!submit
[+] Ransom/Akira.e!submit
[+] Ransom/Linux.Lockbit.e!submit
[+] Trojan/Agent.cls!submit
[+] Trojan/BAT.Obfuscated.an!submit
[+] Trojan/FakeApp.abb!submit
[+] Trojan/FakeApp.abr!submit
[+] Trojan/FakeApp.abs!submit
[+] Trojan/FakeApp.abt!submit
[+] Trojan/FakeApp.abu!submit
[+] Trojan/FakeApp.abv!submit
[+] Trojan/FakeApp.abw!submit
[+] Trojan/FakeApp.abx!submit
[+] Trojan/FakeApp.aby!submit
[+] Trojan/Injector.clm!submit
[+] Trojan/JS.Obfuscated.di!submit
[+] Trojan/KillWin.dj!submit
[+] Trojan/Linux.Agent.dg!submit
[+] Trojan/Linux.Agent.dh!submit
[+] Trojan/Linux.Agent.di!submit
[+] Trojan/Linux.DDos.bh!submit
[+] Trojan/Linux.DDos.bi!submit
[+] Trojan/Linux.Mirai.go!submit
[+] Trojan/Loader.mx!submit
[+] Trojan/Loader.my!submit
[+] Trojan/Loader.mz!submit
[+] Trojan/MSIL.Loader.at!submit
[+] Trojan/MSIL.Obfuscated.kc!submit
[+] Trojan/OSX.Loader.a!submit
[+] Trojan/OSX.Loader.c!submit
[+] Trojan/ShellLoader.ahy!submit
[+] TrojanDownloader/Agent.blx!submit
[+] TrojanDownloader/W64.Agent.cr!submit
[+] TrojanDropper/Agent.alb!submit
[+] TrojanDropper/Agent.alc!submit
[+] TrojanDropper/Agent.ald!submit
[+] TrojanDropper/PS.Agent.z!submit
[-] HEUR:TrojanDropper/Agent.ar!submit
[-] HVM:Backdoor/Lotok.cl!submit
[-] Trojan/BAT.Runner.bs!submit
[-] Trojan/BAT.Runner.bt!submit
[-] Trojan/FakeApp.aae!submit
[-] Trojan/FakeApp.abo!submit
[-] Trojan/FakeApp.abp!submit
[-] Trojan/FakeApp.abq!submit
[-] Trojan/FakeApp.zd!submit
[-] Trojan/Loader.mw!submit
[-] Trojan/MSIL.Disabler.e!submit
[-] Trojan/MSIL.Obfuscated.ka!submit
[-] Trojan/MSIL.Obfuscated.kb!submit
[-] Trojan/PS.Loader.q!submit
[-] Trojan/PS.Loader.r!submit
[-] Trojan/Python.DDos.i!submit
[-] Trojan/Rozena.bf!submit
[-] Trojan/Runner.fn!submit
[-] Trojan/ShellLoader.ahv!submit
[-] Trojan/ShellLoader.ahw!submit
[-] Trojan/ShellLoader.ahx!submit
[-] Trojan/W64.Agent.gm!submit
[-] Trojan/W64.Injector.cb!submit
[-] Trojan/W64.ShellLoader.aj!submit
[-] TrojanDownloader/JS.Agent.ii!submit
[-] TrojanDownloader/PS.Agent.fe!submit
[-] TrojanDownloader/VBS.Agent.kf!submit
[-] TrojanDropper/Agent.akz!submit
[-] TrojanDropper/Agent.ala!submit
[-] TrojanDropper/Android.Agent.ci!submit
[-] TrojanDropper/Android.Agent.cj!submit
[-] TrojanDropper/Android.Agent.ck!submit
[-] TrojanDropper/Android.Agent.cl!submit
[-] TrojanDropper/Android.Agent.cm!submit
[-] TrojanDropper/JS.Agent.cd!submit
[-] TrojanDropper/Python.Loader.a!submit
[-] TrojanSpy/Android.SMSSpy.aq!submit
[-] TrojanSpy/Android.SMSSpy.ar!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1768821989.crithash.txt))

<details>
<summary>
新增正式定义: 18 | 移除正式定义: 1
</summary>

```
[+] Adware/W32.Xra.a!crit
[+] Backdoor/Linux.Mirai.d!crit
[+] Exploit/JS.Brash.a!crit
[+] Exploit/W32.CVE-2025-53136.a!crit
[+] Trojan/HTML.Phishing.os!crit
[+] Trojan/MSIL.Obfuscated.ap!crit
[+] Trojan/PS.Agent.a!crit
[+] Trojan/SCR.ShellCode.j!crit
[+] Trojan/SCR.ShellCode.k!crit
[+] Trojan/SCR.ShellCode.l!crit
[+] Trojan/SCR.ShellLoader.b
[+] Trojan/W32.ShellLoader.v!crit
[+] TrojanDownloader/Linux.Agent.h!crit
[+] TrojanDownloader/OSX.Agent.b!crit
[+] TrojanDownloader/PS.Agent.bp!crit
[+] TrojanDownloader/VBS.Agent.b!crit
[+] TrojanDownloader/W32.Rugmi.ac!crit
[+] TrojanSpy/PS.Stealer.j!crit
[-] Trojan/W32.FakeApp.h!crit
```

</details>

<details>
<summary>
新增遥测定义: 25 | 移除遥测定义: 20
</summary>

```
[+] Backdoor/Linux.Gafgyt.b!crit!submit
[+] Backdoor/PHP.WebShell.u!crit!submit
[+] Backdoor/PHP.WebShell.v!crit!submit
[+] Backdoor/PHP.WebShell.w!crit!submit
[+] Backdoor/PHP.WebShell.x!crit!submit
[+] Backdoor/W32.Lotok.z!crit!submit
[+] HackTool/PS.BruteForce.c!crit!submit
[+] HackTool/W64.Fscan.a!crit!submit
[+] Joke/BAT.Shutdown.b!crit!submit
[+] Trojan/Linux.Mirai.c!crit!submit
[+] Trojan/MSIL.Injector.k!crit!submit
[+] Trojan/MSIL.Obfuscated.aq!crit!submit
[+] Trojan/W32.Agent.aa!crit!submit
[+] Trojan/W32.Agent.y!crit!submit
[+] Trojan/W32.Agent.z!crit!submit
[+] Trojan/W32.ShellLoader.w!crit!submit
[+] Trojan/W64.Injector.f!crit!submit
[+] Trojan/W64.Injector.g!crit!submit
[+] Trojan/W64.Runner.b!crit!submit
[+] Trojan/W64.ShellLoader.d!crit!submit
[+] TrojanDownloader/HTML.Agent.e!crit!submit
[+] TrojanDownloader/W32.Agent.blx!crit!submit
[+] TrojanSpy/MSIL.Stealer.cde!crit!submit
[+] TrojanSpy/PS.Stealer.m!crit!submit
[+] TrojanSpy/W64.Stealer.d!crit!submit
[-] Backdoor/Linux.Mirai.d!crit!submit
[-] Exploit/JS.Brash.a!crit!submit
[-] Exploit/W32.CVE-2025-53136.a!crit!submit
[-] Trojan/HTML.Phishing.os!crit!submit
[-] Trojan/MSIL.Obfuscated.ap!crit!submit
[-] Trojan/PS.Agent.a!crit!submit
[-] Trojan/SCR.ShellCode.j!crit!submit
[-] Trojan/SCR.ShellCode.k!crit!submit
[-] Trojan/SCR.ShellCode.l!crit!submit
[-] Trojan/SCR.ShellLoader.b!submit
[-] Trojan/W32.FakeApp.g!crit!submit
[-] Trojan/W32.HiJack.k!crit!submit
[-] Trojan/W32.ShellLoader.v!crit!submit
[-] TrojanDownloader/Linux.Agent.h!crit!submit
[-] TrojanDownloader/OSX.Agent.b!crit!submit
[-] TrojanDownloader/PS.Agent.bp!crit!submit
[-] TrojanDownloader/VBS.Agent.b!crit!submit
[-] TrojanDownloader/W32.Rugmi.ac!crit!submit
[-] TrojanDropper/W32.Agent.c!crit!submit
[-] TrojanDropper/W32.Agent.d!crit!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1768821989.troj.txt))

新增: 63

</details>
<details>
<summary><b>1768733570</b> - 2026-01-18 10:52:50 UTC</summary>

#### 黑名单哈希变更 ([troj.txt](data/1768733570.troj.txt))

新增: 22

#### 白名单哈希变更 ([hwl.txt](data/1768733570.hwl.txt))

新增: 7

</details>
<details>
<summary><b>1768651961</b> - 2026-01-17 12:12:41 UTC</summary>

#### 黑名单哈希变更 ([troj.txt](data/1768651961.troj.txt))

新增: 21

#### 白名单哈希变更 ([hwl.txt](data/1768651961.hwl.txt))

新增: 4

</details>
<details>
<summary><b>1768562210</b> - 2026-01-16 11:16:50 UTC</summary>

#### 特征项变更 ([pset.txt](data/1768562210.pset.txt))

<details>
<summary>
新增正式定义: 35 | 移除正式定义: 3
</summary>

```
[+] HEUR:Trojan/Injector.clm
[+] HVM:Backdoor/Lotok.ci
[+] HVM:Backdoor/Lotok.cj
[+] HVM:Backdoor/Lotok.ck
[+] HVM:Trojan/Injector.dt
[+] Trojan/BAT.Runner.br
[+] Trojan/FakeApp.aay
[+] Trojan/HiJack.yl
[+] Trojan/Injector.clj
[+] Trojan/Injector.clk
[+] Trojan/Injector.cll
[+] Trojan/JS.Obfuscated.dh
[+] Trojan/LNK.Runner.bq
[+] Trojan/Linux.DDos.bf
[+] Trojan/Linux.DDos.bg
[+] Trojan/Linux.Mirai.gn
[+] Trojan/Loader.mv
[+] Trojan/MSIL.Obfuscated.ka
[+] Trojan/PS.Injector.c
[+] Trojan/Runner.fm
[+] Trojan/ShellLoader.ahs
[+] Trojan/ShellLoader.aht
[+] Trojan/ShellLoader.ahu
[+] Trojan/W64.ShellLoader.n
[+] TrojanDownloader/Agent.blv
[+] TrojanDownloader/Agent.blw
[+] TrojanDownloader/JS.Agent.ih
[+] TrojanDownloader/Linux.Agent.dz
[+] TrojanDownloader/PS.Agent.fc
[+] TrojanDownloader/PS.Agent.fd
[+] TrojanDropper/BAT.Agent.bp
[+] TrojanSpy/MSIL.Formbook.bh
[+] TrojanSpy/MSIL.Formbook.bi
[+] TrojanSpy/Stealer.tj
[+] TrojanSpy/W64.LummaStealer.a
[-] HVM:Trojan/Hook.a
[-] Trojan/FakeApp.aae
[-] Trojan/FakeApp.zd
```

</details>

<details>
<summary>
新增遥测定义: 40 | 移除遥测定义: 36
</summary>

```
[+] HVM:Backdoor/Lotok.cl!submit
[+] HVM:VirTool/Obfuscator.be!submit
[+] OMacro/Thus.n!submit
[+] Trojan/BAT.Runner.bs!submit
[+] Trojan/BAT.Runner.bt!submit
[+] Trojan/FakeApp.aae!submit
[+] Trojan/FakeApp.abo!submit
[+] Trojan/FakeApp.abp!submit
[+] Trojan/FakeApp.abq!submit
[+] Trojan/FakeApp.zd!submit
[+] Trojan/Loader.mw!submit
[+] Trojan/MSIL.Disabler.e!submit
[+] Trojan/MSIL.Obfuscated.kb!submit
[+] Trojan/PS.Loader.q!submit
[+] Trojan/PS.Loader.r!submit
[+] Trojan/Python.DDos.i!submit
[+] Trojan/Rozena.bf!submit
[+] Trojan/Runner.fn!submit
[+] Trojan/ShellLoader.ahv!submit
[+] Trojan/ShellLoader.ahw!submit
[+] Trojan/ShellLoader.ahx!submit
[+] Trojan/W64.Agent.gm!submit
[+] Trojan/W64.Injector.cb!submit
[+] Trojan/W64.Loader.ak!submit
[+] Trojan/W64.ShellLoader.aj!submit
[+] TrojanDownloader/JS.Agent.ii!submit
[+] TrojanDownloader/PS.Agent.fe!submit
[+] TrojanDownloader/VBS.Agent.kf!submit
[+] TrojanDownloader/W64.Agent.cq!submit
[+] TrojanDropper/Agent.akz!submit
[+] TrojanDropper/Agent.ala!submit
[+] TrojanDropper/Android.Agent.ci!submit
[+] TrojanDropper/Android.Agent.cj!submit
[+] TrojanDropper/Android.Agent.ck!submit
[+] TrojanDropper/Android.Agent.cl!submit
[+] TrojanDropper/Android.Agent.cm!submit
[+] TrojanDropper/JS.Agent.cd!submit
[+] TrojanDropper/Python.Loader.a!submit
[+] TrojanSpy/Android.SMSSpy.aq!submit
[+] TrojanSpy/Android.SMSSpy.ar!submit
[-] Backdoor/Lotok.oc!submit
[-] HEUR:Trojan/Injector.clm!submit
[-] HVM:Backdoor/Lotok.ci!submit
[-] HVM:Backdoor/Lotok.cj!submit
[-] HVM:Backdoor/Lotok.ck!submit
[-] HVM:Trojan/Injector.dt!submit
[-] HVM:TrojanDownloader/Small.dq!submit
[-] Trojan/BAT.Runner.br!submit
[-] Trojan/FakeApp.aay!submit
[-] Trojan/HiJack.yl!submit
[-] Trojan/Injector.clj!submit
[-] Trojan/Injector.clk!submit
[-] Trojan/Injector.cll!submit
[-] Trojan/JS.Obfuscated.dh!submit
[-] Trojan/LNK.Runner.bq!submit
[-] Trojan/Linux.DDos.bf!submit
[-] Trojan/Linux.DDos.bg!submit
[-] Trojan/Linux.Mirai.gn!submit
[-] Trojan/Loader.mv!submit
[-] Trojan/PS.Injector.c!submit
[-] Trojan/Runner.fm!submit
[-] Trojan/ShellLoader.ahs!submit
[-] Trojan/ShellLoader.aht!submit
[-] Trojan/ShellLoader.ahu!submit
[-] Trojan/W64.ShellLoader.n!submit
[-] TrojanDownloader/Agent.blv!submit
[-] TrojanDownloader/Agent.blw!submit
[-] TrojanDownloader/JS.Agent.ih!submit
[-] TrojanDownloader/Linux.Agent.dz!submit
[-] TrojanDownloader/PS.Agent.fc!submit
[-] TrojanDownloader/PS.Agent.fd!submit
[-] TrojanDropper/BAT.Agent.bp!submit
[-] TrojanSpy/MSIL.Formbook.bh!submit
[-] TrojanSpy/MSIL.Formbook.bi!submit
[-] TrojanSpy/Stealer.tj!submit
[-] TrojanSpy/W64.LummaStealer.a!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1768562210.crithash.txt))

<details>
<summary>
新增正式定义: 17 | 移除正式定义: 2
</summary>

```
[+] HackTool/Linux.CoinMiner.b!crit
[+] Trojan/HTML.Phishing.or!crit
[+] Trojan/Linux.Mirai.b!crit
[+] Trojan/SCR.Agent.e!crit
[+] Trojan/W32.CrazyScreen.e!crit
[+] Trojan/W32.CrazyScreen.f!crit
[+] Trojan/W32.FakeApp.f!crit
[+] Trojan/W32.FakeApp.h!crit
[+] Trojan/W64.Agent.j!crit
[+] TrojanDownloader/LNK.Agent.d!crit
[+] TrojanDownloader/LNK.Agent.e!crit
[+] TrojanDownloader/Linux.Agent.f!crit
[+] TrojanDownloader/Linux.Agent.g!crit
[+] TrojanDownloader/PS.Agent.bo!crit
[+] TrojanDropper/W32.Agent.o!crit
[+] TrojanSpy/OSX.Stealer.b!crit
[+] TrojanSpy/W64.Noon.s!crit
[-] Backdoor/W32.Lotok.ad!crit
[-] Backdoor/W32.Lotok.ae!crit
```

</details>

<details>
<summary>
新增遥测定义: 35 | 移除遥测定义: 21
</summary>

```
[+] Backdoor/Linux.Mirai.d!crit!submit
[+] Backdoor/MSIL.ReverseShell.d!crit!submit
[+] Backdoor/PS.ReverseShell.i!crit!submit
[+] Exploit/JS.Brash.a!crit!submit
[+] Exploit/W32.CVE-2025-53136.a!crit!submit
[+] Joke/VBS.CrazyWindow.a!crit!submit
[+] Ransom/MSIL.LockFile.g!crit!submit
[+] Ransom/PS.LockFile.b!crit!submit
[+] Ransom/PS.LockFile.c!crit!submit
[+] Ransom/W64.LockFile.d!crit!submit
[+] Trojan/BAT.KillFile.a!crit!submit
[+] Trojan/HTML.Phishing.os!crit!submit
[+] Trojan/MSIL.Obfuscated.ap!crit!submit
[+] Trojan/PS.Agent.a!crit!submit
[+] Trojan/SCR.ShellCode.k!crit!submit
[+] Trojan/SCR.ShellCode.l!crit!submit
[+] Trojan/VBS.KillAV.d!crit!submit
[+] Trojan/W32.HiJack.k!crit!submit
[+] Trojan/W32.Loader.j!crit!submit
[+] Trojan/W32.ShellLoader.v!crit!submit
[+] TrojanDownloader/Linux.Agent.h!crit!submit
[+] TrojanDownloader/MSIL.Runner.f!crit!submit
[+] TrojanDownloader/OSX.Agent.b!crit!submit
[+] TrojanDownloader/PS.Agent.bp!crit!submit
[+] TrojanDownloader/PS.Runner.r!crit!submit
[+] TrojanDownloader/VBS.Agent.b!crit!submit
[+] TrojanDropper/VBS.Runner.d!crit!submit
[+] TrojanDropper/VBS.Starter.b!crit!submit
[+] TrojanDropper/W32.Agent.c!crit!submit
[+] TrojanDropper/W32.Agent.d!crit!submit
[+] TrojanSpy/MSIL.Keylogger.d!crit!submit
[+] TrojanSpy/MSIL.Stealer.cdd!crit!submit
[+] TrojanSpy/PS.Stealer.k!crit!submit
[+] TrojanSpy/W32.Keylogger.d!crit!submit
[+] TrojanSpy/W64.Keylogger.a!crit!submit
[-] Adware/W32.Xra.a!crit!submit
[-] Backdoor/W32.Lotok.ab!crit!submit
[-] HackTool/Linux.CoinMiner.b!crit!submit
[-] Trojan/HTML.Phishing.or!crit!submit
[-] Trojan/Linux.Mirai.b!crit!submit
[-] Trojan/SCR.Agent.e!crit!submit
[-] Trojan/W32.CrazyScreen.e!crit!submit
[-] Trojan/W32.CrazyScreen.f!crit!submit
[-] Trojan/W32.FakeApp.f!crit!submit
[-] Trojan/W32.FakeApp.h!crit!submit
[-] Trojan/W32.HiJack.j!crit!submit
[-] Trojan/W64.Agent.j!crit!submit
[-] TrojanDownloader/LNK.Agent.d!crit!submit
[-] TrojanDownloader/LNK.Agent.e!crit!submit
[-] TrojanDownloader/Linux.Agent.f!crit!submit
[-] TrojanDownloader/Linux.Agent.g!crit!submit
[-] TrojanDownloader/PS.Agent.bo!crit!submit
[-] TrojanDropper/W32.Agent.b!submit
[-] TrojanSpy/MSIL.Keylogger.c!crit!submit
[-] TrojanSpy/OSX.Stealer.b!crit!submit
[-] TrojanSpy/W64.Noon.s!crit!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1768562210.troj.txt))

新增: 70

</details>
<details>
<summary><b>1768481840</b> - 2026-01-15 12:57:20 UTC</summary>

#### 特征项变更 ([pset.txt](data/1768481840.pset.txt))

<details>
<summary>
新增正式定义: 32
</summary>

```
[+] Backdoor/Agent.re
[+] HEUR:Backdoor/JSP.WebShell.q
[+] HEUR:TrojanDownloader/Maloader.d
[+] OMacro/Dropper.gu
[+] Trojan/AutoIT.Injector.fd
[+] Trojan/BAT.Injector.f
[+] Trojan/BAT.Runner.bp
[+] Trojan/BAT.Runner.bq
[+] Trojan/JS.Obfuscated.de
[+] Trojan/JS.Obfuscated.df
[+] Trojan/JS.Obfuscated.dg
[+] Trojan/Linux.CoinMiner.dw
[+] Trojan/Linux.Mirai.gm
[+] Trojan/MSIL.Obfuscated.jz
[+] Trojan/PS.Loader.p
[+] Trojan/ShellLoader.ahm
[+] Trojan/ShellLoader.ahn
[+] Trojan/ShellLoader.aho
[+] Trojan/ShellLoader.ahp
[+] Trojan/ShellLoader.ahq
[+] Trojan/ShellLoader.ahr
[+] TrojanDownloader/Agent.blu
[+] TrojanDownloader/BAT.Agent.gd
[+] TrojanDownloader/JS.Agent.ig
[+] TrojanDownloader/Linux.Agent.dx
[+] TrojanDownloader/Linux.Agent.dy
[+] TrojanDownloader/Maloader.bq
[+] TrojanDownloader/VBS.Agent.ke
[+] TrojanDropper/Agent.akx
[+] TrojanDropper/Agent.aky
[+] TrojanDropper/BAT.Agent.bo
[+] TrojanSpy/ClipBanker.aq
```

</details>

<details>
<summary>
新增遥测定义: 35 | 移除遥测定义: 35
</summary>

```
[+] HEUR:Trojan/Injector.clm!submit
[+] HVM:Backdoor/Lotok.ci!submit
[+] HVM:Backdoor/Lotok.cj!submit
[+] HVM:Backdoor/Lotok.ck!submit
[+] Trojan/BAT.Runner.br!submit
[+] Trojan/FakeApp.aay!submit
[+] Trojan/HiJack.yl!submit
[+] Trojan/Injector.clj!submit
[+] Trojan/Injector.clk!submit
[+] Trojan/Injector.cll!submit
[+] Trojan/JS.Obfuscated.dh!submit
[+] Trojan/LNK.Runner.bq!submit
[+] Trojan/Linux.DDos.bf!submit
[+] Trojan/Linux.DDos.bg!submit
[+] Trojan/Linux.Mirai.gn!submit
[+] Trojan/Loader.mv!submit
[+] Trojan/MSIL.Obfuscated.ka!submit
[+] Trojan/PS.Injector.c!submit
[+] Trojan/Runner.fm!submit
[+] Trojan/ShellLoader.ahs!submit
[+] Trojan/ShellLoader.aht!submit
[+] Trojan/ShellLoader.ahu!submit
[+] Trojan/W64.Agent.gl!submit
[+] Trojan/W64.ShellLoader.n!submit
[+] TrojanDownloader/Agent.blv!submit
[+] TrojanDownloader/Agent.blw!submit
[+] TrojanDownloader/JS.Agent.ih!submit
[+] TrojanDownloader/Linux.Agent.dz!submit
[+] TrojanDownloader/PS.Agent.fc!submit
[+] TrojanDownloader/PS.Agent.fd!submit
[+] TrojanDropper/BAT.Agent.bp!submit
[+] TrojanSpy/MSIL.Formbook.bh!submit
[+] TrojanSpy/MSIL.Formbook.bi!submit
[+] TrojanSpy/Stealer.tj!submit
[+] TrojanSpy/W64.LummaStealer.a!submit
[-] Backdoor/Agent.re!submit
[-] HEUR:Backdoor/JSP.WebShell.q!submit
[-] HEUR:TrojanDownloader/Maloader.d!submit
[-] OMacro/Dropper.gu!submit
[-] Trojan/AutoIT.Injector.fd!submit
[-] Trojan/BAT.Injector.f!submit
[-] Trojan/BAT.Runner.bp!submit
[-] Trojan/BAT.Runner.bq!submit
[-] Trojan/FakeApp.aaj!submit
[-] Trojan/JS.Obfuscated.dd!submit
[-] Trojan/JS.Obfuscated.de!submit
[-] Trojan/JS.Obfuscated.df!submit
[-] Trojan/JS.Obfuscated.dg!submit
[-] Trojan/Linux.CoinMiner.dw!submit
[-] Trojan/Linux.Mirai.gm!submit
[-] Trojan/Loader.mu!submit
[-] Trojan/MSIL.Obfuscated.jz!submit
[-] Trojan/PS.Loader.p!submit
[-] Trojan/ShellLoader.ahm!submit
[-] Trojan/ShellLoader.ahn!submit
[-] Trojan/ShellLoader.aho!submit
[-] Trojan/ShellLoader.ahp!submit
[-] Trojan/ShellLoader.ahq!submit
[-] Trojan/ShellLoader.ahr!submit
[-] TrojanDownloader/Agent.blu!submit
[-] TrojanDownloader/BAT.Agent.gd!submit
[-] TrojanDownloader/JS.Agent.ig!submit
[-] TrojanDownloader/Linux.Agent.dx!submit
[-] TrojanDownloader/Linux.Agent.dy!submit
[-] TrojanDownloader/Maloader.bq!submit
[-] TrojanDownloader/VBS.Agent.ke!submit
[-] TrojanDropper/Agent.akx!submit
[-] TrojanDropper/Agent.aky!submit
[-] TrojanDropper/BAT.Agent.bo!submit
[-] TrojanSpy/ClipBanker.aq!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1768481840.crithash.txt))

<details>
<summary>
新增正式定义: 16
</summary>

```
[+] Backdoor/JSP.WebShell.r
[+] Trojan/HTML.Phishing.op!crit
[+] Trojan/Linux.DDos.a!crit
[+] Trojan/MSIL.Inoci.c!crit
[+] Trojan/MSIL.Loader.at!crit
[+] Trojan/SCR.Runner.fm!crit
[+] Trojan/SCR.Runner.fn!crit
[+] Trojan/SCR.Runner.fo!crit
[+] Trojan/W32.HiJack.y!crit
[+] Trojan/W32.Loader.i!crit
[+] TrojanDownloader/HTML.Agent.c!crit
[+] TrojanDownloader/HTML.Agent.d!crit
[+] TrojanDownloader/PS.Agent.bm!crit
[+] TrojanDropper/JAVA.Agent.a!crit
[+] TrojanDropper/W32.Agent.n!crit
[+] TrojanSpy/W32.Tepfer.f!crit
```

</details>

<details>
<summary>
新增遥测定义: 42 | 移除遥测定义: 19
</summary>

```
[+] Backdoor/PHP.Injector.a!crit!submit
[+] Backdoor/PS.ReverseShell.g!crit!submit
[+] Backdoor/W32.Lotok.ab!crit!submit
[+] HackTool/Linux.CoinMiner.b!crit!submit
[+] HackTool/PHP.Botsant.a!crit!submit
[+] Joke/MSIL.CrazyScreen.a!crit!submit
[+] Joke/VBS.Shutdown.b!crit!submit
[+] Ransom/MSIL.LockFile.e!crit!submit
[+] Ransom/MSIL.LockFile.f!crit!submit
[+] Ransom/VBS.LockFile.a!crit!submit
[+] Ransom/VBS.LockFile.c!crit!submit
[+] Trojan/BAT.KillAV.e!crit!submit
[+] Trojan/HTML.Phishing.or!crit!submit
[+] Trojan/Linux.Mirai.b!crit!submit
[+] Trojan/MSIL.Injector.h!crit!submit
[+] Trojan/MSIL.Injector.i!crit!submit
[+] Trojan/MSIL.Injector.j!crit!submit
[+] Trojan/SCR.Agent.e!crit!submit
[+] Trojan/SCR.ShellLoader.b!submit
[+] Trojan/W32.CrazyScreen.e!crit!submit
[+] Trojan/W32.CrazyScreen.f!crit!submit
[+] Trojan/W32.FakeApp.f!crit!submit
[+] Trojan/W32.FakeApp.g!crit!submit
[+] Trojan/W32.FakeApp.h!crit!submit
[+] Trojan/W32.HiJack.j!crit!submit
[+] Trojan/W64.Agent.j!crit!submit
[+] TrojanDownloader/LNK.Agent.d!crit!submit
[+] TrojanDownloader/LNK.Agent.e!crit!submit
[+] TrojanDownloader/Linux.Agent.f!crit!submit
[+] TrojanDownloader/Linux.Agent.g!crit!submit
[+] TrojanDownloader/MSIL.Starter.a!crit!submit
[+] TrojanDownloader/PS.Agent.bo!crit!submit
[+] TrojanDownloader/PS.Runner.q!crit!submit
[+] TrojanDownloader/PS.Starter.a!crit!submit
[+] TrojanDownloader/PS.Starter.c!crit!submit
[+] TrojanDownloader/PS.Starter.d!crit!submit
[+] TrojanDownloader/W32.Rugmi.ac!crit!submit
[+] TrojanDropper/W32.Agent.b!submit
[+] TrojanSpy/MSIL.Stealer.cdc!crit!submit
[+] TrojanSpy/OSX.Stealer.b!crit!submit
[+] TrojanSpy/PS.Stealer.j!crit!submit
[+] TrojanSpy/W64.Noon.s!crit!submit
[-] Backdoor/JSP.WebShell.r!submit
[-] Backerdoor/PHP.Injector.a!crit!submit
[-] Trojan/HTML.Phishing.op!crit!submit
[-] Trojan/Linux.DDos.a!crit!submit
[-] Trojan/MSIL.Inoci.c!crit!submit
[-] Trojan/MSIL.Loader.at!crit!submit
[-] Trojan/SCR.Runner.fm!crit!submit
[-] Trojan/SCR.Runner.fn!crit!submit
[-] Trojan/SCR.Runner.fo!crit!submit
[-] Trojan/W32.HiJack.y!crit!submit
[-] Trojan/W32.Loader.i!crit!submit
[-] Trojan/W32.ShellLoader.o!crit!submit
[-] Trojan/W32.ShellLoader.p!crit!submit
[-] TrojanDownloader/HTML.Agent.c!crit!submit
[-] TrojanDownloader/HTML.Agent.d!crit!submit
[-] TrojanDownloader/PS.Agent.bm!crit!submit
[-] TrojanDownloader/VBS.Obfuscated.c!crit!submit
[-] TrojanDropper/JAVA.Agent.a!crit!submit
[-] TrojanSpy/W32.Tepfer.f!crit!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1768481840.troj.txt))

新增: 49

</details>
<details>
<summary><b>1768390311</b> - 2026-01-14 11:31:51 UTC</summary>

#### 特征项变更 ([pset.txt](data/1768390311.pset.txt))

<details>
<summary>
新增正式定义: 42 | 移除正式定义: 2
</summary>

```
[+] Backdoor/Agent.rd
[+] Backdoor/Linux.Sliver.c
[+] Backdoor/Lotok.oe
[+] Backdoor/Lotok.ok
[+] Exploit/Vulndriver.t
[+] HEUR:Trojan/HTML.FakeCaptcha.b
[+] HEUR:Trojan/JS.Agent.gr
[+] HVM:Backdoor/Lotok.cf
[+] HVM:TrojanDropper/W64.Agent.cb
[+] Trojan/BAT.Loader.k
[+] Trojan/FakeApp.aaj
[+] Trojan/FakeApp.xp
[+] Trojan/FakeApp.yl
[+] Trojan/JS.Agent.gr
[+] Trojan/JS.Agent.gs
[+] Trojan/JS.Injector.s
[+] Trojan/JS.Runner.s
[+] Trojan/LUA.Agent.g
[+] Trojan/Linux.Mirai.fn
[+] Trojan/Linux.Mirai.gk
[+] Trojan/Loader.mu
[+] Trojan/PS.Loader.o
[+] Trojan/Python.CoinMiner.k
[+] Trojan/ShellLoader.ahk
[+] Trojan/ShellLoader.ahl
[+] Trojan/W64.Loader.aj
[+] Trojan/W64.ShellLoader.j
[+] TrojanDownloader/Agent.blt
[+] TrojanDownloader/BAT.Agent.gc
[+] TrojanDownloader/MSIL.Agent.ajk
[+] TrojanDownloader/Maloader.bo
[+] TrojanDownloader/Maloader.bp
[+] TrojanDownloader/OSX.Agent.h
[+] TrojanDownloader/W64.Agent.cp
[+] TrojanDropper/Agent.aku
[+] TrojanDropper/Agent.akv
[+] TrojanDropper/Agent.akw
[+] TrojanDropper/BAT.Agent.bn
[+] TrojanSpy/MSIL.Formbook.bg
[+] TrojanSpy/Python.Stealer.cp
[+] TrojanSpy/Python.Stealer.cq
[+] TrojanSpy/W64.Stealer.z
[-] Trojan/GenCBL.a
[-] Trojan/GenCBL.b
```

</details>

<details>
<summary>
新增遥测定义: 33 | 移除遥测定义: 41
</summary>

```
[+] Backdoor/Agent.re!submit
[+] HEUR:Backdoor/JSP.WebShell.q!submit
[+] HEUR:TrojanDownloader/Maloader.d!submit
[+] OMacro/Dropper.gu!submit
[+] Trojan/AutoIT.Injector.fd!submit
[+] Trojan/BAT.Injector.f!submit
[+] Trojan/BAT.Runner.bp!submit
[+] Trojan/BAT.Runner.bq!submit
[+] Trojan/JS.Obfuscated.de!submit
[+] Trojan/JS.Obfuscated.df!submit
[+] Trojan/JS.Obfuscated.dg!submit
[+] Trojan/Linux.CoinMiner.dw!submit
[+] Trojan/Linux.Mirai.gm!submit
[+] Trojan/Loader.mu!submit
[+] Trojan/MSIL.Obfuscated.jz!submit
[+] Trojan/PS.Loader.p!submit
[+] Trojan/ShellLoader.ahm!submit
[+] Trojan/ShellLoader.ahn!submit
[+] Trojan/ShellLoader.aho!submit
[+] Trojan/ShellLoader.ahp!submit
[+] Trojan/ShellLoader.ahq!submit
[+] Trojan/ShellLoader.ahr!submit
[+] TrojanDownloader/Agent.blu!submit
[+] TrojanDownloader/BAT.Agent.gd!submit
[+] TrojanDownloader/JS.Agent.ig!submit
[+] TrojanDownloader/Linux.Agent.dx!submit
[+] TrojanDownloader/Linux.Agent.dy!submit
[+] TrojanDownloader/Maloader.bq!submit
[+] TrojanDownloader/VBS.Agent.ke!submit
[+] TrojanDropper/Agent.akx!submit
[+] TrojanDropper/Agent.aky!submit
[+] TrojanDropper/BAT.Agent.bo!submit
[+] TrojanSpy/ClipBanker.aq!submit
[-] Backdoor/Agent.rd!submit
[-] Backdoor/Linux.Sliver.c!submit
[-] Backdoor/Lotok.oe!submit
[-] Backdoor/Lotok.ok!submit
[-] Exploit/Vulndriver.t!submit
[-] HEUR:Trojan/HTML.FakeCaptcha.b!submit
[-] HEUR:Trojan/JS.Agent.gr!submit
[-] HVM:Backdoor/Lotok.cf!submit
[-] HVM:TrojanDropper/W64.Agent.cb!submit
[-] Trojan/Autoit.Injector.ds!submit
[-] Trojan/BAT.Loader.k!submit
[-] Trojan/FakeApp.abb!submit
[-] Trojan/FakeApp.xp!submit
[-] Trojan/FakeApp.yl!submit
[-] Trojan/JS.GenCBL.a!submit
[-] Trojan/JS.GenCBL.b!submit
[-] Trojan/JS.Injector.s!submit
[-] Trojan/JS.Runner.s!submit
[-] Trojan/LUA.Agent.g!submit
[-] Trojan/Linux.Mirai.fn!submit
[-] Trojan/Linux.Mirai.gk!submit
[-] Trojan/PS.Loader.o!submit
[-] Trojan/Python.CoinMiner.k!submit
[-] Trojan/ShellLoader.ahk!submit
[-] Trojan/ShellLoader.ahl!submit
[-] Trojan/W64.Loader.aj!submit
[-] Trojan/W64.ShellLoader.j!submit
[-] TrojanDownloader/Agent.blt!submit
[-] TrojanDownloader/BAT.Agent.gc!submit
[-] TrojanDownloader/MSIL.Agent.ajk!submit
[-] TrojanDownloader/Maloader.bo!submit
[-] TrojanDownloader/OSX.Agent.h!submit
[-] TrojanDownloader/W64.Agent.cp!submit
[-] TrojanDropper/Agent.aku!submit
[-] TrojanDropper/Agent.akv!submit
[-] TrojanDropper/Agent.akw!submit
[-] TrojanDropper/BAT.Agent.bn!submit
[-] TrojanSpy/MSIL.Formbook.bg!submit
[-] TrojanSpy/Python.Stealer.cp!submit
[-] TrojanSpy/Python.Stealer.cq!submit
[-] TrojanSpy/W64.Stealer.z!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1768390311.crithash.txt))

<details>
<summary>
新增正式定义: 11
</summary>

```
[+] Backdoor/Linux.Mirai.c!crit
[+] Backdoor/W32.Lotok.xx!crit
[+] Trojan/JS.ChatgptStealer.a!crit
[+] Trojan/JS.ChatgptStealer.b!crit
[+] Trojan/SCR.Agent.clr!crit
[+] Trojan/W32.HiJack.x!crit
[+] Trojan/W32.Injector.clj!crit
[+] Trojan/W32.ProxyChanger.a!crit
[+] TrojanDownloader/Linux.Agent.e!crit
[+] TrojanSpy/Linux.Agent.a!crit
[+] TrojanSpy/W64.Stealer.tj!crit
```

</details>

<details>
<summary>
新增遥测定义: 30 | 移除遥测定义: 13
</summary>

```
[+] Adware/W32.Xra.a!crit!submit
[+] Backdoor/JSP.WebShell.r!submit
[+] Backdoor/MSIL.ReverseShell.c!crit!submit
[+] Backdoor/PHP.WebShell.t!crit!submit
[+] Exploit/PS.CVE-2016-9192.b!crit!submit
[+] HackTool/PS.BypassUAC.b!crit!submit
[+] Trojan/Linux.DDos.a!crit!submit
[+] Trojan/MSIL.Inoci.c!crit!submit
[+] Trojan/MSIL.Loader.at!crit!submit
[+] Trojan/SCR.Runner.fm!crit!submit
[+] Trojan/SCR.Runner.fn!crit!submit
[+] Trojan/SCR.Runner.fo!crit!submit
[+] Trojan/SCR.ShellCode.j!crit!submit
[+] Trojan/W32.HiJack.y!crit!submit
[+] Trojan/W32.Loader.i!crit!submit
[+] Trojan/W32.ShellLoader.o!crit!submit
[+] Trojan/W32.ShellLoader.p!crit!submit
[+] Trojan/W64.KillWin.a!crit!submit
[+] Trojan/W64.KillWin.b!crit!submit
[+] Trojan/W64.KillWin.d!crit!submit
[+] TrojanDownloader/HTML.Agent.c!crit!submit
[+] TrojanDownloader/HTML.Agent.d!crit!submit
[+] TrojanDownloader/MSIL.Starter.b!crit!submit
[+] TrojanDownloader/PS.Agent.bm!crit!submit
[+] TrojanDropper/JAVA.Agent.a!crit!submit
[+] TrojanSpy/MSIL.Keylogger.c!crit!submit
[+] TrojanSpy/MSIL.Keylogger.e!crit!submit
[+] TrojanSpy/MSIL.Keylogger.f!crit!submit
[+] TrojanSpy/MSIL.Stealer.cdb!crit!submit
[+] TrojanSpy/W32.Tepfer.f!crit!submit
[-] Backdoor/Linux.Mirai.c!crit!submit
[-] Backdoor/W32.Lotok.x!crit!submit
[-] Backdoor/W32.Lotok.xx!crit!submit
[-] Backdoor/W32.Lotok.y!crit!submit
[-] Trojan/JS.ChatgptStealer.a!crit!submit
[-] Trojan/JS.ChatgptStealer.b!crit!submit
[-] Trojan/SCR.Agent.clr!crit!submit
[-] Trojan/W32.HiJack.x!crit!submit
[-] Trojan/W32.Injector.clj!crit!submit
[-] Trojan/W32.ProxyChanger.a!crit!submit
[-] TrojanDownloader/Linux.Agent.e!crit!submit
[-] TrojanSpy/Linux.Agent.a!crit!submit
[-] TrojanSpy/W64.Stealer.tj!crit!submit
```

</details>

#### 行为特征项变更 ([behav.txt](data/1768390311.behav.txt))

<details>
<summary>
新增: 1
</summary>

```
[+] Ransom/LockFile.SA!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1768390311.troj.txt))

新增: 69 | 移除: 1

</details>
<details>
<summary><b>1768303271</b> - 2026-01-13 11:21:11 UTC</summary>

#### 特征项变更 ([pset.txt](data/1768303271.pset.txt))

<details>
<summary>
新增正式定义: 51 | 移除正式定义: 10
</summary>

```
[+] Backdoor/Linux.Mirai.kx
[+] Backdoor/Lotok.od
[+] Backdoor/Lotok.oi
[+] Backdoor/Lotok.oj
[+] Backdoor/PHP.WebShell.cz
[+] Backdoor/PHP.WebShell.da
[+] Backdoor/PHP.WebShell.fk
[+] Backdoor/PHP.WebShell.fm
[+] HEUR:Backdoor/PHP.WebShell.ab
[+] HEUR:Backdoor/PHP.WebShell.ae
[+] HEUR:Trojan/FakeApp.au
[+] HEUR:Trojan/Injector.clj
[+] HEUR:Trojan/KillWin.g
[+] HEUR:TrojanDownloader/Linux.Mirai.bv
[+] HVM:Backdoor/Lotok.ce
[+] HVM:Trojan/ShellLoader.cj
[+] Hacktool/CookieKatz
[+] Trojan/BAT.Agent.gq
[+] Trojan/BAT.Runner.bn
[+] Trojan/BAT.Runner.bo
[+] Trojan/Clipboard.c
[+] Trojan/DLLHijack.z
[+] Trojan/DllHijack.aa
[+] Trojan/DllHijack.z
[+] Trojan/FakeApp.abm
[+] Trojan/FakeApp.abn
[+] Trojan/HiJack.yk
[+] Trojan/JS.Obfuscated.dc
[+] Trojan/KillMBR.cm
[+] Trojan/Linux.Mirai.fu
[+] Trojan/Linux.Mirai.fx
[+] Trojan/Linux.Mirai.gi
[+] Trojan/Linux.Mirai.gj
[+] Trojan/Loader.mt
[+] Trojan/MSIL.Obfuscated.jy
[+] Trojan/OSX.Agent.q
[+] Trojan/Obfuscated.nv
[+] Trojan/PS.Loader.n
[+] Trojan/ShellLoader.ahi
[+] Trojan/ShellLoader.ahj
[+] Trojan/W64.Agent.gk
[+] Trojan/W64.Rozena.p
[+] TrojanDownloader/HTML.Agent.bi
[+] TrojanDownloader/Linux.Agent.dv
[+] TrojanDropper/Maloader.n
[+] TrojanDropper/VBS.Agent.eg
[+] TrojanDropper/W64.Agent.ca
[+] TrojanSpy/OSX.Stealer.r
[+] TrojanSpy/Stealer.ti
[+] TrojanSpy/W64.PwStealer.e
[+] TrojanSpy/W64.Stealer.y
[-] Backdoor/PHP.Webshell.cz
[-] Backdoor/PHP.Webshell.da
[-] Backdoor/PHP.Webshell.fk
[-] Backdoor/PHP.Webshell.fm
[-] HEUR:Backdoor/PHP.Webshell.ab
[-] HEUR:Backdoor/PHP.Webshell.ae
[-] Trojan/FakeApp.aaj
[-] Trojan/FakeApp.aay
[-] Trojan/FakeApp.xp
[-] Trojan/FakeApp.yl
```

</details>

<details>
<summary>
新增遥测定义: 40 | 移除遥测定义: 45
</summary>

```
[+] Backdoor/Agent.rd!submit
[+] Backdoor/Linux.Sliver.c!submit
[+] Backdoor/Lotok.ok!submit
[+] Exploit/Vulndriver.t!submit
[+] HEUR:Trojan/HTML.FakeCaptcha.b!submit
[+] HVM:Backdoor/Lotok.cf!submit
[+] HVM:Trojan/Injector.dt!submit
[+] HVM:TrojanDropper/W64.Agent.cb!submit
[+] Trojan/BAT.Loader.k!submit
[+] Trojan/FakeApp.aaj!submit
[+] Trojan/FakeApp.xp!submit
[+] Trojan/FakeApp.yl!submit
[+] Trojan/JS.GenCBL.a!submit
[+] Trojan/JS.GenCBL.b!submit
[+] Trojan/JS.Injector.s!submit
[+] Trojan/JS.Obfuscated.dd!submit
[+] Trojan/JS.Runner.s!submit
[+] Trojan/LUA.Agent.g!submit
[+] Trojan/Linux.Mirai.gk!submit
[+] Trojan/Linux.Mirai.gl!submit
[+] Trojan/PS.Loader.o!submit
[+] Trojan/Python.CoinMiner.k!submit
[+] Trojan/ShellLoader.ahk!submit
[+] Trojan/ShellLoader.ahl!submit
[+] Trojan/W64.Loader.aj!submit
[+] Trojan/W64.ShellLoader.j!submit
[+] TrojanDownloader/BAT.Agent.gc!submit
[+] TrojanDownloader/LNK.Agent.hc!submit
[+] TrojanDownloader/Linux.Agent.dw!submit
[+] TrojanDownloader/MSIL.Agent.ajk!submit
[+] TrojanDownloader/Maloader.bo!submit
[+] TrojanDownloader/W64.Agent.cp!submit
[+] TrojanDropper/Agent.aku!submit
[+] TrojanDropper/Agent.akv!submit
[+] TrojanDropper/Agent.akw!submit
[+] TrojanDropper/BAT.Agent.bn!submit
[+] TrojanSpy/MSIL.Formbook.bg!submit
[+] TrojanSpy/Python.Stealer.cp!submit
[+] TrojanSpy/Python.Stealer.cq!submit
[+] TrojanSpy/W64.Stealer.z!submit
[-] Backdoor/Linux.Mirai.kx!submit
[-] Backdoor/Lotok.od!submit
[-] Backdoor/Lotok.oi!submit
[-] Backdoor/Lotok.oj!submit
[-] HEUR:Trojan/Injector.clj!submit
[-] HEUR:Trojan/KillWin.g!submit
[-] HEUR:TrojanDownloader/Linux.Mirai.bv!submit
[-] HVM:Backdoor/Lotok.ce!submit
[-] HVM:Trojan/ShellLoader.cj!submit
[-] Rootkit/Agent!submit
[-] Trojan/BAT.Agent.gq!submit
[-] Trojan/BAT.Runner.bn!submit
[-] Trojan/BAT.Runner.bo!submit
[-] Trojan/Clipboard.c!submit
[-] Trojan/DLLHijack.z!submit
[-] Trojan/DllHijack.aa!submit
[-] Trojan/DllHijack.z!submit
[-] Trojan/FakeApp.abm!submit
[-] Trojan/FakeApp.abn!submit
[-] Trojan/HiJack.yk!submit
[-] Trojan/JS.Obfuscated.dc!submit
[-] Trojan/KillMBR.cm!submit
[-] Trojan/Linux.Mirai.fu!submit
[-] Trojan/Linux.Mirai.fx!submit
[-] Trojan/Linux.Mirai.gi!submit
[-] Trojan/Linux.Mirai.gj!submit
[-] Trojan/Loader.mt!submit
[-] Trojan/MSIL.Obfuscated.jy!submit
[-] Trojan/OSX.Agent.q!submit
[-] Trojan/Obfuscated.nv!submit
[-] Trojan/PS.Loader.n!submit
[-] Trojan/ShellLoader.ahi!submit
[-] Trojan/ShellLoader.ahj!submit
[-] Trojan/W64.Agent.gk!submit
[-] Trojan/W64.Rozena.p!submit
[-] TrojanDownloader/HTML.Agent.bi!submit
[-] TrojanDownloader/JS.Agent.gc!submit
[-] TrojanDownloader/Linux.Agent.dv!submit
[-] TrojanDropper/Maloader.n!submit
[-] TrojanDropper/VBS.Agent.eg!submit
[-] TrojanDropper/W64.Agent.ca!submit
[-] TrojanSpy/OSX.Stealer.r!submit
[-] TrojanSpy/Stealer.ti!submit
[-] TrojanSpy/W64.PwStealer.e!submit
[-] TrojanSpy/W64.Stealer.y!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1768303271.crithash.txt))

<details>
<summary>
新增正式定义: 151 | 移除正式定义: 140
</summary>

```
[+] Adware/Android.PornTool.i!crit
[+] Backdoor/W32.Lotok.aa!crit
[+] Exploit/SCR.CVE-2017-0199.a!crit
[+] HackTool/W32.Scrambler.a!crit
[+] Trojan/MSIL.Obfuscated.ao!crit
[+] Trojan/PS.Loader.d!crit
[+] Trojan/SCR.Obfuscator.aa!crit
[+] Trojan/SCR.Obfuscator.ab!crit
[+] Trojan/SCR.Obfuscator.ac!crit
[+] Trojan/SCR.Obfuscator.ad!crit
[+] Trojan/SCR.Obfuscator.ae!crit
[+] Trojan/SCR.Obfuscator.af!crit
[+] Trojan/SCR.Obfuscator.ag!crit
[+] Trojan/SCR.Obfuscator.ah!crit
[+] Trojan/SCR.Obfuscator.ai!crit
[+] Trojan/SCR.Obfuscator.aj!crit
[+] Trojan/SCR.Obfuscator.ak!crit
[+] Trojan/SCR.Obfuscator.al!crit
[+] Trojan/SCR.Obfuscator.am!crit
[+] Trojan/SCR.Obfuscator.an!crit
[+] Trojan/SCR.Obfuscator.ao!crit
[+] Trojan/SCR.Obfuscator.ap!crit
[+] Trojan/SCR.Obfuscator.aq!crit
[+] Trojan/SCR.Obfuscator.ar!crit
[+] Trojan/SCR.Obfuscator.as!crit
[+] Trojan/SCR.Obfuscator.at!crit
[+] Trojan/SCR.Obfuscator.au!crit
[+] Trojan/SCR.Obfuscator.av!crit
[+] Trojan/SCR.Obfuscator.aw!crit
[+] Trojan/SCR.Obfuscator.ax!crit
[+] Trojan/SCR.Obfuscator.ay!crit
[+] Trojan/SCR.Obfuscator.az!crit
[+] Trojan/SCR.Obfuscator.ba!crit
[+] Trojan/SCR.Obfuscator.bb!crit
[+] Trojan/SCR.Obfuscator.bc!crit
[+] Trojan/SCR.Obfuscator.bd!crit
[+] Trojan/SCR.Obfuscator.be!crit
[+] Trojan/SCR.Obfuscator.bf!crit
[+] Trojan/SCR.Obfuscator.bg!crit
[+] Trojan/SCR.Obfuscator.bh!crit
[+] Trojan/SCR.Obfuscator.bi!crit
[+] Trojan/SCR.Obfuscator.bj!crit
[+] Trojan/SCR.Obfuscator.bk!crit
[+] Trojan/SCR.Obfuscator.bl!crit
[+] Trojan/SCR.Obfuscator.bm!crit
[+] Trojan/SCR.Obfuscator.bn!crit
[+] Trojan/SCR.Obfuscator.bo!crit
[+] Trojan/SCR.Obfuscator.bp!crit
[+] Trojan/SCR.Obfuscator.bq!crit
[+] Trojan/SCR.Obfuscator.br!crit
[+] Trojan/SCR.Obfuscator.bs!crit
[+] Trojan/SCR.Obfuscator.bt!crit
[+] Trojan/SCR.Obfuscator.bu!crit
[+] Trojan/SCR.Obfuscator.bv!crit
[+] Trojan/SCR.Obfuscator.bw!crit
[+] Trojan/SCR.Obfuscator.bx!crit
[+] Trojan/SCR.Obfuscator.by!crit
[+] Trojan/SCR.Obfuscator.bz!crit
[+] Trojan/SCR.Obfuscator.ca!crit
[+] Trojan/SCR.Obfuscator.cb!crit
[+] Trojan/SCR.Obfuscator.cc!crit
[+] Trojan/SCR.Obfuscator.cd!crit
[+] Trojan/SCR.Obfuscator.ce!crit
[+] Trojan/SCR.Obfuscator.cf!crit
[+] Trojan/SCR.Obfuscator.cg!crit
[+] Trojan/SCR.Obfuscator.ch!crit
[+] Trojan/SCR.Obfuscator.ci!crit
[+] Trojan/SCR.Obfuscator.cj!crit
[+] Trojan/SCR.Obfuscator.ck!crit
[+] Trojan/SCR.Obfuscator.cl!crit
[+] Trojan/SCR.Obfuscator.cm!crit
[+] Trojan/SCR.Obfuscator.cn!crit
[+] Trojan/SCR.Obfuscator.co!crit
[+] Trojan/SCR.Obfuscator.cp!crit
[+] Trojan/SCR.Obfuscator.cq!crit
[+] Trojan/SCR.Obfuscator.cr!crit
[+] Trojan/SCR.Obfuscator.cs!crit
[+] Trojan/SCR.Obfuscator.ct!crit
[+] Trojan/SCR.Obfuscator.cu!crit
[+] Trojan/SCR.Obfuscator.cv!crit
[+] Trojan/SCR.Obfuscator.cw!crit
[+] Trojan/SCR.Obfuscator.cx!crit
[+] Trojan/SCR.Obfuscator.cy!crit
[+] Trojan/SCR.Obfuscator.cz!crit
[+] Trojan/SCR.Obfuscator.da!crit
[+] Trojan/SCR.Obfuscator.db!crit
[+] Trojan/SCR.Obfuscator.dc!crit
[+] Trojan/SCR.Obfuscator.dd!crit
[+] Trojan/SCR.Obfuscator.de!crit
[+] Trojan/SCR.Obfuscator.df!crit
[+] Trojan/SCR.Obfuscator.dg!crit
[+] Trojan/SCR.Obfuscator.dh!crit
[+] Trojan/SCR.Obfuscator.di!crit
[+] Trojan/SCR.Obfuscator.dj!crit
[+] Trojan/SCR.Obfuscator.dk!crit
[+] Trojan/SCR.Obfuscator.dl!crit
[+] Trojan/SCR.Obfuscator.dm!crit
[+] Trojan/SCR.Obfuscator.dn!crit
[+] Trojan/SCR.Obfuscator.do!crit
[+] Trojan/SCR.Obfuscator.dp!crit
[+] Trojan/SCR.Obfuscator.dq!crit
[+] Trojan/SCR.Obfuscator.dr!crit
[+] Trojan/SCR.Obfuscator.ds!crit
[+] Trojan/SCR.Obfuscator.dt!crit
[+] Trojan/SCR.Obfuscator.du!crit
[+] Trojan/SCR.Obfuscator.dv!crit
[+] Trojan/SCR.Obfuscator.dw!crit
[+] Trojan/SCR.Obfuscator.dx!crit
[+] Trojan/SCR.Obfuscator.dy!crit
[+] Trojan/SCR.Obfuscator.dz!crit
[+] Trojan/SCR.Obfuscator.ea!crit
[+] Trojan/SCR.Obfuscator.eb!crit
[+] Trojan/SCR.Obfuscator.ec!crit
[+] Trojan/SCR.Obfuscator.ed!crit
[+] Trojan/SCR.Obfuscator.ee!crit
[+] Trojan/SCR.Obfuscator.ef!crit
[+] Trojan/SCR.Obfuscator.eg!crit
[+] Trojan/SCR.Obfuscator.eh!crit
[+] Trojan/SCR.Obfuscator.ei!crit
[+] Trojan/SCR.Obfuscator.ej!crit
[+] Trojan/SCR.Obfuscator.ek!crit
[+] Trojan/SCR.Obfuscator.el!crit
[+] Trojan/SCR.Obfuscator.em!crit
[+] Trojan/SCR.Obfuscator.en!crit
[+] Trojan/SCR.Obfuscator.eo!crit
[+] Trojan/SCR.Obfuscator.ep!crit
[+] Trojan/SCR.Obfuscator.eq!crit
[+] Trojan/SCR.Obfuscator.er!crit
[+] Trojan/SCR.Obfuscator.es!crit
[+] Trojan/SCR.Obfuscator.et!crit
[+] Trojan/SCR.Obfuscator.eu!crit
[+] Trojan/SCR.Obfuscator.ev!crit
[+] Trojan/SCR.Obfuscator.ew!crit
[+] Trojan/SCR.Obfuscator.ex!crit
[+] Trojan/SCR.Obfuscator.ey!crit
[+] Trojan/SCR.Obfuscator.ez!crit
[+] Trojan/SCR.Obfuscator.fa!crit
[+] Trojan/SCR.Obfuscator.fb!crit
[+] Trojan/SCR.Obfuscator.fc!crit
[+] Trojan/SCR.Obfuscator.fd!crit
[+] Trojan/SCR.Obfuscator.w!crit
[+] Trojan/SCR.Obfuscator.x!crit
[+] Trojan/SCR.Obfuscator.y!crit
[+] Trojan/SCR.Obfuscator.z!crit
[+] Trojan/SCR.ShellCode.g!crit
[+] Trojan/SCR.ShellCode.h!crit
[+] Trojan/SCR.ShellCode.i!crit
[+] Trojan/SCR.Shellcode.h!crit
[+] Trojan/W32.BypassUAC.a!crit
[+] Trojan/W64.Agent.gk!crit
[+] Trojan/W64.Obfuscated.nw!crit
[-] Exploit/Scr.CVE-2017-0199.a!crit
[-] Trojan/Scr.Obfuscator.a!crit
[-] Trojan/Scr.Obfuscator.aa!crit
[-] Trojan/Scr.Obfuscator.ab!crit
[-] Trojan/Scr.Obfuscator.ac!crit
[-] Trojan/Scr.Obfuscator.ad!crit
[-] Trojan/Scr.Obfuscator.ae!crit
[-] Trojan/Scr.Obfuscator.af!crit
[-] Trojan/Scr.Obfuscator.ag!crit
[-] Trojan/Scr.Obfuscator.ah!crit
[-] Trojan/Scr.Obfuscator.ai!crit
[-] Trojan/Scr.Obfuscator.aj!crit
[-] Trojan/Scr.Obfuscator.ak!crit
[-] Trojan/Scr.Obfuscator.al!crit
[-] Trojan/Scr.Obfuscator.am!crit
[-] Trojan/Scr.Obfuscator.an!crit
[-] Trojan/Scr.Obfuscator.ao!crit
[-] Trojan/Scr.Obfuscator.ap!crit
[-] Trojan/Scr.Obfuscator.aq!crit
[-] Trojan/Scr.Obfuscator.ar!crit
[-] Trojan/Scr.Obfuscator.as!crit
[-] Trojan/Scr.Obfuscator.at!crit
[-] Trojan/Scr.Obfuscator.au!crit
[-] Trojan/Scr.Obfuscator.av!crit
[-] Trojan/Scr.Obfuscator.aw!crit
[-] Trojan/Scr.Obfuscator.ax!crit
[-] Trojan/Scr.Obfuscator.ay!crit
[-] Trojan/Scr.Obfuscator.az!crit
[-] Trojan/Scr.Obfuscator.ba!crit
[-] Trojan/Scr.Obfuscator.bb!crit
[-] Trojan/Scr.Obfuscator.bc!crit
[-] Trojan/Scr.Obfuscator.bd!crit
[-] Trojan/Scr.Obfuscator.be!crit
[-] Trojan/Scr.Obfuscator.bf!crit
[-] Trojan/Scr.Obfuscator.bg!crit
[-] Trojan/Scr.Obfuscator.bh!crit
[-] Trojan/Scr.Obfuscator.bi!crit
[-] Trojan/Scr.Obfuscator.bj!crit
[-] Trojan/Scr.Obfuscator.bk!crit
[-] Trojan/Scr.Obfuscator.bl!crit
[-] Trojan/Scr.Obfuscator.bm!crit
[-] Trojan/Scr.Obfuscator.bn!crit
[-] Trojan/Scr.Obfuscator.bo!crit
[-] Trojan/Scr.Obfuscator.bp!crit
[-] Trojan/Scr.Obfuscator.bq!crit
[-] Trojan/Scr.Obfuscator.br!crit
[-] Trojan/Scr.Obfuscator.bs!crit
[-] Trojan/Scr.Obfuscator.bt!crit
[-] Trojan/Scr.Obfuscator.bu!crit
[-] Trojan/Scr.Obfuscator.bv!crit
[-] Trojan/Scr.Obfuscator.bw!crit
[-] Trojan/Scr.Obfuscator.bx!crit
[-] Trojan/Scr.Obfuscator.by!crit
[-] Trojan/Scr.Obfuscator.bz!crit
[-] Trojan/Scr.Obfuscator.ca!crit
[-] Trojan/Scr.Obfuscator.cb!crit
[-] Trojan/Scr.Obfuscator.cc!crit
[-] Trojan/Scr.Obfuscator.cd!crit
[-] Trojan/Scr.Obfuscator.ce!crit
[-] Trojan/Scr.Obfuscator.cf!crit
[-] Trojan/Scr.Obfuscator.cg!crit
[-] Trojan/Scr.Obfuscator.ch!crit
[-] Trojan/Scr.Obfuscator.ci!crit
[-] Trojan/Scr.Obfuscator.cj!crit
[-] Trojan/Scr.Obfuscator.ck!crit
[-] Trojan/Scr.Obfuscator.cl!crit
[-] Trojan/Scr.Obfuscator.cm!crit
[-] Trojan/Scr.Obfuscator.cn!crit
[-] Trojan/Scr.Obfuscator.co!crit
[-] Trojan/Scr.Obfuscator.cp!crit
[-] Trojan/Scr.Obfuscator.cq!crit
[-] Trojan/Scr.Obfuscator.cr!crit
[-] Trojan/Scr.Obfuscator.cs!crit
[-] Trojan/Scr.Obfuscator.ct!crit
[-] Trojan/Scr.Obfuscator.cu!crit
[-] Trojan/Scr.Obfuscator.cv!crit
[-] Trojan/Scr.Obfuscator.cw!crit
[-] Trojan/Scr.Obfuscator.cx!crit
[-] Trojan/Scr.Obfuscator.cy!crit
[-] Trojan/Scr.Obfuscator.cz!crit
[-] Trojan/Scr.Obfuscator.da!crit
[-] Trojan/Scr.Obfuscator.db!crit
[-] Trojan/Scr.Obfuscator.dc!crit
[-] Trojan/Scr.Obfuscator.dd!crit
[-] Trojan/Scr.Obfuscator.de!crit
[-] Trojan/Scr.Obfuscator.df!crit
[-] Trojan/Scr.Obfuscator.dg!crit
[-] Trojan/Scr.Obfuscator.dh!crit
[-] Trojan/Scr.Obfuscator.di!crit
[-] Trojan/Scr.Obfuscator.dj!crit
[-] Trojan/Scr.Obfuscator.dk!crit
[-] Trojan/Scr.Obfuscator.dl!crit
[-] Trojan/Scr.Obfuscator.dm!crit
[-] Trojan/Scr.Obfuscator.dn!crit
[-] Trojan/Scr.Obfuscator.do!crit
[-] Trojan/Scr.Obfuscator.dp!crit
[-] Trojan/Scr.Obfuscator.dq!crit
[-] Trojan/Scr.Obfuscator.dr!crit
[-] Trojan/Scr.Obfuscator.ds!crit
[-] Trojan/Scr.Obfuscator.dt!crit
[-] Trojan/Scr.Obfuscator.du!crit
[-] Trojan/Scr.Obfuscator.dv!crit
[-] Trojan/Scr.Obfuscator.dw!crit
[-] Trojan/Scr.Obfuscator.dx!crit
[-] Trojan/Scr.Obfuscator.dy!crit
[-] Trojan/Scr.Obfuscator.dz!crit
[-] Trojan/Scr.Obfuscator.ea!crit
[-] Trojan/Scr.Obfuscator.eb!crit
[-] Trojan/Scr.Obfuscator.ec!crit
[-] Trojan/Scr.Obfuscator.ed!crit
[-] Trojan/Scr.Obfuscator.ee!crit
[-] Trojan/Scr.Obfuscator.ef!crit
[-] Trojan/Scr.Obfuscator.eg!crit
[-] Trojan/Scr.Obfuscator.eh!crit
[-] Trojan/Scr.Obfuscator.ei!crit
[-] Trojan/Scr.Obfuscator.ej!crit
[-] Trojan/Scr.Obfuscator.ek!crit
[-] Trojan/Scr.Obfuscator.el!crit
[-] Trojan/Scr.Obfuscator.em!crit
[-] Trojan/Scr.Obfuscator.en!crit
[-] Trojan/Scr.Obfuscator.eo!crit
[-] Trojan/Scr.Obfuscator.ep!crit
[-] Trojan/Scr.Obfuscator.eq!crit
[-] Trojan/Scr.Obfuscator.er!crit
[-] Trojan/Scr.Obfuscator.es!crit
[-] Trojan/Scr.Obfuscator.et!crit
[-] Trojan/Scr.Obfuscator.eu!crit
[-] Trojan/Scr.Obfuscator.ev!crit
[-] Trojan/Scr.Obfuscator.ew!crit
[-] Trojan/Scr.Obfuscator.ex!crit
[-] Trojan/Scr.Obfuscator.ey!crit
[-] Trojan/Scr.Obfuscator.ez!crit
[-] Trojan/Scr.Obfuscator.fa!crit
[-] Trojan/Scr.Obfuscator.fb!crit
[-] Trojan/Scr.Obfuscator.fc!crit
[-] Trojan/Scr.Obfuscator.fd!crit
[-] Trojan/Scr.Obfuscator.w!crit
[-] Trojan/Scr.Obfuscator.x!crit
[-] Trojan/Scr.Obfuscator.y!crit
[-] Trojan/Scr.Obfuscator.z!crit
```

</details>

<details>
<summary>
新增遥测定义: 39 | 移除遥测定义: 24
</summary>

```
[+] Backdoor/Linux.Mirai.c!crit!submit
[+] Backdoor/PHP.WebShell.p!crit!submit
[+] Backdoor/PHP.WebShell.q!crit!submit
[+] Backdoor/PHP.WebShell.r!crit!submit
[+] Backdoor/W32.Lotok.xx!crit!submit
[+] Backdoor/W64.Lotok.ba!crit!submit
[+] Backdoor/W64.Lotok.bb!crit!submit
[+] Backerdoor/PHP.Injector.a!crit!submit
[+] HackTool/MSIL.BruteForce.a!crit!submit
[+] HackTool/MSIL.DDoS.b!crit!submit
[+] OMacro/SCR.Downloader.b!crit!submit
[+] Ransom/MSIL.LockFile.c!crit!submit
[+] Ransom/MSIL.LockFile.d!crit!submit
[+] Trojan/BAT.CoinMiner.d!crit!submit
[+] Trojan/JS.ChatgptStealer.a!crit!submit
[+] Trojan/JS.ChatgptStealer.b!crit!submit
[+] Trojan/SCR.Agent.clr!crit!submit
[+] Trojan/VBS.KillAV.a!crit!submit
[+] Trojan/VBS.KillAV.b!crit!submit
[+] Trojan/W32.HiJack.x!crit!submit
[+] Trojan/W32.Injector.clj!crit!submit
[+] Trojan/W32.Injector.t!crit!submit
[+] Trojan/W32.ProxyChanger.a!crit!submit
[+] TrojanDownloader/BAT.Runner.g!crit!submit
[+] TrojanDownloader/JS.Runner.a!crit!submit
[+] TrojanDownloader/JS.Starter.b!crit!submit
[+] TrojanDownloader/Linux.Agent.e!crit!submit
[+] TrojanDownloader/MSIL.Runner.d!crit!submit
[+] TrojanDownloader/MSIL.Runner.e!crit!submit
[+] TrojanDownloader/VBS.Runner.e!crit!submit
[+] TrojanDownloader/VBS.Runner.f!crit!submit
[+] TrojanDropper/BAT.Starter.b!crit!submit
[+] TrojanDropper/SCR.Agent.a!crit!submit
[+] TrojanSpy/BAT.Stealer.h!crit!submit
[+] TrojanSpy/Linux.Agent.a!crit!submit
[+] TrojanSpy/W32.Stealer.aa!crit!submit
[+] TrojanSpy/W32.Stealer.ac!crit!submit
[+] TrojanSpy/W32.Stealer.z!crit!submit
[+] TrojanSpy/W64.Stealer.tj!crit!submit
[-] Adware/Android.PornTool.i!crit!submit
[-] Backdoor/PHP.Webshell.d!crit!submit
[-] Backdoor/PHP.Webshell.p!crit!submit
[-] Backdoor/PHP.Webshell.q!crit!submit
[-] Backdoor/PHP.Webshell.r!crit!submit
[-] Backdoor/W32.Lotok.aa!crit!submit
[-] Backdoor/W32.Lotok.xe!crit!submit
[-] HEUR:Backdoor/W64.Lotok.a!crit!submit
[-] HEUR:Trojan/W32.HiJack.b!crit!submit
[-] HackTool/W32.Scrambler.a!crit!submit
[-] OMacro/Scr.Downloader.b!crit!submit
[-] Trojan/MSIL.Obfuscated.ao!crit!submit
[-] Trojan/PS.Loader.d!crit!submit
[-] Trojan/SCR.CoinMiner.a!crit!submit
[-] Trojan/SCR.ShellCode.g!crit!submit
[-] Trojan/SCR.ShellCode.h!crit!submit
[-] Trojan/SCR.ShellCode.i!crit!submit
[-] Trojan/SCR.Shellcode.h!crit!submit
[-] Trojan/W32.BypassUAC.a!crit!submit
[-] Trojan/W32.ShellLoader.m!crit!submit
[-] Trojan/W32.ShellLoader.n!crit!submit
[-] Trojan/W64.Agent.gk!crit!submit
[-] Trojan/W64.Obfuscated.nw!crit!submit
[-] TrojanDropper/Scr.Agent.a!crit!submit
```

</details>

#### 行为特征项变更 ([behav.txt](data/1768303271.behav.txt))

<details>
<summary>
新增: 2
</summary>

```
[+] TrojanDropper/MalSetup.OCB!submit
[+] TrojanDropper/MalSetup.OCC!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1768303271.troj.txt))

新增: 102 | 移除: 4

#### 白名单哈希变更 ([hwl.txt](data/1768303271.hwl.txt))

新增: 1

</details>
<details>
<summary><b>1768217225</b> - 2026-01-12 11:27:05 UTC</summary>

#### 特征项变更 ([pset.txt](data/1768217225.pset.txt))

<details>
<summary>
新增正式定义: 36
</summary>

```
[+] Backdoor/Agent.rc
[+] Backdoor/CobaltStrike.oz
[+] Backdoor/Ghost.ca
[+] Backdoor/Linux.Sliver.b
[+] Backdoor/Lotok.of
[+] Backdoor/Lotok.oh
[+] HEUR:Worm/BAT.Autorun.f
[+] HackTool/Linux.BotWarden.a
[+] Ransom/Cerber.ak
[+] Trojan/Agent.clq
[+] Trojan/DLLHijack.y
[+] Trojan/FakeApp.abl
[+] Trojan/GenCBL.a
[+] Trojan/GenCBL.b
[+] Trojan/HTML.Phishing.he
[+] Trojan/Injector.clh
[+] Trojan/Injector.cli
[+] Trojan/Linux.Gafgyt.r
[+] Trojan/Loader.ms
[+] Trojan/MSIL.Obfuscated.jx
[+] Trojan/Obfuscated.nt
[+] Trojan/Obfuscated.nu
[+] Trojan/PS.Runner.u
[+] Trojan/ShellLoader.ahg
[+] Trojan/ShellLoader.ahh
[+] TrojanDownloader/Agent.blq
[+] TrojanDownloader/Agent.bls
[+] TrojanDownloader/HTML.Agent.bh
[+] TrojanDownloader/JS.Agent.if
[+] TrojanDownloader/Linux.Agent.du
[+] TrojanDownloader/VBS.Agent.kd
[+] TrojanDownloader/W64.Agent.co
[+] TrojanSpy/JS.Stealer.bh
[+] TrojanSpy/MSIL.Formbook.bd
[+] TrojanSpy/MSIL.Formbook.be
[+] TrojanSpy/MSIL.Formbook.bf
```

</details>

<details>
<summary>
新增遥测定义: 43 | 移除遥测定义: 37
</summary>

```
[+] Backdoor/Linux.Mirai.kx!submit
[+] Backdoor/Lotok.oi!submit
[+] Backdoor/Lotok.oj!submit
[+] HEUR:Trojan/Injector.clj!submit
[+] HEUR:Trojan/KillWin.g!submit
[+] HEUR:TrojanDownloader/Linux.Mirai.bv!submit
[+] HEUR:TrojanSpy/OSX.Amos.c!submit
[+] HVM:Backdoor/Lotok.ce!submit
[+] HVM:Trojan/ShellLoader.cj!submit
[+] Trojan/Autoit.Injector.ds!submit
[+] Trojan/BAT.Agent.gq!submit
[+] Trojan/BAT.Runner.bn!submit
[+] Trojan/BAT.Runner.bo!submit
[+] Trojan/Clipboard.c!submit
[+] Trojan/DLLHijack.z!submit
[+] Trojan/DllHijack.aa!submit
[+] Trojan/DllHijack.z!submit
[+] Trojan/FakeApp.abb!submit
[+] Trojan/FakeApp.abm!submit
[+] Trojan/FakeApp.abn!submit
[+] Trojan/HiJack.yk!submit
[+] Trojan/JS.Obfuscated.dc!submit
[+] Trojan/KillMBR.cm!submit
[+] Trojan/Linux.Mirai.gi!submit
[+] Trojan/Linux.Mirai.gj!submit
[+] Trojan/Loader.mt!submit
[+] Trojan/MSIL.Obfuscated.jy!submit
[+] Trojan/Obfuscated.nv!submit
[+] Trojan/PS.Loader.n!submit
[+] Trojan/ShellLoader.ahi!submit
[+] Trojan/ShellLoader.ahj!submit
[+] Trojan/W64.Agent.gk!submit
[+] Trojan/W64.Rozena.p!submit
[+] TrojanDownloader/Agent.blt!submit
[+] TrojanDownloader/HTML.Agent.bi!submit
[+] TrojanDownloader/JS.Agent.gc!submit
[+] TrojanDownloader/Linux.Agent.dv!submit
[+] TrojanDropper/Maloader.n!submit
[+] TrojanDropper/VBS.Agent.eg!submit
[+] TrojanDropper/W64.Agent.ca!submit
[+] TrojanSpy/Stealer.ti!submit
[+] TrojanSpy/W64.PwStealer.e!submit
[+] TrojanSpy/W64.Stealer.y!submit
[-] Backdoor/Agent.rc!submit
[-] Backdoor/CobaltStrike.oz!submit
[-] Backdoor/Ghost.ca!submit
[-] Backdoor/Linux.Lotok.a!submit
[-] Backdoor/Lotok.of!submit
[-] Backdoor/Lotok.og!submit
[-] Backdoor/Lotok.oh!submit
[-] HEUR:Worm/BAT.Autorun.f!submit
[-] HackTool/Linux.BotWarden.a!submit
[-] Ransom/Cerber.ak!submit
[-] Trojan/Agent.clq!submit
[-] Trojan/DLLHijack.y!submit
[-] Trojan/FakeApp.abl!submit
[-] Trojan/GenCBL.a!submit
[-] Trojan/GenCBL.b!submit
[-] Trojan/HTML.Phishing.he!submit
[-] Trojan/Injector.clh!submit
[-] Trojan/Injector.cli!submit
[-] Trojan/Linux.Gafgyt.r!submit
[-] Trojan/Loader.ms!submit
[-] Trojan/MSIL.Obfuscated.jx!submit
[-] Trojan/Obfuscated.nt!submit
[-] Trojan/Obfuscated.nu!submit
[-] Trojan/PS.Runner.u!submit
[-] Trojan/ShellLoader.ahg!submit
[-] Trojan/ShellLoader.ahh!submit
[-] TrojanDownloader/Agent.blq!submit
[-] TrojanDownloader/Agent.bls!submit
[-] TrojanDownloader/HTML.Agent.bh!submit
[-] TrojanDownloader/JS.Agent.if!submit
[-] TrojanDownloader/Linux.Agent.du!submit
[-] TrojanDownloader/VBS.Agent.kd!submit
[-] TrojanDownloader/W64.Agent.co!submit
[-] TrojanSpy/JS.Stealer.bh!submit
[-] TrojanSpy/MSIL.Formbook.bd!submit
[-] TrojanSpy/MSIL.Formbook.be!submit
[-] TrojanSpy/MSIL.Formbook.bf!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1768217225.crithash.txt))

<details>
<summary>
新增正式定义: 8
</summary>

```
[+] Backdoor/OSX.NukeSped.a!crit
[+] HackTool/Linux.Usurper.a!crit
[+] Trojan/Python.Agent.bt!crit
[+] Trojan/SCR.ShellCode.e!crit
[+] Trojan/SCR.ShellCode.f!crit
[+] Trojan/W32.Injector.clh!crit
[+] TrojanDownloader/JS.Agent.c!crit
[+] Worm/BAT.Runner.bp!crit
```

</details>

<details>
<summary>
新增遥测定义: 39 | 移除遥测定义: 11
</summary>

```
[+] Adware/Android.PornTool.i!crit!submit
[+] Backdoor/PHP.WebShell.d!crit!submit
[+] Backdoor/PHP.WebShell.s!crit!submit
[+] Backdoor/PS.ReverseShell.f!crit!submit
[+] Backdoor/W32.Lotok.aa!crit!submit
[+] Backdoor/W32.Lotok.x!crit!submit
[+] Backdoor/W32.Lotok.xe!crit!submit
[+] Backdoor/W32.Lotok.y!crit!submit
[+] HEUR:Backdoor/W64.Lotok.a!crit!submit
[+] HackTool/PS.BruteForce.a!crit!submit
[+] HackTool/W32.Scrambler.a!crit!submit
[+] Trojan/MSIL.Obfuscated.ao!crit!submit
[+] Trojan/PS.CoinMiner.a!crit!submit
[+] Trojan/PS.Loader.d!crit!submit
[+] Trojan/SCR.CoinMiner.a!crit!submit
[+] Trojan/SCR.ShellCode.g!crit!submit
[+] Trojan/SCR.ShellCode.h!crit!submit
[+] Trojan/SCR.ShellCode.i!crit!submit
[+] Trojan/SCR.Shellcode.h!crit!submit
[+] Trojan/W32.BypassUAC.a!crit!submit
[+] Trojan/W32.Injector.r!crit!submit
[+] Trojan/W32.Injector.s!crit!submit
[+] Trojan/W32.ShellLoader.m!crit!submit
[+] Trojan/W32.ShellLoader.n!crit!submit
[+] Trojan/W32.ULPM.a!crit!submit
[+] Trojan/W64.Agent.gk!crit!submit
[+] Trojan/W64.Injector.a!crit!submit
[+] Trojan/W64.Obfuscated.nw!crit!submit
[+] TrojanDownloader/MSIL.Runner.c!crit!submit
[+] TrojanDownloader/PS.Runner.p!crit!submit
[+] TrojanDownloader/VBS.Runner.d!crit!submit
[+] TrojanDropper/MSIL.Starter.a!crit!submit
[+] TrojanDropper/MSIL.Starter.b!crit!submit
[+] TrojanDropper/PS.Runner.c!crit!submit
[+] TrojanDropper/VBS.Runner.c!crit!submit
[+] TrojanDropper/W64.Runner.b!crit!submit
[+] TrojanSpy/PS.Stealer.i!crit!submit
[+] TrojanSpy/VBS.Stealer.a!crit!submit
[+] TrojanSpy/W32.Banker.b!crit!submit
[-] Backdoor/OSX.NukeSped.a!crit!submit
[-] Backdoor/W32.Lotok.u!crit!submit
[-] Backdoor/W32.Lotok.v!crit!submit
[-] HackTool/Linux.Usurper.a!crit!submit
[-] Trojan/Python.Agent.bt!crit!submit
[-] Trojan/SCR.ShellCode.e!crit!submit
[-] Trojan/SCR.ShellCode.f!crit!submit
[-] Trojan/W32.Injector.clh!crit!submit
[-] Trojan/W32.ShellLoader.l!crit!submit
[-] TrojanDownloader/JS.Agent.c!crit!submit
[-] Worm/BAT.Runner.bp!crit!submit
```

</details>

#### 行为特征项变更 ([behav.txt](data/1768217225.behav.txt))

<details>
<summary>
新增: 6 | 移除: 4
</summary>

```
[+] ADV:Ransom/Genalocker.ZFA!submit
[+] ADV:Ransom/Genalocker.ZFB!submit
[+] MEMSCAN/Lotok.A!submit
[+] MEMSCAN/SpecialDir.C
[+] TrojanDropper/MalSetup.OCA!submit
[+] TrojanDropper/MalSetup.PB!submit
[-] ADV:Ransom/Genalocker.ZEA!submit
[-] ADV:Ransom/Genalocker.ZEB!submit
[-] TrojanDropper/MalSetup.OA!submit
[-] TrojanDropper/MalSetup.PA!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1768217225.troj.txt))

新增: 42

#### 白名单哈希变更 ([hwl.txt](data/1768217225.hwl.txt))

新增: 2

</details>
<details>
<summary><b>1768128066</b> - 2026-01-11 10:41:06 UTC</summary>

#### 黑名单哈希变更 ([troj.txt](data/1768128066.troj.txt))

新增: 35

#### 白名单哈希变更 ([hwl.txt](data/1768128066.hwl.txt))

新增: 12

</details>

<details>
<summary><b>1768044761</b> - 2026-01-10 11:32:41 UTC</summary>

#### 黑名单哈希变更 ([troj.txt](data/1768044761.troj.txt))

新增: 128

#### 白名单哈希变更 ([hwl.txt](data/1768044761.hwl.txt))

新增: 8

</details>

<details>
<summary><b>1767957379</b> - 2026-01-09 11:16:19 UTC</summary>

#### 特征项变更 ([pset.txt](data/1767957379.pset.txt))

<details>
<summary>
新增正式定义: 35
</summary>

```
[+] Backdoor/Agent.rb
[+] Backdoor/Lotok.oa
[+] Backdoor/Python.Agent.n
[+] Backdoor/Remcos.ax
[+] Exploit/HTML.CVE-2025-54100
[+] HVM:Backdoor/Lotok.cd
[+] HVM:TrojanDropper/W64.Agent.ca
[+] HackTool/Rdp2Tcp.a
[+] Trojan/AutoIt.Runner.g
[+] Trojan/Barys.c
[+] Trojan/FakeApp.aar
[+] Trojan/FakeApp.abj
[+] Trojan/FakeApp.abk
[+] Trojan/HTML.Phishing.hd
[+] Trojan/MSIL.CoinStealer.g
[+] Trojan/MSIL.Obfuscated.jw
[+] Trojan/PS.Loader.m
[+] Trojan/ShellLoader.ahf
[+] Trojan/StrongPity.c
[+] Trojan/W64.Agent.gj
[+] TrojanDownloader/Agent.blp
[+] TrojanDownloader/HTML.Agent.bg
[+] TrojanDownloader/MSIL.Agent.ajj
[+] TrojanDownloader/VBS.Agent.kc
[+] TrojanDropper/Agent.akb
[+] TrojanDropper/Agent.akl
[+] TrojanDropper/Agent.akm
[+] TrojanDropper/Agent.akp
[+] TrojanDropper/Agent.akq
[+] TrojanDropper/Agent.akr
[+] TrojanDropper/Agent.aks
[+] TrojanDropper/Agent.akt
[+] TrojanSpy/Banker.hm
[+] TrojanSpy/Zbot.dj
[+] Worm/Autorun.hc
```

</details>

<details>
<summary>
新增遥测定义: 41 | 移除遥测定义: 36
</summary>

```
[+] Backdoor/Agent.rc!submit
[+] Backdoor/CobaltStrike.oz!submit
[+] Backdoor/Ghost.ca!submit
[+] Backdoor/Linux.Lotok.a!submit
[+] Backdoor/Linux.Mirai.kw!submit
[+] Backdoor/Lotok.od!submit
[+] Backdoor/Lotok.oe!submit
[+] Backdoor/Lotok.of!submit
[+] Backdoor/Lotok.og!submit
[+] Backdoor/Lotok.oh!submit
[+] HEUR:Worm/BAT.Autorun.f!submit
[+] HackTool/Linux.BotWarden.a!submit
[+] Ransom/Cerber.ak!submit
[+] Rootkit/Agent!submit
[+] Trojan/Agent.clq!submit
[+] Trojan/DLLHijack.y!submit
[+] Trojan/FakeApp.abl!submit
[+] Trojan/GenCBL.a!submit
[+] Trojan/GenCBL.b!submit
[+] Trojan/HTML.Phishing.he!submit
[+] Trojan/Injector.clh!submit
[+] Trojan/Injector.cli!submit
[+] Trojan/Linux.Gafgyt.r!submit
[+] Trojan/Loader.ms!submit
[+] Trojan/MSIL.Obfuscated.jx!submit
[+] Trojan/Obfuscated.nt!submit
[+] Trojan/Obfuscated.nu!submit
[+] Trojan/PS.Runner.u!submit
[+] Trojan/ShellLoader.ahg!submit
[+] Trojan/ShellLoader.ahh!submit
[+] TrojanDownloader/Agent.blq!submit
[+] TrojanDownloader/Agent.bls!submit
[+] TrojanDownloader/HTML.Agent.bh!submit
[+] TrojanDownloader/JS.Agent.if!submit
[+] TrojanDownloader/Linux.Agent.du!submit
[+] TrojanDownloader/VBS.Agent.kd!submit
[+] TrojanDownloader/W64.Agent.co!submit
[+] TrojanSpy/JS.Stealer.bh!submit
[+] TrojanSpy/MSIL.Formbook.bd!submit
[+] TrojanSpy/MSIL.Formbook.be!submit
[+] TrojanSpy/MSIL.Formbook.bf!submit
[-] Backdoor/Agent.rb!submit
[-] Backdoor/Lotok.oa!submit
[-] Backdoor/Python.Agent.n!submit
[-] Backdoor/Remcos.ax!submit
[-] Exploit/HTML.CVE-2025-54100.a!submit
[-] HVM:Backdoor/Lotok.cd!submit
[-] HVM:TrojanDropper/W64.Agent.ca!submit
[-] HackTool/Rdp2Tcp.a!submit
[-] Trojan/AutoIt.Runner.g!submit
[-] Trojan/Barys.c!submit
[-] Trojan/FakeApp.aar!submit
[-] Trojan/FakeApp.abb!submit
[-] Trojan/FakeApp.abj!submit
[-] Trojan/FakeApp.abk!submit
[-] Trojan/HTML.Phishing.hd!submit
[-] Trojan/MSIL.CoinStealer.g!submit
[-] Trojan/MSIL.Obfuscated.jw!submit
[-] Trojan/PS.Loader.m!submit
[-] Trojan/ShellLoader.ahf!submit
[-] Trojan/StrongPity.c!submit
[-] Trojan/W64.Agent.gj!submit
[-] TrojanDownloader/Agent.blp!submit
[-] TrojanDownloader/HTML.Agent.bg!submit
[-] TrojanDownloader/MSIL.Agent.ajj!submit
[-] TrojanDownloader/VBS.Agent.kc!submit
[-] TrojanDropper/Agent.akb!submit
[-] TrojanDropper/Agent.akl!submit
[-] TrojanDropper/Agent.akm!submit
[-] TrojanDropper/Agent.akp!submit
[-] TrojanDropper/Agent.akq!submit
[-] TrojanDropper/Agent.akr!submit
[-] TrojanDropper/Agent.aks!submit
[-] TrojanDropper/Agent.akt!submit
[-] TrojanSpy/Banker.hm!submit
[-] TrojanSpy/Zbot.dj!submit
[-] Worm/Autorun.hc!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1767957379.crithash.txt))

<details>
<summary>
新增正式定义: 17 | 移除正式定义: 1
</summary>

```
[+] Backdoor/W32.Agent.e!crit
[+] Backdoor/W32.Lotok.af!crit
[+] Trojan/MSIL.Agent.aak!crit
[+] Trojan/MSIL.Obfuscated.an!crit
[+] Trojan/MSIL.Obfuscated.jw!crit
[+] Trojan/SCR.Agent.c!crit
[+] Trojan/SCR.Agent.d!crit
[+] Trojan/W32.FakeApp.e!crit
[+] Trojan/W32.Obfuscated.nv!crit
[+] Trojan/W32.Obfuscated.nw!crit
[+] Trojan/W64.KillWin.dj!crit
[+] TrojanDownloader/W32.Agent.blp!crit
[+] TrojanDropper/W32.Agent.m!crit
[+] TrojanSpy/MSIL.Formbook.a!crit
[+] Worm/SCR.Autorun.a!crit
[+] Worm/VBS.Capside.a!crit
[+] Worm/W32.Capside.a!crit
[-] Virus/MAYA.FuckVirus.b!crit
```

</details>

<details>
<summary>
新增遥测定义: 35 | 移除遥测定义: 19
</summary>

```
[+] Backdoor/OSX.NukeSped.a!crit!submit
[+] Backdoor/PHP.Webshell.p!crit!submit
[+] Backdoor/PHP.Webshell.q!crit!submit
[+] Backdoor/PHP.Webshell.r!crit!submit
[+] Backdoor/PS.GuidPuller.b!crit!submit
[+] Backdoor/W32.Lotok.u!crit!submit
[+] Backdoor/W32.Lotok.v!crit!submit
[+] HackTool/Linux.Usurper.a!crit!submit
[+] Trojan/BAT.KillAV.c!crit!submit
[+] Trojan/BAT.KillAV.d!crit!submit
[+] Trojan/MSIL.Injector.g!crit!submit
[+] Trojan/Python.Agent.bt!crit!submit
[+] Trojan/SCR.ShellCode.e!crit!submit
[+] Trojan/SCR.ShellCode.f!crit!submit
[+] Trojan/W32.Injector.clh!crit!submit
[+] Trojan/W32.ShellLoader.l!crit!submit
[+] TrojanDownloader/JS.Agent.c!crit!submit
[+] TrojanDownloader/MSIL.Runner.a!crit!submit
[+] TrojanDownloader/MSIL.Runner.b!crit!submit
[+] TrojanDownloader/PS.Runner.h!crit!submit
[+] TrojanDownloader/PS.Runner.i!crit!submit
[+] TrojanDownloader/PS.Runner.j!crit!submit
[+] TrojanDownloader/PS.Runner.k!crit!submit
[+] TrojanDownloader/PS.Runner.l!crit!submit
[+] TrojanDownloader/PS.Runner.m!crit!submit
[+] TrojanDownloader/PS.Runner.n!crit!submit
[+] TrojanDownloader/PS.Runner.o!crit!submit
[+] TrojanDownloader/W32.Runner.c!crit!submit
[+] TrojanDownloader/W32.Runner.d!crit!submit
[+] TrojanDropper/PS.ShellLoader.c!crit!submit
[+] TrojanDropper/VBS.Runner.b!crit!submit
[+] TrojanDropper/W64.ShellLoader.b!crit!submit
[+] TrojanSpy/MSIL.Stealer.ccz!crit!submit
[+] TrojanSpy/MSIL.Stealer.cda!crit!submit
[+] Worm/BAT.Runner.bp!crit!submit
[-] Backdoor/W32.Agent.e!crit!submit
[-] Backdoor/W32.Lotok.af!crit!submit
[-] Backdoor/W32.Lotok.ag!crit!submit
[-] Trojan/MSIL.Agent.aak!crit!submit
[-] Trojan/MSIL.Obfuscated.an!crit!submit
[-] Trojan/MSIL.Obfuscated.jw!crit!submit
[-] Trojan/SCR.Agent.c!crit!submit
[-] Trojan/SCR.Agent.d!crit!submit
[-] Trojan/W32.FakeApp.e!crit!submit
[-] Trojan/W32.Obfuscated.nv!crit!submit
[-] Trojan/W32.Obfuscated.nw!crit!submit
[-] Trojan/W32.ShellLoader.k!crit!submit
[-] Trojan/W64.KillWin.dj!crit!submit
[-] TrojanDownloader/W32.Agent.blp!crit!submit
[-] TrojanDroppper/VBS.Runner.a!crit!submit
[-] TrojanSpy/MSIL.Formbook.a!crit!submit
[-] Worm/SCR.Autorun.a!crit!submit
[-] Worm/VBS.Capside.a!crit!submit
[-] Worm/W32.Capside.a!crit!submit
```

</details>

#### 行为特征项变更 ([behav.txt](data/1767957379.behav.txt))

<details>
<summary>
新增: 2 | 移除: 2
</summary>

```
[+] ADV:Ransom/Genalocker.ZEA!submit
[+] ADV:Ransom/Genalocker.ZEB!submit
[-] ADV:Ransom/Genalocker.ZCB!submit
[-] ADV:Ransom/Genalocker.ZDA!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1767957379.troj.txt))

新增: 137 | 移除: 2

</details>

<details>
<summary><b>1767870070</b> - 2026-01-08 11:01:10 UTC</summary>

#### 特征项变更 ([pset.txt](data/1767870070.pset.txt))

<details>
<summary>
新增正式定义: 42 | 移除正式定义: 1
</summary>

```
[+] Backdoor/Lotok.ob
[+] Backdoor/W64.AdaptixC2.b
[+] Backdoor/W64.Agent.l
[+] Backdoor/W64.Agent.m
[+] HEUR:Backdoor/MSIL.Bladabindi.bc
[+] HEUR:Backdoor/MSIL.Bladabindi.bd
[+] HEUR:Trojan/Injector.cp
[+] HVM:Backdoor/Lotok.bx
[+] HackTool/Python.Winpwnage.a
[+] Ransom/LockFile.ri
[+] Trojan/Agent.clp
[+] Trojan/BAT.Loader.j
[+] Trojan/FakeApp.abg
[+] Trojan/FakeApp.abh
[+] Trojan/FakeApp.abi
[+] Trojan/Linux.Mirai.gg
[+] Trojan/Linux.Mirai.gh
[+] Trojan/Loader.mq
[+] Trojan/Loader.mr
[+] Trojan/Obfuscated.ns
[+] Trojan/Python.DDos.h
[+] Trojan/ShellLoader.ahd
[+] Trojan/ShellLoader.ahe
[+] TrojanDownloader/PS.Agent.fa
[+] TrojanDownloader/PS.Agent.fb
[+] TrojanDownloader/VBS.Agent.kb
[+] TrojanDownloader/W64.Agent.cn
[+] TrojanDropper/Agent.akk
[+] TrojanDropper/Agent.akn
[+] TrojanDropper/Agent.ako
[+] TrojanDropper/MSIL.Agent.jx
[+] TrojanDropper/Python.Agent.n
[+] TrojanDropper/VBS.Agent.ef
[+] TrojanDropper/W64.Agent.bz
[+] TrojanSpy/HTML.Stealer.c
[+] TrojanSpy/Python.Rodico.a
[+] VirTool/Obfuscator.aw
[+] VirTool/Obfuscator.ay
[+] VirTool/Obfuscator.ba
[+] VirTool/Obfuscator.bb
[+] VirTool/Obfuscator.be
[+] VirTool/Obfuscator.db
[-] Backdoor/W64.AdaptixC2.a
```

</details>

<details>
<summary>
新增遥测定义: 33 | 移除遥测定义: 43
</summary>

```
[+] Backdoor/Agent.rb!submit
[+] Backdoor/Lotok.oa!submit
[+] Backdoor/Lotok.oc!submit
[+] Backdoor/Python.Agent.n!submit
[+] Backdoor/Remcos.ax!submit
[+] Exploit/HTML.CVE-2025-54100.a!submit
[+] HEUR:TrojanDropper/Agent.ar!submit
[+] HVM:Backdoor/Lotok.cd!submit
[+] HVM:TrojanDropper/W64.Agent.ca!submit
[+] HackTool/Rdp2Tcp.a!submit
[+] Trojan/AutoIt.Runner.g!submit
[+] Trojan/Barys.c!submit
[+] Trojan/FakeApp.abj!submit
[+] Trojan/FakeApp.abk!submit
[+] Trojan/HTML.Phishing.hd!submit
[+] Trojan/MSIL.CoinStealer.g!submit
[+] Trojan/MSIL.Obfuscated.jw!submit
[+] Trojan/PS.Loader.m!submit
[+] Trojan/ShellLoader.ahf!submit
[+] Trojan/StrongPity.c!submit
[+] Trojan/W64.Agent.gj!submit
[+] TrojanDownloader/Agent.blp!submit
[+] TrojanDownloader/HTML.Agent.bg!submit
[+] TrojanDownloader/MSIL.Agent.ajj!submit
[+] TrojanDownloader/VBS.Agent.kc!submit
[+] TrojanDropper/Agent.akp!submit
[+] TrojanDropper/Agent.akq!submit
[+] TrojanDropper/Agent.akr!submit
[+] TrojanDropper/Agent.aks!submit
[+] TrojanDropper/Agent.akt!submit
[+] TrojanSpy/Banker.hm!submit
[+] TrojanSpy/Zbot.dj!submit
[+] Worm/Autorun.hc!submit
[-] Backdoor/Lotok.ob!submit
[-] Backdoor/W64.AdaptixC2.b!submit
[-] Backdoor/W64.Agent.l!submit
[-] Backdoor/W64.Agent.m!submit
[-] HEUR:Backdoor/MSIL.Bladabindi.bc!submit
[-] HEUR:Backdoor/MSIL.Bladabindi.bd!submit
[-] HEUR:Trojan/BAT.Loader.j!submit
[-] HEUR:Trojan/Injector.cp!submit
[-] HEUR:Trojan/KillWin.dj!submit
[-] HVM:Backdoor/Lotok.bx!submit
[-] Ransom/LockFile.ri!submit
[-] Trojan/Agent.clp!submit
[-] Trojan/BAT.Loader.j!submit
[-] Trojan/FakeApp.abg!submit
[-] Trojan/FakeApp.abh!submit
[-] Trojan/FakeApp.abi!submit
[-] Trojan/Linux.Mirai.gg!submit
[-] Trojan/Linux.Mirai.gh!submit
[-] Trojan/Loader.mq!submit
[-] Trojan/Loader.mr!submit
[-] Trojan/Obfuscated.ns!submit
[-] Trojan/Python.DDos.h!submit
[-] Trojan/ShellLoader.ahd!submit
[-] Trojan/ShellLoader.ahe!submit
[-] TrojanDownloader/PS.Agent.fa!submit
[-] TrojanDownloader/PS.Agent.fb!submit
[-] TrojanDownloader/VBS.Agent.kb!submit
[-] TrojanDownloader/W64.Agent.cn!submit
[-] TrojanDropper/Agent.akk!submit
[-] TrojanDropper/Agent.akn!submit
[-] TrojanDropper/Agent.ako!submit
[-] TrojanDropper/MSIL.Agent.jx!submit
[-] TrojanDropper/Python.Agent.n!submit
[-] TrojanDropper/VBS.Agent.ef!submit
[-] TrojanDropper/W64.Agent.bz!submit
[-] TrojanSpy/HTML.Stealer.c!submit
[-] TrojanSpy/Python.Rodico.a!submit
[-] VirTool/Obfuscator.aw!submit
[-] VirTool/Obfuscator.ay!submit
[-] VirTool/Obfuscator.ba!submit
[-] VirTool/Obfuscator.bb!submit
[-] VirTool/Obfuscator.be!submit
[-] VirTool/Obfuscator.db!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1767870070.crithash.txt))

<details>
<summary>
新增正式定义: 20
</summary>

```
[+] Adware/Android.PornTool.g!crit
[+] Adware/Android.PornTool.h!crit
[+] Adware/W32.Agent.da!crit
[+] Backdoor/Linux.Mirai.a!crit
[+] Backdoor/Linux.Mirai.b!crit
[+] Backdoor/Linux.ReverseShell.a!crit
[+] Backdoor/W64.Agent.g!crit
[+] Backdoor/W64.SparkRAT.a!crit
[+] Exploit/W32.CVE-2025-62215.a!crit
[+] HEUR:Trojan/W32.HiJack.a!crit
[+] HackTool/Linux.CoinMiner.a!crit
[+] Trojan/HTML.Phishing.oq!crit
[+] Trojan/MSIL.Obfuscated.am!crit
[+] Trojan/W32.Obfuscated.nt!crit
[+] TrojanDownloader/MSIL.Maloader.j!crit
[+] TrojanDownloader/VBS.Obfuscated.c!crit
[+] TrojanSpy/Linux.Stealer.b!crit
[+] TrojanSpy/W32.Rodico.a!crit
[+] TrojanSpy/W64.ClipBanker.b!crit
[+] Virus/MAYA.FuckVirus.b!crit
```

</details>

<details>
<summary>
新增遥测定义: 41 | 移除遥测定义: 19
</summary>

```
[+] Backdoor/PS.ReverseShell.d!crit!submit
[+] Backdoor/PS.ReverseShell.e!crit!submit
[+] Backdoor/W32.Agent.e!crit!submit
[+] Backdoor/W32.Lotok.af!crit!submit
[+] Backdoor/W32.Lotok.ag!crit!submit
[+] HEUR:Trojan/W32.HiJack.b!crit!submit
[+] Joke/MSIL.Agent.a!crit!submit
[+] Ransom/MSIL.LockFile.b!crit!submit
[+] Ransom/W64.LockFilet.a!crit!submit
[+] Trojan/MSIL.Agent.aak!crit!submit
[+] Trojan/MSIL.Injector.c!crit!submit
[+] Trojan/MSIL.Injector.d!crit!submit
[+] Trojan/MSIL.Injector.e!crit!submit
[+] Trojan/MSIL.Injector.f!crit!submit
[+] Trojan/MSIL.Obfuscated.an!crit!submit
[+] Trojan/MSIL.Obfuscated.jw!crit!submit
[+] Trojan/SCR.Agent.c!crit!submit
[+] Trojan/SCR.Agent.d!crit!submit
[+] Trojan/W32.FakeApp.e!crit!submit
[+] Trojan/W32.Injector.q!crit!submit
[+] Trojan/W32.Obfuscated.nv!crit!submit
[+] Trojan/W32.Obfuscated.nw!crit!submit
[+] Trojan/W32.ShellLoader.k!crit!submit
[+] Trojan/W64.KillWin.dj!crit!submit
[+] TrojanDownloader/BAT.Runner.e!crit!submit
[+] TrojanDownloader/BAT.Runner.f!crit!submit
[+] TrojanDownloader/PS.Runner.g!crit!submit
[+] TrojanDownloader/W32.Agent.blp!crit!submit
[+] TrojanDropper/MSIL.Agent.b!crit!submit
[+] TrojanDropper/MSIL.Agent.c!crit!submit
[+] TrojanDropper/MSIL.Agent.d!crit!submit
[+] TrojanDropper/W32.Agent.ah!crit!submit
[+] TrojanDropper/W32.DDoS.a!crit!submit
[+] TrojanDroppper/VBS.Runner.a!crit!submit
[+] TrojanSpy/MSIL.Formbook.a!crit!submit
[+] TrojanSpy/MSIL.Keylogger.b!crit!submit
[+] TrojanSpy/MSIL.Stealer.ccx!crit!submit
[+] TrojanSpy/MSIL.Stealer.ccy!crit!submit
[+] Worm/SCR.Autorun.a!crit!submit
[+] Worm/VBS.Capside.a!crit!submit
[+] Worm/W32.Capside.a!crit!submit
[-] Adware/Android.PornTool.g!crit!submit
[-] Adware/Android.PornTool.h!crit!submit
[-] Adware/W32.Agent.da!crit!submit
[-] Backdoor/Linux.Mirai.a!crit!submit
[-] Backdoor/Linux.Mirai.b!crit!submit
[-] Backdoor/Linux.ReverseShell.a!crit!submit
[-] Backdoor/W64.Agent.g!crit!submit
[-] Backdoor/W64.SparkRAT.a!crit!submit
[-] Exploit/W32.CVE-2025-62215.a!crit!submit
[-] HEUR:Trojan/W32.HiJack.a!crit!submit
[-] HackTool/Linux.CoinMiner.a!crit!submit
[-] Trojan/HTML.Phishing.oq!crit!submit
[-] Trojan/MSIL.Obfuscated.am!crit!submit
[-] Trojan/W32.Obfuscated.nt!crit!submit
[-] TrojanDownloader/MSIL.Maloader.j!crit!submit
[-] TrojanSpy/Linux.Stealer.b!crit!submit
[-] TrojanSpy/W32.Rodico.a!crit!submit
[-] TrojanSpy/W64.ClipBanker.b!crit!submit
[-] Virus/MAYA.FuckVirus.b!crit!submit
```

</details>

#### 行为特征项变更 ([behav.txt](data/1767870070.behav.txt))

<details>
<summary>
新增: 2 | 移除: 1
</summary>

```
[+] Backdoor/Lotok.DA!submit
[+] Software:GM/NN.A#NN加速器
[-] Software:GM/NN.A#NN加速器!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1767870070.troj.txt))

新增: 64

</details>

<details>
<summary><b>1767782775</b> - 2026-01-07 10:46:15 UTC</summary>

#### 特征项变更 ([pset.txt](data/1767782775.pset.txt))

<details>
<summary>
新增正式定义: 77
</summary>

```
[+] Backdoor/Agent.ra
[+] Backdoor/Linux.Gafgyt.by
[+] Backdoor/Lotok.nz
[+] Backdoor/W64.Agent.k
[+] Backdoor/Xkcp.a
[+] Exploit/VulnDriver.s
[+] HEUR:Backdoor/Linux.Mirai.ku
[+] HEUR:Trojan/BAT.Loader.j
[+] HEUR:Trojan/BAT.Loader.k
[+] HEUR:Trojan/Injector.co
[+] HEUR:Trojan/JS.Obfuscated.db
[+] HEUR:Trojan/KillMBR.cm
[+] HEUR:Trojan/KillWin.f
[+] HEUR:Trojan/Runner.fm
[+] HEUR:TrojanDownloader/Agent.blo
[+] HEUR:TrojanDownloader/VBS.Agent.gc
[+] HVM:TrojanDropper/W64.Agent.bz
[+] Hacktool/ConnectWise
[+] Rootkit/W64.Agent.l
[+] Trojan/Agent.clo
[+] Trojan/BAT.Loader.i
[+] Trojan/BAT.Pwrsvc.bv
[+] Trojan/DDOS.ae
[+] Trojan/DLLHijack.x
[+] Trojan/DllHijack.x
[+] Trojan/FakeApp.aax
[+] Trojan/FakeApp.aay
[+] Trojan/FakeApp.aaz
[+] Trojan/FakeApp.aba
[+] Trojan/FakeApp.abc
[+] Trojan/FakeApp.abd
[+] Trojan/FakeApp.abe
[+] Trojan/FakeApp.abf
[+] Trojan/FakeApp.zi
[+] Trojan/HiJack.yj
[+] Trojan/JS.Obfuscated.da
[+] Trojan/KillAV.dc
[+] Trojan/Linux.Mirai.fq
[+] Trojan/Linux.Mirai.fv
[+] Trojan/Linux.Mirai.gc
[+] Trojan/Linux.Mirai.gd
[+] Trojan/Linux.Mirai.ge
[+] Trojan/Linux.Mirai.gf
[+] Trojan/Loader.mo
[+] Trojan/Loader.mp
[+] Trojan/MSIL.Injector.qg
[+] Trojan/MSIL.Obfuscated.jv
[+] Trojan/NSIS.Injector.f
[+] Trojan/Runner.fl
[+] Trojan/ShellLoader.aha
[+] Trojan/ShellLoader.ahb
[+] Trojan/ShellLoader.ahc
[+] Trojan/ShellcodeRunner.b
[+] Trojan/W64.Injector.bz
[+] Trojan/W64.Injector.ca
[+] TrojanDownloader/Agent.bln
[+] TrojanDownloader/Agent.blo
[+] TrojanDownloader/BAT.Agent.gb
[+] TrojanDownloader/Linux.Agent.dp
[+] TrojanDownloader/Linux.Mozi.c
[+] TrojanDownloader/Maloader.bn
[+] TrojanDropper/Agent.akf
[+] TrojanDropper/Agent.akg
[+] TrojanDropper/Agent.akh
[+] TrojanDropper/Agent.aki
[+] TrojanDropper/Agent.akj
[+] TrojanDropper/BAT.Agent.bm
[+] TrojanDropper/Maloader.m
[+] TrojanSpy/MSIL.ClipBanker.av
[+] TrojanSpy/Stealer.th
[+] TrojanSpy/W64.ClipBanker.e
[+] TrojanSpy/W64.PwStealer.d
[+] TrojanSpy/W64.Stealer.x
[+] Virus/MAYA.FuckVirus.a
[+] Worm/Autorun.ha
[+] Worm/Autorun.hb
[+] Worm/Phorpiex.o
```

</details>

<details>
<summary>
新增遥测定义: 47 | 移除遥测定义: 47
</summary>

```
[+] Backdoor/Lotok.ob!submit
[+] Backdoor/W64.Agent.l!submit
[+] Backdoor/W64.Agent.m!submit
[+] HEUR:Backdoor/MSIL.Bladabindi.bc!submit
[+] HEUR:Backdoor/MSIL.Bladabindi.bd!submit
[+] HEUR:Trojan/Injector.cp!submit
[+] HEUR:Trojan/JS.Agent.gr!submit
[+] HEUR:Trojan/KillWin.dj!submit
[+] HVM:Backdoor/Lotok.bx!submit
[+] HVM:Trojan/Injector.ah!submit
[+] HVM:Trojan/Injector.cn!submit
[+] HVM:Trojan/SelfDel.e!submit
[+] Ransom/LockFile.ri!submit
[+] Trojan/Agent.clp!submit
[+] Trojan/BAT.Loader.j!submit
[+] Trojan/FakeApp.aar!submit
[+] Trojan/FakeApp.abg!submit
[+] Trojan/FakeApp.abh!submit
[+] Trojan/FakeApp.abi!submit
[+] Trojan/Linux.Mirai.gg!submit
[+] Trojan/Linux.Mirai.gh!submit
[+] Trojan/Loader.mq!submit
[+] Trojan/Loader.mr!submit
[+] Trojan/Obfuscated.ns!submit
[+] Trojan/Python.DDos.h!submit
[+] Trojan/ShellLoader.ahd!submit
[+] Trojan/ShellLoader.ahe!submit
[+] TrojanDownloader/PS.Agent.fa!submit
[+] TrojanDownloader/PS.Agent.fb!submit
[+] TrojanDownloader/VBS.Agent.kb!submit
[+] TrojanDownloader/W64.Agent.cn!submit
[+] TrojanDropper/Agent.akk!submit
[+] TrojanDropper/Agent.akl!submit
[+] TrojanDropper/Agent.akm!submit
[+] TrojanDropper/Agent.akn!submit
[+] TrojanDropper/Agent.ako!submit
[+] TrojanDropper/MSIL.Agent.jx!submit
[+] TrojanDropper/Python.Agent.n!submit
[+] TrojanDropper/VBS.Agent.ef!submit
[+] TrojanDropper/W64.Agent.bz!submit
[+] TrojanSpy/Python.Rodico.a!submit
[+] VirTool/Obfuscator.aw!submit
[+] VirTool/Obfuscator.ay!submit
[+] VirTool/Obfuscator.ba!submit
[+] VirTool/Obfuscator.bb!submit
[+] VirTool/Obfuscator.be!submit
[+] VirTool/Obfuscator.db!submit
[-] Backdoor/Agent.ra!submit
[-] Backdoor/Linux.Gafgyt.by!submit
[-] Backdoor/Lotok.nz!submit
[-] Backdoor/W64.Agent.k!submit
[-] Backdoor/Xkcp.a!submit
[-] HEUR:Backdoor/Linux.Mirai.ku!submit
[-] HEUR:Trojan/BAT.Loader.k!submit
[-] HEUR:Trojan/Injector.co!submit
[-] HEUR:TrojanDownloader/Agent.blo!submit
[-] HVM:Trojan/Hook.a!submit
[-] Rootkit/W64.Agent.l!submit
[-] Trojan/BAT.Loader.i!submit
[-] Trojan/FakeApp.aax!submit
[-] Trojan/FakeApp.aay!submit
[-] Trojan/FakeApp.aaz!submit
[-] Trojan/FakeApp.aba!submit
[-] Trojan/FakeApp.abc!submit
[-] Trojan/FakeApp.abd!submit
[-] Trojan/FakeApp.abe!submit
[-] Trojan/FakeApp.zi!submit
[-] Trojan/Linux.Mirai.fq!submit
[-] Trojan/Linux.Mirai.fv!submit
[-] Trojan/Linux.Mirai.gc!submit
[-] Trojan/Linux.Mirai.gd!submit
[-] Trojan/Linux.Mirai.ge!submit
[-] Trojan/Linux.Mirai.gf!submit
[-] Trojan/Loader.mo!submit
[-] Trojan/MSIL.Injector.qg!submit
[-] Trojan/MSIL.Obfuscated.jv!submit
[-] Trojan/NSIS.Injector.f!submit
[-] Trojan/Runner.fl!submit
[-] Trojan/ShellLoader.aha!submit
[-] Trojan/ShellLoader.ahb!submit
[-] Trojan/ShellcodeRunner.b!submit
[-] Trojan/W64.Injector.bz!submit
[-] TrojanDownloader/Agent.bln!submit
[-] TrojanDownloader/Linux.Agent.dp!submit
[-] TrojanDownloader/Linux.Mozi.c!submit
[-] TrojanDropper/Agent.akf!submit
[-] TrojanDropper/Agent.akg!submit
[-] TrojanSpy/MSIL.ClipBanker.av!submit
[-] TrojanSpy/Stealer.th!submit
[-] TrojanSpy/W64.ClipBanker.e!submit
[-] TrojanSpy/W64.PwStealer.d!submit
[-] TrojanSpy/W64.Stealer.x!submit
[-] Virus/MAYA.FuckVirus.a!submit
[-] Worm/Autorun.ha!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1767782775.crithash.txt))

<details>
<summary>
新增正式定义: 18
</summary>

```
[+] Backdoor/W32.Lotok.ae!crit
[+] Backdoor/W64.Havoc.a!crit
[+] Ransom/W32.BTCware.i!crit
[+] Ransom/W64.Filecoder.b!crit
[+] Trojan/Android.Harly.a!crit
[+] Trojan/Android.Winge.a!crit
[+] Trojan/MSIL.Agent.aaj!crit
[+] Trojan/MSIL.Androm.a!crit
[+] Trojan/OSX.TrojanDownloader.a!crit
[+] Trojan/SCR.FakeApp.b!crit
[+] Trojan/SCR.Loader.a!crit
[+] Trojan/SCR.Loader.mp!crit
[+] Trojan/W32.HiJack.w!crit
[+] Trojan/W32.Loader.mp!crit
[+] TrojanDropper/W32.Agent.l!crit
[+] TrojanSpy/SCR.Stealer.b!crit
[+] TrojanSpy/SCR.Stealer.c!crit
[+] TrojanSpy/W64.ClipBanker.a!crit
```

</details>

<details>
<summary>
新增遥测定义: 19 | 移除遥测定义: 14
</summary>

```
[+] Adware/Android.PornTool.g!crit!submit
[+] Adware/Android.PornTool.h!crit!submit
[+] Adware/W32.Agent.da!crit!submit
[+] Backdoor/Linux.Mirai.b!crit!submit
[+] Backdoor/Linux.ReverseShell.a!crit!submit
[+] Backdoor/W64.Agent.g!crit!submit
[+] Backdoor/W64.SparkRAT.a!crit!submit
[+] Exploit/W32.CVE-2025-62215.a!crit!submit
[+] HEUR:Trojan/W32.HiJack.a!crit!submit
[+] HackTool/Linux.CoinMiner.a!crit!submit
[+] Trojan/HTML.Phishing.oq!crit!submit
[+] Trojan/MSIL.Obfuscated.am!crit!submit
[+] Trojan/W32.Obfuscated.nt!crit!submit
[+] TrojanDownloader/MSIL.Maloader.j!crit!submit
[+] TrojanDownloader/VBS.Obfuscated.c!crit!submit
[+] TrojanSpy/Linux.Stealer.b!crit!submit
[+] TrojanSpy/W32.Rodico.a!crit!submit
[+] TrojanSpy/W64.ClipBanker.b!crit!submit
[+] Virus/MAYA.FuckVirus.b!crit!submit
[-] Backdoor/W32.Lotok.ae!crit!submit
[-] Backdoor/W64.Havoc.a!crit!submit
[-] Ransom/W32.BTCware.i!crit!submit
[-] Trojan/Android.Harly.a!crit!submit
[-] Trojan/Android.Winge.a!crit!submit
[-] Trojan/MSIL.Agent.aaj!crit!submit
[-] Trojan/SCR.FakeApp.a!crit!submit
[-] Trojan/SCR.Loader.mp!crit!submit
[-] Trojan/W32.HiJack.w!crit!submit
[-] Trojan/W32.Loader.mp!crit!submit
[-] Trojan/W32.ShellLoader.j!crit!submit
[-] TrojanSpy/SCR.Stealer.b!crit!submit
[-] TrojanSpy/SCR.Stealer.c!crit!submit
[-] TrojanSpy/W64.ClipBanker.a!crit!submit
```

</details>

#### 行为特征项变更 ([behav.txt](data/1767782775.behav.txt))

<details>
<summary>
新增: 2 | 移除: 1
</summary>

```
[+] Software:GM/NN.A#NN加速器!submit
[+] Software:OS/Gooxion.AA#固信终端
[-] Software:OS/Gooxion.AA#固信终端安全!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1767782775.troj.txt))

新增: 50

</details>

<details>
<summary><b>1767697383</b> - 2026-01-06 11:03:03 UTC</summary>

#### 黑名单哈希变更 ([troj.txt](data/1767697383.troj.txt))

新增: 125 | 移除: 1

</details>

<details>
<summary><b>1767610360</b> - 2026-01-05 10:52:40 UTC</summary>

#### 特征项变更 ([pset.txt](data/1767610360.pset.txt))

<details>
<summary>
新增正式定义: 34 | 移除正式定义: 6
</summary>

```
[+] Backdoor/Linux.Mirai.kv
[+] Backdoor/Lotok.ny
[+] Backdoor/MSIL.AsyncRAT.ab
[+] HEUR:Ransom/Filecoder.ek
[+] HVM:Backdoor/Lotok.cg
[+] HVM:Backdoor/Lotok.ch
[+] HVM:Trojan/MalBehav.gen!AM
[+] HVM:TrojanDownloader/Small.dq
[+] HackTool/ConnectWiseControl.h
[+] Trojan/BAT.Shutdown.e
[+] Trojan/FakeApp.aav
[+] Trojan/FakeApp.aaw
[+] Trojan/Injector.clg
[+] Trojan/KillDisk.eb
[+] Trojan/Loader.mn
[+] Trojan/MSIL.Obfuscated.jt
[+] Trojan/MSIL.Obfuscated.ju
[+] Trojan/ShellLoader.agx
[+] Trojan/ShellLoader.agy
[+] Trojan/ShellLoader.agz
[+] Trojan/W64.Injector.bx
[+] Trojan/W64.Injector.by
[+] Trojan/W64.Rhadamanthys.a
[+] TrojanDownloader/JS.Agent.ie
[+] TrojanDownloader/Maloader.bm
[+] TrojanDropper/Agent.ajt
[+] TrojanDropper/Agent.akc
[+] TrojanDropper/Agent.akd
[+] TrojanDropper/Agent.ake
[+] TrojanDropper/JS.Agent.cc
[+] TrojanDropper/LNK.Agent.q
[+] TrojanDropper/PS.Agent.y
[+] TrojanDropper/W64.Agent.bx
[+] TrojanSpy/Keylogger.fd
[-] HVM:Backdoor/Lotok.bx
[-] HVM:Backdoor/Lotok.cd
[-] HVM:Backdoor/Lotok.ce
[-] HVM:Backdoor/Lotok.cf
[-] Trojan/FakeApp.aar
[-] Trojan/FakeApp.zi
```

</details>

<details>
<summary>
新增遥测定义: 41 | 移除遥测定义: 34
</summary>

```
[+] Backdoor/Agent.ra!submit
[+] Backdoor/Lotok.nz!submit
[+] Backdoor/W64.AdaptixC2.b!submit
[+] Backdoor/W64.Agent.k!submit
[+] Backdoor/Xkcp.a!submit
[+] HEUR:Trojan/Injector.co!submit
[+] HEUR:TrojanDownloader/Agent.blo!submit
[+] Rootkit/StartPage.ad!submit
[+] Rootkit/W64.Agent.l!submit
[+] Trojan/BAT.Loader.i!submit
[+] Trojan/FakeApp.aay!submit
[+] Trojan/FakeApp.aaz!submit
[+] Trojan/FakeApp.aba!submit
[+] Trojan/FakeApp.abb!submit
[+] Trojan/FakeApp.abc!submit
[+] Trojan/FakeApp.abd!submit
[+] Trojan/FakeApp.abe!submit
[+] Trojan/FakeApp.zi!submit
[+] Trojan/Linux.Mirai.gd!submit
[+] Trojan/Linux.Mirai.ge!submit
[+] Trojan/Linux.Mirai.gf!submit
[+] Trojan/Loader.mo!submit
[+] Trojan/MSIL.Injector.qg!submit
[+] Trojan/MSIL.Obfuscated.jv!submit
[+] Trojan/NSIS.Injector.f!submit
[+] Trojan/Runner.fl!submit
[+] Trojan/ShellLoader.aha!submit
[+] Trojan/ShellLoader.ahb!submit
[+] Trojan/ShellcodeRunner.b!submit
[+] Trojan/StartPage.lj!submit
[+] Trojan/W64.Injector.bz!submit
[+] TrojanDownloader/Agent.bln!submit
[+] TrojanDropper/Agent.akf!submit
[+] TrojanDropper/Agent.akg!submit
[+] TrojanSpy/MSIL.ClipBanker.av!submit
[+] TrojanSpy/Stealer.th!submit
[+] TrojanSpy/W64.ClipBanker.e!submit
[+] TrojanSpy/W64.PwStealer.d!submit
[+] TrojanSpy/W64.Stealer.x!submit
[+] Virus/MAYA.FuckVirus.a!submit
[+] Worm/Autorun.ha!submit
[-] Backdoor/Linux.Mirai.kv!submit
[-] Backdoor/Lotok.ny!submit
[-] Backdoor/MSIL.AsyncRAT.ab!submit
[-] HEUR:Ransom/Filecoder.ek!submit
[-] HEUR:Trojan/FakeApp.doi!submit
[-] HVM:Backdoor/Lotok.cg!submit
[-] HVM:Backdoor/Lotok.ch!submit
[-] HackTool/ConnectWiseControl.h!submit
[-] Rootkit/Hook.at!submit
[-] Trojan/BAT.Shutdown.e!submit
[-] Trojan/FakeApp.aav!submit
[-] Trojan/FakeApp.aaw!submit
[-] Trojan/Injector.clg!submit
[-] Trojan/KillDisk.eb!submit
[-] Trojan/Loader.mn!submit
[-] Trojan/MSIL.Obfuscated.jt!submit
[-] Trojan/MSIL.Obfuscated.ju!submit
[-] Trojan/ShellLoader.agx!submit
[-] Trojan/ShellLoader.agy!submit
[-] Trojan/ShellLoader.agz!submit
[-] Trojan/W64.Injector.bx!submit
[-] Trojan/W64.Injector.by!submit
[-] Trojan/W64.Rhadamanthys.a!submit
[-] TrojanDownloader/JS.Agent.ie!submit
[-] TrojanDownloader/Maloader.bm!submit
[-] TrojanDropper/Agent.ajt!submit
[-] TrojanDropper/Agent.akc!submit
[-] TrojanDropper/Agent.akd!submit
[-] TrojanDropper/Agent.ake!submit
[-] TrojanDropper/JS.Agent.cc!submit
[-] TrojanDropper/LNK.Agent.q!submit
[-] TrojanDropper/PS.Agent.y!submit
[-] TrojanDropper/W64.Agent.bx!submit
[-] TrojanSpy/Keylogger.fd!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1767610360.crithash.txt))

<details>
<summary>
新增正式定义: 11
</summary>

```
[+] Trojan/BAT.Runner.bn!crit
[+] Trojan/MSIL.Obfuscated.al!crit
[+] Trojan/SCR.KillLinux.b!crit
[+] Trojan/SCR.ShellCode.d!crit
[+] Trojan/W32.FakeApp.d!crit
[+] Trojan/W64.Loader.aj!crit
[+] Trojan/W64.Loader.ak!crit
[+] Trojan/W64.ShellLoader.k!crit
[+] TrojanDownloader/PS.Agent.bn!crit
[+] TrojanDownloader/XML.Agent.a!crit
[+] TrojanDropper/W64.Maloader.m!crit
```

</details>

<details>
<summary>
新增遥测定义: 13 | 移除遥测定义: 14
</summary>

```
[+] Backdoor/W32.Lotok.ae!crit!submit
[+] Backdoor/W64.Havoc.a!crit!submit
[+] Ransom/W32.BTCware.i!crit!submit
[+] Trojan/Android.Harly.a!crit!submit
[+] Trojan/Android.Winge.a!crit!submit
[+] Trojan/HTML.Phishing.op!crit!submit
[+] Trojan/MSIL.Agent.aaj!crit!submit
[+] Trojan/SCR.FakeApp.a!crit!submit
[+] Trojan/SCR.Loader.mp!crit!submit
[+] Trojan/W32.HiJack.w!crit!submit
[+] Trojan/W32.Loader.mp!crit!submit
[+] Trojan/W32.ShellLoader.j!crit!submit
[+] TrojanSpy/SCR.Stealer.c!crit!submit
[-] Trojan/BAT.Runner.bn!crit!submit
[-] Trojan/MSIL.Obfuscated.al!crit!submit
[-] Trojan/SCR.KillLinux.b!crit!submit
[-] Trojan/SCR.ShellCode.d!crit!submit
[-] Trojan/W32.Agent.gj!crit!submit
[-] Trojan/W32.Agent.x!crit!submit
[-] Trojan/W32.FakeApp.d!crit!submit
[-] Trojan/W32.ShellLoader.i!crit!submit
[-] Trojan/W64.Loader.aj!crit!submit
[-] Trojan/W64.Loader.ak!crit!submit
[-] Trojan/W64.ShellLoader.jaaa!crit!submit
[-] TrojanDownloader/PS.Agent.bn!crit!submit
[-] TrojanDownloader/XML.Agent.a!crit!submit
[-] TrojanDropper/W64.Maloader.m!crit!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1767610360.troj.txt))

新增: 78 | 移除: 2

</details>

<details>
<summary><b>1767527465</b> - 2026-01-04 11:51:05 UTC</summary>

#### 特征项变更 ([pset.txt](data/1767527465.pset.txt))

<details>
<summary>
新增正式定义: 34 | 移除正式定义: 1
</summary>

```
[+] Adware/Android.PornTool.m
[+] Backdoor/Linux.Gafgyt.bz
[+] Backdoor/Linux.Mirai.ku
[+] Backdoor/W64.AdaptixC2.a
[+] HEUR:Trojan/BAT.Loader.i
[+] HEUR:Trojan/FakeApp.aam
[+] Joke/BAT.ForkBomb.d
[+] Ransom/Filecoder.ei
[+] Trojan/Agent.cln
[+] Trojan/FakeApp.aam
[+] Trojan/FakeApp.aau
[+] Trojan/HTML.Injector.n
[+] Trojan/Injector.ckx
[+] Trojan/Injector.cle
[+] Trojan/Injector.clf
[+] Trojan/KillMBR.cl
[+] Trojan/Loader.mc
[+] Trojan/MSIL.Obfuscated.js
[+] Trojan/MSIL.Runner.l
[+] Trojan/MSIL.Runner.m
[+] Trojan/ReverseShell.x
[+] Trojan/ShellLoader.agw
[+] Trojan/W64.Injector.bw
[+] TrojanDownloader/Agent.blm
[+] TrojanDownloader/JS.Agent.id
[+] TrojanDownloader/Maloader.bl
[+] TrojanDropper/Agent.ajx
[+] TrojanDropper/Agent.ajy
[+] TrojanDropper/Agent.ajz
[+] TrojanDropper/Agent.aka
[+] TrojanDropper/BAT.Maloader.e
[+] TrojanDropper/W64.Agent.bw
[+] TrojanSpy/KeyLogger.fc
[+] TrojanSpy/MSIL.Stealer.kt
[-] TrojanDropper/Agent.ajt
```

</details>

<details>
<summary>
新增遥测定义: 38 | 移除遥测定义: 35
</summary>

```
[+] Backdoor/Linux.Mirai.kv!submit
[+] Backdoor/Lotok.ny!submit
[+] Backdoor/MSIL.AsyncRAT.ab!submit
[+] HEUR:Ransom/Filecoder.ek!submit
[+] HVM:Backdoor/Lotok.cg!submit
[+] HVM:Backdoor/Lotok.ch!submit
[+] HVM:Trojan/MalBehav.h!submit
[+] HVM:TrojanDownloader/Small.dq!submit
[+] HackTool/ConnectWiseControl.h!submit
[+] Ransom/LockFile.qw!submit
[+] Rootkit/Hook.at!submit
[+] Trojan/BAT.Shutdown.e!submit
[+] Trojan/FakeApp.aav!submit
[+] Trojan/FakeApp.aaw!submit
[+] Trojan/FakeApp.aax!submit
[+] Trojan/Injector.clg!submit
[+] Trojan/KillDisk.eb!submit
[+] Trojan/Loader.mn!submit
[+] Trojan/MSIL.Obfuscated.jt!submit
[+] Trojan/MSIL.Obfuscated.ju!submit
[+] Trojan/ShellLoader.agx!submit
[+] Trojan/ShellLoader.agy!submit
[+] Trojan/ShellLoader.agz!submit
[+] Trojan/W64.Injector.bx!submit
[+] Trojan/W64.Injector.by!submit
[+] Trojan/W64.Rhadamanthys.a!submit
[+] TrojanDownloader/JS.Agent.ie!submit
[+] TrojanDownloader/Maloader.bm!submit
[+] TrojanDropper/Agent.ajt!submit
[+] TrojanDropper/Agent.akb!submit
[+] TrojanDropper/Agent.akc!submit
[+] TrojanDropper/Agent.akd!submit
[+] TrojanDropper/Agent.ake!submit
[+] TrojanDropper/JS.Agent.cc!submit
[+] TrojanDropper/LNK.Agent.q!submit
[+] TrojanDropper/PS.Agent.y!submit
[+] TrojanDropper/W64.Agent.bx!submit
[+] TrojanSpy/Keylogger.fd!submit
[-] Adware/Android.PornTool.m!submit
[-] Backdoor/Linux.Gafgyt.bz!submit
[-] Backdoor/Linux.Mirai.ku!submit
[-] Backdoor/W64.AdaptixC2.a!submit
[-] HEUR:Trojan/BAT.Loader.i!submit
[-] HEUR:Trojan/FakeApp.aam!submit
[-] Joke/BAT.ForkBomb.d!submit
[-] Ransom/Filecoder.ei!submit
[-] Trojan/Agent.cln!submit
[-] Trojan/FakeApp.aam!submit
[-] Trojan/FakeApp.aau!submit
[-] Trojan/HTML.Injector.n!submit
[-] Trojan/Injector.ckx!submit
[-] Trojan/Injector.cle!submit
[-] Trojan/Injector.clf!submit
[-] Trojan/KillMBR.cl!submit
[-] Trojan/Loader.mc!submit
[-] Trojan/MSIL.Obfuscated.js!submit
[-] Trojan/MSIL.Runner.l!submit
[-] Trojan/MSIL.Runner.m!submit
[-] Trojan/ReverseShell.x!submit
[-] Trojan/ShellLoader.agv!submit
[-] Trojan/ShellLoader.agw!submit
[-] Trojan/W64.Injector.bw!submit
[-] TrojanDownloader/Agent.blm!submit
[-] TrojanDownloader/JS.Agent.id!submit
[-] TrojanDownloader/Maloader.bl!submit
[-] TrojanDropper/Agent.ajx!submit
[-] TrojanDropper/Agent.ajy!submit
[-] TrojanDropper/Agent.ajz!submit
[-] TrojanDropper/Agent.aka!submit
[-] TrojanDropper/BAT.Maloader.e!submit
[-] TrojanDropper/W64.Agent.bw!submit
[-] TrojanSpy/KeyLogger.fc!submit
[-] TrojanSpy/MSIL.Stealer.kt!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1767527465.crithash.txt))

<details>
<summary>
新增正式定义: 14
</summary>

```
[+] Adware/Android.PornTool.e!crit
[+] Adware/Android.PornTool.f!crit
[+] Backdoor/MSIL.Bladabindi.bc!crit
[+] Trojan/MSIL.ClipBanker.l!crit
[+] Trojan/MSIL.Obfuscated.js!crit
[+] Trojan/Python.Obfuscated.i!crit
[+] Trojan/SCR.ShellCode.c
[+] Trojan/W32.HiJack.v!crit
[+] Trojan/W32.RigelMiner.a!crit
[+] Trojan/W32.RigelMiner.b!crit
[+] TrojanDownloader/Linux.Agent.d!crit
[+] TrojanDownloader/W32.ShellLoader.a!crit
[+] TrojanDownloader/W64.Agent.b!crit
[+] TrojanDownloader/W64.ShellcodeRunner.a!crit
```

</details>

<details>
<summary>
新增遥测定义: 41 | 移除遥测定义: 15
</summary>

```
[+] Backdoor/Linux.Mirai.a!crit!submit
[+] Backdoor/MSIL.ReverseShell.a!crit!submit
[+] Backdoor/MSIL.ReverseShell.b!crit!submit
[+] Backdoor/PHP.WebShell.g!crit!submit
[+] Backdoor/PHP.WebShell.h!crit!submit
[+] Backdoor/PHP.WebShell.i!crit!submit
[+] Backdoor/PHP.WebShell.j!crit!submit
[+] Backdoor/PHP.WebShell.k!crit!submit
[+] Backdoor/PHP.WebShell.l!crit!submit
[+] Backdoor/PHP.WebShell.m!crit!submit
[+] Backdoor/PHP.WebShell.n!crit!submit
[+] Backdoor/PHP.WebShell.o!crit!submit
[+] HEUR:Trojan/W32.Obfuscated.a!crit!submit
[+] Joke/BAT.KeyJammer.a!crit!submit
[+] Joke/BAT.KillWin.a!crit!submit
[+] Ransom/MSIL.LockFile.a!crit!submit
[+] Ransom/MSIL.LockScreen.a!crit!submit
[+] Trojan/BAT.Runner.bn!crit!submit
[+] Trojan/MSIL.Agent.a!crit!submit
[+] Trojan/MSIL.Injector.a!crit!submit
[+] Trojan/MSIL.Injector.b!crit!submit
[+] Trojan/MSIL.Obfuscated.al!crit!submit
[+] Trojan/SCR.KillLinux.b!crit!submit
[+] Trojan/SCR.ShellCode.d!crit!submit
[+] Trojan/W32.Agent.gj!crit!submit
[+] Trojan/W32.Agent.x!crit!submit
[+] Trojan/W32.FakeApp.d!crit!submit
[+] Trojan/W32.ShellLoader.i!crit!submit
[+] Trojan/W64.Loader.aj!crit!submit
[+] Trojan/W64.Loader.ak!crit!submit
[+] Trojan/W64.ShellLoader.jaaa!crit!submit
[+] TrojanDownloader/PS.Agent.bn!crit!submit
[+] TrojanDownloader/XML.Agent.a!crit!submit
[+] TrojanDropper/MSIL.ShellLoader.b!crit!submit
[+] TrojanDropper/W64.Maloader.m!crit!submit
[+] TrojanSpy/MSIL.Keylogger.a!crit!submit
[+] TrojanSpy/MSIL.Stealer.ccu!crit!submit
[+] TrojanSpy/MSIL.Stealer.ccv!crit!submit
[+] TrojanSpy/MSIL.Stealer.ccw!crit!submit
[+] TrojanSpy/SCR.Stealer.b!crit!submit
[+] TrojanSpy/W64.ClipBanker.a!crit!submit
[-] Adware/Android.PornTool.e!crit!submit
[-] Adware/Android.PornTool.f!crit!submit
[-] Backdoor/MSIL.Bladabindi.bc!crit!submit
[-] Backdoor/W32.Lotok.r!crit!submit
[-] Trojan/MSIL.ClipBanker.l!crit!submit
[-] Trojan/MSIL.Obfuscated.js!crit!submit
[-] Trojan/Python.Obfuscated.i!crit!submit
[-] Trojan/SCR.ShellCode.c!crit!submit
[-] Trojan/W32.HiJack.v!crit!submit
[-] Trojan/W32.RigelMiner.a!crit!submit
[-] Trojan/W32.RigelMiner.b!crit!submit
[-] TrojanDownloader/Linux.Agent.d!crit!submit
[-] TrojanDownloader/W32.ShellLoader.a!crit!submit
[-] TrojanDownloader/W64.Agent.b!crit!submit
[-] TrojanDownloader/W64.ShellcodeRunner.a!crit!submit
```

</details>

#### 行为特征项变更 ([behav.txt](data/1767527465.behav.txt))

<details>
<summary>
新增: 2 | 移除: 1
</summary>

```
[+] Backdoor/Lotok.P
[+] TrojanDropper/MalSetup.OB!submit
[-] Backdoor/Lotok.ZAB!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1767527465.troj.txt))

新增: 20

</details>

<details>
<summary><b>1767443553</b> - 2026-01-03 12:32:33 UTC</summary>

#### 黑名单哈希变更 ([troj.txt](data/1767443553.troj.txt))

新增: 41

</details>

<details>
<summary><b>1767352866</b> - 2026-01-02 11:21:06 UTC</summary>

#### 黑名单哈希变更 ([troj.txt](data/1767352866.troj.txt))

新增: 61 | 移除: 1

</details>

<details>
<summary><b>1767267452</b> - 2026-01-01 11:37:32 UTC</summary>

#### 黑名单哈希变更 ([troj.txt](data/1767267452.troj.txt))

新增: 86 | 移除: 2

#### 白名单哈希变更 ([hwl.txt](data/1767267452.hwl.txt))

新增: 4

</details>

<details>
<summary><b>1767177959</b> - 2025-12-31 10:45:59 UTC</summary>

#### 特征项变更 ([pset.txt](data/1767177959.pset.txt))

<details>
<summary>
新增正式定义: 31
</summary>

```
[+] Backdoor/Lotok.nq
[+] HEUR:Trojan/ShellLoader.agv
[+] HVM:Backdoor/Lotok.cf
[+] Rootkit/MiniFilter.b
[+] Trojan/BAT.KillWin.bd
[+] Trojan/BAT.Runner.bm
[+] Trojan/Bladabindi.e
[+] Trojan/CoinMiner.la
[+] Trojan/FakeApp.aap
[+] Trojan/FakeApp.aaq
[+] Trojan/FakeApp.aar
[+] Trojan/FakeApp.aas
[+] Trojan/FakeApp.aat
[+] Trojan/Injector.cld
[+] Trojan/MSIL.Obfuscated.jr
[+] Trojan/Python.CoinMiner.j
[+] Trojan/Python.Popups.b
[+] Trojan/Runner.fk
[+] Trojan/ShellLoader.agv
[+] Trojan/VBS.Agent.em
[+] Trojan/W64.Loader.ae
[+] Trojan/W64.Loader.af
[+] Trojan/W64.Loader.ag
[+] Trojan/W64.Loader.ah
[+] Trojan/W64.Loader.ai
[+] Trojan/W64.ReverseShell.a
[+] TrojanDownloader/JS.Agent.ic
[+] TrojanDownloader/MSIL.Agent.aji
[+] TrojanDownloader/PS.Agent.ey
[+] TrojanDownloader/PS.Agent.ez
[+] TrojanDropper/Agent.ajw
```

</details>

<details>
<summary>
新增遥测定义: 30 | 移除遥测定义: 30
</summary>

```
[+] Adware/Android.PornTool.m!submit
[+] Backdoor/Linux.Gafgyt.bz!submit
[+] Backdoor/Linux.Mirai.ku!submit
[+] HEUR:Trojan/BAT.Loader.k!submit
[+] HVM:Trojan/Injector.bo!submit
[+] Ransom/Filecoder.ei!submit
[+] Trojan/Agent.cln!submit
[+] Trojan/FakeApp.aam!submit
[+] Trojan/FakeApp.aau!submit
[+] Trojan/Injector.cle!submit
[+] Trojan/Injector.clf!submit
[+] Trojan/KillMBR.cl!submit
[+] Trojan/Linux.Mirai.gc!submit
[+] Trojan/MSIL.Obfuscated.js!submit
[+] Trojan/MSIL.Runner.l!submit
[+] Trojan/MSIL.Runner.m!submit
[+] Trojan/ReverseShell.x!submit
[+] Trojan/ShellLoader.agw!submit
[+] Trojan/W64.Injector.bw!submit
[+] TrojanDownloader/Agent.blm!submit
[+] TrojanDownloader/JS.Agent.id!submit
[+] TrojanDownloader/Maloader.bl!submit
[+] TrojanDropper/Agent.ajx!submit
[+] TrojanDropper/Agent.ajy!submit
[+] TrojanDropper/Agent.ajz!submit
[+] TrojanDropper/Agent.aka!submit
[+] TrojanDropper/BAT.Maloader.e!submit
[+] TrojanDropper/W64.Agent.bw!submit
[+] TrojanSpy/KeyLogger.fc!submit
[+] TrojanSpy/MSIL.Stealer.kt!submit
[-] Backdoor/Lotok.nq!submit
[-] HEUR:Trojan/ShellLoader.agv!submit
[-] HVM:Backdoor/Lotok.cf!submit
[-] Rootkit/MiniFilter.b!submit
[-] Trojan/BAT.KillWin.bd!submit
[-] Trojan/BAT.Runner.bm!submit
[-] Trojan/Bladabindi.e!submit
[-] Trojan/CoinMiner.la!submit
[-] Trojan/FakeApp.aap!submit
[-] Trojan/FakeApp.aaq!submit
[-] Trojan/FakeApp.aar!submit
[-] Trojan/FakeApp.aas!submit
[-] Trojan/FakeApp.aat!submit
[-] Trojan/Injector.cld!submit
[-] Trojan/MSIL.Obfuscated.jr!submit
[-] Trojan/Python.CoinMiner.j!submit
[-] Trojan/Python.Popups.b!submit
[-] Trojan/Runner.fk!submit
[-] Trojan/VBS.Agent.em!submit
[-] Trojan/W64.Loader.ae!submit
[-] Trojan/W64.Loader.af!submit
[-] Trojan/W64.Loader.ag!submit
[-] Trojan/W64.Loader.ah!submit
[-] Trojan/W64.Loader.ai!submit
[-] Trojan/W64.ReverseShell.a!submit
[-] TrojanDownloader/JS.Agent.ic!submit
[-] TrojanDownloader/MSIL.Agent.aji!submit
[-] TrojanDownloader/PS.Agent.ey!submit
[-] TrojanDownloader/PS.Agent.ez!submit
[-] TrojanDropper/Agent.ajw!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1767177959.crithash.txt))

<details>
<summary>
新增正式定义: 5
</summary>

```
[+] Trojan/SCR.ShellCode.b!crit
[+] Trojan/VBS.Loader.e
[+] Trojan/W32.HiJack.u!crit
[+] Trojan/W64.Agent.gj!crit
[+] TrojanSpy/SCR.Stealer.a!crit
```

</details>

<details>
<summary>
新增遥测定义: 16 | 移除遥测定义: 8
</summary>

```
[+] Adware/Android.PornTool.e!crit!submit
[+] Adware/Android.PornTool.f!crit!submit
[+] Backdoor/MSIL.Bladabindi.bc!crit!submit
[+] Backdoor/W32.Lotok.r!crit!submit
[+] Trojan/MSIL.ClipBanker.l!crit!submit
[+] Trojan/MSIL.Obfuscated.js!crit!submit
[+] Trojan/Python.Obfuscated.i!crit!submit
[+] Trojan/SCR.ShellCode.c!crit!submit
[+] Trojan/SCR.ShellLoader.a!crit!submit
[+] Trojan/W32.HiJack.v!crit!submit
[+] Trojan/W32.RigelMiner.a!crit!submit
[+] Trojan/W32.RigelMiner.b!crit!submit
[+] TrojanDownloader/Linux.Agent.d!crit!submit
[+] TrojanDownloader/W32.ShellLoader.a!crit!submit
[+] TrojanDownloader/W64.Agent.b!crit!submit
[+] TrojanDownloader/W64.ShellcodeRunner.a!crit!submit
[-] Trojan/SCR.Loader.a!crit!submit
[-] Trojan/SCR.ShellCode.b!crit!submit
[-] Trojan/W32.Agent.w!crit!submit
[-] Trojan/W32.HiJack.u!crit!submit
[-] Trojan/W64.Agent.gj!crit!submit
[-] Trojan/W64.ShellLoader.j!crit!submit
[-] TrojanDownloader/W32.Maloader.bl!crit!submit
[-] TrojanSpy/SCR.Stealer.a!crit!submit
```

</details>

#### 行为特征项变更 ([behav.txt](data/1767177959.behav.txt))

<details>
<summary>
新增: 4 | 移除: 3
</summary>

```
[+] ADV:Ransom/Genalocker.ZDA!submit
[+] Backdoor/Lotok.QDA
[+] Backdoor/Lotok.QDB
[+] TrojanDropper/MalSetup.P
[-] ADV:Ransom/Genalocker.ZCA!submit
[-] Backdoor/Lotok.QDA!submit
[-] Backdoor/Lotok.QDB!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1767177959.troj.txt))

新增: 30

</details>

<details>
<summary><b>1767093364</b> - 2025-12-30 11:16:04 UTC</summary>

#### 特征项变更 ([pset.txt](data/1767093364.pset.txt))

<details>
<summary>
新增正式定义: 56
</summary>

```
[+] Backdoor/Agent.nf
[+] Backdoor/Agent.od
[+] Backdoor/JS.Webshell.l
[+] Backdoor/Lotok.nw
[+] Backdoor/Lotok.nx
[+] Backdoor/W64.Agent.i
[+] HEUR:Trojan/Agent.clm
[+] HEUR:Trojan/BAT.KillWin.bc
[+] HEUR:Trojan/FakeApp.at
[+] HEUR:Trojan/KillWin.e
[+] HVM:Backdoor/Lotok.cd
[+] HVM:Backdoor/Lotok.ce
[+] HVM:Trojan/ShellLoader.ci
[+] HackTool/Python.RemoteExec.a
[+] Hacktool/CoinMiner
[+] Rootkit/Inject.b
[+] Trojan/Agent.clm
[+] Trojan/BAT.Agent.gp
[+] Trojan/BAT.Injector.d
[+] Trojan/BAT.Injector.e
[+] Trojan/BAT.KillWin.ba
[+] Trojan/BAT.Loader.h
[+] Trojan/FakeApp.aal
[+] Trojan/FakeApp.aan
[+] Trojan/FakeApp.aao
[+] Trojan/JS.Agent.gp
[+] Trojan/JS.Agent.gq
[+] Trojan/JS.Loader.d
[+] Trojan/KillAV.db
[+] Trojan/Linux.CoinMiner.dt
[+] Trojan/Linux.CoinMiner.du
[+] Trojan/Linux.CoinMiner.dv
[+] Trojan/Linux.DDoS.be
[+] Trojan/Linux.Mirai.fz
[+] Trojan/Linux.Mirai.ga
[+] Trojan/Linux.Mirai.gb
[+] Trojan/Loader.mm
[+] Trojan/MSIL.Injector.qf
[+] Trojan/MSIL.Obfuscated.jq
[+] Trojan/Python.KillDisk.e
[+] Trojan/ShellLoader.agr
[+] Trojan/ShellLoader.ags
[+] Trojan/ShellLoader.agt
[+] Trojan/ShellLoader.agu
[+] Trojan/W64.Loader.ab
[+] Trojan/W64.Loader.ac
[+] Trojan/W64.Loader.ad
[+] Trojan/W64.Merlin.a
[+] TrojanDownloader/JS.Agent.ib
[+] TrojanDownloader/Linux.Hajime.b
[+] TrojanDownloader/PS.Agent.ex
[+] TrojanDownloader/Rugmi.ab
[+] TrojanDropper/Agent.ajt
[+] TrojanDropper/Agent.aju
[+] TrojanDropper/Agent.ajv
[+] TrojanSpy/MSIL.Stealer.ks
```

</details>

<details>
<summary>
新增遥测定义: 35 | 移除遥测定义: 55
</summary>

```
[+] Backdoor/Linux.Gafgyt.by!submit
[+] Backdoor/Lotok.nq!submit
[+] Backdoor/W64.AdaptixC2.a!submit
[+] HEUR:Backdoor/Linux.Mirai.ku!submit
[+] HEUR:Trojan/BAT.Loader.j!submit
[+] HEUR:Trojan/FakeApp.aam!submit
[+] HEUR:Trojan/ShellLoader.agv!submit
[+] HVM:Backdoor/Lotok.cf!submit
[+] Rootkit/MiniFilter.b!submit
[+] Trojan/BAT.KillWin.bd!submit
[+] Trojan/BAT.Runner.bm!submit
[+] Trojan/Bladabindi.e!submit
[+] Trojan/FakeApp.aap!submit
[+] Trojan/FakeApp.aaq!submit
[+] Trojan/FakeApp.aar!submit
[+] Trojan/FakeApp.aas!submit
[+] Trojan/FakeApp.aat!submit
[+] Trojan/Injector.cld!submit
[+] Trojan/MSIL.Obfuscated.jr!submit
[+] Trojan/Python.CoinMiner.j!submit
[+] Trojan/Python.Popups.b!submit
[+] Trojan/Runner.fk!submit
[+] Trojan/ShellLoader.agv!submit
[+] Trojan/VBS.Agent.em!submit
[+] Trojan/W64.Loader.ae!submit
[+] Trojan/W64.Loader.af!submit
[+] Trojan/W64.Loader.ag!submit
[+] Trojan/W64.Loader.ah!submit
[+] Trojan/W64.Loader.ai!submit
[+] Trojan/W64.ReverseShell.a!submit
[+] TrojanDownloader/JS.Agent.ic!submit
[+] TrojanDownloader/MSIL.Agent.aji!submit
[+] TrojanDownloader/PS.Agent.ey!submit
[+] TrojanDownloader/PS.Agent.ez!submit
[+] TrojanDropper/Agent.ajw!submit
[-] Backdoor/Agent.nf!submit
[-] Backdoor/Agent.od!submit
[-] Backdoor/JS.Webshell.l!submit
[-] Backdoor/Lotok.nw!submit
[-] Backdoor/Lotok.nx!submit
[-] Backdoor/W64.Agent.i!submit
[-] Exploit/Vulndriver.s!submit
[-] HEUR:Trojan/Agent.clm!submit
[-] HEUR:Trojan/BAT.KillWin.bc!submit
[-] HEUR:Trojan/FakeApp.at!submit
[-] HEUR:Trojan/KillWin.e!submit
[-] HVM:Backdoor/Lotok.cd!submit
[-] HVM:Backdoor/Lotok.ce!submit
[-] HVM:Trojan/ShellLoader.ci!submit
[-] HackTool/Python.RemoteExec.a!submit
[-] Rootkit/Inject.b!submit
[-] Trojan/Agent.clm!submit
[-] Trojan/BAT.Agent.gp!submit
[-] Trojan/BAT.Injector.d!submit
[-] Trojan/BAT.Injector.e!submit
[-] Trojan/BAT.Loader.h!submit
[-] Trojan/FakeApp.aal!submit
[-] Trojan/FakeApp.aam!submit
[-] Trojan/FakeApp.aan!submit
[-] Trojan/FakeApp.aao!submit
[-] Trojan/JS.Agent.gp!submit
[-] Trojan/JS.Agent.gq!submit
[-] Trojan/JS.Loader.d!submit
[-] Trojan/KillAV.db!submit
[-] Trojan/Linux.CoinMiner.du!submit
[-] Trojan/Linux.CoinMiner.dv!submit
[-] Trojan/Linux.DDoS.be!submit
[-] Trojan/Linux.Mirai.fz!submit
[-] Trojan/Linux.Mirai.ga!submit
[-] Trojan/Linux.Mirai.gb!submits
[-] Trojan/Loader.mm!submit
[-] Trojan/MSIL.Injector.qf!submit
[-] Trojan/MSIL.Obfuscated.jq!submit
[-] Trojan/Python.KillDisk.e!submit
[-] Trojan/ShellLoader.agr!submit
[-] Trojan/ShellLoader.ags!submit
[-] Trojan/ShellLoader.agt!submit
[-] Trojan/ShellLoader.agu!submit
[-] Trojan/W64.Loader.ab!submit
[-] Trojan/W64.Loader.ac!submit
[-] Trojan/W64.Loader.ad!submit
[-] Trojan/W64.Merlin.a!submit
[-] TrojanDownloader/JS.Agent.ib!submit
[-] TrojanDownloader/Linux.Hajime.b!submit
[-] TrojanDownloader/PS.Agent.ex!submit
[-] TrojanDownloader/Rugmi.ab!submit
[-] TrojanDropper/Agent.ajt!submit
[-] TrojanDropper/Agent.aju!submit
[-] TrojanDropper/Agent.ajv!submit
[-] TrojanSpy/MSIL.Stealer.ks!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1767093364.crithash.txt))

<details>
<summary>
新增正式定义: 8
</summary>

```
[+] Backdoor/W32.Small.z!crit
[+] Backdoor/W64.Agent.f!crit
[+] Exploit/SCR.CVE-2017-0199.b!crit
[+] Trojan/MSIL.Obfuscated.aj!crit
[+] Trojan/MSIL.Obfuscated.ak!crit
[+] Trojan/MSIL.ShellLoader.a!crit
[+] Trojan/W32.Scar.d!crit
[+] TrojanDropper/W32.Tedy.a!crit
```

</details>

<details>
<summary>
新增遥测定义: 8 | 移除遥测定义: 12
</summary>

```
[+] Trojan/SCR.Loader.a!crit!submit
[+] Trojan/SCR.ShellCode.b!crit!submit
[+] Trojan/W32.Agent.w!crit!submit
[+] Trojan/W32.HiJack.u!crit!submit
[+] Trojan/W64.Agent.gj!crit!submit
[+] Trojan/W64.ShellLoader.j!crit!submit
[+] TrojanDownloader/W32.Maloader.bl!crit!submit
[+] TrojanSpy/SCR.Stealer.a!crit!submit
[-] Backdoor/W32.Lotok.q!crit!submit
[-] Backdoor/W32.Small.z!crit!submit
[-] Backdoor/W64.Agent.f!crit!submit
[-] Exploit/SCR.CVE-2017-0199.b!crit!submit
[-] Trojan/MSIL.Obfuscated.aj!crit!submit
[-] Trojan/MSIL.Obfuscated.ak!crit!submit
[-] Trojan/MSIL.ShellLoader.a!crit!submit
[-] Trojan/W32.Agent.cln!crit!submit
[-] Trojan/W32.Agent.v!crit!submit
[-] Trojan/W32.Scar.d!crit!submit
[-] Trojan/W32.ShellLoader.h!crit!submit
[-] TrojanDropper/W32.Tedy.a!crit!submit
```

</details>

#### 行为特征项变更 ([behav.txt](data/1767093364.behav.txt))

<details>
<summary>
新增: 5 | 移除: 2
</summary>

```
[+] ADV:Ransom/Genalocker.ZCA!submit
[+] ADV:Ransom/Genalocker.ZCB!submit
[+] Backdoor/Lotok.QDA!submit
[+] Backdoor/Lotok.QDB!submit
[+] TrojanDropper/MalSetup.PA!submit
[-] ADV:Ransom/Genalocker.ZBA!submit
[-] ADV:Ransom/Genalocker.ZBB!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1767093364.troj.txt))

新增: 77

</details>

<details>
<summary><b>1767007867</b> - 2025-12-29 11:31:07 UTC</summary>

#### 特征项变更 ([pset.txt](data/1767007867.pset.txt))

<details>
<summary>
新增正式定义: 49 | 移除正式定义: 1
</summary>

```
[+] Backdoor/JSP.WebShell.bw
[+] Backdoor/Linux.Gafgyt.bx
[+] Backdoor/Lotok.nr
[+] Backdoor/Lotok.ns
[+] Backdoor/Lotok.nt
[+] Backdoor/Lotok.nu
[+] Backdoor/Python.Agent.m
[+] Exploit/CVE-2016-0099.c
[+] HEUR:Trojan/ShellLoader.az
[+] HEUR:TrojanDownloader/Maloader.bl
[+] HEUR:TrojanDropper/Agent.aq
[+] HEUR:Worm/Autorun.ak
[+] HVM:Trojan/ShellLoader.ch
[+] HVM:TrojanSpy/Stealer.p
[+] HackTool/ProxyTool.i
[+] HackTool/W64.Merlin.a
[+] OMacro/Downloader.bov
[+] Rootkit/Injecter
[+] Trojan/BAT.Runner.bl
[+] Trojan/FakeApp.aaf
[+] Trojan/FakeApp.aag
[+] Trojan/FakeApp.aah
[+] Trojan/FakeApp.aai
[+] Trojan/FakeApp.aaj
[+] Trojan/FakeApp.aak
[+] Trojan/HTML.Obfuscator.b
[+] Trojan/HiJack.yh
[+] Trojan/Hijack.yh
[+] Trojan/Hijack.yi
[+] Trojan/Linux.Merlin.b
[+] Trojan/Linux.Mirai.fy
[+] Trojan/Loader.mj
[+] Trojan/Loader.mk
[+] Trojan/Loader.ml
[+] Trojan/Merlin.b
[+] Trojan/Merlin.c
[+] Trojan/PS.Loader.l
[+] Trojan/Runner.fj
[+] Trojan/ShellLoader.agp
[+] Trojan/Sonbokli.a
[+] TrojanDownloader/Linux.Hajime.c
[+] TrojanDownloader/PS.Agent.ew
[+] TrojanDownloader/Python.Netloader.h
[+] TrojanDownloader/VBS.Agent.ka
[+] TrojanDropper/Agent.ajr
[+] TrojanDropper/Agent.ajs
[+] TrojanDropper/Linux.Exploit.a
[+] TrojanSpy/AutoIt.Stealer.k
[+] TrojanSpy/Python.SteamStealer.a
[-] Backdoor/Lotok.nq
```

</details>

<details>
<summary>
新增遥测定义: 56 | 移除遥测定义: 59
</summary>

```
[+] Backdoor/Agent.nf!submit
[+] Backdoor/Agent.od!submit
[+] Backdoor/JS.Webshell.l!submit
[+] Backdoor/Linux.Mirai.ko!submit
[+] Backdoor/Lotok.nw!submit
[+] Backdoor/Lotok.nx!submit
[+] Backdoor/W64.Agent.i!submit
[+] Exploit/Vulndriver.s!submit
[+] HEUR:Trojan/Agent.clm!submit
[+] HEUR:Trojan/BAT.KillWin.bc!submit
[+] HEUR:Trojan/BAT.Loader.i!submit
[+] HEUR:Trojan/FakeApp.at!submit
[+] HEUR:Trojan/KillWin.e!submit
[+] HVM:Backdoor/Lotok.cd!submit
[+] HVM:Backdoor/Lotok.ce!submit
[+] HVM:Trojan/ShellLoader.ci!submit
[+] HackTool/Python.RemoteExec.a!submit
[+] Rootkit/Inject.b!submit
[+] Trojan/Agent.clm!submit
[+] Trojan/BAT.Agent.gp!submit
[+] Trojan/BAT.Injector.d!submit
[+] Trojan/BAT.Injector.e!submit
[+] Trojan/BAT.Loader.h!submit
[+] Trojan/CoinMiner.la!submit
[+] Trojan/FakeApp.aal!submit
[+] Trojan/FakeApp.aam!submit
[+] Trojan/FakeApp.aan!submit
[+] Trojan/FakeApp.aao!submit
[+] Trojan/JS.Agent.gp!submit
[+] Trojan/JS.Agent.gq!submit
[+] Trojan/JS.Loader.d!submit
[+] Trojan/KillAV.db!submit
[+] Trojan/Linux.CoinMiner.du!submit
[+] Trojan/Linux.CoinMiner.dv!submit
[+] Trojan/Linux.DDoS.be!submit
[+] Trojan/Linux.Mirai.fz!submit
[+] Trojan/Linux.Mirai.ga!submit
[+] Trojan/Linux.Mirai.gb!submits
[+] Trojan/Loader.mm!submit
[+] Trojan/MSIL.Injector.qf!submit
[+] Trojan/MSIL.Obfuscated.jq!submit
[+] Trojan/Python.KillDisk.e!submit
[+] Trojan/ShellLoader.agr!submit
[+] Trojan/ShellLoader.ags!submit
[+] Trojan/ShellLoader.agt!submit
[+] Trojan/ShellLoader.agu!submit
[+] Trojan/W64.Loader.ab!submit
[+] Trojan/W64.Loader.ac!submit
[+] Trojan/W64.Loader.ad!submit
[+] Trojan/W64.Merlin.a!submit
[+] TrojanDownloader/JS.Agent.ib!submit
[+] TrojanDownloader/PS.Agent.ex!submit
[+] TrojanDownloader/Rugmi.ab!submit
[+] TrojanDropper/Agent.ajt!submit
[+] TrojanDropper/Agent.aju!submit
[+] TrojanDropper/Agent.ajv!submit
[-] Backdoor/JSP.WebShell.bw!submit
[-] Backdoor/Kingsoft.c!submit
[-] Backdoor/Linux.Gafgyt.bx!submit
[-] Backdoor/Lotok.nr!submit
[-] Backdoor/Lotok.ns!submit
[-] Backdoor/Lotok.nt!submit
[-] Backdoor/Lotok.nu!submit
[-] Exploit/CVE-2016-0099.c!submit
[-] HEUR:Trojan/ShellLoader.az!submit
[-] HEUR:TrojanDownloader/Maloader.bl!submit
[-] HEUR:TrojanDropper/Agent.aq!submit
[-] HEUR:Worm/Autorun.ak!submit
[-] HVM:Trojan/ShellLoader.ch!submit
[-] HVM:TrojanSpy/Stealer.p!submit
[-] HackTool/CoinMiner!submit
[-] HackTool/ProxyTool.i!submit
[-] HackTool/W64.Merlin.a!submit
[-] OMacro/Downloader.bov!submit
[-] Rootkit/Injecter!submit
[-] Trojan/BAT.Runner.bl!submit
[-] Trojan/CowLock.a!submit
[-] Trojan/FakeApp.aaf!submit
[-] Trojan/FakeApp.aag!submit
[-] Trojan/FakeApp.aah!submit
[-] Trojan/FakeApp.aai!submit
[-] Trojan/FakeApp.aaj!submit
[-] Trojan/FakeApp.aak!submit
[-] Trojan/Gooxion.a!submit
[-] Trojan/HTML.Obfuscator.b!submit
[-] Trojan/HiJack.yh!submit
[-] Trojan/Hijack.yh!submit
[-] Trojan/Hijack.yi!submit
[-] Trojan/Linux.Merlin.b!submit
[-] Trojan/Linux.Mirai.fy!submit
[-] Trojan/Loader.mj!submit
[-] Trojan/Loader.mk!submit
[-] Trojan/Loader.ml!submit
[-] Trojan/Merlin.b!submit
[-] Trojan/Merlin.c!submit
[-] Trojan/PS.Loader.l!submit
[-] Trojan/Runner.fj!submit
[-] Trojan/ShellLoader.agf!submit
[-] Trojan/ShellLoader.agm!submit
[-] Trojan/ShellLoader.agp!submit
[-] Trojan/Sonbokli.a!submit
[-] Trojan/VBS.Agent.bv!submit
[-] TrojanClicker/Agent.by!submit
[-] TrojanDownloader/Linux.Hajime.c!submit
[-] TrojanDownloader/PS.Agent.ew!submit
[-] TrojanDownloader/Python.Netloader.h!submit
[-] TrojanDownloader/VBS.Agent.ka!submit
[-] TrojanDropper/Agent.ajr!submit
[-] TrojanDropper/Agent.ajs!submit
[-] TrojanDropper/Linux.Exploit.a!submit
[-] TrojanDropper/Spacecolon.a!submit
[-] TrojanSpy/AutoIt.Stealer.k!submit
[-] TrojanSpy/Delf.ad!submit
[-] TrojanSpy/MSIL.Agent.da!submit
[-] TrojanSpy/Python.SteamStealer.a!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1767007867.crithash.txt))

<details>
<summary>
新增正式定义: 9
</summary>

```
[+] Backdoor/W64.Agent.d!crit
[+] Backdoor/W64.Agent.e!crit
[+] Joke/Python.Agent.b!crit
[+] Joke/W64.Agent.az!crit
[+] Trojan/MSIL.Obfuscated.ai!crit
[+] Trojan/MSIL.PureLogStealer.a!crit
[+] Trojan/W64.Agent.clm!crit
[+] Trojan/W64.CoinMiner.a!crit
[+] Trojan/W64.Loader.b!crit
```

</details>

<details>
<summary>
新增遥测定义: 11 | 移除遥测定义: 12
</summary>

```
[+] Backdoor/W32.Lotok.q!crit!submit
[+] Backdoor/W32.Small.z!crit!submit
[+] Backdoor/W64.Agent.f!crit!submit
[+] Exploit/SCR.CVE-2017-0199.b!crit!submit
[+] Trojan/MSIL.Obfuscated.aj!crit!submit
[+] Trojan/MSIL.Obfuscated.ak!crit!submit
[+] Trojan/MSIL.ShellLoader.a!crit!submit
[+] Trojan/W32.Agent.cln!crit!submit
[+] Trojan/W32.Agent.v!crit!submit
[+] Trojan/W32.ShellLoader.h!crit!submit
[+] TrojanDropper/W32.Tedy.a!crit!submit
[-] Backdoor/W32.Lotok.p!crit!submit
[-] Backdoor/W64.Agent.d!crit!submit
[-] Backdoor/W64.Agent.e!crit!submit
[-] Joke/Python.Agent.b!crit!submit
[-] Joke/W64.Agent.az!crit!submit
[-] Trojan/MSIL.Obfuscated.ai!crit!submit
[-] Trojan/MSIL.PureLogStealer.a!crit!submit
[-] Trojan/W32.Agent.clm!crit!submit
[-] Trojan/W32.Agent.u!crit!submit
[-] Trojan/W64.Agent.clm!crit!submit
[-] Trojan/W64.CoinMiner.a!crit!submit
[-] Trojan/W64.Loader.b!crit!submit
```

</details>

#### 行为特征项变更 ([behav.txt](data/1767007867.behav.txt))

<details>
<summary>
新增: 1 | 移除: 1
</summary>

```
[+] TrojanDropper/MalSetup.OA!submit
[-] TrojanDropper/MalSetup.O!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1767007867.troj.txt))

新增: 81

#### 白名单哈希变更 ([hwl.txt](data/1767007867.hwl.txt))

新增: 1

</details>

<details>
<summary><b>1766920695</b> - 2025-12-28 11:18:15 UTC</summary>

#### 黑名单哈希变更 ([troj.txt](data/1766920695.troj.txt))

新增: 111

#### 白名单哈希变更 ([hwl.txt](data/1766920695.hwl.txt))

新增: 1

</details>

<details>
<summary><b>1766836824</b> - 2025-12-27 12:00:24 UTC</summary>

#### 黑名单哈希变更 ([troj.txt](data/1766836824.troj.txt))

新增: 99 | 移除: 1

</details>

<details>
<summary><b>1766750454</b> - 2025-12-26 12:00:54 UTC</summary>

#### 特征项变更 ([pset.txt](data/1766750454.pset.txt))

<details>
<summary>
新增正式定义: 51 | 移除正式定义: 3
</summary>

```
[+] Backdoor/Agent.mv
[+] Backdoor/Lotok.nk
[+] Backdoor/Lotok.nl
[+] Backdoor/Lotok.nm
[+] Backdoor/Lotok.nn
[+] Backdoor/Lotok.no
[+] Backdoor/Lotok.np
[+] Backdoor/Lotok.nq
[+] Backdoor/Lotok.nv
[+] Backdoor/Python.ReverseRAT.c
[+] HEUR:Trojan/Agent.ea
[+] HEUR:Trojan/Injector.cn
[+] HEUR:Trojan/MSIL.Obfuscated.jp
[+] HEUR:Worm/AutoRun.aj
[+] HVM:Backdoor/Lotok.bz
[+] HVM:Backdoor/Lotok.ca
[+] HVM:Backdoor/Lotok.cb
[+] HVM:Backdoor/Lotok.cc
[+] HVM:Trojan/ShellLoader.cg
[+] HackTool/GodPotato.b
[+] Ransom/Filecoder.eg
[+] Trojan/FakeApp.aab
[+] Trojan/FakeApp.aac
[+] Trojan/FakeApp.aad
[+] Trojan/FakeApp.aae
[+] Trojan/Glupteba.c
[+] Trojan/Injector.clc
[+] Trojan/LNK.Starter.cv
[+] Trojan/Linux.Mirai.fw
[+] Trojan/Loader.mh
[+] Trojan/Loader.mi
[+] Trojan/MSIL.Obfuscated.jp
[+] Trojan/PS.Loader.k
[+] Trojan/Python.Obfuscator.d
[+] Trojan/Runner.fi
[+] Trojan/ShellLoader.agm
[+] Trojan/ShellLoader.agn
[+] Trojan/ShellLoader.ago
[+] Trojan/ShellLoader.agq
[+] Trojan/VBS.Obfuscator.q
[+] Trojan/W64.Loader.aa
[+] Trojan/W64.Loader.z
[+] TrojanDownloader/Agent.bjw
[+] TrojanDownloader/Agent.bll
[+] TrojanDownloader/PS.Agent.et
[+] TrojanDownloader/PS.Agent.eu
[+] TrojanDownloader/PS.Agent.ev
[+] TrojanDownloader/W64.Agent.cl
[+] TrojanDownloader/W64.Agent.cm
[+] TrojanDropper/BAT.Agent.bl
[+] TrojanDropper/Maloader.l
[-] HEUR:OMacro/Downloader.cu
[-] TrojanDownloader/Linux.Netloader.f
[-] TrojanDropper/Linux.Exploit.a
```

</details>

<details>
<summary>
新增遥测定义: 57 | 移除遥测定义: 50
</summary>

```
[+] Backdoor/JSP.WebShell.bw!submit
[+] Backdoor/Linux.Gafgyt.bx!submit
[+] Backdoor/Lotok.nr!submit
[+] Backdoor/Lotok.ns!submit
[+] Backdoor/Lotok.nt!submit
[+] Backdoor/Lotok.nu!submit
[+] Backdoor/Python.ReverseRAT.d!submit
[+] Exploit/CVE-2016-0099.c!submit
[+] HEUR:Trojan/ShellLoader.az!submit
[+] HEUR:TrojanDownloader/Maloader.bl!submit
[+] HEUR:TrojanDropper/Agent.aq!submit
[+] HEUR:Worm/Autorun.ak!submit
[+] HVM:Trojan/ShellLoader.ch!submit
[+] HVM:TrojanSpy/Stealer.p!submit
[+] HackTool/CoinMiner!submit
[+] HackTool/ProxyTool.i!submit
[+] HackTool/W64.Merlin.a!submit
[+] OMacro/Downloader.bov!submit
[+] Rootkit/Injecter!submit
[+] Trojan/BAT.Runner.bk!submit
[+] Trojan/BAT.Runner.bl!submit
[+] Trojan/FakeApp.aag!submit
[+] Trojan/FakeApp.aah!submit
[+] Trojan/FakeApp.aai!submit
[+] Trojan/FakeApp.aaj!submit
[+] Trojan/FakeApp.aak!submit
[+] Trojan/Gooxion.a!submit
[+] Trojan/HTML.Injector.n!submit
[+] Trojan/HTML.Obfuscator.b!submit
[+] Trojan/HiJack.yh!submit
[+] Trojan/Hijack.yh!submit
[+] Trojan/Hijack.yi!submit
[+] Trojan/Linux.CoinMiner.dt!submit
[+] Trojan/Linux.Merlin.b!submit
[+] Trojan/Loader.mj!submit
[+] Trojan/Loader.mk!submit
[+] Trojan/Loader.ml!submit
[+] Trojan/Merlin.b!submit
[+] Trojan/Merlin.c!submit
[+] Trojan/PS.Loader.l!submit
[+] Trojan/Runner.fj!submit
[+] Trojan/ShellLoader.agf!submit
[+] Trojan/ShellLoader.agp!submit
[+] Trojan/Sonbokli.a!submit
[+] TrojanDownloader/Linux.Hajime.b!submit
[+] TrojanDownloader/Linux.Hajime.c!submit
[+] TrojanDownloader/Linux.Mozi.c!submit
[+] TrojanDownloader/Linux.Netloader.f!submit
[+] TrojanDownloader/PS.Agent.ew!submit
[+] TrojanDownloader/Python.Netloader.h!submit
[+] TrojanDownloader/VBS.Agent.ka!submit
[+] TrojanDropper/Agent.ajr!submit
[+] TrojanDropper/Agent.ajs!submit
[+] TrojanDropper/Linux.Exploit.a!submit
[+] TrojanSpy/AutoIt.Stealer.k!submit
[+] TrojanSpy/MSIL.Stealer.ks!submit
[+] TrojanSpy/Python.SteamStealer.a!submit
[-] Backdoor/Agent.mv!submit
[-] Backdoor/Lotok.nk!submit
[-] Backdoor/Lotok.nl!submit
[-] Backdoor/Lotok.nm!submit
[-] Backdoor/Lotok.nn!submit
[-] Backdoor/Lotok.no!submit
[-] Backdoor/Lotok.np!submit
[-] Backdoor/Lotok.nq!submit
[-] Backdoor/Python.ReverseRAT.c!submit
[-] HEUR:Trojan/Agent.ea!submit
[-] HEUR:Trojan/Injector.cn!submit
[-] HEUR:Trojan/MSIL.Obfuscated.jp!submit
[-] HEUR:Worm/AutoRun.aj!submit
[-] HVM:Backdoor/Lotok.bz!submit
[-] HVM:Backdoor/Lotok.ca!submit
[-] HVM:Backdoor/Lotok.cb!submit
[-] HVM:Backdoor/Lotok.cc!submit
[-] HVM:Trojan/ShellLoader.cg!submit
[-] HackTool/GodPotato.b!submit
[-] Ransom/Filecoder.eg!submit
[-] Trojan/Agent.cll!submit
[-] Trojan/FakeApp.aab!submit
[-] Trojan/FakeApp.aac!submit
[-] Trojan/FakeApp.aad!submit
[-] Trojan/FakeApp.aae!submit
[-] Trojan/Glupteba.c!submit
[-] Trojan/Injector.clc!submit
[-] Trojan/LNK.Starter.cv!submit
[-] Trojan/Linux.Mirai.fw!submit
[-] Trojan/Loader.mh!submit
[-] Trojan/Loader.mi!submit
[-] Trojan/MSIL.Obfuscated.jm!submit
[-] Trojan/MSIL.Obfuscated.jp!submit
[-] Trojan/PS.Loader.k!submit
[-] Trojan/Python.Obfuscator.d!submit
[-] Trojan/Runner.fi!submit
[-] Trojan/ShellLoader.agn!submit
[-] Trojan/ShellLoader.ago!submit
[-] Trojan/VBS.Obfuscator.q!submit
[-] Trojan/W64.Loader.aa!submit
[-] Trojan/W64.Loader.z!submit
[-] TrojanDownloader/Agent.bjw!submit
[-] TrojanDownloader/Agent.bll!submit
[-] TrojanDownloader/PS.Agent.et!submit
[-] TrojanDownloader/PS.Agent.eu!submit
[-] TrojanDownloader/PS.Agent.ev!submit
[-] TrojanDownloader/W64.Agent.cl!submit
[-] TrojanDownloader/W64.Agent.cm!submit
[-] TrojanDropper/BAT.Agent.bl!submit
[-] TrojanDropper/Maloader.l!submit
```

</details>

#### 关键哈希特征项变更 ([crithash.txt](data/1766750454.crithash.txt))

<details>
<summary>
新增正式定义: 9
</summary>

```
[+] Trojan/MSIL.Obfuscated.ah!crit
[+] Trojan/SCR.CoinMiner.b!crit
[+] Trojan/W32.CoinMiner.la!crit
[+] Trojan/W64.ShellLoader.c!crit
[+] TrojanDownloader/AutoIT.Maloader.a!crit
[+] TrojanDownloader/JS.Agent.b!crit
[+] TrojanDownloader/JS.Netloader.f!crit
[+] TrojanDropper/W32.Agent.ag!crit
[+] TrojanDropper/W32.Agent.k!crit
```

</details>

<details>
<summary>
新增遥测定义: 38 | 移除遥测定义: 11
</summary>

```
[+] Backdoor/BAT.ReverseShell.a!crit!submit
[+] Backdoor/W32.Lotok.o!crit!submit
[+] Backdoor/W32.Lotok.p!crit!submit
[+] Backdoor/W64.Agent.d!crit!submit
[+] Backdoor/W64.Agent.e!crit!submit
[+] HackTool/PHP.Botsant.b!crit!submit
[+] Joke/BAT.Qhost.a!crit!submit
[+] Joke/Python.Agent.b!crit!submit
[+] Joke/W64.Agent.az!crit!submit
[+] Ransom/PS.HideFile.a!crit!submit
[+] Trojan/BAT.CoinMiner.b!crit!submit
[+] Trojan/MSIL.Coinminer.a!crit!submit
[+] Trojan/MSIL.Obfuscated.ai!crit!submit
[+] Trojan/MSIL.PureLogStealer.a!crit!submit
[+] Trojan/PS.LockFile.a!crit!submit
[+] Trojan/W32.Agent.clm!crit!submit
[+] Trojan/W32.Agent.u!crit!submit
[+] Trojan/W32.Injector.p!crit!submit
[+] Trojan/W32.Scar.d!crit!submit
[+] Trojan/W64.Agent.clm!crit!submit
[+] Trojan/W64.CoinMiner.a!crit!submit
[+] Trojan/W64.Loader.b!crit!submit
[+] TrojanDownloader/BAT.Runner.a!crit!submit
[+] TrojanDownloader/BAT.Runner.c!crit!submit
[+] TrojanDownloader/BAT.Runner.d!crit!submit
[+] TrojanDownloader/PS.Agent.a!crit!submit
[+] TrojanDownloader/PS.Runner.d!crit!submit
[+] TrojanDownloader/PS.Runner.e!crit!submit
[+] TrojanDownloader/PS.Runner.f!crit!submit
[+] TrojanDownloader/W32.Runner.b!crit!submit
[+] TrojanDownloader/W64.Maloader.a!crit!submit
[+] TrojanDropper/MSIL.Agent.a!crit!submit
[+] TrojanDropper/PS.Runner.b!crit!submit
[+] TrojanSpy/PS.Stealer.h!crit!submit
[+] TrojanSpy/W32.Keylogger.b!crit!submit
[+] TrojanSpy/W32.Stealer.y!crit!submit
[+] TrojanSpy/W64.Stealer.b!crit!submit
[+] TrojanSpy/W64.Stealer.c!crit!submit
[-] BackDoor/BAT.ReverseShell.a!crit!submit
[-] Backdoor/W32.Lotok.l!crit!submit
[-] Hacktool/PHP.Botsant.b!crit!submit
[-] Trojan/MSIL.Obfuscated.ah!crit!submit
[-] Trojan/W32.CoinMiner.la!crit!submit
[-] Trojan/W32.Obfuscated.ns!crit!submit
[-] Trojan/W64.ShellLoader.c!crit!submit
[-] TrojanDownloader/AutoIT.Maloader.a!crit!submit
[-] TrojanDownloader/JS.Agent.b!crit!submit
[-] TrojanDownloader/JS.Netloader.f!crit!submit
[-] TrojanDropper/W32.Agent.ag!crit!submit
```

</details>

#### 行为特征项变更 ([behav.txt](data/1766750454.behav.txt))

<details>
<summary>
新增: 1
</summary>

```
[+] Software:OS/Gooxion.AA#固信终端安全!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1766750454.troj.txt))

新增: 152

</details>

<details>
<summary><b>1766655657</b> - 2025-12-25 09:40:57 UTC</summary>

#### 特征项变更 ([pset.txt](data/1766655657.pset.txt))

新增正式定义: 65,357

新增遥测定义: 881

#### 关键哈希特征项变更 ([crithash.txt](data/1766655657.crithash.txt))

新增正式定义: 74,410

新增遥测定义: 5,883

#### 行为特征项变更 ([behav.txt](data/1766655657.behav.txt))

新增: 896

#### 黑名单哈希变更 ([troj.txt](data/1766655657.troj.txt))

新增: 186,016

#### 白名单哈希变更 ([hwl.txt](data/1766655657.hwl.txt))

新增: 141,833

</details>

## 许可协议

本更新日志仅供参考。火绒病毒库为火绒安全软件所有。
