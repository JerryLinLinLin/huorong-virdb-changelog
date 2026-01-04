# 火绒病毒库更新日志

本仓库跟踪[火绒安全软件](https://www.huorong.cn/)病毒库的变更。
每次更新显示与上一版本相比新增的检测项/报毒名(pset.txt), 黑名单哈希(troj.txt)和白名单哈希(hwl.txt)。

> **免责声明**：本项目非火绒官方出品，仅供学习和技术交流使用。作者不对使用本项目造成的任何后果负责。

## 概览

- **最新版本**: `1767443553` (2026-01-03 12:32:33 UTC)
- **检测项总数**: 66,406
- **黑名单哈希总数**: 186,750
- **白名单哈希总数**: 142,021
- **已跟踪版本数**: 10

## 检测项分类分布

```mermaid
pie showData
    title Top 10
    "Trojan" : 23706
    "TrojanDownloader" : 9720
    "Backdoor" : 6455
    "TrojanSpy" : 6063
    "OMacro" : 3392
    "Virus" : 2819
    "TrojanDropper" : 2663
    "Adware" : 2345
    "VirTool" : 2292
    "Ransom" : 1982
    "Other" : 4969
```


---

## 更新日志

### 2026-01-03

**版本**: `1767443553` (2026-01-03 12:32:33 UTC)

#### 黑名单哈希变更 ([troj.txt](data/1767443553.troj.txt))

新增: 41

**统计**:

| 指标 | 数值 |
|------|-----:|
| 检测项总数 | 66,406 |
| 黑名单哈希总数 | 186,750 |
| 白名单哈希总数 | 142,021 |
| PSET 记录 | 71,134 |
| TROJ 哈希 | 187,044 |
| HWL 记录 | 142,021 |

---

### 2026-01-02

**版本**: `1767352866` (2026-01-02 11:21:06 UTC)

#### 黑名单哈希变更 ([troj.txt](data/1767352866.troj.txt))

新增: 61 | 移除: 1

**统计**:

| 指标 | 数值 |
|------|-----:|
| 检测项总数 | 66,406 |
| 黑名单哈希总数 | 186,709 |
| 白名单哈希总数 | 142,021 |
| PSET 记录 | 71,134 |
| TROJ 哈希 | 187,003 |
| HWL 记录 | 142,021 |

---

### 2026-01-01

**版本**: `1767267452` (2026-01-01 11:37:32 UTC)

#### 黑名单哈希变更 ([troj.txt](data/1767267452.troj.txt))

新增: 86 | 移除: 2

#### 白名单哈希变更 ([hwl.txt](data/1767267452.hwl.txt))

新增: 4

**统计**:

| 指标 | 数值 |
|------|-----:|
| 检测项总数 | 66,406 |
| 黑名单哈希总数 | 186,649 |
| 白名单哈希总数 | 142,021 |
| PSET 记录 | 71,134 |
| TROJ 哈希 | 186,943 |
| HWL 记录 | 142,021 |

---

### 2025-12-31

**版本**: `1767177959` (2025-12-31 10:45:59 UTC)

#### 检测项变更 ([pset.txt](data/1767177959.pset.txt))

<details>
<summary>
新增: 62 | 移除: 31
</summary>

```
[+] Adware/Android.PornTool.m!submit
[+] Backdoor/Linux.Gafgyt.bz!submit
[+] Backdoor/Linux.Mirai.ku!submit
[+] Backdoor/Lotok.nq
[+] HEUR:Trojan/BAT.Loader.k!submit
[+] HEUR:Trojan/ShellLoader.agv
[+] HVM:Backdoor/Lotok.cf
[+] HVM:Trojan/Injector.bo!submit
[+] HackTool/Python.Winpwnage.a
[+] Ransom/Filecoder.ei!submit
[+] Rootkit/MiniFilter.b
[+] Trojan/Agent.cln!submit
[+] Trojan/BAT.KillWin.bd
[+] Trojan/BAT.Runner.bm
[+] Trojan/Bladabindi.e
[+] Trojan/CoinMiner.la
[+] Trojan/FakeApp.aam!submit
[+] Trojan/FakeApp.aap
[+] Trojan/FakeApp.aaq
[+] Trojan/FakeApp.aar
[+] Trojan/FakeApp.aas
[+] Trojan/FakeApp.aat
[+] Trojan/FakeApp.aau!submit
[+] Trojan/Injector.cld
[+] Trojan/Injector.cle!submit
[+] Trojan/Injector.clf!submit
[+] Trojan/KillMBR.cl!submit
[+] Trojan/Linux.Mirai.gc!submit
[+] Trojan/MSIL.Obfuscated.jr
[+] Trojan/MSIL.Obfuscated.js!submit
[+] Trojan/MSIL.Runner.l!submit
[+] Trojan/MSIL.Runner.m!submit
[+] Trojan/Python.CoinMiner.j
[+] Trojan/Python.Popups.b
[+] Trojan/ReverseShell.x!submit
[+] Trojan/Runner.fk
[+] Trojan/ShellLoader.agv
[+] Trojan/ShellLoader.agw!submit
[+] Trojan/VBS.Agent.em
[+] Trojan/W64.Injector.bw!submit
[+] Trojan/W64.Loader.ae
[+] Trojan/W64.Loader.af
[+] Trojan/W64.Loader.ag
[+] Trojan/W64.Loader.ah
[+] Trojan/W64.Loader.ai
[+] Trojan/W64.ReverseShell.a
[+] TrojanDownloader/Agent.blm!submit
[+] TrojanDownloader/JS.Agent.ic
[+] TrojanDownloader/JS.Agent.id!submit
[+] TrojanDownloader/MSIL.Agent.aji
[+] TrojanDownloader/Maloader.bl!submit
[+] TrojanDownloader/PS.Agent.ey
[+] TrojanDownloader/PS.Agent.ez
[+] TrojanDropper/Agent.ajw
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
[-] HackTool/Python.Winpwnage.a!submit
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

#### 黑名单哈希变更 ([troj.txt](data/1767177959.troj.txt))

新增: 30

**统计**:

| 指标 | 数值 |
|------|-----:|
| 检测项总数 | 66,406 |
| 黑名单哈希总数 | 186,565 |
| 白名单哈希总数 | 142,017 |
| PSET 记录 | 71,134 |
| TROJ 哈希 | 186,859 |
| HWL 记录 | 142,017 |

---

### 2025-12-30

**版本**: `1767093364` (2025-12-30 11:16:04 UTC)

#### 检测项变更 ([pset.txt](data/1767093364.pset.txt))

<details>
<summary>
新增: 91 | 移除: 55
</summary>

```
[+] Backdoor/Agent.nf
[+] Backdoor/Agent.od
[+] Backdoor/JS.Webshell.l
[+] Backdoor/Linux.Gafgyt.by!submit
[+] Backdoor/Lotok.nq!submit
[+] Backdoor/Lotok.nw
[+] Backdoor/Lotok.nx
[+] Backdoor/W64.AdaptixC2.a!submit
[+] Backdoor/W64.Agent.i
[+] HEUR:Backdoor/Linux.Mirai.ku!submit
[+] HEUR:Trojan/Agent.clm
[+] HEUR:Trojan/BAT.KillWin.bc
[+] HEUR:Trojan/BAT.Loader.j!submit
[+] HEUR:Trojan/FakeApp.aam!submit
[+] HEUR:Trojan/FakeApp.at
[+] HEUR:Trojan/KillWin.e
[+] HEUR:Trojan/ShellLoader.agv!submit
[+] HVM:Backdoor/Lotok.cd
[+] HVM:Backdoor/Lotok.ce
[+] HVM:Backdoor/Lotok.cf!submit
[+] HVM:Trojan/ShellLoader.ci
[+] HackTool/Python.RemoteExec.a
[+] HackTool/Python.Winpwnage.a!submit
[+] Hacktool/CoinMiner
[+] Rootkit/Inject.b
[+] Rootkit/MiniFilter.b!submit
[+] Trojan/Agent.clm
[+] Trojan/BAT.Agent.gp
[+] Trojan/BAT.Injector.d
[+] Trojan/BAT.Injector.e
[+] Trojan/BAT.KillWin.bd!submit
[+] Trojan/BAT.Loader.h
[+] Trojan/BAT.Runner.bm!submit
[+] Trojan/Bladabindi.e!submit
[+] Trojan/FakeApp.aal
[+] Trojan/FakeApp.aan
[+] Trojan/FakeApp.aao
[+] Trojan/FakeApp.aap!submit
[+] Trojan/FakeApp.aaq!submit
[+] Trojan/FakeApp.aar!submit
[+] Trojan/FakeApp.aas!submit
[+] Trojan/FakeApp.aat!submit
[+] Trojan/Injector.cld!submit
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
[+] Trojan/MSIL.Obfuscated.jr!submit
[+] Trojan/Python.CoinMiner.j!submit
[+] Trojan/Python.KillDisk.e
[+] Trojan/Python.Popups.b!submit
[+] Trojan/Runner.fk!submit
[+] Trojan/ShellLoader.agr
[+] Trojan/ShellLoader.ags
[+] Trojan/ShellLoader.agt
[+] Trojan/ShellLoader.agu
[+] Trojan/ShellLoader.agv!submit
[+] Trojan/VBS.Agent.em!submit
[+] Trojan/W64.Loader.ab
[+] Trojan/W64.Loader.ac
[+] Trojan/W64.Loader.ad
[+] Trojan/W64.Loader.ae!submit
[+] Trojan/W64.Loader.af!submit
[+] Trojan/W64.Loader.ag!submit
[+] Trojan/W64.Loader.ah!submit
[+] Trojan/W64.Loader.ai!submit
[+] Trojan/W64.Merlin.a
[+] Trojan/W64.ReverseShell.a!submit
[+] TrojanDownloader/JS.Agent.ib
[+] TrojanDownloader/JS.Agent.ic!submit
[+] TrojanDownloader/Linux.Hajime.b
[+] TrojanDownloader/MSIL.Agent.aji!submit
[+] TrojanDownloader/PS.Agent.ex
[+] TrojanDownloader/PS.Agent.ey!submit
[+] TrojanDownloader/PS.Agent.ez!submit
[+] TrojanDownloader/Rugmi.ab
[+] TrojanDropper/Agent.ajt
[+] TrojanDropper/Agent.aju
[+] TrojanDropper/Agent.ajv
[+] TrojanDropper/Agent.ajw!submit
[+] TrojanSpy/MSIL.Stealer.ks
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

#### 黑名单哈希变更 ([troj.txt](data/1767093364.troj.txt))

新增: 77

**统计**:

| 指标 | 数值 |
|------|-----:|
| 检测项总数 | 66,375 |
| 黑名单哈希总数 | 186,535 |
| 白名单哈希总数 | 142,017 |
| PSET 记录 | 71,103 |
| TROJ 哈希 | 186,829 |
| HWL 记录 | 142,017 |

---

### 2025-12-29

**版本**: `1767007867` (2025-12-29 11:31:07 UTC)

#### 检测项变更 ([pset.txt](data/1767007867.pset.txt))

<details>
<summary>
新增: 105 | 移除: 60
</summary>

```
[+] Backdoor/Agent.nf!submit
[+] Backdoor/Agent.od!submit
[+] Backdoor/JS.Webshell.l!submit
[+] Backdoor/JSP.WebShell.bw
[+] Backdoor/Linux.Gafgyt.bx
[+] Backdoor/Linux.Mirai.ko!submit
[+] Backdoor/Lotok.nr
[+] Backdoor/Lotok.ns
[+] Backdoor/Lotok.nt
[+] Backdoor/Lotok.nu
[+] Backdoor/Lotok.nw!submit
[+] Backdoor/Lotok.nx!submit
[+] Backdoor/Python.Agent.m
[+] Backdoor/W64.Agent.i!submit
[+] Exploit/CVE-2016-0099.c
[+] Exploit/Vulndriver.s!submit
[+] HEUR:Trojan/Agent.clm!submit
[+] HEUR:Trojan/BAT.KillWin.bc!submit
[+] HEUR:Trojan/BAT.Loader.i!submit
[+] HEUR:Trojan/FakeApp.at!submit
[+] HEUR:Trojan/KillWin.e!submit
[+] HEUR:Trojan/ShellLoader.az
[+] HEUR:TrojanDownloader/Maloader.bl
[+] HEUR:TrojanDropper/Agent.aq
[+] HEUR:Worm/Autorun.ak
[+] HVM:Backdoor/Lotok.cd!submit
[+] HVM:Backdoor/Lotok.ce!submit
[+] HVM:Trojan/ShellLoader.ch
[+] HVM:Trojan/ShellLoader.ci!submit
[+] HVM:TrojanSpy/Stealer.p
[+] HackTool/ProxyTool.i
[+] HackTool/Python.RemoteExec.a!submit
[+] HackTool/W64.Merlin.a
[+] OMacro/Downloader.bov
[+] Rootkit/Inject.b!submit
[+] Rootkit/Injecter
[+] Trojan/Agent.clm!submit
[+] Trojan/BAT.Agent.gp!submit
[+] Trojan/BAT.Injector.d!submit
[+] Trojan/BAT.Injector.e!submit
[+] Trojan/BAT.Loader.h!submit
[+] Trojan/BAT.Runner.bl
[+] Trojan/CoinMiner.la!submit
[+] Trojan/FakeApp.aaf
[+] Trojan/FakeApp.aag
[+] Trojan/FakeApp.aah
[+] Trojan/FakeApp.aai
[+] Trojan/FakeApp.aaj
[+] Trojan/FakeApp.aak
[+] Trojan/FakeApp.aal!submit
[+] Trojan/FakeApp.aam!submit
[+] Trojan/FakeApp.aan!submit
[+] Trojan/FakeApp.aao!submit
[+] Trojan/HTML.Obfuscator.b
[+] Trojan/HiJack.yh
[+] Trojan/Hijack.yh
[+] Trojan/Hijack.yi
[+] Trojan/JS.Agent.gp!submit
[+] Trojan/JS.Agent.gq!submit
[+] Trojan/JS.Loader.d!submit
[+] Trojan/KillAV.db!submit
[+] Trojan/Linux.CoinMiner.du!submit
[+] Trojan/Linux.CoinMiner.dv!submit
[+] Trojan/Linux.DDoS.be!submit
[+] Trojan/Linux.Merlin.b
[+] Trojan/Linux.Mirai.fy
[+] Trojan/Linux.Mirai.fz!submit
[+] Trojan/Linux.Mirai.ga!submit
[+] Trojan/Linux.Mirai.gb!submits
[+] Trojan/Loader.mj
[+] Trojan/Loader.mk
[+] Trojan/Loader.ml
[+] Trojan/Loader.mm!submit
[+] Trojan/MSIL.Injector.qf!submit
[+] Trojan/MSIL.Obfuscated.jq!submit
[+] Trojan/Merlin.b
[+] Trojan/Merlin.c
[+] Trojan/PS.Loader.l
[+] Trojan/Python.KillDisk.e!submit
[+] Trojan/Runner.fj
[+] Trojan/ShellLoader.agp
[+] Trojan/ShellLoader.agr!submit
[+] Trojan/ShellLoader.ags!submit
[+] Trojan/ShellLoader.agt!submit
[+] Trojan/ShellLoader.agu!submit
[+] Trojan/Sonbokli.a
[+] Trojan/W64.Loader.ab!submit
[+] Trojan/W64.Loader.ac!submit
[+] Trojan/W64.Loader.ad!submit
[+] Trojan/W64.Merlin.a!submit
[+] TrojanDownloader/JS.Agent.ib!submit
[+] TrojanDownloader/Linux.Hajime.c
[+] TrojanDownloader/PS.Agent.ew
[+] TrojanDownloader/PS.Agent.ex!submit
[+] TrojanDownloader/Python.Netloader.h
[+] TrojanDownloader/Rugmi.ab!submit
[+] TrojanDownloader/VBS.Agent.ka
[+] TrojanDropper/Agent.ajr
[+] TrojanDropper/Agent.ajs
[+] TrojanDropper/Agent.ajt!submit
[+] TrojanDropper/Agent.aju!submit
[+] TrojanDropper/Agent.ajv!submit
[+] TrojanDropper/Linux.Exploit.a
[+] TrojanSpy/AutoIt.Stealer.k
[+] TrojanSpy/Python.SteamStealer.a
[-] Backdoor/JSP.WebShell.bw!submit
[-] Backdoor/Kingsoft.c!submit
[-] Backdoor/Linux.Gafgyt.bx!submit
[-] Backdoor/Lotok.nq
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

#### 黑名单哈希变更 ([troj.txt](data/1767007867.troj.txt))

新增: 81

#### 白名单哈希变更 ([hwl.txt](data/1767007867.hwl.txt))

新增: 1

**统计**:

| 指标 | 数值 |
|------|-----:|
| 检测项总数 | 66,339 |
| 黑名单哈希总数 | 186,458 |
| 白名单哈希总数 | 142,017 |
| PSET 记录 | 71,066 |
| TROJ 哈希 | 186,752 |
| HWL 记录 | 142,017 |

---

### 2025-12-28

**版本**: `1766920695` (2025-12-28 11:18:15 UTC)

#### 黑名单哈希变更 ([troj.txt](data/1766920695.troj.txt))

新增: 111

#### 白名单哈希变更 ([hwl.txt](data/1766920695.hwl.txt))

新增: 1

**统计**:

| 指标 | 数值 |
|------|-----:|
| 检测项总数 | 66,294 |
| 黑名单哈希总数 | 186,377 |
| 白名单哈希总数 | 142,016 |
| PSET 记录 | 71,018 |
| TROJ 哈希 | 186,671 |
| HWL 记录 | 142,016 |

---

### 2025-12-27

**版本**: `1766836824` (2025-12-27 12:00:24 UTC)

#### 黑名单哈希变更 ([troj.txt](data/1766836824.troj.txt))

新增: 99 | 移除: 1

**统计**:

| 指标 | 数值 |
|------|-----:|
| 检测项总数 | 66,294 |
| 黑名单哈希总数 | 186,266 |
| 白名单哈希总数 | 142,015 |
| PSET 记录 | 71,018 |
| TROJ 哈希 | 186,560 |
| HWL 记录 | 142,015 |

---

### 2025-12-26

**版本**: `1766750454` (2025-12-26 12:00:54 UTC)

#### 检测项变更 ([pset.txt](data/1766750454.pset.txt))

<details>
<summary>
新增: 108 | 移除: 53
</summary>

```
[+] Backdoor/Agent.mv
[+] Backdoor/JSP.WebShell.bw!submit
[+] Backdoor/Linux.Gafgyt.bx!submit
[+] Backdoor/Lotok.nk
[+] Backdoor/Lotok.nl
[+] Backdoor/Lotok.nm
[+] Backdoor/Lotok.nn
[+] Backdoor/Lotok.no
[+] Backdoor/Lotok.np
[+] Backdoor/Lotok.nq
[+] Backdoor/Lotok.nr!submit
[+] Backdoor/Lotok.ns!submit
[+] Backdoor/Lotok.nt!submit
[+] Backdoor/Lotok.nu!submit
[+] Backdoor/Lotok.nv
[+] Backdoor/Python.ReverseRAT.c
[+] Backdoor/Python.ReverseRAT.d!submit
[+] Exploit/CVE-2016-0099.c!submit
[+] HEUR:Trojan/Agent.ea
[+] HEUR:Trojan/Injector.cn
[+] HEUR:Trojan/MSIL.Obfuscated.jp
[+] HEUR:Trojan/ShellLoader.az!submit
[+] HEUR:TrojanDownloader/Maloader.bl!submit
[+] HEUR:TrojanDropper/Agent.aq!submit
[+] HEUR:Worm/AutoRun.aj
[+] HEUR:Worm/Autorun.ak!submit
[+] HVM:Backdoor/Lotok.bz
[+] HVM:Backdoor/Lotok.ca
[+] HVM:Backdoor/Lotok.cb
[+] HVM:Backdoor/Lotok.cc
[+] HVM:Trojan/ShellLoader.cg
[+] HVM:Trojan/ShellLoader.ch!submit
[+] HVM:TrojanSpy/Stealer.p!submit
[+] HackTool/CoinMiner!submit
[+] HackTool/GodPotato.b
[+] HackTool/ProxyTool.i!submit
[+] HackTool/W64.Merlin.a!submit
[+] OMacro/Downloader.bov!submit
[+] Ransom/Filecoder.eg
[+] Rootkit/Injecter!submit
[+] Trojan/BAT.Runner.bk!submit
[+] Trojan/BAT.Runner.bl!submit
[+] Trojan/FakeApp.aab
[+] Trojan/FakeApp.aac
[+] Trojan/FakeApp.aad
[+] Trojan/FakeApp.aae
[+] Trojan/FakeApp.aag!submit
[+] Trojan/FakeApp.aah!submit
[+] Trojan/FakeApp.aai!submit
[+] Trojan/FakeApp.aaj!submit
[+] Trojan/FakeApp.aak!submit
[+] Trojan/Glupteba.c
[+] Trojan/Gooxion.a!submit
[+] Trojan/HTML.Injector.n!submit
[+] Trojan/HTML.Obfuscator.b!submit
[+] Trojan/HiJack.yh!submit
[+] Trojan/Hijack.yh!submit
[+] Trojan/Hijack.yi!submit
[+] Trojan/Injector.clc
[+] Trojan/LNK.Starter.cv
[+] Trojan/Linux.CoinMiner.dt!submit
[+] Trojan/Linux.Merlin.b!submit
[+] Trojan/Linux.Mirai.fw
[+] Trojan/Loader.mh
[+] Trojan/Loader.mi
[+] Trojan/Loader.mj!submit
[+] Trojan/Loader.mk!submit
[+] Trojan/Loader.ml!submit
[+] Trojan/MSIL.Obfuscated.jp
[+] Trojan/Merlin.b!submit
[+] Trojan/Merlin.c!submit
[+] Trojan/PS.Loader.k
[+] Trojan/PS.Loader.l!submit
[+] Trojan/Python.Obfuscator.d
[+] Trojan/Runner.fi
[+] Trojan/Runner.fj!submit
[+] Trojan/ShellLoader.agf!submit
[+] Trojan/ShellLoader.agm
[+] Trojan/ShellLoader.agn
[+] Trojan/ShellLoader.ago
[+] Trojan/ShellLoader.agp!submit
[+] Trojan/ShellLoader.agq
[+] Trojan/Sonbokli.a!submit
[+] Trojan/VBS.Obfuscator.q
[+] Trojan/W64.Loader.aa
[+] Trojan/W64.Loader.z
[+] TrojanDownloader/Agent.bjw
[+] TrojanDownloader/Agent.bll
[+] TrojanDownloader/Linux.Hajime.b!submit
[+] TrojanDownloader/Linux.Hajime.c!submit
[+] TrojanDownloader/Linux.Mozi.c!submit
[+] TrojanDownloader/Linux.Netloader.f!submit
[+] TrojanDownloader/PS.Agent.et
[+] TrojanDownloader/PS.Agent.eu
[+] TrojanDownloader/PS.Agent.ev
[+] TrojanDownloader/PS.Agent.ew!submit
[+] TrojanDownloader/Python.Netloader.h!submit
[+] TrojanDownloader/VBS.Agent.ka!submit
[+] TrojanDownloader/W64.Agent.cl
[+] TrojanDownloader/W64.Agent.cm
[+] TrojanDropper/Agent.ajr!submit
[+] TrojanDropper/Agent.ajs!submit
[+] TrojanDropper/BAT.Agent.bl
[+] TrojanDropper/Linux.Exploit.a!submit
[+] TrojanDropper/Maloader.l
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
[-] HEUR:OMacro/Downloader.cu
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
[-] TrojanDownloader/Linux.Netloader.f
[-] TrojanDownloader/PS.Agent.et!submit
[-] TrojanDownloader/PS.Agent.eu!submit
[-] TrojanDownloader/PS.Agent.ev!submit
[-] TrojanDownloader/W64.Agent.cl!submit
[-] TrojanDownloader/W64.Agent.cm!submit
[-] TrojanDropper/BAT.Agent.bl!submit
[-] TrojanDropper/Linux.Exploit.a
[-] TrojanDropper/Maloader.l!submit
```

</details>

#### 黑名单哈希变更 ([troj.txt](data/1766750454.troj.txt))

新增: 152

**统计**:

| 指标 | 数值 |
|------|-----:|
| 检测项总数 | 66,294 |
| 黑名单哈希总数 | 186,168 |
| 白名单哈希总数 | 142,015 |
| PSET 记录 | 71,018 |
| TROJ 哈希 | 186,462 |
| HWL 记录 | 142,015 |

---

### 2025-12-25

**版本**: `1766655657` (2025-12-25 09:40:57 UTC)

#### 检测项变更 ([pset.txt](data/1766655657.pset.txt))

新增: 66,239

#### 黑名单哈希变更 ([troj.txt](data/1766655657.troj.txt))

新增: 186,016

#### 白名单哈希变更 ([hwl.txt](data/1766655657.hwl.txt))

新增: 142,015

**统计**:

| 指标 | 数值 |
|------|-----:|
| 检测项总数 | 66,239 |
| 黑名单哈希总数 | 186,016 |
| 白名单哈希总数 | 142,015 |
| PSET 记录 | 70,957 |
| TROJ 哈希 | 186,310 |
| HWL 记录 | 142,015 |

---

## 许可协议

本更新日志仅供参考。火绒病毒库为火绒安全软件所有。
