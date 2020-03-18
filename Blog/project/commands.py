from project import app, db
from project.models import User, Article
import click

@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def initdb(username, password):
    click.echo("Initializing the database...")
    db.create_all()

    admin = User.query.get(1)
    if admin:
        click.echo("The administrator already exists, updating...")
        admin.username = username
        admin.password = password
    else:
        admin = User(username=username, password=password)
        db.session.add(admin)
        db.session.commit()
    # for i in range(20):
        # initial = Article(id=i+1, title='Hello', author='TuringC', body='Welcome to my blog!'+ 'This is NO.' + str(i) + ' !')
        # db.session.add(initial)
    initial = Article(id=1, title='Hello Visitor', author='TuringC', body='Welcome to TuringC\'s blog!')
    db.session.add(initial)
    initial = Article(title='离散数学及其应用', author='TuringC', body='计算机科学丛书：离散数学及其应用（原书第7版）》是介绍离散数学理论和方法的经典教材，已经成为采用率最高的离散数学教材，被美国众多名校用作教材，获得了极大的成功。中文版也已被国内大学广泛采用为教材。作者参考使用教师和学生的反馈，并结合自身对教育的洞察，对第7版做了大量的改进，使其成为更有效的教学工具。《计算机科学丛书：离散数学及其应用（原书第7版）》可作为1至2个学期的离散数学课入门教材，适用于数学、计算机科学、计算机工程、信息技术等专业的学生。')
    db.session.add(initial)
    initial = Article(title='统计学完全教程', author='TuringC', body='由美国当代著名统计学家L·沃塞曼所著的《统计学元全教程》是一本几乎包含了统计学领域全部知识的优秀教材。本书除了介绍传统数理统计学的全部内容以外，还包含了Bootstrap方法（自助法）、独立性推断、因果推断、图模型、非参数回归、正交函数光滑法、分类、统计学理论及数据挖掘等统计学领域的新方法和技术。本书不但注重概率论与数理统计基本理论的阐述，同时还强调数据分析能力的培养。本书中含有大量的实例以帮助广大读者快速掌握使用R软件进行统计数据分析。')
    db.session.add(initial)
    initial = Article(title='编译原理：原理、技术与工具', author='TuringC', body='本书全面、深入地探讨了编译器设计方面的重要主题，包括词法分析、语法分析、语法制导定义和语法制导翻译、运行时刻环境、目标代码生成、代码优化技术、并行性检测以及过程间分析技术，并在相关章节中给出大量的实例。与上一版相比，本书进行了全面的修订，涵盖了编译器开发方面的最新进展。每章中都提供了大量的系统及参考文献。\n  本书是编译原理课程方面的经典教材，内容丰富，适合作为高等院校计算机及相关专业本科生及研究生的编译原理课程的教材，也是广大技术人员的极佳参考读物。')
    db.session.add(initial)
    initial = Article(title='形式语言与自动机导论', author='TuringC', body='本书是理论计算机科学方面的优秀教材，主要介绍形式语言、自动机、可计算性和相关内容。本书特别注意定义、定理的准确性和严格性，在定理的证明中给出了直观的动机和框架，避免多余的数学细节，这有利于培养学生形式化和严格的数学推理能力，加强对问题的理解；本书通过精心设计的大量示例，生动剖析了各种定理和定义，概念清晰，深入浅出。每章后面还给出了难度不同的习题，并给出部分习题的解答，可使学生加深对基本原理的理解并增强应用能力。　　本书主要介绍形式语言、自动机、可计算性和相关内容。主要内容包括：计算理论导引、有穷自动机、正则语言与正则文法、上下文无关语言及文法、下推自动机、图灵机、形式语言和自动机的层次结构、计算复杂性等。每节后面都给出了习题，并包含部分习题的解答，方便教学。')
    db.session.add(initial)
    initial = Article(title='深入理解计算机系统', author='TuringC', body='本书从程序员的视角详细阐述计算机系统的本质概念，并展示这些概念如何实实在在地影响应用程序的正确性、性能和实用性。全书共12章，主要内容包括信息的表示和处理、程序的机器级表示、处理器体系结构、优化程序性能、存储器层次结构、链接、异常控制流、虚拟存储器、系统级I/O、网络编程、并发编程等。书中提供大量的例子和练习，并给出部分答案，有助于读者加深对正文所述概念和知识的理解。\n   本书的最大优点是为程序员描述计算机系统的实现细节，帮助其在大脑中构造一个层次型的计算机系统，从最底层的数据在内存中的表示到流水线指令的构成，到虚拟存储器，到编译系统，到动态加载库，到最后的用户态应用。通过掌握程序是如何映射到系统上，以及程序是如何执行的，读者能够更好地理解程序的行为为什么是这样的，以及效率低下是如何造成的。')
    db.session.add(initial)
    initial = Article(title='深入理解Java虚拟机：JVM高级特性与最佳实践', author='TuringC', body='深入理解Java虚拟机:JVM高级特性与最佳实践(第2版)》内容简介：第1版两年内印刷近10次，4家网上书店的评论近4?000条，98%以上的评论全部为5星级的好评，是整个Java图书领域公认的经典著作和超级畅销书，繁体版在台湾也十分受欢迎。第2版在第1版的基础上做了很大的改进：根据最新的JDK 1.7对全书内容进行了全面的升级和补充；增加了大量处理各种常见JVM问题的技巧和最佳实践；增加了若干与生产环境相结合的实战案例；对第1版中的错误和不足之处的修正；等等。第2版不仅技术更新、内容更丰富，而且实战性更强。')
    db.session.add(initial)
    initial = Article(title='操作系统：精髓与设计原理', author='TuringC', body='本书不仅全面地讲述了操作系统的基本概念、原理和方法，还清楚地展现了当代操作系统的本质和特点。作者针对近几年操作系统领域的最新变化，对操作系统的设计原理进行深入的阐述，同时将其对操作系统整个领域全面而深入的理解呈现给读者。')
    db.session.add(initial)
    db.session.commit()
    click.echo('Initialized Database.')