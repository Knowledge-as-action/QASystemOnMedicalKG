# 验证安装成功
import py2neo

# 注意，这里的用户名为neo4j全局用户名，而非DBMS或者database的名称
g = Graph('http://localhost:7474', auth=('neo4j', 'ABC123'))