---
    author: admin
    comments: true
    date: 2010-06-25 01:24:26
    layout: post
    slug: base-64-code-decode
    title: Base 64 算法加解密算法总结
    wordpress_id: 773
    categories:
- PROGRAM
---

上次只给出了加密算法

现在将完整算法给出

源文件名为：base64.c

------------------------------------------------------------------------分隔线-------------------------------------------------------------------------------------
[code langague="c"]
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//base64编码表
    static char base64_table[] = {
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2',
'3', '4', '5', '6', '7', '8', '9', '+', '/', '\0'
};

    static int base64_reverse_table[] = {
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63,
52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1,
-1,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1,
-1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1
};

    static char str_pad ='=';//pad 用“=”标记

    char *base64_decode(char *str,int length)
{
    int i=0;
    int	j=0;
    int ch;
    char *result,*p;
    if(str ==NULL || length < 0) return NULL;
    result = (char *)malloc((length /4)*3);
    p=result;
    if(result == NULL )
{
    printf("malloc failed\n");
    return NULL;
}
    while((ch = *str++) != '\0' && length-- > 0)
{
    if(ch == str_pad)break;
//根据字符取得字符在base64_table里面的索引值
    ch = base64_reverse_table[ch];
    switch(i % 4)
{
    case 0 : result[j] = ch << 2; break;
    case 1 : result[j++] |= ch >> 4;
    result[j] = (ch & 0x0f) << 4;
    break;
    case 2 : result[j++] |= ch >> 2;
    result[j] = (ch & 0x03) << 6;
    break;
    case 3 : result[j++] |= ch;break;
}
    i++;
}
    result[j] = '\0';
//打印结果看看.
    printf("result:%s\n",p);
    return p;
}

    char *base64_encode(char *str, int length)
{  
    char *result,*p;
    if(str == NULL || length <1)return NULL;          
//分配空间,加密后的字符串长度是原字符串的4/3
    result = (char *)malloc(((length + 2)/3)*4);
    p = result;
    if(result == NULL)
{
    printf("malloc failed\n");
    return NULL;
}
//这是剩余字符串长度大于等于3的情况
//通过位移来截取字节的位数
//第一个字节右移2位，得到base64的第一个目标字符
//第一个字节&0x03（00000011）后，再加上第二个字节右移4位，得到base64的第二个目标字符
//第二个字节&0x0f (00001111) 后，再加上第三个字节右移4位，得到base64的第三个目标字符
//第三个字节&0x3f (00111111) 后，得到base64的第四个目标字符
    while( length > 2)
{
*result++ = base64_table[str[0] >> 2];
*result++ = base64_table[((str[0] & 0x03) << 4) + (str[1] >> 4)];
*result++ = base64_table[((str[1] & 0x0f) << 2) + (str[2] >> 6)];
*result++ = base64_table[str[2] & 0x3f];
    length -= 3;
    str += 3;
}
//剩余字符串长度小于3
    if(length != 0)
{
*result++ = base64_table[str[0] >> 2];
//剩余长度为2
    if(length > 1)
{
*result++ = base64_table[((str[0] & 0x03) << 4) + (str[1] >> 4)];
*result++ = base64_table[(str[1] & 0x0f) << 2];
*result++ = str_pad; //不够的补"="
}
//剩余字符串长度是1
    else
{
*result++ = base64_table[(str[0] & 0x03) << 4];
*result++ = str_pad;//不够的补"="
*result++ = str_pad;//不够的补"="
}
}
*result ='\0';
//输出结果
    printf("result:%s\n",p);
    return p;
}

    int main(int agrc,char **argv)
{
    char *str,*result;
    int len;
    str = argv[1];
    len  = strlen(str);
    printf("the len is %d \n",len);
    result = base64_encode(str, len);

    strlen(result);
    result = base64_decode(result, len);
    return 1;
}

[/code]

编译源文件 gcc -o base64 base.c

运行./base64 hello

[http://jackywdx.cn/2009/05/base64_algorithm/](http://jackywdx.cn/2009/05/base64_algorithm/) 

