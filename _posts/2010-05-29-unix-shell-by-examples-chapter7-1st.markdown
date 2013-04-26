---
    author: admin
    comments: true
    date: 2010-05-29 16:26:28
    layout: post
    title: unix shell范例精解第七章课后习题《一》
    wordpress_id: 108
    categories:
- PROGRAM
    tags:
- unix shell
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

上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注：以上内容被写进chapter7这个文档

请编写一个能产生如下输出的nawk的脚本：

***CAMPAIGN  1998  CONTRIBUTIONS*** 

--------------------------------------------------------------------------------------

NAME PHONE Jan  |  Feb  |  Mar  |  Total.Donated

--------------------------------------------------------------------------------------

Mike  Harrington  (510) 548-1278  250.00  100.00  175.00  525.00

Christian  Dobbins  (408) 538-2358  155.00  90.00  201.00  446.00

Susan  Dalsass  (206) 654-3279  250.00  60.00  50.00  360.00

Archie  McNichol  (206) 548-1348  250.00  100.00  175.00  525.00

Jody  Savage  (206) 548-1278  15.00  188.00  150.00  353.00

Guy  Quigley  (916) 343-6410  250.00  100.00  175.00  525.00

Dan  Savage  (406) 298-7744  450.00  300.00  275.00  1025.00

Nancy  McNeil  (510) 548-5258  250.00  80.00  75.00  405.00

John  Goldenrod  (916) 348-4278  250.00  100.00  175.00  525.00

Chet  Main  (510) 548-5258  50.00  95.00  135.00  280.00

Tom  Savage  (408) 926-3456  250.00  168.00  200.00  618.00

Elizabeth  Stachelin  (916) 440-1763  175.00  75.00  300.00  550.00

-------------------------------------------------------------------------------

SUMMARY  

-------------------------------------------------------------------------------

THe campaign recevied a total of $6137.00 for this quaiter

The average donation for the 12 contributions was $511.42

The highest contribution was $450.00

The lowest contribution was $15.00

% nawk -f nawk.sc chapter7

    nawk.sc 的内容如下 

BEGIN{  printf("\t\t\t  ***CAMPAIGN 1998 CONTRIBUTIONS***\t\t\t\n";) 
    printf("--------------------------------------------------------------------------------------\n") 
    printf("NAME\t\t\t PHONE\t\tJan  |   Feb   |  Mar   | Total.Donated\n") 
    printf("--------------------------------------------------------------------------------------\n")      
FS="[ :]" }
{ 
    while(count<NR){count++;sum+=$5+$6+$7;}
    printf("%-10s %10s   %s %s   %6.2f    %6.2f     %6.2f    %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7) 
{print $5|"sort -n -b -o 1.txt +0 -1"} 
{print $6|"sort -n -b -o 1.txt +0 -1"}
{print $7|"sort -n -b -o 1.txt +0 -1"} }
END{for(i=1;("cat 1.txt"|getline d);i++) 
{ if(i==1) "min=d if(i==3*NR) max=d }
    printf("-------------------------------------------------------------------------------\n") 
    printf("\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n") 
    printf("-------------------------------------------------------------------------------\n") 
    printf("THe campaign recevied a total of $%6.2f for this quaiter\n",sum) 
    printf("The average donation for the 12 contributions was $%6.2f\n",sum/12)
    printf("The highest contribution was $%6.2f\n",max) 
    printf("The lowest contribution was $%5.2f\n",min) }

感觉自己在排序这块写的比较累赘- -！待以后改进吧

