# psutil文档-中文版

源文档: <https://psutil.readthedocs.io/en/latest/>{target="_blank"}

基于版本 5.3.0

相关项目:

* GRR: GRR Rapid Response 是一个专注于远程实时取证的事件响应框架。
  
    SourceCode: <https://github.com/google/grr>{target="_blank"} - google

* osquery: osquery 是一个 SQL 驱动的操作系统检测、监控和分析框架。适用于 Linux、macOS、Windows 和 FreeBSD。
  
    SourceCode: <https://github.com/osquery/osquery>{target="_blank"}

* Glances: Glances 是一个跨平台的监控工具，旨在通过curses 或基于Web 的界面呈现大量监控信息。 该信息根据用户界面的大小动态调整。
  
    SourceCode: <https://github.com/nicolargo/glances>{target="_blank"}

* psDash: psdash 是 Linux 的系统信息 Web 仪表板，使用主要由 psutil 提供的数据 - 因此得名。
  
    SourceCode: <https://github.com/Jahaja/psdash>{target="_blank"}

* Ajenti 是一个 Linux 和 BSD 模块化服务器管理面板。 Ajenti 2 提供了一个新的界面和更好的架构，使用 Python3 和 AngularJS 开发。
  
    SourceCode: <https://github.com/ajenti/ajenti>{target="_blank"}

* Home Assistant(家庭助手): 将本地控制和隐私放在首位的家庭自动化开源项目。 由全球修补匠和 DIY 爱好者社区提供支持。 非常适合在 Raspberry Pi 或本地服务器上运行。

    SourceCode: <https://github.com/home-assistant/core>{target="_blank"}

## **快速链接**

!!! info "注"

    这里的链接是指向到原网站的。

* [主页](https://github.com/giampaolo/psutil){target="_blank"}
* [安装](https://github.com/giampaolo/psutil/blob/master/INSTALL.rst){target="_blank"}
* [讨论](http://groups.google.com/group/psutil/topics){target="_blank"}
* [下载](https://pypi.org/project/psutil/#files){target="_blank"}
* [博客](https://gmpy.dev/tags/psutil){target="_blank"}
* [贡献](https://github.com/giampaolo/psutil/blob/master/CONTRIBUTING.md){target="_blank"}
* [开发者指南](https://github.com/giampaolo/psutil/blob/master/docs/DEVGUIDE.rst){target="_blank"}
* [](https://github.com/giampaolo/psutil/blob/master/HISTORY.rst){target="_blank"}

## **关于** (About)

psutil (python版的系统和进程实用包) 是一个跨平台库, 可用于在**Python**程序中检索正在运行的**进程**和**系统利用率**(CPU, 内存, 磁盘, 网络, 设备)的相关信息。该包实现了由Unix命令行工具提供的许多功能，例如: `ps`, `top`, `lsof`, `netstat`, `ifconfig`, `who`, `df`, `kill`, `free`, `nice`, `ionice`, `iostat`, `iotop`, `uptime`, `pidof`, `tty`, `taskset`, `pmap`. psutil 目前支持下面这些平台:

* **Linux**
* **Windows**
* **macOS**
* **FreeBSD**, **OpenBSD**, **NetBSD**
* **Sun Solaris**
* **AIX**

支持的Python版本是 **2.6**, **2.7** 和 **3.4+**. [PyPy](http://pypy.org/) 也可以工作.

当前psutil文档是作为单个HTML页面分发(发布)的。

## **基金** (Funding)

尽管psutil是免费软件并且会一直是，但该项目会从一些资金赞助中得到支持。就时间上而言, 持续解决漏洞报告和维护会花费我大量时间，几乎无法持续。如果您是一家大量使用psutil的商业公司, 您可以考虑通过[GitHub][github], [Open Collective][openCollective] 或 [PayPal][paypal]成为本项目的赞助商，同时会将您公司的logo展示在这儿和psutil文档中。

[github]: https://github.com/sponsors/giampaolo '赞助 giampaolo'
[openCollective]: https://opencollective.com/psutil '赞助 psutil'
[paypal]: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=A9ZS7PKKRM3S8 '赞助 giampaolo'

### 赞助 (Sponsors)

<p>
    <a href="https://tidelift.com/subscription/pkg/pypi-psutil?utm_source=pypi-psutil&amp;utm_medium=referral&amp;utm_campaign=readme">
        <img width="185" src="https://github.com/giampaolo/psutil/raw/master/docs/_static/tidelift-logo.svg?s=185&v=4">
    </a>
    &nbsp;&nbsp;
    <a href="https://sansec.io/">
        <img src="https://sansec.io/assets/images/logo.svg">
    </a>
</p>

添加您的[logo](https://github.com/sponsors/giampaolo)

### 支持 (Supporters)

<span>
  <a href="https://github.com/dbwiddis">
    <img height="40" width="40" title="Daniel Widdis" src="https://avatars1.githubusercontent.com/u/9291703?s=88&amp;v=4">
  </a>
  <a href="https://github.com/aristocratos">
    <img height="40" width="40" title="aristocratos" src="https://avatars3.githubusercontent.com/u/59659483?s=96&amp;v=4">
  </a>
  <a href="https://github.com/cybersecgeek">
    <img height="40" width="40" title="cybersecgeek" src="https://avatars.githubusercontent.com/u/12847926?v=4">
  </a>
  <a href="https://github.com/scoutapm-sponsorships">
    <img height="40" width="40" title="scoutapm-sponsorships" src="https://avatars.githubusercontent.com/u/71095532?v=4">
  </a>
  <a href="https://opencollective.com/chenyoo-hao">
    <img height="40" width="40" title="Chenyoo Hao" src="https://images.opencollective.com/chenyoo-hao/avatar/40.png">
  </a>
  <a href="https://opencollective.com/alexey-vazhnov">
    <img height="40" width="40" title="Alexey Vazhnov" src="https://images.opencollective.com/alexey-vazhnov/daed334/avatar/40.png">
  </a>
</span>

添加你的[头像](https://github.com/sponsors/giampaolo)

## **安装** (Install)

在 Linux, Windows, macOS:

```shell
pip install psutil
```

对于其他平台，请参阅更详细的[安装说明](https://github.com/giampaolo/psutil/blob/master/INSTALL.rst)

## **系统** (System related functions)

### CPU

#### **执行时间**

**psutil.cpu_times(percpu=False)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.cpu_times) <a name="psutil.cpu_times"></a>

返回一个命名元组的CPU时间信息，每个属性代表 CPU 在给定模式下花费的秒数。 属性可用性因平台而异。

* **user**: 进程在用户模式(user mode)下执行所花费的时间； 在 Linux 上，这也包括访客时间(guest time)。
* **system**: 进程在内核模式(kernel mode)下执行所花费的时间。
* **idle**: 空闲时间。

特定平台的字段:

* **nice** (UNIX): niced(优先) 进程在用户模式(user mode)下所花费的时间; 在 Linux 上，这也包括访客优先时间(guest_nice time)。
* **iowait** (Linux): 等待 I/O 完成所花费的时间。 这不计入空闲时间中。
* **irq** (Linux, BSD): 服务硬件中断所花费的时间。
* **softirq** (Linux): 服务软件中断所花费的时间。
* **steal** (Linux 2.6.11+): 在虚拟化环境中运行的其他操作系统所花费的时间。
* **guest** (Linux 2.6.24+): 在 Linux 内核的控制下为客户操作系统运行虚拟 CPU 所花费的时间
* **guest_nice** (Linux 3.2.0+): niced(优先) 访客进程所花费的时间 (用于在 Linux 内核控制下的客户操作系统的虚拟 CPU)
* **interrupt** (Windows): 服务硬件中断所花费的时间 ( 类似于 UNIX 上的“irq”)
* **dpc** (Windows): 服务延迟过程调用服务中断 (DPC) 所花费的时间； DPC 是运行优先级低于标准中断(interrupts)的中断。

**译注**: DPC是“Deferred Procedure Call”的缩写，意为推迟了的过程（函数）调用。参考: [延迟过程调用][windows-dpc]

当 _percpu_ 为 `True` 时，返回系统上每个逻辑 CPU 的命名元组列表。 列表的第一个元素指的是第一个 CPU，第二个元素指的是第二个 CPU，依此类推。 列表的顺序在调用之间是一致的。 Linux 上的示例输出：

```python
>>> import psutil
>>> psutil.cpu_times()
scputimes(user=17411.7, nice=77.99, system=3797.02, idle=51266.57, iowait=732.58, irq=0.01, softirq=142.43, steal=0.0, guest=0.0, guest_nice=0.0)
```

4.1.0 版本中更新: 对于Windows平台新增 **_interrupt_** 和 **_dpc_** 字段.

**⚠️警告**: CPU 时间总是应该随着时间的推移而增加，或者至少保持不变，那是因为时间不能倒流。令人惊讶的是，有时情况并非如此（至少在 Windows 和 Linux 上）, 参考 [#1210][issue-1210].

[issue-1210]: https://github.com/giampaolo/psutil/issues/1210#issuecomment-363046156 "CPU steal stuck at 100%"
[windows-dpc]: https://zh.wikipedia.org/wiki/%E5%BB%B6%E8%BF%9F%E8%BF%87%E7%A8%8B%E8%B0%83%E7%94%A8 "延迟过程调用"

#### **利用率**

**psutil.cpu_percent(interval=None, percpu=False)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.cpu_percent) <a name="psutil.cpu_percent"></a>

返回一个浮点数，以百分比形式表示当前系统范围内的 CPU 利用率。 当间隔 > `0.0` 时比较间隔前后经过的系统 CPU 时间（阻塞）。 当间隔为 `0.0` 或 `None` 时，比较自上次调用或模块导入以来经过的系统 CPU 时间，立即返回。这意味着第一次调用它时，它会返回一个你应该忽略的无意义的 `0.0` 值。在这种情况下，为了准确起见，建议在两次调用之间至少间隔 `0.1` 秒来调用此函数。当 **_percpu_** 为 `True` 时，返回一个浮点数列表，以百分比形式表示每个 CPU 的利用率。 列表的第一个元素指的是第一个 CPU，第二个元素指的是第二个 CPU，依此类推。列表的顺序在调用之间是一致的。

```python
>>> import psutil
>>> # blocking
>>> psutil.cpu_percent(interval=1)
2.0
>>> # non-blocking (percentage since last call)
>>> psutil.cpu_percent(interval=None)
2.9
>>> # blocking, per-cpu
>>> psutil.cpu_percent(interval=1, percpu=True)
[2.0, 1.0]
>>>
```

**⚠️警告**: 第一次使用 **_interval_** = `0.0` 或 `None` 调用此函数时，它将返回一个无意义的 `0.0` 值，您应该忽略该值。

#### **时间利用率详细**

**psutil.cpu_times_percent(interval=None, percpu=False)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.cpu_times_percent)

就像 [cpu_percent()](#psutil.cpu_percent) ，但提供 [psutil.cpu_times(percpu=True)](#psutil.cpu_times) 返回的每个 CPU 的**_时间利用率百分比。interval_** 和 **_percpu_** 参数的含义与 [cpu_percent()](#psutil.cpu_percent) 中的含义相同。 在 Linux 上，“**guest**”和“**guest\_nice**”百分比不计入“**user**”和“**user\_nice**”百分比。

**⚠️警告**: 第一次使用 **_interval_** = `0.0` 或 `None` 调用此函数时，它将返回一个无意义的 `0.0` 值，应该忽略该值。

_4.1.0 版本中更新_: 对于Windows平台返回值将包含两个新字段 `interrupt` 和 `dpc` 。

#### **核心数量**

**psutil.cpu_count(logical=True)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.cpu_count) <a name="psutil.cpu_count"></a>

返回系统中逻辑 CPU 的数量（与 Python 3.4 中的 [os.cpu_count][os.cpu_count] 相同）或 `None` 如果未确定。“逻辑 CPU”是指物理内核数乘以每个内核上可以运行的线程数（这称为超线程）。如果 **_logical_** 为 False，则仅返回物理内核的数量，如果未确定，则返回 `None`。 在 OpenBSD 和 NetBSD 上 `psutil.cpu_count(logical=False)` 总是返回 `None` 。下面是具有 2 个内核 + 超线程的系统示例:

[os.cpu_count]: https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count"

```python
>>> import psutil
>>> psutil.cpu_count()
4
>>> psutil.cpu_count(logical=False)
2
```

请注意， `psutil.cpu_count()` 可能不一定等于当前进程可以使用的实际 CPU 数量。如果进程 CPU 亲和性已更改、正在使用 Linux cgroups 或（在 Windows 的情况下）在使用处理器组或具有超过 64 个 CPU 的系统上，这可能会有所不同。 可用 CPU 的数量可以通过以下方式获得：

```python
>>> len(psutil.Process().cpu_affinity())
1
psutil.cpu_stats()
```

#### **统计信息**

**psutil.cpu_stats()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.cpu_stats)

将各种 CPU 统计信息作为命名元组返回:

* **ctx_switches**: 自启动以来的上下文切换次数（自愿 + 非自愿）.
* **interrupts**: 自启动以来的中断数.
* **soft_interrupts**: 自启动以来的软件中断数。 在 Windows 和 SunOS 上始终设置为 0.
* **syscalls**: 自启动以来的系统调用数。 在 Linux 上始终设置为 0.

样例 (Linux):

```python
>>> import psutil
>>> psutil.cpu_stats()
scpustats(ctx_switches=20455687, interrupts=6598984, soft_interrupts=2134212, syscalls=0)
```

_4.1.0 版本中新增。_

#### **频率信息**

**psutil.cpu_freq(percpu=False)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.cpu_freq)

将 CPU 频率作为命名元组返回，包括以 Mhz 表示的当前、最小和最大频率。 在 Linux 中当前频率报告实时值，在所有其他平台上它代表标称的“固定”值。如果 **_percpu_** 为 `True` 并且系统支持 per-cpu 频率检索（仅限 Linux），则为每个 CPU 返回一个频率列表，如果不是，则返回一个包含单个元素的列表。如果无法确定最小值和最大值，则将它们设置为 0。

样例 (Linux):

```python
>>> import psutil
>>> psutil.cpu_freq()
scpufreq(current=931.42925, min=800.0, max=3500.0)
>>> psutil.cpu_freq(percpu=True)
[scpufreq(current=2394.945, min=800.0, max=3500.0),
 scpufreq(current=2236.812, min=800.0, max=3500.0),
 scpufreq(current=1703.609, min=800.0, max=3500.0),
 scpufreq(current=1754.289, min=800.0, max=3500.0)]
```

可用平台: Linux, macOS, Windows, FreeBSD

_5.1.0版本中新增。_

_5.5.1版本中更新：添加了 FreeBSD 支持。_

#### **负载信息**

**psutil.getloadavg()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.getloadavg)

以元组形式返回过去 1、5 和 15 分钟的平均系统负载。“负载”表示处于可运行状态的进程，要么使用 CPU，要么等待使用 CPU（例如，等待磁盘 I/O）。在 UNIX 系统上，这依赖于 [os.getloadavg][os.getloadavg]。在 Windows 上，这是通过使用 Windows API 来模拟的，该 API 产生一个线程，该线程保持在后台运行并每 5 秒更新一次结果，模仿 UNIX 行为。因此，在 Windows 上，第一次调用它，在接下来的 5 秒内，它将返回一个无意义的 (`0.0, 0.0, 0.0`) 元组。返回的数字仅在与系统上安装的 CPU 内核数相关时才有意义。 因此，例如，具有 10 个逻辑 CPU 的系统上的值 3.14 意味着系统负载在过去 N 分钟内为 31.4%。

[os.getloadavg]: https://docs.python.org/zh-cn/3/library/os.html#os.getloadavg "获得平均负载"

```python
>>> import psutil
>>> psutil.getloadavg()
(3.14, 3.89, 4.67)
>>> psutil.cpu_count()
10
>>> # percentage representation
>>> [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
[31.4, 38.9, 46.7]
```

可用平台: Unix, Windows

_5.6.2 版本中新增。_

### 内存 (Memory)

#### **运行内存**

**psutil.virtual_memory()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.virtual_memory)

以包含以下字段的命名元组形式返回有关系统内存使用情况的统计信息，以**字节**为单位。 主要指标：

* `total`: 总物理内存（独占交换）。
* `available`: 可以立即分配给进程而无需系统进行交换的内存。这是通过根据平台对不同的内存值求和来计算的，它应该用于以跨平台方式监控实际内存使用情况。

其他指标:

* `used`: 使用的内存，计算方式因平台而异，仅供参考。 **total - free** 不一定匹配 **used**。
* `free`: 根本没有使用（归零）的随时可用的内存； 请注意，这并不反映实际可用内存（请改用可用(`available`)内存）。 **total - used** 不一定匹配 **free**。
* `active` (UNIX): 当前正在使用或最近使用的内存，因此它在 RAM 中。
* `inactive` (UNIX): 标记为未使用的内存。
* `buffers` (Linux, BSD): 缓存文件系统元数据等内容。
* `cached` (Linux, BSD): 缓存各种东西。
* `shared` (Linux, BSD): 可以被多个进程同时访问的内存。
* `slab` (Linux): 内核数据结构缓存。
* `wired` (BSD, macOS): 标记为始终保留在 RAM 中的内存。 它永远不会移动到磁盘。

已用(`used`)和可用(`available`)的总和不一定等于总数(`total`)。 在 Windows 上可用(`available`)和免费(`free`)是一样的。 请参阅 [meminfo.py][meminfo.py] 脚本并提供了有关如何以可读形式**转换字节**的示例。

[meminfo.py]: https://github.com/giampaolo/psutil/blob/master/scripts/meminfo.py "meminfo.py"

**注意**: 如果您只想知道跨平台方式还剩下多少物理内存，只需依赖可用(`available`)字段即可。

```python
>>> import psutil
>>> mem = psutil.virtual_memory()
>>> mem
svmem(total=10367352832, available=6472179712, percent=37.6, used=8186245120, free=2181107712, active=4748992512, inactive=2758115328, buffers=790724608, cached=3500347392, shared=787554304, slab=199348224)
>>>
>>> THRESHOLD = 100 * 1024 * 1024  # 100MB
>>> if mem.available <= THRESHOLD:
...     print("warning")
...
>>>
```

_4.2.0 版本中修改: 在Linux中新增了 `shared` 指标。_

_5.4.4 版本中修改: 在Linux中新增了 `slab` 指标。_

#### **交换内存**

**psutil.swap_memory()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.swap_memory)

将系统交换内存统计信息作为命名元组返回，包括以下字段：

* `total`: 以字节为单位的总交换内存
* `used`: 使用的交换内存（以字节为单位）
* `free`: 以字节为单位的空闲交换内存
* `percent`: 百分比使用率计算为 `(total - available) / total * 100`
* `sin`: 系统从磁盘换入的字节数（累计）
* `sout`: 系统从磁盘换出的字节数（累计）

Windows 上的 **sin** 和 **sout** 始终设置为 0。参阅 [meminfo.py][meminfo.py] 脚本，同时提供了有关如何以可读的形式**转换字节**的示例。

```python
>>> import psutil
>>> psutil.swap_memory()
sswap(total=2097147904L, used=886620160L, free=1210527744L, percent=42.3, sin=1050411008, sout=1906720768)
```

_5.2.3 版本中修改: 在 Linux 上，此函数依赖 /proc fs 而不是 sysinfo() 系统调用，以便它可以与 `psutil.PROCFS_PATH` 结合使用，以检索有关 Linux 容器（例如 Docker 和 Heroku）的内存信息。_

### 磁盘 (Disks)

#### **磁盘挂载信息**

**psutil.disk_partitions(all=False)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.disk_partitions)

将所有挂载的磁盘分区作为命名元组列表返回，包括设备、挂载点和文件系统类型，类似于 UNIX 上的“`df`”命令。如果 **_all_** 参数都为 `False` ，它会尝试仅区分和返回物理设备（例如硬盘、CD-ROM 驱动器、USB 密钥）并忽略所有其他设备（例如伪(pseudo)、内存、重复、无法访问的文件系统）。请注意， **_all_** 参数并非在所有系统上都完全可靠（例如，在 BSD 上，此参数被忽略）。请参阅提供示例用法的 [disk_usage.py][disk_usage.py] 脚本。 返回具有以下字段的命名元组列表：

[disk_usage.py]: https://github.com/giampaolo/psutil/blob/master/scripts/disk_usage.py "disk_usage.py"

* `device`: 设备路径（例如“`/dev/hda1`”）。 在 Windows 上，这是驱动器号（例如“`C:\\`”）。
* `mountpoint`: 挂载点路径（例如“`/`”）。 在 Windows 上，这是驱动器号（例如“`C:\\`”）。
* `fstype`: 分区文件系统（例如 UNIX 上的“`ext3`”或 Windows 上的“`NTFS`”）。
* `opts`: 一个逗号分隔的字符串，指示驱动器/分区的不同挂载选项。 平台相关。
* `maxfile`: 文件名可以具有的最大长度。
* `maxpath`: 路径名（目录名 + 基本文件名）的最大长度。

```python
>>> import psutil
>>> psutil.disk_partitions()
[sdiskpart(device='/dev/sda3', mountpoint='/', fstype='ext4', opts='rw,errors=remount-ro', maxfile=255, maxpath=4096),
 sdiskpart(device='/dev/sda7', mountpoint='/home', fstype='ext4', opts='rw', maxfile=255, maxpath=4096)]
```

_5.7.4 版本中修改: 新增 **maxfile** 和 **maxpath** 字段_

#### **磁盘利用率**

**psutil.disk_usage(path)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.disk_usage)

返回有关包含给定路径的分区的磁盘使用统计信息作为命名元组，包括以字节表示的总空间(**total**)、已用空间(**used**)和可用空间(**free**)，以及使用百分比(**percentage** usage)。如果路径(**_path_**)不存在，则引发 `OSError`。 从 Python 3.3 开始，这也可以作为 [shutil.disk_usage][shutil.disk_usage] 使用（参见 [BPO-12442][BPO-12442]）。 请参阅提供示例用法的 [disk_usage.py][disk_usage.py] 脚本。

[shutil.disk_usage]: https://docs.python.org/zh-cn/3/library/shutil.html#shutil.disk_usage. "shutil.disk_usage"
[BPO-12442]: https://bugs.python.org/issue12442 "BPO-12442"

```python
>>> import psutil
>>> psutil.disk_usage('/')
sdiskusage(total=21378641920, used=4809781248, free=15482871808, percent=22.5)
```

**注意**: UNIX 通常为 root 用户保留 5% 的总磁盘空间。UNIX 上的 **_total_** 和 **_used_** 字段是指总空间和已用空间，而 **_free_** 表示用户可用的空间，**_percent_** 表示用户利用率（参见[源代码][source-code]）。这就是为什么百分比(**_percent_**)值可能看起来比您预期的大 5%。 另请注意，这 4 个值都与“`df`” 命令行程序一致的。

[source-code]: https://github.com/giampaolo/psutil/blob/3dea30d583b8c1275057edb1b3b720813b4d0f60/psutil/_psposix.py#L123 "source-code"

_4.3.0 版本中修改: 百分比(**percent**)值考虑了`root`保留空间。_

#### **磁盘IO统计**

**psutil.disk_io_counters(perdisk=False, nowrap=True)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.disk_io_counters)

将系统范围的磁盘 I/O 统计信息作为命名元组返回，包括以下字段：

* `read_count`: 读取次数
* `write_count`: 写入次数
* `read_bytes`: 读取的字节数
* `write_bytes`: 写入的字节数

特定于平台的字段:

* `read_time`(除了 NetBSD 和 OpenBSD): 从磁盘读取所花费的时间（以毫秒为单位）
* `write_time`(除了 NetBSD 和 OpenBSD): 写入磁盘所花费的时间（以毫秒为单位）
* `busy_time`(Linux, FreeBSD):  花费在实际 I/O 上的时间（以毫秒为单位）
* `read_merged_count` (Linux): 合并读取的数量（参见 [iostats][iostats] 文档）
* `write_merged_count` (Linux): 合并写入的数量（请参阅 [iostats][iostats] 文档）

[iostats]: https://www.kernel.org/doc/Documentation/iostats.txt "iostats"

如果 **_perdisk_** 为 `True` ，则将系统上安装的每个物理磁盘的相同信息作为字典返回，分区名称作为键，上面描述的命名元组作为值。有关示例应用程序，参见 [iotoop.py][iotoop.py]。在某些系统（例如 Linux）上，在非常繁忙或寿命很长的系统上，内核返回的数字可能会溢出并换行（从零开始）。如果 **_nowrap_** 为 `True`，psutil 将在函数调用中检测并调整这些数字，并将“旧值”添加到“新值”，以便返回的数字始终增加或保持不变，但永远不会减少。`disk_io_counters.cache_clear()` 可用于使 **_nowrap_** 缓存无效。 在 Windows 上，可能需要首先从 cmd.exe 发出 `diskperf -y` 命令以启用 IO 计数器。 在无盘机器上，如果 **_perdisk_** 为 `True`，此函数将返回 `None` 或 `{}`。

[iotoop.py]: https://github.com/giampaolo/psutil/blob/master/scripts/iotop.py "io top"

```python
>>> import psutil
>>> psutil.disk_io_counters()
sdiskio(read_count=8141, write_count=2431, read_bytes=290203, write_bytes=537676, read_time=5868, write_time=94922)
>>>
>>> psutil.disk_io_counters(perdisk=True)
{'sda1': sdiskio(read_count=920, write_count=1, read_bytes=2933248, write_bytes=512, read_time=6016, write_time=4),
 'sda2': sdiskio(read_count=18707, write_count=8830, read_bytes=6060, write_bytes=3443, read_time=24585, write_time=1572),
 'sdb1': sdiskio(read_count=161, write_count=0, read_bytes=786432, write_bytes=0, read_time=44, write_time=0)}
```

**注意**: 在 Windows 上，可能需要先执行“`diskperf -y`”命令，否则该函数将找不到任何磁盘。

_5.3.0 版本中修改: 由于新的 nowrap 参数，数字不再在调用之间换行（从零开始）。_

_4.0.0 版本中修改: 添加了 **busy_time**(Linux, FreeBSD),**read_merged_count**和**write_merged_count** (Linux) 字段。_

_4.0.0 版本中修改: NetBSD 不再有 **read_time**和**write_time** 字段。_

### 网络 (Network)

#### **网络统计信息**

**psutil.net_io_counters(pernic=False, nowrap=True)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.net_io_counters)

将系统范围的网络 I/O 统计信息作为命名元组返回，包括以下属性：

* `bytes_sent`: 发送的字节数
* `bytes_recv`: 接收的字节数
* `packets_sent`: 发送的数据包数
* `packets_recv`: 收到的数据包数
* `errin`: 接收时的错误总数
* `errout`: 发送时的错误总数
* `dropin`: 丢弃的传入数据包总数
* `dropout`: 丢弃的传出数据包总数（在 macOS 和 BSD 上始终为 0）

如果 **_pernic_** 为 True，则将系统上安装的每个网络接口的相同信息作为字典返回，其中网络接口名称作为键，上面描述的命名元组作为值。在某些系统（例如 Linux）上，在非常繁忙或寿命很长的系统上，内核返回的数字可能会溢出并换行（从零开始）。如果 **_nowrap_** 为 `True` ，psutil 将在函数调用中检测并调整这些数字，并将“旧值”添加到“新值”，以便返回的数字始终增加或保持不变，但永远不会减少。`net_io_counters.cache_clear()` 可用于使 **_nowrap_** 缓存无效。 在没有网络接口的机器上，如果 **_pernic_** 为 `True` ，此函数将返回 `None` 或 `{}`。

```python
>>> import psutil
>>> psutil.net_io_counters()
snetio(bytes_sent=14508483, bytes_recv=62749361, packets_sent=84311, packets_recv=94888, errin=0, errout=0, dropin=0, dropout=0)
>>>
>>> psutil.net_io_counters(pernic=True)
{'lo': snetio(bytes_sent=547971, bytes_recv=547971, packets_sent=5075, packets_recv=5075, errin=0, errout=0, dropin=0, dropout=0),
'wlan0': snetio(bytes_sent=13921765, bytes_recv=62162574, packets_sent=79097, packets_recv=89648, errin=0, errout=0, dropin=0, dropout=0)}
```

示例应用程序另请参阅 [nettop.py][nettop.py] 和 [ifconfig.py][ifconfig.py] 。

[nettop.py]: https://github.com/giampaolo/psutil/blob/master/scripts/nettop.py "nettop.py"
[ifconfig.py]: https://github.com/giampaolo/psutil/blob/master/scripts/ifconfig.py "ifconfig.py"

*5.3.0 版本中修改: 由于新的 **_nowrap_** 参数，数字不再在调用之间换行（从零开始）。*

#### **网络连接信息**

**psutil.net_connections(kind='inet')** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.net_connections) <a name="psutil.net_connections"></a>

以命名元组列表的形式返回系统范围的套接字连接。 每个命名元组提供 7 个属性：

* `fd`: 套接字文件描述符。 如果连接指向当前进程，则可以将其传递给 [socket.fromfd][socket.fromfd] 以获得可用的套接字对象。 在 Windows 和 SunOS 上，这始终设置为 `-1`。
* `family`: 地址族，[AF_INET][AF_INET]、[AF_INET6][AF_INET6] 或 [AF_UNIX][AF_UNIX]。
* `type`: 地址类型，[SOCK_STREAM][SOCK_STREAM][SOCK_STREAM]、[SOCK_DGRAM][SOCK_DGRAM] 或 [SOCK_SEQPACKET][SOCK_SEQPACKET]。
* `laddr`: 在 [AF_UNIX][AF_UNIX] 套接字的情况下，本地地址作为`(ip, port)`命名元组或路径(`path`)。 对于 UNIX 套接字，请参阅下面的注释。
* `raddr`: 在 [AF_UNIX][AF_UNIX] 套接字的情况下，远程地址作为`(ip, port)`命名元组或绝对路径(`path`)。当远程端点未连接时，您将获得一个空元组 (AF_INET*) 或 `""` (AF_UNIX)。 对于 UNIX 套接字，请参阅下面的注释。
* `status`: 表示 TCP 连接的状态。 返回值是 [psutil.CONN_*][psutil.CONN_*] 常量之一（字符串）。 对于 UDP 和 UNIX 套接字，这始终是 `psutil.CONN_NONE`。
* `pid`: 如果可检索打开套接字的进程的PID，否则为`None`。 在某些平台（例如 Linux）上，此字段的可用性根据进程权限（需要 root）而变化。

[socket.fromfd]: https://docs.python.org/3/library/socket.html#socket.fromfd "socket.fromfd"
[AF_INET]: https://docs.python.org/zh-cn/3/library/socket.html#socket.AF_INET "AF_INET"
[AF_INET6]: https://docs.python.org/zh-cn/3/library/socket.html#socket.AF_INET6 "AF_INET6"
[AF_UNIX]: https://docs.python.org/zh-cn/3/library/socket.html#socket.AF_UNIX "AF_UNIX"
[SOCK_STREAM]: https://docs.python.org/zh-cn/3/library/socket.html#socket.SOCK_STREAM "SOCK_STREAM"
[SOCK_DGRAM]: https://docs.python.org/zh-cn/3/library/socket.html#socket.SOCK_DGRAM "SOCK_DGRAM"
[SOCK_SEQPACKET]: https://docs.python.org/zh-cn/3/library/socket.html#socket.SOCK_SEQPACKET "SOCK_SEQPACKET"
[psutil.CONN_*]: https://psutil.readthedocs.io/en/latest/#connections-constants "psutil.CONN_* 常量"

**_kind_** 参数是一个字符串，用于过滤符合以下条件的连接：

| Kind 值 | 连接使用                       |
| ------- | ------------------------------ |
| "inet"  | IPv4 和 IPv6                   |
| "inet4" | IPv4                           |
| "inet6" | IPv6                           |
| "tcp"   | TCP                            |
| "tcp4"  | 基于 IPv4 的 TCP               |
| "tcp6"  | 基于 IPv6 的 TCP               |
| "udp"   | UDP                            |
| "udp4"  | 基于 IPv4 的 UDP               |
| "udp6"  | 基于 IPv6 的 UDP               |
| "unix"  | UNIX 套接字（UDP 和 TCP 协议） |
| "all"   | 所有可能的族和协议的总和       |

在 macOS 和 AIX 上，此功能需要 root 权限。 要获得每个进程的连接，请使用 [Process.connections()](#Process.connections)。 另请参阅 [netstat.py][netstat.py] 示例脚本。 例子：

[netstat.py]: https://github.com/giampaolo/psutil/blob/master/scripts/netstat.py "netstat.py"

```python
>>> import psutil
>>> psutil.net_connections()
[pconn(fd=115, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=addr(ip='10.0.0.1', port=48776), raddr=addr(ip='93.186.135.91', port=80), status='ESTABLISHED', pid=1254),
 pconn(fd=117, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=addr(ip='10.0.0.1', port=43761), raddr=addr(ip='72.14.234.100', port=80), status='CLOSING', pid=2987),
 pconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=addr(ip='10.0.0.1', port=60759), raddr=addr(ip='72.14.234.104', port=80), status='ESTABLISHED', pid=None),
 pconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=addr(ip='10.0.0.1', port=51314), raddr=addr(ip='72.14.234.83', port=443), status='SYN_SENT', pid=None)
 ...]
```

**注释**: (macOS 和 AIX) 除非以 root 用户身份运行，否则 [psutil.AccessDenied](#psutil.AccessDenied) 异常总是会抛出。 这是操作系统的限制，`lsof` 也是如此。

**注释**: (Solaris) 不支持 UNIX 套接字。

**注释**: (Linux, FreeBSD) UNIX 套接字的“raddr”字段始终设置为`“”`。 这是操作系统的限制。

**注释**: (OpenBSD) UNIX 套接字的“laddr”和“raddr”字段始终设置为`“”`。 这是操作系统的限制。

_2.1.0 版本中新增._

*5.3.0 版本中修改: : 套接字“fd”现在设置为实数而不是 `-1`。*

_5.3.0 版本中修改: : “laddr”和“raddr”被命名为元组。_

#### **网卡地址信息**

**psutil.net_if_addrs()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.net_if_addrs) <a name="psutil.net_if_addrs"></a>

返回与系统上安装的每个 NIC（网络接口卡）关联的地址作为字典，其键是 NIC 名称，值是分配给 NIC 的每个地址的命名元组列表。 每个命名元组包括 5 个字段：

* `family`: 地址族，[AF_INET][AF_INET] 或 [AF_INET6][AF_INET6] 或 [psutil.AF_LINK](#psutil.AF_LINK)，指的是 MAC 地址。
* `address`: 主 NIC 地址（始终设置）。
* `netmask`: 网络掩码地址（可能是 `None` ）。
* `broadcast`: 广播地址（可能是 `None` ）。
* `ptp`: 代表“点对点”(point to point)； 它是点对点接口（通常是 VPN）上的目标地址。 广播和 ptp 是互斥的。 可能为 `None`。

样例:

```python
>>> import psutil
>>> psutil.net_if_addrs()
{'lo': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast='127.0.0.1', ptp=None),
        snicaddr(family=<AddressFamily.AF_INET6: 10>, address='::1', netmask='ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', broadcast=None, ptp=None),
        snicaddr(family=<AddressFamily.AF_LINK: 17>, address='00:00:00:00:00:00', netmask=None, broadcast='00:00:00:00:00:00', ptp=None)],
 'wlan0': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='192.168.1.3', netmask='255.255.255.0', broadcast='192.168.1.255', ptp=None),
           snicaddr(family=<AddressFamily.AF_INET6: 10>, address='fe80::c685:8ff:fe45:641%wlan0', netmask='ffff:ffff:ffff:ffff::', broadcast=None, ptp=None),
           snicaddr(family=<AddressFamily.AF_LINK: 17>, address='c4:85:08:45:06:41', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)]}
>>>
```

另请参阅示例应用程序 [nettop.py][nettop.py] 和 [ifconfig.py][ifconfig.py]。

**注释**: 如果对其他协议家族（例如 AF_BLUETOOTH）感兴趣，可以使用更强大的 [netifaces][netifaces] 扩展。

**Note**: 你可以有多个相同系列的地址与每个接口相关联（这就是为什么 dict 值是列表）。

**Note**: Windows 不支持广播和 ptp，并且始终为 `None` 。

[netifaces]: https://pypi.org/project/netifaces/ "netifaces"

_3.0.0 版本中新增._

*3.2.0 版本中修改: 添加了 **ptp** 字段。*

*4.4.0 版本中修改: 添加了对 Windows 上不再是 `None` 的网络掩码字段的支持。*

#### **网卡状态**

**psutil.net_if_stats()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.net_if_stats) <a name="psutil.net_if_stats"></a>

以字典形式返回系统上安装的每个 NIC（网络接口卡）的信息，其键是 NIC 名称，值是具有以下字段的命名元组：

* `isup`: 一个布尔值，指示 NIC 是否已启用并正在运行（意味着以太网电缆或 Wi-Fi 已连接）。
* `duplex`: 双工通信类型； 它可以是 [NIC_DUPLEX_FULL][NIC_DUPLEX_FULL]、[NIC_DUPLEX_HALF][NIC_DUPLEX_HALF] 或 [NIC_DUPLEX_UNKNOWN][NIC_DUPLEX_UNKNOWN]。
* `speed`: 以兆位 (MB) 表示的 NIC 速度，如果无法确定（例如“本地主机”），它将设置为 `0`。
* `mtu`: NIC 的最大传输单位，以字节为单位。

[NIC_DUPLEX_FULL]: #psutil.NIC_DUPLEX_FULL "psutil.NIC_DUPLEX_FULL"
[NIC_DUPLEX_HALF]: #psutil.NIC_DUPLEX_HALF "psutil.NIC_DUPLEX_HALF"
[NIC_DUPLEX_UNKNOWN]: #psutil.NIC_DUPLEX_UNKNOWN "psutil.NIC_DUPLEX_UNKNOWN"

样例:

```python
>>> import psutil
>>> psutil.net_if_stats()
{'eth0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=100, mtu=1500),
 'lo': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=65536)}
```

另请参阅示例应用程序 [nettop.py][nettop.py] 和 [ifconfig.py][ifconfig.py]。

_3.0.0 版本中新增._

*5.7.3 版本中修改: UNIX 上的 **isup** 同时还会检查 NIC 是否正在运行。*

### 传感器 (Sensors)

#### **温度**

**psutil.sensors_temperatures(fahrenheit=False)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.sensors_temperatures)

返回硬件温度。 每个条目都是一个命名元组，代表某个硬件温度传感器（它可能是 CPU、硬盘或其他东西，取决于操作系统及其配置）。所有温度均以摄氏度表示，除非华氏度(**_fahrenheit_**)设置为 True。 如果操作系统不支持传感器，则返回空字典。 例子：

```python
>>> import psutil
>>> psutil.sensors_temperatures()
{'acpitz': [shwtemp(label='', current=47.0, high=103.0, critical=103.0)],
 'asus': [shwtemp(label='', current=47.0, high=None, critical=None)],
 'coretemp': [shwtemp(label='Physical id 0', current=52.0, high=100.0, critical=100.0),
              shwtemp(label='Core 0', current=45.0, high=100.0, critical=100.0),
              shwtemp(label='Core 1', current=52.0, high=100.0, critical=100.0),
              shwtemp(label='Core 2', current=45.0, high=100.0, critical=100.0),
              shwtemp(label='Core 3', current=47.0, high=100.0, critical=100.0)]}
```

另请参阅示例应用脚本 [temperatures.py][temperatures.py] 和 [sensors.py][sensors.py]。

[temperatures.py]: https://github.com/giampaolo/psutil/blob/master/scripts/temperatures.py "temperatures.py"
[sensors.py]: https://github.com/giampaolo/psutil/blob/master/scripts/sensors.py "sensors.py"

可用平台: Linux, FreeBSD

_5.1.0 版本中新增._

_5.5.0 版本中修改: 添加了对FreeBSD的支持。_

#### **风扇**

**psutil.sensors_fans()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.sensors_fans)

返回硬件风扇速度。 每个条目都是一个命名元组，代表某个硬件传感器风扇。 风扇速度以 RPM（每分钟转数）表示。 如果操作系统不支持传感器，则返回空字典。 例子：

```python
>>> import psutil
>>> psutil.sensors_fans()
{'asus': [sfan(label='cpu_fan', current=3200)]}
```

另请参阅示例应用脚本 [fans.py][fans.py] 和 [sensors.py][sensors.py]。

[fans.py]: https://github.com/giampaolo/psutil/blob/master/scripts/fans.py "fans.py"

可用平台: Linux

_5.2.0 版本中新增._

#### **电池**

**psutil.sensors_battery()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.sensors_battery) <a name="psutil.sensors_battery"></a>

将电池状态信息作为包含以下值的命名元组返回。 如果未安装电池或无法确定指标，则返回 `None` 。

* `percent`: 电池电量剩余百分比。
* `secsleft`: 电池电量耗尽前还剩多少秒的粗略近似值。 如果连接了交流电源线，则此项设置为 [psutil.POWER_TIME_UNLIMITED](#psutil.POWER_TIME_UNLIMITED)。 如果无法确定，则将其设置为 [psutil.POWER_TIME_UNKNOWN](#psutil.POWER_TIME_UNKNOWN)。
* `power_plugged`: 如果 AC 电源线已连接，则为 `True` ，否则为 `False` ，如果无法确定则为 `None` 。

例子:

```python
>>> import psutil
>>>
>>> def secs2hours(secs):
...     mm, ss = divmod(secs, 60)
...     hh, mm = divmod(mm, 60)
...     return "%d:%02d:%02d" % (hh, mm, ss)
...
>>> battery = psutil.sensors_battery()
>>> battery
sbattery(percent=93, secsleft=16628, power_plugged=False)
>>> print("charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft)))
charge = 93%, time left = 4:37:08
```

另请参阅示例应用脚本 [battery.py][battery.py] 和 [sensors.py][sensors.py]。

[battery.py]: https://github.com/giampaolo/psutil/blob/master/scripts/battery.py  "battery.py"

可用平台: Linux, Windows, FreeBSD

_5.1.0 版本中新增._

_5.4.2 版本中修改: 添加了 macOS 支持._

### 其他系统信息(Other system info)

#### **启动时间**

**psutil.boot_time()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.boot_time)

返回自纪元(epoch)以来以秒表示的系统启动时间。 例子：

```python
>>> import psutil, datetime
>>> psutil.boot_time()
1389563460.0
>>> datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
'2014-01-12 22:51:00'
```

**注释**: 在 Windows 上，如果它在不同的进程中使用，这个函数可能会返回一个减少(off by) 1 秒的时间（参阅[问题 #1007][issue#1007]）。

[issue#1007]: https://github.com/giampaolo/psutil/issues/1007 "issue #1007"

#### **用户**

**psutil.users()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.users)

将当前连接在系统上的用户作为命名元组列表返回，包括以下字段：

* `name`: 用户名.
* `terminal`: 与用户关联的 `tty` 或 `伪tty` ，如果有，否则为 `None` 。
* `host`: 与条目关联的主机名（如果有）。
* `started`: 创建时间作为一个浮点数，以自纪元（epoch）以来的秒数表示。
* `pid`: 登录进程的 PID（如 sshd、tmux、gdm-session-worker 等）。 在 Windows 和 OpenBSD 上，PID 始终为 `None` 。

例子:

```python
>>> import psutil
>>> psutil.users()
[suser(name='giampaolo', terminal='pts/2', host='localhost', started=1340737536.0, pid=1352),
 suser(name='giampaolo', terminal='pts/3', host='localhost', started=1340737792.0, pid=1788)]
```

5.3.0 版本中修改: added “pid” field

## **进程** (Processes)

### **函数** (Functions)

#### **进程ID列表**

**psutil.pids()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.pids) <a name="psutil.pids"></a>

返回当前正在运行的**进程ID**(PID)的排序列表。 迭代所有进程并避免竞争条件 [process_iter()](#psutil.process_iter) 应该是首选。

```python
>>> import psutil
>>> psutil.pids()
[1, 2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, ..., 32498]
```

_5.6.0 版本中修改: PIDs 排序后返回。_

#### **迭代进程**

**psutil.process_iter(attrs=None, ad_value=None)** - 原文 <a name="psutil.process_iter"></a>

返回一个迭代器，为本地机器上的所有正在运行的进程产生一个 [Process](#psutil.Process) 类实例。 这应该优于 [psutil.pids()](#psutil.pids) 来迭代进程，因为它不受竞争条件的影响。

每个 [Process](#psutil.Process) 实例只创建一次，然后在下次调用 [psutil.process_iter()](#psutil.process_iter) 时缓存（如果 PID 仍然存在）。 它还确保进程 PID 不被重用。

***attrs*** 和 ***ad_value*** 与 [Process.as_dict()](#Process.as_dict) 具有相同的含义。 如果指定了 ***attrs*** ，则 [Process.as_dict()](#Process.as_dict) 结果将存储为附加到返回的 [Process](#psutil.Process) 实例的 `info` 属性。 如果 ***attrs*** 是一个空列表，它将检索所有进程信息（比较慢）。

返回进程的排序顺序基于它们的 PID。

例子:

```python
>>> import psutil
>>> for proc in psutil.process_iter(['pid', 'name', 'username']):
...     print(proc.info)
...
{'name': 'systemd', 'pid': 1, 'username': 'root'}
{'name': 'kthreadd', 'pid': 2, 'username': 'root'}
{'name': 'ksoftirqd/0', 'pid': 3, 'username': 'root'}
...
```

创建类似于 `{pid: info, ...}` 数据结构的字典：

```python
>>> import psutil
>>> procs = {p.pid: p.info for p in psutil.process_iter(['name', 'username'])}
>>> procs
{1: {'name': 'systemd', 'username': 'root'},
 2: {'name': 'kthreadd', 'username': 'root'},
 3: {'name': 'ksoftirqd/0', 'username': 'root'},
 ...}
```

*5.3.0 版本中修改: 新增 “**attrs**” 和 “**ad_value**” 参数.*

#### **检查进程是否存在**

**psutil.pid_exists(pid)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.pid_exists)

检查给定的 PID 是否存在于当前进程列表中。 这比执行 `pid in psutil.pids()` 更快，应该是首选。

#### **等待进程终止**

**psutil.wait_procs(procs, timeout=None, callback=None)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.wait_procs)<a name="psutil.wait_proces"></a>

等待 [Process](#psutil.Process) 实例列表终止的快捷函数。 返回一个 `(gone, alive)` 元组，指示哪些进程已经消失，哪些仍然活着。消失的进程实例将有一个新的 ***returncode*** 属性，表示 [Process.wait()](#Process.wait) 返回的进程退出状态。***callback*** 参数是一个函数，当正在等待的进程之一终止并且 [Process](#psutil.Process) 实例作为回调参数传递时会被调用（该实例还将具有 ***returncode*** 属性集合）。一旦所有进程终止或超时（单位:秒）发生，此函数将返回。 与 [Process.wait()](#Process.wait) 不同，如果发生超时，它不会引发 [TimeoutExpired](#psutil.TimeoutExpired)。 一个典型的用例可能是：

* 将 ***SIGTERM*** 信号发送到进程列表
* 给他们一些时间来终止
* 发送 ***SIGKILL*** 给那些还活着的进程

终止并等待此进程的所有子进程的示例：

```python
import psutil

def on_terminate(proc):
    print("process {} terminated with exit code {}".format(proc, proc.returncode))

procs = psutil.Process().children()
for p in procs:
    p.terminate()

gone, alive = psutil.wait_procs(procs, timeout=3, callback=on_terminate)
for p in alive:
    p.kill()
```

### **异常** (Exceptions)

#### **异常基类**

`class` **psutil.Error** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Error)

基本异常类。 所有其他异常都继承自这个异常。

#### **进程不存在**

`class` **psutil.NoSuchProcess(pid, name=None, msg=None)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.NoSuchProcess) <a name="psutil.NoSuchProcess"></a>

当在当前进程列表中找不到具有给定 pid 的进程或进程不再存在时，由 [Process](#psutil.Process) 类的方法抛出。 ***name*** 是进程消失之前的名称，只有在之前调用 [Process.name()](#Process.name) 时才会设置。

#### **僵尸进程**

`class` **psutil.ZombieProcess(pid, name=None, ppid=None, msg=None)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.ZombieProcess) <a name="psutil.ZombieProcess"></a>

在 UNIX 上查询僵尸进程（Windows 没有僵尸进程）时，这可能由 [Process](#psutil.Process) 类的方法抛出。 如果在进程变成僵尸之前调用 [Process.name()](#Process.name) 或 [Process.ppid()](#Process.ppid) 方法，则 ***name*** 和 ***ppid*** 属性可用。

**注释**: 这是 [NoSuchProcess](#psutil.NoSuchProcess) 的子类，因此如果对检索僵尸进程不感兴趣（例如，在使用 [process_iter()](#psutil.process_iter) 时），可以忽略此异常并只捕获 [NoSuchProcess](#psutil.NoSuchProcess) 。

_3.0.0 版本中新增._

#### **无权限**

`class` **psutil.AccessDenied(pid=None, name=None, msg=None)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.AccessDenied) <a name="psutil.AccessDenied"></a>

当由于权限不足而拒绝执行操作时，由 [Process](#psutil.Process) 类的方法抛出。 如果之前调用了 [Process.name()](#Process.name)，则 ***name*** 属性可用。

#### **超时**

`class` **psutil.TimeoutExpired(seconds, pid=None, name=None, msg=None)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.TimeoutExpired) <a name="psutil.TimeoutExpired"></a>

如果超时到期并且进程仍然存在，则由 [Process.wait()](#Process.wait) 方法引发。 如果之前调用了 [Process.name()](#Process.name)，则 ***name*** 属性可用。

### **进程类** (Process class)

`class` **psutil.Process(pid=None)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process) <a name="psutil.Process"></a>

代表具有给定 ***pid*** 的系统(OS)进程。 如果省略 ***pid*** ，则使用当前进程的 ***pid*** ([os.getpid][os.getpid])。 如果 ***pid*** 不存在，则抛出 [NoSuchProcess](#psutil.NoSuchProcess) 异常。 在 Linux 上， ***pid*** 也可以指 线程ID（[threads()](#Process.threads) 方法返回的 ***id*** 字段）。 访问该类的方法时，始终准备捕获 [NoSuchProcess](#psutil.NoSuchProcess) 和 [AccessDenied](#psutil.AccessDenied) 异常。 内建函数 [hash][[builtin.hash]] 可用于此类的实例，以便随着时间的推移唯一地标识进程（hash值由 `进程 PID + 创建时间` 混合后确定）。 因此，它也可以与 [set][typs.set] 一起使用。

**注释**： 为了同时有效地获取有关进程的多个信息，请确保使用 [oneshot()](#Process.oneshot) 上下文管理器或 [as_dict()](#Process.as_dict) 实例方法。

**注释**： 此类和进程绑定的方式是通过其唯一 PID 。这意味着如果进程终止并且操作系统重用其 PID，最终可能会与另一个进程交互。抢先检查进程身份（通过 PID + 创建时间）的唯一例外是以下方法：[nice()](#Process.nice) (set), [ionice()](#Process.ionice) (set), [cpu_affinity()](#Process.cpu_affinity) (set), [rlimit()](#Process.rlimit) (set) , [children()](#Process.children), [parent()](#Process.parent), [parents()](Process.parents), [suspend()](#Process.suspend), [resume()](#Process.resume), [send_signal()](#Process.send_signal), [terminate()](#Process.terminate), [kill()](#Process.kill)。为了防止所有其他方法出现此问题，可以在查询进程之前使用 [is_running()](#Process.is_running) 或 [process_iter()](#psutil.process_iter) 以防迭代所有进程。但必须注意的是，除非处理非常“旧(old)”（非活动(inactive)）的 [Process](#psutil.Process) 实例，否则这几乎不会构成问题。

[os.getpid]: https://docs.python.org/3/library/os.html#os.getpid "os.getpid"
[typs.set]: https://docs.python.org/zh-cn/3/library/stdtypes.html#types-set. "内置类型 Set"

**译注**: 进程类方法一览

* Process.[oneshot()](#Process.oneshot) - 快照
* Process.[pid](#Process.pid) - 进程ID
* Process.[ppid()](#Process.ppid) - 父进程ID
* Process.[name()](#Process.name) - 进程名称
* Process.[exe()](#Process.exe) - 可执行文件绝对路径
* Process.[cmdline()](#Process.cmdline) - 执行命令行
* Process.[environ()](#Process.environ) - 环境变量
* Process.[create_time()](#Process.create_time) - 创建时间
* Process.[as_dict(attrs=None, ad_value=None)](#Process.as_dict) - 字典信息
* Process.[parent()](#Process.parent) - 父进程
* Process.[parents()](#Process.parents) - 父进程列表
* Process.[status()](#Process.status) - 进程状态
* Process.[cwd()](#Process.cwd) - 执行目录
* Process.[username()](#Process.username) - 所属用户名
* Process.[uids()](#Process.uids) - 用户ID
* Process.[gids()](#Process.gids) - 组ID
* Process.[terminal()](#Process.terminal) - 终端
* Process.[nice(value=None)](#Process.nice) - 优先级
* Process.[ionice(ioclass=None, value=None)](#Process.ionice) - I/O优先级
* Process.[rlimit(resource, limits=None)](#Process.rlimit) - 资源限制
* Process.[io_counters()](#Process.io_counters) - I/O统计
* Process.[num_ctx_switches()](#Process.num_ctx_switches) - 上下文切换数
* Process.[num_fds()](#Process.num_fds) - 文件描述符数
* Process.[num_handles()](#Process.num_handles) - 句柄数
* Process.[num_threads()](#Process.num_threads) - 线程数
* Process.[threads()](#Process.threads) - 线程
* Process.[cpu_times()](#Process.cpu_times) - cpu时间
* Process.[cpu_percent(interval=None)](#Process.cpu_percent) - cpu利用率
* Process.[cpu_affinity(cpus=None)](#Process.cpu_affinity) - cpu亲和度
* Process.[cpu_num()](#Process.cpu_num) - cpu数量
* Process.[memory_info()](#Process.memory_info) - 内存信息
* Process.[memory_info_ex()](#Process.memory_info_ex) - 已废弃
* Process.[memory_full_info()](#Process.memory_full_info) - 内存完全信息
* Process.[memory_percent(memtype="rss")](#Process.memory_percent) - 内存利用率
* Process.[memory_maps(grouped=True)](#Process.memory_maps) - 内存映射
* Process.[children(recursive=False)](#Process.children) - 子进程
* Process.[open_files()](#Process.open_files) - 打开的文件
* Process.[connections(kind="inet")](#Process.connections) - 网络连接
* Process.[is_running()](#Process.is_running) - 是否正在运行
* Process.[send_signal(signal)](#Process.send_signal) - 发送信号
* Process.[suspend()](#Process.suspend) - 暂停进程
* Process.[resume()](#Process.resume) - 恢复进程
* Process.[terminate()](#Process.terminate) - 终止进程
* Process.[kill()](#Process.kill) - 杀死进程
* Process.[wait(timeout=None)](#Process.wait) - 等待
* pstuil.[Popen](#Popen) - 执行子程序

#### **快照**

**Process.oneshot()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.oneshot) <a name="Process.oneshot" ></a>
  
实例的上下文管理器可显著加快同时检索多个进程信息的速度。内部不同的进程信息（例如 [name()](#Process.name), [ppid()](#Process.ppid), [uids()](#Process.uids), [create_time()](#Process.create_time), ...）可以通过使用相同的例程获取，但只返回一个值，其他值被丢弃。当使用上下文管理器时，内部只执行一次（在下面的 [name()](#Process.name) 示例中），返回感兴趣的值并缓存其他值。共享相同内部例程的后续调用将返回缓存值。 退出上下文管理器块时清除缓存。建议是每次检索有关该进程的多个信息时都使用此方法。 如果很幸运，获取值将会得到极大的加速。 例子：

```python
>>> import psutil
>>> p = psutil.Process()
>>> with p.oneshot():
...     p.name()  # execute internal routine once collecting multiple info
...     p.cpu_times()  # return cached value
...     p.cpu_percent()  # return cached value
...     p.create_time()  # return cached value
...     p.ppid()  # return cached value
...     p.status()  # return cached value
...
>>>
```

以下是可以利用加速的方法列表，具体取决于使用的平台。在下表中，垂直列表示哪些进程方法可以在某个平台内调用时内部有效地组合在一起。最后一行 (speedup) 显示了将所有方法一起调用时可以获得的加速比的近似值（最佳情况）。

**译注**: 原文说的是 “horizontal emtpy rows” 水平空行，但根据表格实际内容，应为某个平台对应的垂直列，并且原文的 “The last column” 应该是指最后一行。

| **Linux**                                       | **Windows**                                     | **macOS**                                       | **BSD**                                         | **SunOS**                                   | **AIX**                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| [cpu_num()](#Process.cpu_num)                   | [cpu_percent()](#Process.cpu_percent)           | [cpu_percent()](#Process.cpu_percent)           | [cpu_num()](#Process.cpu_num)                   | [name()](#Process.name)                     | [name()](#Process.name)                     |
| [cpu_percent()](#Process.cpu_percent)           | [cpu_times()](#Process.cpu_times)               | [cpu_times()](#Process.cpu_times)               | [cpu_percent()](#Process.cpu_percent)           | [cmdline()](#Process.cmdline)               | [cmdline()](#Process.cmdline)               |
| [cpu_times()](#Process.cpu_times)               | [io_counters()](#Process.io_counters)           | [memory_info()](#Process.memory_info)           | [cpu_times()](#Process.cpu_times)               | [create_time()](#Process.create_time)       | [create_time()](#Process.create_time)       |
| [create_time()](#Process.create_time)           | [memory_info()](#Process.memory_info)           | [memory_percent()](#Process.memory_percent)     | [create_time()](#Process.create_time)           | -                                           | -                                           |
| [name()](#Process.name)                         | [memory_maps()](#Process.memory_maps)           | [num_ctx_switches()](#Process.num_ctx_switches) | [gids()](#Process.gids)                         | [memory_info()](#Process.memory_info)       | [memory_info()](#Process.memory_info)       |
| [ppid()](#Process.ppid)                         | [num_ctx_switches()](#Process.num_ctx_switches) | [num_threads()](#Process.num_threads)           | [io_counters()](#Process.io_counters)           | [memory_percent()](#Process.memory_percent) | [memory_percent()](#Process.memory_percent) |
| [status()](#Process.status)                     | [num_handles()](#Process.num_handles)           | -                                               | [name()](#Process.name)                         | [num_threads()](#Process.num_threads)       | [num_threads()](#Process.num_threads)       |
| [terminal()](#Process.terminal)                 | [num_threads()](#Process.num_threads)           | [create_time()](#Process.create_time)           | [memory_info()](#Process.memory_info)           | [ppid()](#Process.ppid)                     | [ppid()](#Process.ppid)                     |
| -                                               | [username()](#Process.username)                 | [gids()](#Process.gids)                         | [memory_percent()](#Process.memory_percent)     | [status()](#Process.status)                 | [status()](#Process.status)                 |
| [gids()](#Process.gids)                         | -                                               | [name()](#Process.name)                         | [num_ctx_switches()](#Process.num_ctx_switches) | [terminal()](#Process.terminal)             | [terminal()](#Process.terminal)             |
| [num_ctx_switches()](#Process.num_ctx_switches) | [exe()](#Process.exe)                           | [ppid()](#Process.ppid)                         | [ppid()](#Process.ppid)                         | -                                           | -                                           |
| [num_threads()](#Process.num_threads)           | [name()](#Process.name)                         | [status()](#Process.status)                     | [status()](#Process.status)                     | [gids()](#Process.gids)                     | [gids()](#Process.gids)                     |
| [uids()](#Process.uids)                         | -                                               | [terminal()](#Process.terminal)                 | [terminal()](#Process.terminal)                 | [uids()](#Process.uids)                     | [uids()](#Process.uids)                     |
| [username()](#Process.username)                 | -                                               | [uids()](#Process.uids)                         | [uids()](#Process.uids)                         | [username()](#Process.username)             | [username()](#Process.username)             |
| -                                               | -                                               | [username()](#Process.username)                 | [username()](#Process.username)                 | -                                           | -                                           |
| [memory_full_info()](#Process.memory_full_info) | -                                               | -                                               | -                                               | -                                           | -                                           |
| [memory_maps()](#Process.memory_maps)           | -                                               | -                                               | -                                               | -                                           | -                                           |
| speedup: +2.6x                                  | speedup: +1.8x / +6.5x                          | speedup: +1.9x                                  | speedup: +2.0x                                  | speedup: +1.3x                              | speedup: +1.3x                              |

_5.0.0 版本中新增._

#### **进程ID**

**Process.pid** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.pid) <a name="Process.pid" ></a>

进程PID 。 这是该类的唯一一个属性（只读）。

#### **父进程ID**

**Process.ppid()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.ppid) <a name="Process.ppid" ></a>

返回父进程PID。 在 Windows 上，第一次调用后会缓存返回值。在 POSIX 类型机器上时则不会缓存，因为如果进程变成僵尸进程， ***ppid*** 可能会改变，另见 [parent()](#Process.parent) 和 [parents()](#Process.parents) 方法。

#### **进程名称**

**Process.name()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.name) <a name="Process.name" ></a>

返回进程名称. 在 Windows 上，第一次调用后会缓存返回值。在 POSIX 类型机器上时则不会缓存， 因为进程名称可能会改变。 另请参阅如何[按名称查找进程](#find-process-by-name)。

#### **可执行文件绝对路径**

**Process.exe()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.exe) <a name="Process.exe" ></a>

进程的可执行文件绝对路径。 在某些系统上，这也可能是一个空字符串。 返回值在第一次调用后被缓存。

```python
>>> import psutil
>>> psutil.Process().exe()
'/usr/bin/python2.7'
```

#### **执行命令行**

**Process.cmdline()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.cmdline) <a name="Process.cmdline" ></a>

此进程的作为字符串列表的命令号调用。 由于进程的命令行可能会更改，因此不会缓存返回值。

```python
>>> import psutil
>>> psutil.Process().cmdline()
['python', 'manage.py', 'runserver']
```

#### **环境变量**

**Process.environ()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.environ) <a name="Process.environ" ></a>

进程的作为字典的环境变量。 **注意**：这可能不会反映进程开始后所做的更改。

```python
>>> import psutil
>>> psutil.Process().environ()
{'LC_NUMERIC': 'it_IT.UTF-8', 'QT_QPA_PLATFORMTHEME': 'appmenu-qt5', 'IM_CONFIG_PHASE': '1', 'XDG_GREETER_DATA_DIR': '/var/lib/lightdm-data/giampaolo', 'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated', 'XDG_CURRENT_DESKTOP': 'Unity', 'UPSTART_EVENTS': 'started starting', 'GNOME_KEYRING_PID': '', 'XDG_VTNR': '7', 'QT_IM_MODULE': 'ibus', 'LOGNAME': 'giampaolo', 'USER': 'giampaolo', 'PATH': '/home/giampaolo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/giampaolo/svn/sysconf/bin', 'LC_PAPER': 'it_IT.UTF-8', 'GNOME_KEYRING_CONTROL': '', 'GTK_IM_MODULE': 'ibus', 'DISPLAY': ':0', 'LANG': 'en_US.UTF-8', 'LESS_TERMCAP_se': '\x1b[0m', 'TERM': 'xterm-256color', 'SHELL': '/bin/bash', 'XDG_SESSION_PATH': '/org/freedesktop/DisplayManager/Session0', 'XAUTHORITY': '/home/giampaolo/.Xauthority', 'LANGUAGE': 'en_US', 'COMPIZ_CONFIG_PROFILE': 'ubuntu', 'LC_MONETARY': 'it_IT.UTF-8', 'QT_LINUX_ACCESSIBILITY_ALWAYS_ON': '1', 'LESS_TERMCAP_me': '\x1b[0m', 'LESS_TERMCAP_md': '\x1b[01;38;5;74m', 'LESS_TERMCAP_mb': '\x1b[01;31m', 'HISTSIZE': '100000', 'UPSTART_INSTANCE': '', 'CLUTTER_IM_MODULE': 'xim', 'WINDOWID': '58786407', 'EDITOR': 'vim', 'SESSIONTYPE': 'gnome-session', 'XMODIFIERS': '@im=ibus', 'GPG_AGENT_INFO': '/home/giampaolo/.gnupg/S.gpg-agent:0:1', 'HOME': '/home/giampaolo', 'HISTFILESIZE': '100000', 'QT4_IM_MODULE': 'xim', 'GTK2_MODULES': 'overlay-scrollbar', 'XDG_SESSION_DESKTOP': 'ubuntu', 'SHLVL': '1', 'XDG_RUNTIME_DIR': '/run/user/1000', 'INSTANCE': 'Unity', 'LC_ADDRESS': 'it_IT.UTF-8', 'SSH_AUTH_SOCK': '/run/user/1000/keyring/ssh', 'VTE_VERSION': '4205', 'GDMSESSION': 'ubuntu', 'MANDATORY_PATH': '/usr/share/gconf/ubuntu.mandatory.path', 'VISUAL': 'vim', 'DESKTOP_SESSION': 'ubuntu', 'QT_ACCESSIBILITY': '1', 'XDG_SEAT_PATH': '/org/freedesktop/DisplayManager/Seat0', 'LESSCLOSE': '/usr/bin/lesspipe %s %s', 'LESSOPEN': '| /usr/bin/lesspipe %s', 'XDG_SESSION_ID': 'c2', 'DBUS_SESSION_BUS_ADDRESS': 'unix:abstract=/tmp/dbus-9GAJpvnt8r', '_': '/usr/bin/python', 'DEFAULTS_PATH': '/usr/share/gconf/ubuntu.default.path', 'LC_IDENTIFICATION': 'it_IT.UTF-8', 'LESS_TERMCAP_ue': '\x1b[0m', 'UPSTART_SESSION': 'unix:abstract=/com/ubuntu/upstart-session/1000/1294', 'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/usr/share/upstart/xdg:/etc/xdg', 'GTK_MODULES': 'gail:atk-bridge:unity-gtk-module', 'XDG_SESSION_TYPE': 'x11', 'PYTHONSTARTUP': '/home/giampaolo/.pythonstart', 'LC_NAME': 'it_IT.UTF-8', 'OLDPWD': '/home/giampaolo/svn/curio_giampaolo/tests', 'GDM_LANG': 'en_US', 'LC_TELEPHONE': 'it_IT.UTF-8', 'HISTCONTROL': 'ignoredups:erasedups', 'LC_MEASUREMENT': 'it_IT.UTF-8', 'PWD': '/home/giampaolo/svn/curio_giampaolo', 'JOB': 'gnome-session', 'LESS_TERMCAP_us': '\x1b[04;38;5;146m', 'UPSTART_JOB': 'unity-settings-daemon', 'LC_TIME': 'it_IT.UTF-8', 'LESS_TERMCAP_so': '\x1b[38;5;246m', 'PAGER': 'less', 'XDG_DATA_DIRS': '/usr/share/ubuntu:/usr/share/gnome:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop', 'XDG_SEAT': 'seat0'}
```

_4.0.0 版本中新增._

_5.3.0 版本中修改: 新增 SunOS 支持。_

_5.6.3 版本中修改: 新增 AIX 支持。_

_5.7.3 版本中修改: 新增 BSD 支持。_

#### **创建时间**

**Process.create_time()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.create_time) <a name="Process.create_time" ></a>

进程创建时间，以自纪元以来的秒数表示的浮点数。 返回值在第一次调用后被缓存。

```python
>>> import psutil, datetime
>>> p = psutil.Process()
>>> p.create_time()
1307289803.47
>>> datetime.datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
'2011-03-05 18:03:52'
```

#### **字典信息**

**Process.as_dict(attrs=None, ad_value=None)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.as_dict) <a name="Process.as_dict" ></a>

以字典形式检索进程的多个信息的实例方法。如果指定了 ***attrs*** ，则它必须是反映 [Process](#psutil.Process) 类可用的属性名称的字符串列表。以下是可能的字符串值列表：`'cmdline'`, `'connections'`, `'cpu_affinity'`, `'cpu_num'`, `'cpu_percent'`, `'cpu_times'`, `'create_time'`, `'cwd'`, `'environ'`, `'exe'`, `'gids'`, `'io_counters'`, `'ionice'`, `'memory_full_info'`, `'memory_info'`, `'memory_maps'`, `'memory_percent'`, `'name'`, `'nice'`, `'num_ctx_switches'`, `'num_fds'`, `'num_handles'`, `'num_threads'`, `'open_files'`, `'pid'`, `'ppid'`, `'status'`, `'terminal'`, `'threads'`, `'uids'`, `'username'`. 如果没有传递 ***attrs*** 参数，则假定为所有公共的只读属性。***ad_value*** 是分配给字典键的值，以防在检索该特定进程信息时引发 [AccessDenied](#psutil.AccessDenied) 或 [ZombieProcess](#psutil.ZombieProcess) 异常。 在内部， [as_dict()](#Process.as_dict) 使用 [oneshot()](#Process.oneshot) 上下文管理器，因此也无需使用它。

```python
>>> import psutil
>>> p = psutil.Process()
>>> p.as_dict(attrs=['pid', 'name', 'username'])
{'username': 'giampaolo', 'pid': 12366, 'name': 'python'}
>>>
>>> # get a list of valid attrs names
>>> list(psutil.Process().as_dict().keys())
['status', 'cpu_num', 'num_ctx_switches', 'pid', 'memory_full_info', 
 'connections', 'cmdline', 'create_time', 'ionice', 'num_fds', 
 'memory_maps', 'cpu_percent', 'terminal', 'ppid', 'cwd', 'nice', 
 'username', 'cpu_times', 'io_counters', 'memory_info', 'threads', 
 'open_files', 'name', 'num_threads', 'exe', 'uids', 'gids', 
 'cpu_affinity', 'memory_percent', 'environ']
```

*3.0.0 版本中修改: **ad_value** 在引发 [ZombieProcess](#psutil.ZombieProcess) 异常时也使用，不仅是 [AccessDenied](#psutil.AccessDenied)。*

*4.5.0 版本中修改: 由于 [oneshot()](#Process.oneshot) 上下文管理器，[as_dict()](#Process.as_dict) 的速度要快得多。*

#### **父进程**

**Process.parent()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.parent) <a name="Process.parent" ></a>

将父进程作为 [Process](#psutil.Process) 对象返回的实例方法，抢先检查 PID 是否已被重用。 如果没有已知的父 PID，则返回 `None` 。 另请参见 [ppid()](#Process.ppid) 和 [parents()](#Process.parents) 方法。

#### **父进程列表**

**Process.parents()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.parents) <a name="Process.parents" ></a>

以列表形式返回当前进程的所有父进程的实例方法, 如果没有父进程，返回空列表。同样参考 [ppid()](#Process.ppid) 和 [parent()](#Process.parent) 方法.

译注例子:

```python
>>> psutil.Process().parents()
[psutil.Process(pid=79791, name='zsh', status='running', started='2021-12-09 17:23:11'), psutil.Process(pid=3483, name='Code Helper (Renderer)', status='running', started='2021-12-02 16:07:48'), psutil.Process(pid=3479, name='Code Helper (Renderer)', status='running', started='2021-12-02 16:07:48'), psutil.Process(pid=471, name='Electron', status='running', started='2021-12-02 16:07:35'), psutil.Process(pid=1, name='launchd', status='running', started='2021-12-02 16:07:20'), psutil.Process(pid=0, name='kernel_task', status='running', started='2021-12-02 16:07:20')]
```

_5.6.0 版本中新增._

#### **进程状态**

**Process.status()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.status) <a name="Process.status" ></a>

以字符串方式返回当前进程状态。 返回的字符串是 [psutil.STATUS_*](#process-status-constant) 常量之一。

译注例子:

```python
>>> psutil.Process().status()
'running'
```

#### **执行目录**

**Process.cwd()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.cwd) <a name="Process.cwd" ></a>

以绝对路径的方式返回进程当前执行目录。

译注例子:

```python
>>> psutil.Process().cwd()
'/xxxx/xxxx/scripts/demo'
```

_5.6.4 版本中修改: 新增 NetBSD 支持。_

#### **所属用户名**

**Process.username()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.username) <a name="Process.username" ></a>

返回拥有当前进程的用户名。 在 UNIX 上，这是通过使用真实进程 uid 来计算的。

#### **用户ID**

**Process.uids()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.uids) <a name="Process.uids" ></a>

返回一个由 (ruid, euid, suid) 所组成的元组，分别表示当前进程的真实用户ID，有效用户ID和暂存用户ID。这与 [os.getresuid][os.getresuid] 相同，但可用于任何进程 PID。

[os.getresuid]: https://docs.python.org/zh-cn/3/library/os.html#os.getresuid "os.getresuid"

译注例子:

```python
>>> psutil.Process().uids()
puids(real=501, effective=501, saved=501)
```

_可用平台: UNIX。_

#### **组ID**

**Process.gids()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.gids) <a name="Process.gids" ></a>

返回一个由 (rgid, egid, sgid) 所组成的元组，分别表示当前进程的真实组ID，有效组ID和暂存组ID。这与 [os.getresgid][os.getresgid] 相同，但可用于任何进程 PID。

[os.getresgid]: https://docs.python.org/zh-cn/3/library/os.html#os.getresgid "os.getresgid"

_可用平台: UNIX。_

#### **终端**

**Process.terminal()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.terminal) <a name="Process.terminal" ></a>

与此进程关联的终端（如果有），否则为 `None`。 类似于“`tty`”命令，但可用于任何进程PID。

_可用平台: UNIX。_

#### **优先级**

**Process.nice(value=None)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.nice) <a name="Process.nice" ></a>

获取或设置进程良好度（优先级）。 在 UNIX 上，这是一个数字，通常从 `-20` 到 `20` 。nice 值越高，进程的优先级越低。

```python
>>> import psutil
>>> p = psutil.Process()
>>> p.nice(10)  # set
>>> p.nice()  # get
10
>>>
```

从 Python 3.3 开始，此功能类似于 [os.getpriority][os.getpriority] 和 [os.setpriority][os.setpriority]（参见 [BPO-10784][BPO-10784]）。 在 Windows 上，这是通过 Windows API 的 [GetPriorityClass][GetPriorityClass] 和 [SetPriorityClass][SetPriorityClass] 实现的，***value*** 是 [psutil.*_PRIORITY_CLASS](#process-priority-constant) 常量之一， 对应于MSDN文档。 在 Windows 上增加进程优先级的示例如下：

[os.getpriority]: https://docs.python.org/zh-cn/3/library/os.html#os.getpriority  "os.getpriority"
[os.setpriority]: https://docs.python.org/zh-cn/3/library/os.html#os.setpriority "os.setpriority"
[BPO-10784]: https://bugs.python.org/issue10784  "BPO-10784"
[GetPriorityClass]: https://docs.microsoft.com/zh-cn/windows/desktop/api/processthreadsapi/nf-processthreadsapi-getpriorityclass ""
[SetPriorityClass]: https://docs.microsoft.com/zh-cn/windows/desktop/api/processthreadsapi/nf-processthreadsapi-setpriorityclass ""

```python
>>> p.nice(psutil.HIGH_PRIORITY_CLASS)
```

#### **I/O优先级**

**Process.ionice(ioclass=None, value=None)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.ionice) <a name="Process.ionice" ></a>

获取或设置进程的I/O良好度(优先级)。如果没有提供参数，它作为一个 get，在 Linux 上返回一个 `(ioclass, value)` 元组，在 Windows 上返回一个 ***ioclass*** 整数。如果提供了 ***ioclass*** ，它将作为一个集合。 在这种情况下，只能在 Linux 上指定一个附加值(***value***)，以便进一步提高或降低 I/O 优先级。下面是与平台相关的 ***ioclass*** 值。

Linux (参阅 [ioprio_get][ioprio_get]手册):

[ioprio_get]: https://linux.die.net/man/2/ioprio_get  "获取I/O优先级值手册"

* `IOPRIO_CLASS_RT`: (高) 该进程每次都首先访问磁盘。 小心使用它，因为它会使整个系统挨饿。 可以指定额外的优先级，范围从 `0`（最高）到 `7`（最低）。
* `IOPRIO_CLASS_BE`: (一般) 未设置特定 I/O 优先级的任何进程的默认值。 附加优先级范围从 `0`（最高）到 `7`（最低）。
* `IOPRIO_CLASS_IDLE`: (低) 在没有其他人需要磁盘时获取 I/O 时间。 不接受任何附加价值。
* `IOPRIO_CLASS_NONE`: 先前未设置优先级时返回。

Windows:

* `IOPRIO_HIGH`: 最高优先级.
* `IOPRIO_NORMAL`: 默认优先级.
* `IOPRIO_LOW`: 低优先级.
* `IOPRIO_VERYLOW`: 最低优先级.

下面是一个关于如何根据使用的平台设置最高 I/O 优先级的示例：

```python
>>> import psutil
>>> p = psutil.Process()
>>> if psutil.LINUX:
...     p.ionice(psutil.IOPRIO_CLASS_RT, value=7)
... else:
...     p.ionice(psutil.IOPRIO_HIGH)
...
>>> p.ionice()  # get
pionice(ioclass=<IOPriority.IOPRIO_CLASS_RT: 1>, value=7)
```

_可用平台: Linux, Windows Vista+ 。_

*5.6.2 版本中修改: Windows 接受新的 `IOPRIO_*` 常量，包括新的 `IOPRIO_HIGH`。*

#### **资源限制**

**Process.rlimit(resource, limits=None)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.rlimit) <a name="Process.rlimit" ></a>

读写进程资源限制(参见 [prlimit][prlimit] 手册)。 ***resource*** 是 [psutil.RLIMIT_*](#process-resources-const)常量之一。 ***limits*** 是一个 `(soft, hard)` 元组。本函数作用与 [resource.getrlimit][resource.getrlimit] 和 [resource.getrlimit][resource.getrlimit] 一样，不过本函数可以作用于任何进程PID，不仅仅是 [os.getpid][os.getpid]所获取的 。读时，返回值是一个 `(soft, hard)` 元组。每个值可以是 整数 或 [psutil.RLIMIT_*](#process-resources-const)。 例子：

[prlimit]: https://linux.die.net/man/2/prlimit "prlimit"
[resource.getrlimit]: https://docs.python.org/3/library/resource.html#resource.getrlimit  "resource.getrlimit"
[procinfo.py]: https://github.com/giampaolo/psutil/blob/master/scripts/procinfo.py "procinfo.py"

```python
>>> import psutil
>>> p = psutil.Process()
>>> p.rlimit(psutil.RLIMIT_NOFILE, (128, 128))   # process can open max 128 file descriptors
>>> p.rlimit(psutil.RLIMIT_FSIZE, (1024, 1024))  # can create files no bigger than 1024 bytes
>>> p.rlimit(psutil.RLIMIT_FSIZE)                # get
(1024, 1024)
>>>
```

同样参考 [procinfo.py][procinfo.py] 脚本

_可用平台: Linux, FreeBSD._

_5.7.3 版本中修改: 新增 FreeBSD 支持。_

#### I/O 统计

**Process.io_counters()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.io_counters) <a name="Process.io_counters" ></a>

返回以命名元组形式的进程I/O分析数据，在liunx平台上可以参考 [/proc 文件系统文档][proce filesystem document]。

[proce filesystem document]: https://stackoverflow.com/questions/3633286/what-do-the-counters-in-proc-pid-io-mean "What do the counters in /proc/[pid]/io mean?"

* `read_count`: 执行的读取操作数（累计）。 这应该计算的是与读取相关的系统调用的数量，例如 UNIX 上的 `read()` 和 `pread()`。
* `write_count`: 执行的写入操作数（累计）。 这应该计算的是与写入相关的系统调用的数量，例如 UNIX 上的 `write()` 和 `pwrite()`。
* `read_bytes`: 读取的字节数（累计）。 在 BSD 上总是 -1。
* `write_bytes`: 写入的字节数（累计）。 在 BSD 上总是 -1。
  
特定于 Linux:

* `read_chars` (Linux): 此进程传递给 `read()` 和 `pread()` 系统调用的字节数（累积）。与 `read_bytes` 不同，它不关心是否发生了实际的物理磁盘 I/O。
* `write_chars` (Linux): 此进程传递给 `write()` 和 `pwrite()` 系统调用的字节数（累积）。与 `write_bytes` 不同，它不关心是否发生了实际的物理磁盘 I/O。

特定于 Windows :

* `other_count` (Windows): 除读取和写入操作外执行的 I/O 操作数。
* `other_bytes` (Windows): 在读取和写入操作以外的操作期间传输的字节数。

```python
>>> import psutil
>>> p = psutil.Process()
>>> p.io_counters()
pio(read_count=454556, write_count=3456, read_bytes=110592, write_bytes=0, read_chars=769931, write_chars=203)
```

_可用平台: Linux, BSD, Windows, AIX._

*5.2.0 版本中修改: 在 Linux 平台增加 **read_chars** 和 **write_chars** 字段; 在 Windows 平台增加 **other_count** 和 **other_bytes** 字段.*

#### **上下文切换数**

**Process.num_ctx_switches()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.num_ctx_switches) <a name="Process.num_ctx_switches" ></a>

进程执行的自愿和非自愿上下文切换的次数（累积）。

_5.4.1 版本中修改: 增加 AIX 支持._

#### **文件描述符数**

**Process.num_fds()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.num_fds) <a name="Process.num_fds" ></a>

此进程当前打开的文件描述符的数量（非累积）。

_可用平台: UNIX._

#### **句柄数**

**Process.num_handles()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.num_handles) <a name="Process.num_handles" ></a>

此进程当前使用的句柄数（非累积）。

_可用平台: Windows。_

#### **线程数**

**Process.num_threads()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.num_threads) <a name="Process.num_threads" ></a>

此进程当前使用的线程数（非累积）。

#### **线程**

**Process.threads()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.threads) <a name="Process.threads" ></a>

将进程打开的线程作为命名元组列表返回。 在 OpenBSD 上，此方法需要 root 权限。

* `id`: 内核分配的原生线程ID。 如果 `pid` 引用当前进程，则与 [threading.Thread] 类的 [native_id][Thread.native_id] 属性匹配，并可将引用用于在当前的 Python 应用程序中运行的各个 Python 线程。
* `user_time`: 在用户模式下花费的时间。
* `system_time`: 在内核模式中花费的时间。

[Thread.native_id]: https://docs.python.org/3/library/threading.html#threading.Thread.native_id "Thread native id"
[threading.Thread]: https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread class"

#### **CPU时间**

**Process.cpu_times()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.cpu_times) <a name="Process.cpu_times" ></a>

Return a named tuple representing the accumulated process times, in seconds (see explanation). This is similar to os.times but can be used for any process PID.

返回一个命名元组，表示累计处理时间，以秒为单位（见[解释](http://stackoverflow.com/questions/556405/)）。 这类似于 [os.times][os.times] 但可用于任何进程 PID。

[os.times]: https://docs.python.org/zh-cn/library/os.html#os.times "os.times"

* `user`: 在用户模式下花费的时间。
* `system`: 在内核模式中花费的时间。
* `children_user`: 所有子进程的用户时间（在 Windows 和 macOS 上始终为 0）。
* `children_system`: 所有子进程的系统时间（在 Windows 和 macOS 上始终为 0）。
* `iowait`: (Linux) 等待阻塞 I/O 完成所花费的时间。 这个值被排除在用户和系统时间计数之外（因为 CPU 没有做任何工作）。

```python
>>> import psutil
>>> p = psutil.Process()
>>> p.cpu_times()
pcputimes(user=0.03, system=0.67, children_user=0.0, children_system=0.0, iowait=0.08)
>>> sum(p.cpu_times()[:2])  # cumulative, excluding children and iowait
0.70
```

*4.1.0 版本中修改: 返回两个额外的字段：**children_user** 和 **children_system** 。*

*5.6.4 版本中修改: 在 Linux 上添加了 **iowait** 字段。*

#### **CPU利用率**

**Process.cpu_percent(interval=None)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.cpu_percent) <a name="Process.cpu_percent" ></a>

返回一个浮点数，以百分比形式表示进程 CPU 利用率，如果进程在不同 CPU 上运行多个线程，则该值也可以 `> 100.0`。当间隔 `> 0.0` 时，将处理时间与间隔（阻塞）前后经过的系统 CPU 时间进行比较。当间隔为 `0.0` 或 `None` 时，将进程时间与自上次调用以来经过的系统 CPU 时间进行比较，立即返回。这意味着第一次调用它时，它会返回一个应该忽略的无意义的 `0.0` 值。在这种情况下，为了准确起见，建议在两次调用之间至少间隔 `0.1` 秒再次调用此函数。

例子:

```python
>>> import psutil
>>> p = psutil.Process()
>>> # blocking
>>> p.cpu_percent(interval=1)
2.0
>>> # non-blocking (percentage since last call)
>>> p.cpu_percent(interval=None)
2.9
```

`注意`: *如果进程在不同 CPU 内核上运行多个线程，则返回值可以 `> 100.0`。*

`注意`: 返回的值在所有可用 CPU 之间明确没有平均分配（与 [psutil.cpu_percent()](#psutil.cpu_percent) 不同）。 这意味着在具有 2 个逻辑 CPU 的系统上运行的繁忙循环进程将被报告为具有 100% 的 CPU 利用率而不是 50%。 这样做是为了与顶级(***top***) UNIX 实例程序保持一致，并且更容易识别独立于 CPU 数量而占用 CPU 资源的进程。 必须注意的是，Windows 上的 `taskmgr.exe` 不会像这样运行（它会报告 50% 的使用率）。 要模拟 Windows `taskmgr.exe` 行为，可以执行以下操作：`p.cpu_percent() / psutil.cpu_count()`。

`警告`: 第一次使用 `interval = 0.0` 或 `None` 调用此方法时，它将返回一个无意义的 `0.0` 值，应该忽略该值。

#### **CPU亲和度**

**Process.cpu_affinity(cpus=None)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.cpu_affinity) <a name="Process.cpu_affinity" ></a>

读写当前[CPU亲和度][CPU affinity]。[CPU亲和度][CPU affinity]包括告诉操作系统仅在一组有限的 CPU 上运行进程（在 Linux 命令行上，通常使用 taskset 命令）。如果没有传递参数，它会以整数列表的形式返回当前的 CPU 亲和性。如果传递参数，它必须是指定新 CPU 关联的整数列表。如果传递空列表，则假定（并设置）所有CPU 都符合条件。在某些系统（例如 Linux）上，所有可用的逻辑CPU并不能用 `list(range(psutil.cpu_count()))` 代表。

[CPU affinity]: http://www.linuxjournal.com/article/6799?page=0,0 "cpu 亲和度"

```python
>>> import psutil
>>> psutil.cpu_count()
4
>>> p = psutil.Process()
>>> # get
>>> p.cpu_affinity()
[0, 1, 2, 3]
>>> # set; from now on, process will run on CPU #0 and #1 only
>>> p.cpu_affinity([0, 1])
>>> p.cpu_affinity()
[0, 1]
>>> # reset affinity against all eligible CPUs
>>> p.cpu_affinity([])
```

可用平台: Linux, Windows, FreeBSD

_2.2.0 版本中修改: 新增 FreeBSD 支持._

_5.1.0 版本中修改: 可以传递一个空列表来设置所有 CPU 都符合条件。_

#### **CPU数量**

**Process.cpu_num()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.cpu_num) <a name="Process.cpu_num" ></a>

返回此进程当前正在运行的 CPU数。返回值应该 `<=` [psutil.cpu_count()][#psutil.cpu_count]。在 FreeBSD 上，某些内核进程可能返回 `-1`。它可以与 [psutil.cpu_percent(percpu=True)](#psutil.cpu_percent) 结合使用来观察分布在多个 CPU 上的系统工作负载，如 [cpu_distribution.py][cpu_distribution.py] 示例脚本所示。

[cpu_distribution.py]: https://github.com/giampaolo/psutil/blob/master/scripts/cpu_distribution.py "cpu_distribution.py"

_可用平台: Linux, FreeBSD, SunOS。_

5.1.0 版本中新增.

#### **内存信息**

**Process.memory_info()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.memory_info) <a name="Process.memory_info" ></a>

返回具有变量字段的命名元组，具体取决于表示有关进程的内存信息的平台。 所有平台上可用的 ***“portable”*** 字段是 `rss` 和 `vms` 。 所有数字都以字节表示。

| Linux  | macOS   | BSD   | Solaris | AIX | Windows                |
| ------ | ------- | ----- | ------- | --- | ---------------------- |
| rss    | rss     | rss   | rss     | rss | rss(`wset`的别名 )     |
| vms    | vms     | vms   | vms     | vms | vms (`pagefile`的别名) |
| shared | pfaults | text  | -       | -   | num_page_faults        |
| text   | pageins | data  | -       | -   | peak_wset              |
| lib    | -       | stack | -       | -   | wset                   |
| data   | -       | -     | -       | -   | peak_paged_pool        |
| dirty  | -       | -     | -       | -   | paged_pool             |
| -      | -       | -     | -       | -   | peak_nonpaged_pool     |
| -      | -       | -     | -       | -   | nonpaged_pool          |
| -      | -       | -     | -       | -   | pagefile               |
| -      | -       | -     | -       | -   | peak_pagefile          |
| -      | -       | -     | -       | -   | private                |

* `rss`: 又名 "**常驻内存大小**"(Resident Set Size), 这是进程使用的非交换物理内存。在 UNIX 上，它匹配“`top`”的 ***RES*** 列）。在 Windows 上，这是 ***wset*** 字段的别名，它匹配 `taskmgr.exe` 的 “Mem Usage” 列。
* `vms`: 又名 “**虚拟内存大小**”(Virtual Memory Size), 这是进程使用的虚拟内存总量。在 UNIX 上，它匹配“`top`”的 ***VIRT*** 列。 在 Windows 上，这是 ***pagefile*** 字段的别名，它匹配 `taskmgr.exe` 的“Mem Usage” “VM Size”列。
* `shared`: (Linux) 可能与其他进程**共享的内存**。 这与`“top”`的 ***SHR*** 列匹配。
* `text` (Linux, BSD): 又名 TRS (text resident set) 专用于可执行代码的内存量。 这与`“top”`的 ***CODE*** 列匹配。
* `data` (Linux, BSD): 又名 DRS (data resident set) 用于非可执行代码的物理内存量。它匹配`“top”`的 ***DATA*** 列。
* `lib` (Linux): 共享库使用的内存。
* `dirty` (Linux): 脏页数。
* `pfaults` (macOS): 页错误数。
* `pageins` (macOS): 实际页面的数量。

对于 Windows 字段的解释依赖于 [PROCESS_MEMORY_COUNTERS_EX][PROCESS_MEMORY_COUNTERS_EX] 结构文档。 Linux 上的示例：

[PROCESS_MEMORY_COUNTERS_EX]: https://docs.microsoft.com/en-us/windows/desktop/api/psapi/ns-psapi-_process_memory_counters_ex "process memory counters ex"

```python
>>> import psutil
>>> p = psutil.Process()
>>> p.memory_info()
pmem(rss=15491072, vms=84025344, shared=5206016, text=2555904, lib=0, data=9891840, dirty=0)
```

*4.0.0 版本中修改: 多个字段返回, 不仅仅是 **rss** 和 **vms**.*

**Process.memory_info_ex()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.memory_info_ex) <a name="Process.memory_info_ex" ></a>

与 [memory_info()](#Process.memory_info) 相同（已弃用）。

***⚠️警告**:*在 4.0.0 版本中已弃用；使用 [memory_info()](#Process.memory_info) 替换.*

#### **内存完全信息**

**Process.memory_full_info()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.memory_full_info) <a name="Process.memory_full_info" ></a>

此方法返回与 [memory_info()](#Process.memory_info) 相同的信息，此外，在某些平台（Linux、macOS、Windows）上，还提供额外的指标（`USS`、`PSS` 和 `swap` ）。附加指标更好地表示了“有效”进程内存消耗（在 USS 的情况下），如[本博文][blog-post]中详细解释的那样。它通过传递整个进程地址来实现。因此，它通常需要比 [memory_info()](#Process.memory_info) 更高的用户权限，并且速度要慢得多。在没有实现额外字段的平台上，这只是返回与 [memory_info()](#Process.memory_info) 相同的指标。

[blog-post]: https://gmpy.dev/blog/2016/real-process-memory-and-environ-in-python "blog post with USS"

* `uss` (Linux, macOS, Windows): 又名 “Unique Set Size”, 这是一个进程唯一的内存，如果进程现在终止，它将被释放。
* `pss` (Linux): 又名 “Proportional Set Size”, 是与其他进程共享的内存量，以在共享它的进程之间平均分配的方式计算。例如：如果一个进程拥有 10 MB 的空间，并且与另一个进程共享 10 MB，则其 PSS 将为 15 MB。
* `swap` (Linux): 已交换出到磁盘的内存量。

**注释**: *`uss` 可能是确定进程实际使用多少内存的最具代表性的指标。它表示如果进程现在终止将被释放的内存量。*

**译注**: 参考: [VSS/RSS/PSS/USS 的介绍](https://www.jianshu.com/p/3bab26d25d2e)

Linux 上的例子:

```python
>>> import psutil
>>> p = psutil.Process()
>>> p.memory_full_info()
pfullmem(rss=10199040, vms=52133888, shared=3887104, text=2867200, lib=0, data=5967872, dirty=0, uss=6545408, pss=6872064, swap=0)
>>>
```

同样参考示例脚本: [procsmem.py][procsmem.py]

[procsmem.py]: https://github.com/giampaolo/psutil/blob/master/scripts/procsmem.py "procsmem.py"

_4.0.0 版本中新增._

#### **内存利用率**

**Process.memory_percent(memtype="rss")** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.memory_percent) <a name="Process.memory_percent" ></a>

将进程内存与总物理系统内存进行比较，并以百分比形式计算进程内存利用率。 ***memtype*** 参数是一个字符串，它指示您要比较的进程内存类型。您可以在 [memory_info()](#Process.memory_info) 和 [memory_full_info()](#Process.memory_full_info) 返回的命名元组字段名称之间进行选择（默认为“***rss***”）。

*4.0.0 版本中修改: 新增 **memtype** 参数.*

#### **内存映射**

**Process.memory_maps(grouped=True)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.memory_maps) <a name="Process.memory_maps" ></a>

将进程的映射内存区域作为命名元组列表返回，其字段根据平台而变化。 此方法可用于获取进程内存使用情况的详细表示，如此处所述（最重要的值是“**私有**(private)”内存）。如果 ***grouped*** 为 `True`，则具有相同路径的映射区域将组合在一起，并且将不同的内存字段相加。如果 ***grouped*** 为 `False` ，则每个映射区域都显示为单个实体，命名元组还将包括映射区域的地址空间 (***addr***) 和权限集 (***perms***)。 有关示例应用程序，请参阅 [pmap.py][pmap.py]。

[pmap.py]: https://github.com/giampaolo/psutil/blob/master/scripts/pmap.py "pmap.py"

| Linux         | Windows | FreeBSD      | Solaris   |
| ------------- | ------- | ------------ | --------- |
| rss           | rss     | rss          | rss       |
| size          | -       | private      | anonymous |
| pss           | -       | ref_count    | locked    |
| shared_clean  | -       | shadow_count | -         |
| shared_dirty  | -       | -            | -         |
| private_clean | -       | -            | -         |
| private_dirty | -       | -            | -         |
| referenced    | -       | -            | -         |
| anonymous     | -       | -            | -         |
| swap          | -       | -            | -         |

```python
>>> import psutil
>>> p = psutil.Process()
>>> p.memory_maps()
[pmmap_grouped(path='/lib/x8664-linux-gnu/libutil-2.15.so', rss=32768, size=2125824, pss=32768, shared_clean=0, shared_dirty=0, private_clean=20480, private_dirty=12288, referenced=32768, anonymous=12288, swap=0),
pmmap_grouped(path='/lib/x8664-linux-gnu/libc-2.15.so', rss=3821568, size=3842048, pss=3821568, shared_clean=0, shared_dirty=0, private_clean=0, private_dirty=3821568, referenced=3575808, anonymous=3821568, swap=0),
...]
```

_可用平台: Linux, Windows, FreeBSD, SunOS。_

5.6.0 版本中修改: 删除 macOS 支持，因为天生就坏了(参见[问题#1291][issue-1291])

[issue-1291]: https://github.com/giampaolo/psutil/issues/1291 "issue #1291"

#### **子进程**

**Process.children(recursive=False)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.children) <a name="Process.children" ></a>

将此进程的子进程作为 Process 实例列表返回。如果 ***recursive*** 为 `True` ，则返回所有父子后代。假设A为一个进程的伪代码示例：

```python
  A ─┐
    │
    ├─ B (child) ─┐
    │             └─ X (grandchild) ─┐
    │                                └─ Y (great grandchild)
    ├─ C (child)
    └─ D (child)

>>> p.children()
B, C, D
>>> p.children(recursive=True)
B, X, Y, C, D
```

**注释**: 在上面的例子中，如果进程 X 消失，进程 Y 也不会被返回，因为对进程 A 的引用丢失了。 这个[单元测试][unite-test-children]很好地总结了这个概念。 另请参阅如何[终止进程树](#kill-process-tree)和[终止子进程](#kill-children-process)。

[unite-test-children]: https://github.com/giampaolo/psutil/blob/65a52341b55faaab41f68ebc4ed31f18f0929754/psutil/tests/test_process.py#L1064-L1075 "父子进程单元测试"

#### **打开的文件**

**Process.open_files()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.open_files) <a name="Process.open_files" ></a>

以命名元组列表返回进程打开的常规文件，包括以下字段：

* `path`: 绝对文件名。
* `fd`: 文件描述符编号； 在 Windows 上，这始终是 -1。

仅限 Linux：

* `position` (Linux): 文件（偏移）位置。
* `mode` (Linux): 一个字符串，指示文件是如何打开的，类似于 [open][builtin-open] 内置模式参数。 可能的值为`“r”`、`“w”`、`“a”`、`“r+”`和`“a+”`。 以二进制或文本模式（`“b”`或`“t”`）打开的文件之间没有区别。
* `flags` (Linux): 打开文件时传递给底层 C 调用 [os.open][os-open] 的标志（例如 [os.O_RDONLY][os-O-RDONLY]、[os.O_TRUNC][os-O-TRUNC] 等）。

[builtin-open]: https://docs.python.org/zh-cn/3/library/functions.html#open "内建函数open"
[os-open]: https://docs.python.org/3/library/os.html#os.open "os.open"
[os-O-RDONLY]: https://docs.python.org/3/library/os.html#os.O_RDONLY "os.O_RDONLY"
[os-O-TRUNC]: https://docs.python.org/3/library/os.html#os.O_TRUNC "os.O_TRUNC"

```python
>>> import psutil
>>> f = open('file.ext', 'w')
>>> p = psutil.Process()
>>> p.open_files()
[popenfile(path='/home/giampaolo/svn/psutil/file.ext', fd=3, position=0, mode='w', flags=32769)]
```

**⚠️警告**: 在 Windows 上，由于底层 Windows API 的一些限制，在检索某些文件句柄时可能会挂起，因此此方法不可靠。 为了解决这个问题，psutil 会生成一个线程来确定文件句柄名称，如果它在 100 毫秒后没有响应，则将其杀死。这意味着 Windows 上的此方法不能保证枚举所有常规文件句柄（请参阅[问题 597][issue-597]）。 像 ***ProcessHacker*** 这样的工具也有同样的限制。

[issue-597]: https://github.com/giampaolo/psutil/pull/595 "issue-#597"

**⚠️警告**: 在 BSD 上，由于内核错误，此方法可以返回带有空路径（`“”`）的文件，因此它不可靠（请参阅[问题 597][issue-597]）。

_3.1.0 版本中修改: 不再挂在 Windows 上。_

*4.1.0 版本中修改: Linux平台中新增 **position** , **mode** 和 **flags** 字段。*

#### **网络连接**

**Process.connections(kind="inet")** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.connections) <a name="Process.connections" ></a>

将进程打开的socket连接作为命名元组列表返回。要获得系统范围的连接，请使用 [psutil.net_connections()](#psutil.net_connections)。 每个命名元组提供 6 个属性：

* `fd`: 套接字文件描述符。 这可以传递给 [socket.fromfd][socket.fromfd] 以获得可用的套接字对象。在 Windows、FreeBSD 和 SunOS 上，它始终设置为 -1。
* `family`: 地址族，[AF_INET][AF_INET]、[AF_INET6][AF_INET6] 或 [AF_UNIX][AF_UNIX] 。
* `type`: 地址类型，[SOCK_STREAM][SOCK_STREAM] 、[SOCK_DGRAM][SOCK_DGRAM] 或 [SOCK_SEQPACKET][SOCK_SEQPACKET] 。
* `laddr`: 在 [AF_UNIX][AF_UNIX] 套接字的情况下，本地地址作为 `(ip, port)` 命名元组或路径。 对于 UNIX 套接字，请参阅下面的注释。
* `raddr`: 在 UNIX 套接字的情况下，远程地址作为`(ip, port)` 命名元组或绝对路径。 当远程端点未连接时，您将获得一个空元组 (**AF_INET\***) 或 `""` (**AF_UNIX**)。 对于 UNIX 套接字，请参阅下面的注释。
* `status`: 表示 TCP 连接的状态。 返回值是 [psutil.CONN_*](#connections-constants) 常量之一。 对于 UDP 和 UNIX 套接字，这始终是 [psutil.CONN_NONE](#psutil.CONN_NONE)。

***kind*** 参数是一个字符串，用于过滤符合以下条件的连接：

| Kind 值   | 网络连接使用                   |
| --------- | ------------------------------ |
| `"inet"`  | IPv4 和 IPv6                   |
| `"inet4"` | IPv4                           |
| `"inet6"` | IPv6                           |
| `"tcp"`   | TCP                            |
| `"tcp4"`  | 基于 IPv4 的 TCP               |
| `"tcp6"`  | 基于 IPv6 的 TCP               |
| `"udp"`   | UDP                            |
| `"udp4"`  | 基于 IPv4 的 UDP               |
| `"udp6"`  | 基于 IPv6 的 UDP               |
| `"unix"`  | UNIX 套接字（UDP 和 TCP 协议） |
| `"all"`   | 所有可能的族和协议的总和       |

例子:

```python
>>> import psutil
>>> p = psutil.Process(1694)
>>> p.name()
'firefox'
>>> p.connections()
[pconn(fd=115, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=addr(ip='10.0.0.1', port=48776), raddr=addr(ip='93.186.135.91', port=80), status='ESTABLISHED'),
pconn(fd=117, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=addr(ip='10.0.0.1', port=43761), raddr=addr(ip='72.14.234.100', port=80), status='CLOSING'),
pconn(fd=119, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=addr(ip='10.0.0.1', port=60759), raddr=addr(ip='72.14.234.104', port=80), status='ESTABLISHED'),
pconn(fd=123, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>, laddr=addr(ip='10.0.0.1', port=51314), raddr=addr(ip='72.14.234.83', port=443), status='SYN_SENT')]
```

**注释**: _(Solaris) 不支持 UNIX 套接字。_

**注释**: *(Linux, FreeBSD) UNIX 套接字的“**raddr**”字段始终设置为`“”`。 这是操作系统的限制。*

**注释**: (OpenBSD) *UNIX 套接字的“**laddr**”和“**raddr**”字段始终设置为`“”`。 这是操作系统的限制。*

**注释**: (AIX) [psutil.AccessDenied](#psutil.AccessDenied) 异常总是抛出，除非以 `root` 身份运行（`lsof` 也是如此）。

*5.3.0 版本中修改: : “**laddr**”和“**raddr**”被命名为元组。*

#### **是否正在运行**

**Process.is_running()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.is_running) <a name="Process.is_running" ></a>

返回当前进程是否在当前进程列表中运行。 这在进程消失并且它的 PID 被另一个进程重用的情况下也是可靠的，因此它优于执行 `psutil.pid_exists(p.pid)`。

**注释**: 如果进程是僵尸进程（`p.status() == psutil.STATUS_ZOMBIE`），这也将返回 `True`。

#### **发送信号**

**Process.send_signal(signal)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.send_signal) <a name="Process.send_signal" ></a>

发送信号(参阅 [信号模块手册][信号模块手册])以抢先检查 PID 是否已被重用。在 UNIX 上，这与 `os.kill(pid, sig)` 相同。在 Windows 上仅支持 `SIGTERM` `、CTRL_C_EVENT` 和 `CTRL_BREAK_EVENT` 信号，并且 `SIGTERM` 被视为 [kill()](#Process.kill) 的别名。另请参阅如何[终止进程树](#kill-process-tree)和[终止子进程](#kill-child-process)。

[信号模块手册]: https://docs.python.org//library/signal.html "signal module"

*3.2.0 版本中修改: 添加了对 Windows 上的 `CTRL_C_EVENT` 和 `CTRL_BREAK_EVENT` 信号的支持。*

#### **暂停运行**

**Process.suspend()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.suspend) <a name="Process.suspend" ></a>

使用 ***SIGSTOP*** 信号暂停进程执行抢先检查 PID 是否已被重用。 在 UNIX 上，这与 `os.kill(pid, signal.SIGSTOP)` 相同。 在 Windows 上，这是通过暂停所有进程线程执行来完成的。

#### **恢复运行**

**Process.resume()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.resume) <a name="Process.resume" ></a>

使用 SIGCONT 信号恢复进程执行抢先检查 PID 是否已被重用。 在 UNIX 上，这与 `os.kill(pid, signal.SIGCONT)` 相同。 在 Windows 上，这是通过恢复所有进程线程执行来完成的。

#### **终止进程**

**Process.terminate()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.terminate) <a name="Process.terminate" ></a>

使用 SIGTERM 信号预先检查 PID 是否已被重用终止进程。 在 UNIX 上，这与 `os.kill(pid, signal.SIGTERM)` 相同。 在 Windows 上，这是 [kill()](#Process.kill) 的别名。 另请参阅如何[终止进程树](#kill-process-tree)和[终止子进程](#kill-child-process)。

#### **杀死进程**

**Process.kill()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.kill) <a name="Process.kill" ></a>

通过使用 SIGKILL 信号抢先检查 PID 是否已被重用来杀死当前进程。 在 UNIX 上，这与 `os.kill(pid, signal.SIGKILL)` 相同。 在 Windows 上，这是通过使用 [TerminateProcess][win.TerminateProcess] 来完成的。 另请参阅如何[终止进程树](#kill-process-tree)和[终止子进程](#kill-child-process)。

[win.TerminateProcess]: https://docs.microsoft.com/en-us/windows/desktop/api/processthreadsapi/nf-processthreadsapi-terminateprocess "WIN终止进程"

#### **等待**

**Process.wait(timeout=None)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Process.wait)  <a name="Process.wait" ></a>

等待进程 PID 终止。 有关返回值的详细信息在 UNIX 和 Windows 上有所不同。

在 UNIX: 如果进程正常终止，则返回值是一个正整数 `>= 0` 表示退出代码。 如果进程被信号终止，则返回导致终止的信号的否定值（例如 `-SIGTERM`）。如果 PID 不是 [os.getpid][os.getpid]（当前进程）的子进程，请等待进程消失并返回 `None` 。 如果 PID 不存在，则立即返回 `None` 。

[getExitCodeProcess]: https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getexitcodeprocess "getExitCodeProcess"

在 Windows: 始终返回退出代码，它是由 [GetExitCodeProcess][getExitCodeProcess] 返回的正整数。

***timeout*** 参数以秒表示。 如果指定并且进程仍然活着，则引发 [TimeoutExpired](#psutil.TimeoutExpired) 异常。 `timeout=0` 可用于非阻塞应用程序：它会立即返回或引发 [TimeoutExpired](#psutil.TimeoutExpired) 异常。

返回值被缓存。 要等待多个进程，请使用 [psutil.wait_procs()](#psutil.wait_proces) 。

```python
>>> import psutil
>>> p = psutil.Process(9891)
>>> p.terminate()
>>> p.wait()
<Negsignal.SIGTERM: -15>
```

5.7.1 版本中修改: 返回值被缓存（而不是返回 `None` ）。

5.7.1 版本中修改: 在 POSIX 上，如果出现负信号，则将以可读的枚举返回。

#### **执行子程序**

**`class` psutil.Popen(\*args, \*\*kwargs)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.Popen) <a name="Popen" ></a>

与 [subprocess.Popen][subprocess.Popen] 相同，但此外它还在单个类中提供所有 [psutil.Process][psutil.Process] 的方法。 对于以下两个类共有的方法，psutil 的实现更优先：[send_signal()](#Process.send_signal)、[terminate()](#Process.terminate)、[kill()](#Process.kill)。 这样做是为了避免在其 `PID` 被重用的情况下杀死另一个进程，修复了 [BPO-6973][BPO-6973]。

[subprocess.Popen]: https://docs.python.org/zh-cn/3/library/subprocess.html#subprocess.Popen "subprocess.Popen"
[psutil.Process]: #psutil.Process "psutil.Process"
[BPO-6973]: https://bugs.python.org/issue6973 "BPO-6973"

```python
>>> import psutil
>>> from subprocess import PIPE
>>>
>>> p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"], stdout=PIPE)
>>> p.name()
'python'
>>> p.username()
'giampaolo'
>>> p.communicate()
('hello\n', None)
>>> p.wait(timeout=2)
0
>>>
```

_版本 4.4.0 中改变: 新增支持上下文管理._

## **Windows 服务** (Windows services)

### **迭代服务**

**psutil.win_service_iter()** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.win_service_iter)<a name="psutil.win_service_iter"></a>

返回一个迭代器，为安装的所有 Windows 服务生成一个 [WindowsService](https://psutil.readthedocs.io/en/latest/#psutil.WindowsService) 类实例。

_版本 4.2.0 中新增._

_可用平台: Windows。_

### **根据名称获取服务**

**psutil.win_service_get(name)** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.win_service_get)<a name="psutil.win_service_get"></a>

按名称获取 Windows 服务，返回 [WindowsService](https://psutil.readthedocs.io/en/latest/#psutil.WindowsService) 实例。 如果不存在具有此类名称的服务，则抛出 [psutil.NoSuchProcess](https://psutil.readthedocs.io/en/latest/#psutil.NoSuchProcess) 异常。

_版本 4.2.0 中新增._

_可用平台: Windows._

### **win服务类**

`class` **psutil.WindowsService** - [原文](https://psutil.readthedocs.io/en/latest/#psutil.WindowsService)

表示具有给定名称的 Windows 服务。 此类由 [win_service_iter()](#psutil.win_service_iter) 和 [win_service_get()](#psutil.win_service_get) 函数返回，不应直接实例化。

* `name`() - [原文](https://psutil.readthedocs.io/en/latest/#psutil.WindowsService.name)
    服务名称. 此字符串是引用服务的方式，可以传递给 [win_service_get()](#psutil.win_service_get) 获取一个新的 WindowsService 实例。
* `display_name`() - [原文](https://psutil.readthedocs.io/en/latest/#psutil.WindowsService.display_name)
    服务显示名称。当这个类被实例化时，该值被缓存。
* `binpath`() - [原文](https://psutil.readthedocs.io/en/latest/#psutil.WindowsService.binpath)
    作为字符串的服务二进制/exe 文件的完全限定路径，包括命令行参数。
* `username`() - [原文](https://psutil.readthedocs.io/en/latest/#psutil.WindowsService.username)
    拥有此服务的用户的名称。
* `start_type`() - [原文](https://psutil.readthedocs.io/en/latest/#psutil.WindowsService.start_type)
    一个字符串，可以是“自动”(automatic)、“手动”(manual)或“禁用”(disabled)。
* `pid`() - [原文](https://psutil.readthedocs.io/en/latest/#psutil.WindowsService.pid)
    进程 PID，如果有，否则为 `None` 。 这可以传递给 [Process](#psutil.Process) 类来控制服务的进程。
* `status`() - [原文](https://psutil.readthedocs.io/en/latest/#psutil.WindowsService.status)
    服务状态为字符串，可以是“running”、“paused”、“start_pending”、“pause_pending”、“continue_pending”、“stop_pending”或“stopped”。
* `description`() - [原文](https://psutil.readthedocs.io/en/latest/#psutil.WindowsService.description)
    服务详细说明。
* `as_dict`()- [原文](https://psutil.readthedocs.io/en/latest/#psutil.WindowsService.as_dict)
    将上述所有信息作为字典检索的实例方法。

_版本 4.2.0 中新增._

_可用平台: Windows._

演示代码:

```python
>>> import psutil
>>> list(psutil.win_service_iter())
[<WindowsService(name='AeLookupSvc', display_name='Application Experience') at 38850096>,
<WindowsService(name='ALG', display_name='Application Layer Gateway Service') at 38850128>,
<WindowsService(name='APNMCP', display_name='Ask Update Service') at 38850160>,
<WindowsService(name='AppIDSvc', display_name='Application Identity') at 38850192>,
...]
>>> s = psutil.win_service_get('alg')
>>> s.as_dict()
{'binpath': 'C:\\Windows\\System32\\alg.exe',
'description': 'Provides support for 3rd party protocol plug-ins for Internet Connection Sharing',
'display_name': 'Application Layer Gateway Service',
'name': 'alg',
'pid': None,
'start_type': 'manual',
'status': 'stopped',
'username': 'NT AUTHORITY\\LocalService'}
```

## **常量** (Constants)

### **操作系统**

参考: [原文](https://psutil.readthedocs.io/en/latest/#operating-system-constants)

* psutil.**POSIX**
* psutil.**LINUX**
* psutil.**WINDOWS**
* psutil.**MACOS**
* psutil.**FREEBSD**
* psutil.**NETBSD**
* psutil.**OPENBSD**
* psutil.**BSD**
* psutil.**SUNOS**
* psutil.**AIX**
  `bool` 常量, 该常量定义了你属于什么平台. 例如: 如果在Windows平台, **WINDOWS** 常量将会为 `True`, 其他平台将会为 `False`.
  版本 4.0.0. 中新增
  版本 5.4.0 中改变过: 新增 AIX

* psutil.**OSX**
  **MACOS** 的别名.
  **注意**: 版本 5.4.7 中已弃用; 使用 **MACOS** 替换.
  
* psutil.**PROCFS_PATH**
  Linux、Solaris 和 AIX 上 /proc 文件系统的路径（默认为`“/proc”`）。您可能希望在导入 psutil 后立即重新设置此常量，以防您的 /proc 文件系统安装在其他地方，或者您想检索有关 Linux 容器（如 Docker、Heroku 或 LXC）的信息（请参阅[此处](https://fabiokung.com/2014/03/13/memory-inside-linux-containers/)了解更多信息）。必须注意的是，此技巧仅适用于依赖 /proc 文件系统的 API（例如[内存 API](#内存-Memory)和大多数 [Process](#psutil.Process) 类方法）。
  可用平台: Linux, Solaris, AIX
  _3.2.3 版本中新增._
  _3.4.2 版本中修改: 也可在 Solaris 上使用。_
  _5.4.0 版本中修改: 也可以在 AIX 上使用。_

### **进程状态** (Process status constants) <a name="process-status-constant"></a>

参考: [原文](https://psutil.readthedocs.io/en/latest/#process-status-constants)

* psutil.**STATUS_RUNNING**
* psutil.**STATUS_SLEEPING**
* psutil.**STATUS_DISK_SLEEP**
* psutil.**STATUS_STOPPED**
* psutil.**STATUS_TRACING_STOP**
* psutil.**STATUS_ZOMBIE**
* psutil.**STATUS_DEAD**
* psutil.**STATUS_WAKE_KILL**
* psutil.**STATUS_WAKING**
* psutil.**STATUS_PARKED)**(_Linux_)
* psutil.**STATUS_IDLE)**(_Linux_, _macOS_, _FreeBSD_)
* psutil.**STATUS_LOCKED)**(_FreeBSD_)
* psutil.**STATUS_WAITING)**(_FreeBSD_)
* psutil.**STATUS_SUSPENDED)**(_NetBSD_
  表示进程状态。 由 [psutil.Process.status()](#Process.status) 返回。
  _3.4.1 版本中新增: STATUS_SUSPENDED (NetBSD)._
  _5.4.7 版本中新增: STATUS_PARKED (Linux)._

### **进程优先级** (Process priority constants) <a name="process-priority-constant"></a>

参考: [原文](https://psutil.readthedocs.io/en/latest/#process-priority-constants)

[ionice]: http://linux.die.net/man/1/ionice "ionice"

* psutil.**REALTIME_PRIORITY_CLASS**
* psutil.**HIGH_PRIORITY_CLASS**
* psutil.**ABOVE_NORMAL_PRIORITY_CLASS**
* psutil.**ABOVE_NORMAL_PRIORITY_CLASS**
* psutil.**NORMAL_PRIORITY_CLASS**
* psutil.**IDLE_PRIORITY_CLASS**
* psutil.**BELOW_NORMAL_PRIORITY_CLASS**
  表示 Windows 上进程的优先级（请参阅 [SetPriorityClass][SetPriorityClass]）。 它们可以与 [psutil.Process.nice()](#Process.nice) 结合使用来获取或设置进程优先级。
  可用平台: Windows
* psutil.**IOPRIO_CLASS_NONE**
* psutil.**IOPRIO_CLASS_RT**
* psutil.**IOPRIO_CLASS_BE**
* psutil.**IOPRIO_CLASS_IDLE**
  一组整数，表示 Linux 上进程的 I/O 优先级。 它们可以与 [psutil.Process.nice()](#Process.nice) 结合使用来获取或设置进程 I/O 优先级。 ***IOPRIO_CLASS_NONE*** 和 ***IOPRIO_CLASS_BE*** （尽力而为）是任何未设置特定 I/O 优先级的进程的默认值。***IOPRIO_CLASS_RT***（实时）意味着进程将首先访问磁盘，而不管系统中发生了什么。 ***IOPRIO_CLASS_IDLE*** 意味着当没有其他人需要磁盘时，进程将获得 I/O 时间。 有关更多信息，请参阅 [ionice][ionice] 命令行实用程序或 [ioprio_get] 系统调用的手册。
  可用平台: Linux
* psutil.**IOPRIO_VERYLOW**
* psutil.**IOPRIO_LOW**
* psutil.**IOPRIO_NORMAL**
* psutil.**IOPRIO_HIGH**
  一组整数，表示 Windows 上进程的 I/O 优先级。 它们可以与 [psutil.Process.nice()](#Process.nice) 结合使用来获取或设置进程 I/O 优先级。
  _可用平台: Windows._
  _5.6.2 版本中新增._

### **进程资源** (Process resources constants) <a name="process-resources-const"></a>

参考: [原文](https://psutil.readthedocs.io/en/latest/#process-resources-constants)

* **Linux** / **FreeBSD**:
  * psutil.**RLIM_INFINITY**
  * psutil.**RLIMIT_AS**
  * psutil.**RLIMIT_CORE**
  * psutil.**RLIMIT_CPU**
  * psutil.**RLIMIT_DATA**
  * psutil.**RLIMIT_FSIZE**
  * psutil.**RLIMIT_MEMLOCK**
  * psutil.**RLIMIT_NOFILE**
  * psutil.**RLIMIT_NPROC**
  * psutil.**RLIMIT_RSS**
  * psutil.**RLIMIT_STACK**
* 仅限 **Linux**:
  * psutil.**RLIMIT_LOCKS**
  * psutil.**RLIMIT_MSGQUEUE**
  * psutil.**RLIMIT_NICE**
  * psutil.**RLIMIT_RTPRIO**
  * psutil.**RLIMIT_RTTIME**
  * psutil.**RLIMIT_SIGPENDING**
* 仅限 **FreeBSD**:
  * psutil.**RLIMIT_SWAP**
  * psutil.**RLIMIT_SBSIZE**
  * psutil.**RLIMIT_NPTS**

用于获取和设置与 [psutil.Process.rlimit()](#Process.rlimit) 结合使用的进程资源限制的常量。 有关更多信息，请参阅 [resource.getrlimit][resource.getrlimit]。

_可用平台: Linux, FreeBSD._

5.7.3 版本中修改: 新增 FreeBSD 支持, 新增 ***RLIMIT_SWAP***, ***RLIMIT_SBSIZE***, ***RLIMIT_NPTS*** 常量.

### **网络连接** (Connections constants) <a name="connections-constants">

参考: [原文](https://psutil.readthedocs.io/en/latest/#connections-constants)

* psutil.**CONN_ESTABLISHED**
* psutil.**CONN_SYN_SENT**
* psutil.**CONN_SYN_RECV**
* psutil.**CONN_FIN_WAIT1**
* psutil.**CONN_FIN_WAIT2**
* psutil.**CONN_TIME_WAIT**
* psutil.**CONN_CLOSE**
* psutil.**CONN_CLOSE_WAIT**
* psutil.**CONN_LAST_ACK**
* psutil.**CONN_LISTEN**
* psutil.**CONN_CLOSING**
* psutil.**CONN_NONE**  <a name="psutil.CONN_NONE"></a>
* psutil.**CONN_DELETE_TCB**(_Windows_)
* psutil.**CONN_IDLE**(_Solaris_)
* psutil.**CONN_BOUND**(_Solaris_)

一组表示 TCP 连接状态的字符串。 由 [psutil.Process.connections()](#Process.connections) 和 [psutil.net_connections()](#psutil.net_connections)（status 字段）返回。

### **硬件** (Hardware constants)

参考: [原文](https://psutil.readthedocs.io/en/latest/#hardware-constants)

* AF_LINK <a name="psutil.AF_LINK"></a>
  标识与网络接口关联的 MAC 地址的常量。 与 [psutil.net_if_addrs()](#psutil.net_if_addrs) 结合使用。
  _3.0.0 版本中新增._
* NIC_DUPLEX_FULL <a name="psutil.NIC_DUPLEX_FULL"></a>
* NIC_DUPLEX_HALF <a name="psutil.NIC_DUPLEX_HALF"></a>
* NIC_DUPLEX_UNKNOWN <a name="psutil.NIC_DUPLEX_UNKNOWN"></a>
  标识 NIC（网络接口卡）是全速模式还是半速模式的常量。 ***NIC_DUPLEX_FULL*** 表示网卡可以同时发送和接收数据（文件），***NIC_DUPLEX_FULL*** 表示网卡可以一次发送或接收数据。 与 [psutil.net_if_stats()](#psutil.net_if_stats) 结合使用。
  _3.0.0 版本中新增._
* POWER_TIME_UNKNOWN <a name="psutil.POWER_TIME_UNKNOWN">
* POWER_TIME_UNLIMITED <a name="psutil.POWER_TIME_UNLIMITED">
  电池剩余时间是否无法确定或无限。 可以分配给 [psutil.sensors_battery()](#psutil.sensors_battery) 的 ***secsleft*** 字段。
  5.1.0 版本中新增.
* version_info
  检查 psutil 安装版本的元组。 例子：

  ```python
  >>> import psutil
  >>> if psutil.version_info >= (4, 5):
  ...    pass
  ```

## **工具函数** (Recipes)

### **按名称查找进程** (Find process by name) <a name="find-process-by-name"></a>

参考: [原文](https://psutil.readthedocs.io/en/latest/#find-process-by-name)

根据 [Process.name()](#Process.name) 核查字符串：

```python
import psutil

def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(['name']):
        if p.info['name'] == name:
            ls.append(p)
    return ls
```

更高级一点，根据 [Process.name()](#Process.name)、[Process.exe()](#Process.exe) 和 [Process.cmdline()](#Process.cmdline) 检查字符串：

```python
import os
import psutil

def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(["name", "exe", "cmdline"]):
        if name == p.info['name'] or \
                p.info['exe'] and os.path.basename(p.info['exe']) == name or \
                p.info['cmdline'] and p.info['cmdline'][0] == name:
            ls.append(p)
    return ls
```

### **终止进程树** (Kill process tree) <a name="kill-process-tree"></a>

参考: [原文](https://psutil.readthedocs.io/en/latest/#kill-process-tree)

```python
import os
import signal
import psutil

def kill_proc_tree(pid, sig=signal.SIGTERM, include_parent=True,
                   timeout=None, on_terminate=None):
    """Kill a process tree (including grandchildren) with signal
    "sig" and return a (gone, still_alive) tuple.
    "on_terminate", if specified, is a callback function which is
    called as soon as a child terminates.
    """
    assert pid != os.getpid(), "won't kill myself"
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    if include_parent:
        children.append(parent)
    for p in children:
        try:
            p.send_signal(sig)
        except psutil.NoSuchProcess:
            pass
    gone, alive = psutil.wait_procs(children, timeout=timeout,
                                    callback=on_terminate)
    return (gone, alive)
```

### **过滤和排序进程** (Filtering and sorting processes)

参考: [原文](https://psutil.readthedocs.io/en/latest/#filtering-and-sorting-processes)

这个代码样例合集将展示如果通过`process_iter()`函数去过滤和排序进程。开始:

```python
>>> import psutil
>>> from pprint import pprint as pp
```

当前用户拥有的进程:

```python
>>> import getpass
>>> pp([(p.pid, p.info['name']) for p in psutil.process_iter(['name', 'username']) if p.info['username'] == getpass.getuser()])
(16832, 'bash'),
(19772, 'ssh'),
(20492, 'python')]
```

正在运行的进程:

```python
>>> pp([(p.pid, p.info) for p in psutil.process_iter(['name', 'status']) if p.info['status'] == psutil.STATUS_RUNNING])
[(1150, {'name': 'Xorg', 'status': 'running'}),
 (1776, {'name': 'unity-panel-service', 'status': 'running'}),
 (20492, {'name': 'python', 'status': 'running'})]
```

使用log日志文件的进程:

```python
>>> for p in psutil.process_iter(['name', 'open_files']):
...      for file in p.info['open_files'] or []:
...          if file.path.endswith('.log'):
...               print("%-5s %-10s %s" % (p.pid, p.info['name'][:10], file.path))
...
1510  upstart    /home/giampaolo/.cache/upstart/unity-settings-daemon.log
2174  nautilus   /home/giampaolo/.local/share/gvfs-metadata/home-ce08efac.log
2650  chrome     /home/giampaolo/.config/google-chrome/Default/data_reduction_proxy_leveldb/000003.log
```

进程消耗超过500M的内存:

```python
>>> pp([(p.pid, p.info['name'], p.info['memory_info'].rss) for p in psutil.process_iter(['name', 'memory_info']) if p.info['memory_info'].rss > 500 * 1024 * 1024])
[(2650, 'chrome', 532324352),
 (3038, 'chrome', 1120088064),
 (21915, 'sublime_text', 615407616)]
```

CPU耗时最多的前 3 个进程：

```python
>>> pp([(p.pid, p.info['name'], sum(p.info['cpu_times'])) for p in sorted(psutil.process_iter(['name', 'cpu_times']), key=lambda p: sum(p.info['cpu_times'][:2]))][-3:])
[(2721, 'chrome', 10219.73),
 (1150, 'Xorg', 11116.989999999998),
 (2650, 'chrome', 18451.97)]
```

### **字节转换** (Bytes conversion)

参考: [原文](https://psutil.readthedocs.io/en/latest/#bytes-conversion)

```python
import psutil

def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

total = psutil.disk_usage('/').total
print(total)
print(bytes2human(total))
```

…打印:

```python
100399730688
93.5G
```

## **常见问题** (FAQs)

参考: [原文](https://psutil.readthedocs.io/en/latest/#faqs)

* Q: 为什么某些进程我会无权限?
* A: 当你查询其他用户拥有的进程时可能会发生这种情况，尤其是在 macOS (参考[问题 #883](https://github.com/giampaolo/psutil/issues/883)) 和 Windows 上。不幸的是，除了以更高的权限运行 Python 进程之外，对此无能为力。 在 Unix 上，你可以以 root 身份运行 Python 进程或使用 SUID 位（ps 和 netstat 执行此操作）。 在 Windows 上，你可以将 Python 进程作为 NT AUTHORITY\SYSTEM 运行，或者将 Python 脚本安装为 Windows 服务（ProcessHacker 执行此操作）。
* Q: 支持在windows系统的MinGW上运行吗?
* A: 不支持, 你应该使用 Visual Studio (参阅 [开发指南](https://github.com/giampaolo/psutil/blob/master/docs/DEVGUIDE.rst)).

## **测试** (Running tests)

参考: [原文](https://psutil.readthedocs.io/en/latest/#running-tests)

```python
python3 -m psutil.tests
```

### debug模式 (Debug mode) - [原文](https://psutil.readthedocs.io/en/latest/#debug-mode)

如果想调试异常情况或报告一个漏洞，使用环境变量`PSUTIL_DEBUG`开启调试模式将会非常有用。在调试模式中，psutil会(或者不会)打印额外的信息到标准错误输出(stderr)。通常这些错误情况并不严重，因此常被忽略（防止崩溃）。在调试模式启动时单元测试是自动运行的。在Unix中：

```python
$ PSUTIL_DEBUG=1 python3 script.py
psutil-debug [psutil/_psutil_linux.c:150]> setmntent() failed (ignored)
```

在windows系统中:

```python
set PSUTIL_DEBUG=1 python.exe script.py
psutil-debug [psutil/arch/windows/process_info.c:90]> NtWow64ReadVirtualMemory64(pbi64.PebBaseAddress) -> 998 (Unknown error) (ignored)
```

## **安全** (Security)

参考: [原文](https://psutil.readthedocs.io/en/latest/#security)

在报告安全漏洞时, 请使用 [Tidelift 安全联系人](https://tidelift.com/security). Tidelift 将协调修复和披露。

## **开发指南** (Development guide)

参考: [原文](https://psutil.readthedocs.io/en/latest/#development-guide-1)

如果你想开发psutil，先看看[开发指南](https://github.com/giampaolo/psutil/blob/master/docs/DEVGUIDE.rst).

## **平台支持历史** (Platforms support history)

参考: [原文](https://psutil.readthedocs.io/en/latest/#platforms-support-history)

* psutil 5.8.1 (2021-10): MidnightBSD
* psutil 5.8.0 (2020-12): PyPy 2 on Windows
* psutil 5.7.1 (2020-07): Windows Nano
* psutil 5.7.0 (2020-02): drop Windows XP & Server 2003 support
* psutil 5.7.0 (2020-02): PyPy 3 on Windows
* psutil 5.4.0 (2017-11): AIX
* psutil 3.4.1 (2016-01): NetBSD
* psutil 3.3.0 (2015-11): OpenBSD
* psutil 1.0.0 (2013-07): Solaris
* psutil 0.1.1 (2009-03): FreeBSD
* psutil 0.1.0 (2009-01): Linux, Windows, macOS

支持的python版本是 `2.6`, `2.7`, `3.4+` 和 `PyPy3`.

## **时间线** (Timeline)

参考: [原文](https://psutil.readthedocs.io/en/latest/#timeline)

* 2020-12-19: [5.8.0](https://pypi.org/project/psutil/5.8.0/#files) - [what’s new](https://github.com/giampaolo/psutil/blob/master/HISTORY.rst#580) - [diff](https://github.com/giampaolo/psutil/compare/release-5.7.3...release-5.8.0#files_bucket)
* 2020-10-23: 5.7.3 - what’s new - diff
* 2020-07-15: 5.7.2 - what’s new - diff
* 2020-07-15: 5.7.1 - what’s new - diff
* 2020-02-18: 5.7.0 - what’s new - diff
* 2019-11-26: 5.6.7 - what’s new - diff
* 2019-11-25: 5.6.6 - what’s new - diff
* 2019-11-06: 5.6.5 - what’s new - diff
* 2019-11-04: 5.6.4 - what’s new - diff
* 2019-06-11: 5.6.3 - what’s new - diff
* 2019-04-26: 5.6.2 - what’s new - diff
* 2019-03-11: 5.6.1 - what’s new - diff
* 2019-03-05: 5.6.0 - what’s new - diff
* 2019-02-15: 5.5.1 - what’s new - diff
* 2019-01-23: 5.5.0 - what’s new - diff
* 2018-10-30: 5.4.8 - what’s new - diff
* 2018-08-14: 5.4.7 - what’s new - diff
* 2018-06-07: 5.4.6 - what’s new - diff
* 2018-04-14: 5.4.5 - what’s new - diff
* 2018-04-13: 5.4.4 - what’s new - diff
* 2018-01-01: 5.4.3 - what’s new - diff
* 2017-12-07: 5.4.2 - what’s new - diff
* 2017-11-08: 5.4.1 - what’s new - diff
* 2017-10-12: 5.4.0 - what’s new - diff
* 2017-09-10: 5.3.1 - what’s new - diff
* 2017-09-01: 5.3.0 - what’s new - diff
* 2017-04-10: 5.2.2 - what’s new - diff
* 2017-03-24: 5.2.1 - what’s new - diff
* 2017-03-05: 5.2.0 - what’s new - diff
* 2017-02-07: 5.1.3 - what’s new - diff
* 2017-02-03: 5.1.2 - what’s new - diff
* 2017-02-03: 5.1.1 - what’s new - diff
* 2017-02-01: 5.1.0 - what’s new - diff
* 2016-12-21: 5.0.1 - what’s new - diff
* 2016-11-06: 5.0.0 - what’s new - diff
* 2016-10-05: 4.4.2 - what’s new - diff
* 2016-10-25: 4.4.1 - what’s new - diff
* 2016-10-23: 4.4.0 - what’s new - diff
* 2016-09-01: 4.3.1 - what’s new - diff
* 2016-06-18: 4.3.0 - what’s new - diff
* 2016-05-14: 4.2.0 - what’s new - diff
* 2016-03-12: 4.1.0 - what’s new - diff
* 2016-02-17: 4.0.0 - what’s new - diff
* 2016-01-20: 3.4.2 - what’s new - diff
* 2016-01-15: 3.4.1 - what’s new - diff
* 2015-11-25: 3.3.0 - what’s new - diff
* 2015-10-04: 3.2.2 - what’s new - diff
* 2015-09-03: 3.2.1 - what’s new - diff
* 2015-09-02: 3.2.0 - what’s new - diff
* 2015-07-15: 3.1.1 - what’s new - diff
* 2015-07-15: 3.1.0 - what’s new - diff
* 2015-06-18: 3.0.1 - what’s new - diff
* 2015-06-13: 3.0.0 - what’s new - diff
* 2015-02-02: 2.2.1 - what’s new - diff
* 2015-01-06: 2.2.0 - what’s new - diff
* 2014-09-26: 2.1.3 - what’s new - diff
* 2014-09-21: 2.1.2 - what’s new - diff
* 2014-04-30: 2.1.1 - what’s new - diff
* 2014-04-08: 2.1.0 - what’s new - diff
* 2014-03-10: 2.0.0 - what’s new - diff
* 2013-11-25: 1.2.1 - what’s new - diff
* 2013-11-20: 1.2.0 - what’s new - diff
* 2013-10-22: 1.1.2 - what’s new - diff
* 2013-10-08: 1.1.1 - what’s new - diff
* 2013-09-28: 1.1.0 - what’s new - diff
* 2013-07-12: 1.0.1 - what’s new - diff
* 2013-07-10: 1.0.0 - what’s new - diff
* 2013-05-03: 0.7.1 - what’s new - diff
* 2013-04-12: 0.7.0 - what’s new - diff
* 2012-08-16: 0.6.1 - what’s new - diff
* 2012-08-13: 0.6.0 - what’s new - diff
* 2012-06-29: 0.5.1 - what’s new - diff
* 2012-06-27: 0.5.0 - what’s new - diff
* 2011-12-14: 0.4.1 - what’s new - diff
* 2011-10-29: 0.4.0 - what’s new - diff
* 2011-07-08: 0.3.0 - what’s new - diff
* 2011-03-20: 0.2.1 - what’s new - diff
* 2010-11-13: 0.2.0 - what’s new - diff
* 2010-03-02: 0.1.3 - what’s new - diff
* 2009-05-06: 0.1.2 - what’s new - diff
* 2009-03-06: 0.1.1 - what’s new - diff
* 2009-01-27: 0.1.0 - what’s new - diff
