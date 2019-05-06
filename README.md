# python_zxing <br>
echo "# python_zxing" >> README.md <br>
git init <br>
git add README.md <br>
git commit -m "first commit" <br>
git remote add origin https://github.com/lizhihua0625/python_zxing.git <br>
git push -u origin master <br>

或者

git remote add origin https://github.com/lizhihua0625/python_zxing.git <br>
git push -u origin master <br>

不废话，直接来说 我的目的是解析二维码 <br>

https://github.com/zxing/zxing  是基于这个的 <br>

我有试过window7下面，python3.6 成功 <br>
java version "1.8.0_181" <br>
Java(TM) SE Runtime Environment (build 1.8.0_181-b13) <br>
Java HotSpot(TM) 64-Bit Server VM (build 25.181-b13, mixed mode) <br>

但是相同的环境，window10 解析二维码失败 <br>
centos7 也是解析失败，但是整了好久，找朋友帮忙，终于搞定啦，比较麻烦，学习下吧 <br>
openjdk version "1.8.0_212" <br>
OpenJDK Runtime Environment (build 1.8.0_212-b04) <br>
OpenJDK 64-Bit Server VM (build 25.212-b04, mixed mode) <br>

Apache Maven 3.2.5 (12a6b3acb947671f09b81f49094c53f426d8cea1; 2014-12-14T12:29:23-05:00) <br>
Maven home: /usr/local/maven3 <br>
Java version: 1.8.0_212, vendor: Oracle Corporation <br>
Java home: /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.212.b04-0.el7_6.x86_64/jre <br>
Default locale: en_US, platform encoding: UTF-8 <br>
OS name: "linux", version: "5.0.8-1.el7.elrepo.x86_64", arch: "amd64", family: "unix" <br>

代码里面改了些东西，还是需要注意的 <br>

git clone https://github.com/zxing/zxing.git  <br>
cd zxing <br>
mvn install <br>
cd core <br>
wget http://central.maven.org/maven2/com/google/zxing/core/2.2/core-2.2.jar <br>
mv core-2.2.jar core.jar # Rename <br>
mvn install <br>
cd zxing/javase <br>
wget http://central.maven.org/maven2/com/google/zxing/javase/2.2/javase-2.2.jar <br>
mv javase-2.2.jar javase.jar # Rename <br>
mvn install <br>
git clone git://github.com/oostendo/python-zxing.git <br>

这些步骤，经走下来，我测试通过的，是如此

mvn install -Dmaven.test.skip=true   #需要执行这个
core.jar  javase.jar  jcommander-1.72.jar  复制到和你要执行的文件同级目录下面
testZxing  是下载的别人的，试了，不好用，应该也需要改点什么，和我环境不匹配，应该如此
可能是环境的问题，我还改了Swap
[root@fantastic-hat-2 local]# free -h
              total        used        free      shared  buff/cache   available
Mem:           1.0G        305M         68M        952K        626M        527M
Swap:          2.2G        532M        1.7G

可能不需要这么大，但是请参考自己改一下，比较好
请参考
https://blog.csdn.net/zhbzhbzhbbaby/article/details/80810721

具体改了哪里，我不记得啦，没法整理，有需要的朋友，可以自己比较看看，如果不对，请指正，3162289690@qq.com




















