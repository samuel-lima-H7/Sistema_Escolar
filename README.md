# Sistema\_Escolar



###### Sistema de gerenciamento escolar desenvolvido em Python para praticar lógica de programação, funções, estruturas de dados e manipulação de arquivos. Seu principal objetivo é cadastrar alunos em um banco de dados que registra as notas de cada matéria respectiva a cada aluno; além de gerar um pdf de boletim escolar do aluno selecionado.

#### 

### **Funcionalidades**



* ###### Cadastro de alunos no banco de dados do CSV.
* ###### Cadastros das notas de cada matéria do aluno selecionado.
* ###### Geração de boletim escolar no aluno selecionado.



### **Tecnologias Utilizadas**



* ###### Python, como linguagem central
* ###### CSV(Comma-Separated Values): formato utilizado para armazenamento dos dados brutos
* ###### A biblioteca ReportLab, como ferramenta principal na geração do boletim em PDF



### **Requisitos para uso**



* ###### Instalar o ReportLab para a geração do boletim



### **Como executar**



* ###### Executar o main.py, uma vez que ele oferece a escolha e seleção de todas as outras funcionalidades



### **Estrutura do Projeto**



###### &#x09;Estrutura do projeto

###### 

###### projeto/



###### ├── main.py

###### │

###### ├── armazenamento\_info.py

###### │

###### ├── armazenamento\_notas.py

###### ├── armazenamento\_info\_em\_database.py

###### ├── armazenamento\_direto\_no\_database.py

###### │

###### ├── resgate\_de\_info.py

###### ├── cria\_boletim.py

###### │

###### └── boletins/





###### &#x09;Organização dos módulos



* ###### main.py: Contém o menu principal e direciona a execução para a funcionalidade selecionada.

###### 

* ###### armazenamento\_info.py: responsável pelo cadastro de alunos.



* ###### armazenamento\_notas.py: organiza os dados das notas.
* ###### armazenamento\_info\_em\_database.py: prepara e organiza informações para o banco de dados.
* ###### armazenamento\_direto\_no\_database.py: atualiza os dados armazenados.



* ###### resgate\_de\_info.py: recupera informações necessárias para o boletim.
* ###### cria\_boletim.py: gera os boletins escolares em PDF.

###### 

###### &#x09;Pasta boletins/

###### 

* ###### Armazena os boletins em PDF gerados pelo sistema.

###### 

###### &#x20;

###### 

