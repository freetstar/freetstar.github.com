---
    author: admin
    comments: true
    date: 2010-06-01 19:35:07
    layout: post
    slug: unix-shells-by-example-chapter-7-3rd
    title: unix shell范例精解第七章课后习题《三》
    wordpress_id: 229
    categories:
- PROGRAM
---

Mike Harrington:(510) 548-1278:250:100:175

Christian Dobbins:(408) 538-2358:155:90:201

Susan Dalsass:(206) 654-3279:250:60:50

Archie McNichol:(206) 548-1348:250:100:175

Jody Savage:(206) 548-1278:15:188:150

Guy Quigley:(916) 343-6410:250:100:175

Dan Savage:(406) 298-7744:450:300:275

Nancy McNeil:(510) 548-5258:250:80:75

John Goldenrod:(916) 348-4278:250:100:175

Chet Main:(510) 548-5258:50:95:135

Tom Savage:(408) 926-3456:250:168:200

Elizabeth Stachelin:(916) 440-1763:175:75:300

上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额

注:以上内容被写进chapter7这个文档

请编写一个用户自定义函数,要求该函书能返回指定月份的人均捐款数额.月份由命令行传入

文件内容:

BEGIN{
FS="[ :]"
    printf "*******Please input the month you want to check***** \n"
    getline month < "/dev/tty"
}

{
Add(month+4)
}

    function Add(m)
{
    count++;
    total+=$m
    aver = total/12
    if(count==12) return aver
    else next
}

END{printf "The #%d month's average is %6.2f \n",month,aver}

