
"""
Give the correct commands. Remember cd does not work with pipe.
(a)You are in the directory books and want to list the fles in the subdirectory chapters. What is the command?
(b)You have a file my_text.py one level up from where you are. How do you remove that file in a single command?
(c)what is a command that changes the name from file6.txt to file_ 6.txt instead?
(d)The wild card * can be used to refer to all the fles in a directory if used with certain commands, How could 
you copy all the fles from where you are right now in the fle tree to a server? Assume the serveraddress is 
server.name and that your username is abcd1234
(e)cd ~ takes you back to your home directory, What other command does, too?
(f)You have file . txt in your current directory, The command you give is the following:
cat file.txt> file2.txt,propose a simple way to get the same result with another command!


ls chapters
rm ../my_text.py
mv file6.txt file_6.txt
scp * abcd1234@server.name:
cd
cp file.txt file2.txt

(a) 问题：你在books目录下，想列出子目录chapters中的文件，命令是什么？
解释：需要使用ls命令来列出文件，但要指定chapters目录路径
答案：ls chapters
(b) 问题：有一个文件my_text.py在上一级目录，如何用单个命令删除它？
解释：使用rm命令删除文件，通过../来指向上一级目录
答案：rm ../my_text.py
(c) 问题：如何将file6.txt重命名为file_6.txt？
解释：使用mv命令可以重命名文件
答案：mv file6.txt file_6.txt
(d) 问题：如何将当前目录下的所有文件复制到服务器？
解释：使用scp命令，*通配符表示所有文件，需要指定用户名和服务器地址
答案：scp * abcd1234@server.name:
(e) 问题：除了cd ~，还有什么命令可以返回主目录？
解释：cd后面不跟任何参数也可以返回主目录
答案：cd
(f) 问题：当前目录有file.txt，命令是cat file.txt > file2.txt，用另一个命令实现相同结果？
解释：这个命令是将file.txt的内容复制到file2.txt，可以用cp命令直接复制
答案：cp file.txt file2.txt
补充说明：

cat file.txt > file2.txt 是通过重定向将文件内容输出到新文件
cp file.txt file2.txt 直接复制文件，效果相同但更简单
cd命令确实不能用管道（pipe）操作，因为cd是shell内置命令
在使用这些命令时要注意文件权限

这些都是Linux/Unix系统中常用的基本文件操作命令，理解它们的用法对于文件管理非常重要。



Question 7 [max 2 p.]
You have a file file7.txt. Here is the content:
The city is large
The country is larger
The continent has the same as the country
The city is called Sidney
How do you use a command chain that outputs the second line of the file in the Terminal?

cat file7.txt | head -n 2 | tail -n 1
head -n 2 file7.txt | tail -n 1

"""