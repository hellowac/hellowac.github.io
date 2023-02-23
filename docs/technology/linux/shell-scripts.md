# shell脚本实战

书籍参考: <https://www.ituring.com.cn/book/2485>

## 统计当前变量PATH中可执行文件和不可执行文件的数量

```shell
#!/bin/bash
# 命令统计: 一个简单的脚本，可以计算出当前PATH中有多少可执行命令。 
IFS=":"
count=0 ; nonex=0
for directory in $PATH ;  do
  if [ -d "$directory" ] ; then
    for command in "$directory"/* ; do
      if [ -x "$command" ] ; then
        count="$(( $count + 1 ))"
      else
        nonex="$(( $nonex + 1 ))"
      fi
    done
  fi
done

echo "$count 个命令, 以及 $nonex 个不可执行的入口"
# echo  "$count commands, and $nonex entries that weren't executable"

exit 0
```

<!-- more -->

## 格式化过长的行

```shell
#!/bin/bash
# fmt -- 文本格式化使用工具，可用作nroff的包装器。
# 加入两个实用选项：-w X，指定行宽；-h，允许连字符。

while getopts "hw:" opt; do
    case $opt in
      h ) hyph=1              ;;
      w ) width="$OPTARG"     ;;
    esac
  done
shift $(($OPTIND - 1))

nroff << EOF
  .ll ${width:-72}
  .na
  .hy ${hyph:-0}
  .pl 1
  $(cat "$@")
  EOF

  exit 0
```

## 删除文件时做备份

```shell
#!/bin/bash
# newrm -- 现有rm命令的替代命令。
# 该脚本通过在用户主目录中创建的一个新目录实现了基本的文件恢复功能。
# 它既可以恢复目录，也可以恢复单个文件。如果用户指定了-f选项，则不归档被删除的文件。

# 重要的警告: 你需要安排cron作业或执行类似的操作清理归档目录。否则，
# 系统并不会真正删除任何文件，这将造成磁盘空间不足。

  archivedir="$HOME/.deleted-files"
  realrm="$(which rm)"
  copy="$(which cp) -R"
  if [ $# -eq 0 ] ; then          # 由rm命令输出用法错误信息。
    exec $realrm                  # 当前shell会被/bin/rm替换掉。
  fi

# 解析所有的选项，从中查找-f选项。

  flags=""

  while getopts "dfiPRrvW" opt
  do
    case $opt in
      f ) exec $realrm "$@"     ;; # exec调用可以使该脚本直接退出。
      * ) flags="$flags -$opt"  ;; # 将其他选项留给rm命令。
    esac
  done
  shift $(( $OPTIND - 1 ))

  # 主脚本开始
  # =================
  # 确保$archivedir存在。

 if [ ! -d $archivedir] ; then
    if [ ! -w $HOME ] ; then
      echo "$0 failed: can't create $archivedir in $HOME" >&2
      exit 1
    fi
    mkdir $archivedir
   chmod 700 $archivedir         # 请保留点隐私。
  fi

  for arg
  do   newname="$archivedir/$(date "+%S.%M.%H.%d.%m").$(basename "$arg")"
    if [ -f "$arg" -o -d "$arg" ] ; then
      $copy "$arg" "$newname"
    fi
  done

exec $realrm $flags "$@"        # 由realrm替换掉当前shell。
```
