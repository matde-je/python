class Paper:
    def __init__(self, title, authors):
        self.__title = title
        self.__authors = []
        for a in authors:
            if a not in self.__authors:
                self.__authors.append(a)
        
    @property
    def title_(self):
        return self.__title
    @property
    def authors_(self):
        return self.__authors
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__title == other.__title
    
    def __str__(self):
        return f"{self.__title}, {self.__authors}"

class Review:
    def __init__(self, revisor, titulo):
        self.__revisor = revisor
        self.__titulo = titulo
        self.comment = ""
        self.result = None
        
    @property
    def titulo_(self):
        return self.__titulo
    @property
    def revisor_(self):
        return self.__revisor

    def results(self, r, c):
        self.result = r
        self.comment = c
    
    def is_completed(self):
        if self.result != None:
             return True
        else:
            return False
    
    def commentarie(self):
        assert self.is_completed() == True
        return self.comment
    
    def acceptance(self):
        assert self.is_completed() == True
        return self.result
    
    def __str__(self):
        return f"{self.__revisor}, {self.__titulo}, {self.result}, {self.comment}"

class Conference:
    def __init__(self):
        self.articles = []
        self.revisor = []
        self.revisions = []
        
    def register_article(self, article):
        assert article.title_ not in self.articles
        self.articles.append(article)
    
    def new_revisor(self, nome):
        assert nome not in self.revisor
        self.revisor.append(nome)
        
    def register_revision(self, revisor, titulo):
        r = Review(revisor, titulo)
        self.revisions.append(r)
        
    def register_result(self, title, revisor, r, com):
        for r1 in self.revisions:
            if r1.titulo_ == title and r1.revisor_ == revisor:
                r1.results(r, com)
                return
    
    def article_(self, title):
        for art in self.articles:
            if art.title_ == title:
                return art
        return None
    
    def number_articles(self):
        return len(self.articles)
        
    def number_revisors(self):
        return len(self.revisor)
    
    def number_incomplete(self):
        num = 0
        for i in range(len(self.revisions)):
            if self.revisions[i].is_completed() == False:
                num += 1
        return num
        
    def is_article_registered(self, title):
        for art in self.articles:
            if art.title_ == title:
                return True
        return False
        
    def is_revisor_registered(self, nome):
        if nome in self.revisor:
            return True
        else:
            return False
        
    def is_revision_registered(self, title, name):
        for r1 in self.revisions:
            if r1.titulo_ == title and r1.revisor_ == name:
                return True
        return False

    def is_revision_over(self, title, nome):
        for r1 in self.revisions:
            if r1.revisor_ == nome and r1.titulo_ == title:
                return r1.is_completed() == True
            
    def is_article_accepted(self, title, nome):
        for r1 in self.revisions:
            if r1.revisor_ == nome and r1.titulo_ == title:
                return r1.result == "Aceite"
        return False

    def is_article_approved(self, title):
        for r1 in self.revisions:
            if r1.titulo_ == title: 
                if r1.result != "Aceite":
                    return False  
        return True

    def is_article_disapproved(self, title):
        for r1 in self.revisions:
            if r1.titulo_ == title: 
                if r1.result != "Rejeitado":
                    return False
        return True

    def is_article_unrevised(self, title):
        for r1 in self.revisions:
            if r1.titulo_ == title: 
                return r1.is_completed() == False
        return False
        
    def is_article_unrevised2(self):
        for art in self.articles:
            for r2 in self.revisions:
                if r2.titulo_ == art.title_:
                    return False
        return True
                    
    def show_revisions_of_article(self, title):
        for r1 in self.revisions:
            if r1.titulo_ == title:
                r1.__str__()
            
    def estado_confe(self):
            aceitelst = []
            rejeitadolst = []
            porreverlst = []
            for r in self.revisions:
                if r.is_completed() == False:
                    porreverlst.append(r)
                elif r.result == "Aceite":
                    aceitelst.append(r)
                elif r.result == "Rejeitado":
                    rejeitadolst.append(r)
            print("Artigos aceites: ")
            for a in aceitelst:
                print(a)
            print("Artigos rejeitados: ")
            for b in rejeitadolst:
                print(b)
            print("Artigos por rever: ")
            for c in porreverlst:
                print(c)

def menu1():
    print("1. Introduzir novo artigo")
    print("2. Introduzir novo revisor")
    print("3. Introduzir nova revisão")
    print("4. Introduzir resultado de revisão")
    print("5. Estado da conferência")
    print("6. Estatísticas")
    print("7. Sair")

c3 = Conference() 
def menu():
    title = []
    num_autores = []
    autorlst = []
    while True:
        menu1()
        a = int(input("Introduza a sua opção: "))
        if a == 1:
            tin = input("Introduza o título: ")
            if c3.is_article_registered(tin) == True:
                print("Título já existe na conferência.")
            else:
                title.append(tin)
                num_autores1 = int(input("Introduza  número de autores do artigo: "))
                while num_autores1 <= 0:
                    num_autores1 = int(input("Introduza  número de autores do artigo: "))
                num_autores.append(num_autores1)
                num_autores0 = num_autores1
                while num_autores0 > 0:
                    autor = input("Introduza o autor: ")
                    autorlst.append(autor)
                    num_autores0 = num_autores0 - 1
                c3.register_article(Paper(tin, autorlst))
            
        elif a == 2:
            nome = input("Introduza o nome: ")
            if nome in c3.revisor:
                print("Revisor já existe na conferência.")
            else:
                c3.new_revisor(nome)
               
        elif a == 3:
            tin = input("Introduza título do artigo: ")
            if c3.article_(tin) == None:
                    print("Artigo não existe na conferência.")
            else:
                revisor = input("Introduza o nome do revisor: ")
                if revisor not in c3.revisor:
                    print("Revisor não existe na conferência.")
                else:
                    if c3.is_revision_registered(tin, revisor) == True:
                        print("Esse revisor já está encarregado desse artigo.")
                    else:
                        c3.register_revision(revisor, tin)
                
        elif a == 4:
            tin = input("Introduza título do artigo: ")
            if not c3.is_article_registered(tin):
                print("Artigo não existe na conferência.")
            else:
                revisor = input("Introduza o nome do revisor: ")
                if revisor not in c3.revisor:
                    print("Revisor não existe na conferência.")
                else:
                    if c3.is_revision_registered(tin, revisor) == True:
                        result = input("Introduza o resultado da revisão (Aceite/Rejeitado): ")
                        while result != "Aceite" and result != "Rejeitado":
                            print("Introduza um resultado válido.")
                            result = input("Introduza o resultado da revisão (Aceite/Rejeitado): ")
                        comment = input("Introduza o comentário de revisão: ")
                        c3.register_result(tin, revisor, result, comment)
                
        elif a == 5:
            c3.estado_confe()
                   
        elif a == 6:
            length = 0
            for art in c3.articles:
                length = len(art.authors_)
            print("Média de autores por artigo:", length / c3.number_articles())
            art = 0
            for r in c3.revisions:
                art += 1
            print("Média de artigos por revisor:", art / c3.number_revisors())
            print("Média de revisores por artigo:", art / c3.number_articles())
            
        elif a == 7:
            nome = input("Nome do ficheiro: ")
            f = open(nome, 'w')
            autorlst1 = []
            tit = len(title) -1 
            num = len(num_autores) - 1
            aut = len(autorlst) - 1
            num2 = 0
            while tit >= 0 and num >= 0 and aut >= 0 and num2 >= 0:
                num2 = num_autores[num]
                while num2 != 0:
                    autorlst1.append(autorlst[aut])
                    aut -= 1
                    num2 -= 1
                f.write(title[tit] + ";" + str(num_autores[num]) + ";" + ";".join(map(str, autorlst1)))
                autorlst1.clear() 
                tit -= 1
                num -= 1
                f.write("\n")
            f.close()
            return

menu()

import numpy as np
from matplotlib import pyplot as plt

aut = 0
for art in c3.articles:
    aut = len(art.authors_)
ypoints = np.array([aut / c3.number_articles()])
plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

arti = []
for r in c3.revisions:
    if r.result == "Aceite" or r.result == "Rejeitado":
        arti.append(r.titulo_)
ypoints = np.array([len(arti) / c3.number_revisors()])
plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

rev = 0
for r in c3.revisions:
    rev += 1
ypoints = np.array([rev / c3.number_articles()])
plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

lstrev = []
counts = {}
a = ""
for r1 in c3.revisions:
    a = r1.revisor_
    lstrev.append(a)
for i in lstrev:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
        
lstval = list(counts.values())
lstkey = list(counts.keys())
mydata = np.zeros([len(counts), 2], int)
counter = 0
for i in range(len(lstval)):
        for c in counts:
            index2 = i
            while i < len(lstval):
                if counts[c] == lstval[index2]:
                    counter += 1
                    index2 += 1
        mydata[i, 0] = lstval[i]
        mydata[i, 1] = counter
        counter = 0
        
print(mydata)

labels = [str(i) for i in mydata[:,0]]
plt.bar(labels, mydata[:,1])
plt.show()
