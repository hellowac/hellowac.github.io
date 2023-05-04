# C基础

C 语言是一种通用的高级语言，最初是由丹尼斯·里奇在贝尔实验室为开发 UNIX 操作系统而设计的。C 语言最开始是于 1972 年在 DEC PDP-11 计算机上被首次实现。

在 1978 年，布莱恩·柯林汉（Brian Kernighan）和丹尼斯·里奇（Dennis Ritchie）制作了 C 的第一个公开可用的描述，现在被称为 K&R 标准。

UNIX 操作系统，C编译器，和几乎所有的 UNIX 应用程序都是用 C 语言编写的。由于各种原因，C 语言现在已经成为一种广泛使用的专业语言。

相关网络资料：

1. C语言基础教程：<https://www.runoob.com/cprogramming/c-tutorial.html>
2. 从头开始学习C语言：<https://www.cprogramming.com/tutorial/c-tutorial.html>
3. 快速掌握C语言：<https://www.codecademy.com/learn/learn-c>
4. 让你轻松理解C语言：<https://www.edx.org/course/programming-c-microsoft-dev210x>
5. 高级C语言编程：<https://www.udacity.com/course/advanced-c-programming--ud210>

## 指针

{++**变量为了表示数据而生，指针为了传递数据而生。**++}

**指针没有那么神秘，他就是一个变量，不过放的是别的变量地址。**

```c
#include <stdio.h>

int main()
{
    int var_runoob = 10;
    int *p; // 定义指针变量

    p = &var_runoob;

    printf("var_runoob的变量地址是: %p\n", p);

    // gcc ./point.c -o point
    // var_runoob的变量地址是: 0x7ff7bee7b328


    int var = 10;
    int *p;
    p = &var;

    printf("p - %d *p - %d\n", p, *p);

    // p - -1209400532 *p - 10

    return 0;
}
```

### 应用场景

**智能音响**：音频处理

```c
char pcm_data_char;
char pcm_data_arrary[4096];

void pcmSpeex(char *data) {
    // TODO
}

pcmSpeex(&pcm_data_char);
pcmSpeex(pcm_data_arrary);

```

**场景一**：通过函数交换两个值时，用变量传递与指针传递。

```c
#include <stdio.h>

void swap(int data1, int data2)
{
    int temp = data1;
    data1 = data2;
    data2 = data1;
}

void swap2(int *data1, int *data2)
{
    int temp = *data1;
    *data1 = *data2;
    *data2 = temp;
}



int main()
{

    int a = 10, b = 20;
    // swap(a, b);      // a - 10 , b - 20
    swap2(&a, &b); // a - 20 , b - 10
    printf("a - %d , b - %d\n", a, b);
}
```

**场景二**：如果你有一个或两三个保险柜,那么你可以将这几个保险柜的钥匙都放在身上.如果你有几百个保险柜,你还愿意都将钥匙放在身上吗?

```c
#include <stdio.h>

void open(int *key, int num)
{
    printf("data = %d\n", key[num]);
}

int main()
{

    int key[100] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    open(key, 5);

```

## 回调函数

`指针的实用功能`

为什么有？有什么用？

1. 送餐机器人：地盘移动到目标位置后，如何通知应用程序？
2. 智能音箱：网络通知该表后，如何通知应用程序？

**传统方式：**

1. 开放变量，让别人直接获取
2. 通过getStatus()类似的函数定时获取

**建议方式:**

回调方式实现

```c
#include <stdio.h>

typedef struct
{
    int status;
    void (*statusChange)(); // 函数指针
} T_Device;

T_Device g_Device;

void addCallBackFunc(void (*pstatusChange)(int status))
{
    g_Device.statusChange = pstatusChange;
};

int getStatus()
{
    return g_Device.status;
};

void run()
{
    g_Device.status = 10;
    if (g_Device.status == 10)
    {
        if (g_Device.statusChange != NULL)
        {
            g_Device.statusChange(g_Device.status);
        };
    };
};

// 用户代码
void callBack(int status)
{
    printf("callBack\n");
    printf("status = %d\n", status);
};

int main()
{
    int status = getStatus();
    addCallBackFunc(callBack);
    run();
};
```

## 常用数据结构

1. 智能音箱：配网时，获取到网络列表后，进行过滤，如何写过滤函数？

- malloc 裸机不建议使用，带操作系统的可以 (容易出现内存碎片，导致内存利用率不足)
- freertos 实现类内存管理池
- inux 有内存管理的模块 (实际访问映射表、不直接访问硬件地址)

```c
void handleWifiList(const char * plistdata,int len){
    char *mdata =(char *)malloc(len);
    memcpy(mdata,plistdata,len);
    free(m data);
}
```

**常用数据结构**：

1. 数组
2. 栈
3. 堆
4. 队列
5. 链表
6. 树
