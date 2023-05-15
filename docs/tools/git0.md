# git常用操作备忘

## `commit` 之后回退一个版本

```powershell
git reset --soft HEAD^
```

此时commit撤销，代码变更保留。

可选参数:

--mixed
: 撤销commit，撤销add，不撤销代码改动，为默认参数。

--soft
: 撤销commit，不撤销add，不撤销代码改动。

--hard
: 撤销commit，撤销add，撤销代码改动。

!!! info "官方指南"

    - 命令行: [git-reset](https://git-scm.com/docs/git-reset/zh_HANS-CN){target="_blank"}
    - 命令行: [git-重置揭密](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%87%8D%E7%BD%AE%E6%8F%AD%E5%AF%86){target="_blank"}
