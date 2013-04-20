---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

---
author: admin
comments: true
date: 2010-05-31 17:03:43
layout: post
slug: unix-shell-by-example-chapter7-2nd
title: unix shell范例精解第七章课后习题《二》
wordpress_id: 211
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

	上面这个数据库的记录内容包括姓名，电话号码和最近3个月的竞选捐款数额 注:以上内容被写进chapter7这个文档

	请编写一个能产生如下输出的nawk的脚本：

		***FIRST QUARTERLY REPROT*** 

		***CAMPAIGN  1998  CONTRIBUTIONS*** <!-- more -->

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

		---------------------------------------------------------------------------------------

		SUMMARY  

		---------------------------------------------------------------------------------------

		THe campaign recevied a total of $6137.00 for this quaiter

		The average donation for the 12 contributions was $511.42

		The highest total contribution was 1025.00 made by Dan

		***THANKS Dan ***

		The following people donated over $500.00 to the campaign

		They are eligible for the quarterly drawing

		Listed are their names (sorted by last names) and phone numbers:

		Mike Harrington-- (510) 548-1278

		Archie McNichol-- (206) 548-1348

		Guy Quigley-- (916) 343-6410

		Dan Savage-- (406) 298-7744

		John Goldenrod-- (916) 348-4278

		Tom Savage-- (408) 926-3456

		Elizabeth Stachelin-- (916) 440-1763

		Thanks to all of you for your continued support!!

	我的脚本文件

	cat nawk7.2.sc

> 
		
> 
> 
			BEGIN{
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***FIRST QUARTERLY REPROT***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t  ***CAMPAIGN  1998  CONTRIBUTIONS***\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "NAME\t\t\t  PHONE\t\tJan  |  Feb  |  Mar  |  Total.Donated\n"
		
> 
> 
		
> 
> 
			printf "--------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			FS="[ :]"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			#compute the max donation and donor's name
		
> 
> 
		
> 
> 
			#print the donate status
		
> 
> 
		
> 
> 
			#print the average
		
> 
> 
		
> 
> 
			#put the record into the matrix
		
> 
> 
		
> 
> 
			{ 
		
> 
> 
		
> 
> 
			while(count<NR){count++;$8=$5+$6+$7;sum+=$8;if($8>max){max=$8;name=$1}}
		
> 
> 
		
> 
> 
			printf "%-10s %10s  %s %s  %6.2f  %6.2f  %6.2f  %6.2f \n",$1,$2,$3,$4,$5,$6,$7,$5+$6+$7
		
> 
> 
		
> 
> 
			average=int(sum/1200)*100
		
> 
> 
		
> 
> 
			for(i=1;i<=4;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if($8>500) matrix[NR,i] = $i
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			END{
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "\t\t\t\t\t\ SUMMARY \t\t\t\t\t\t\t\n"
		
> 
> 
		
> 
> 
			printf "---------------------------------------------------------------------------------------\n"
		
> 
> 
		
> 
> 
			printf "THe campaign recevied a total of $%6.2f for this quaiter\n",sum
		
> 
> 
		
> 
> 
			printf "The average donation for the 12 contributions was $%6.2f\n",sum/12 
		
> 
> 
		
> 
> 
			printf "The highest total contribution was %6.2f made by %s \n ", max,name
		
> 
> 
		
> 
> 
			printf " ***THANKS %s ***  \n",name
		
> 
> 
		
> 
> 
			printf "The following people donated over $%6.2f to the campaign\n",average
		
> 
> 
		
> 
> 
			printf "They are eligible for the quarterly drawing \n"
		
> 
> 
		
> 
> 
			printf "Listed are their names (sorted by last names) and phone numbers:\n"
		
> 
> 
		
> 
> 
			for(i=1;i<=NR;i++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			for(j=1;j<=4;j++)
		
> 
> 
		
> 
> 
			{
		
> 
> 
		
> 
> 
			if(matrix[i,j]) printf " %s", matrix[i,j]
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==2) printf "--"
		
> 
> 
		
> 
> 
			if(matrix[i,j] && j==4) printf "\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			}
		
> 
> 
		
> 
> 
			printf "\t\t Thanks to all of you for your continued support!!\n"
		
> 
> 
		
> 
> 
			}
		
> 
> 

	格式控制比较麻烦- -!

