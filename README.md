# 📡 Projetos com Sensores ESP32 usando Python

---

## 📘 Sobre

Este repositório contém 4 projetos desenvolvidos com a placa **ESP32**, integrados com **Python**, utilizando o ambiente **Thonny IDE**. Os circuitos foram simulados na plataforma **Wokwi** e montados fisicamente, com sucesso.

### Os projetos desenvolvidos:

1. **Detector de Luminosidade**  
   Utiliza um sensor LDR para detectar a intensidade da luz ambiente.

2. **Detector de Presença**  
   Utiliza um sensor PIR para detectar movimentos próximos ao sensor.

3. **Detector de Umidade do Solo**  
   Ideal para monitorar a umidade da terra em vasos ou hortas, usando um sensor de umidade capacitivo.

4. **Leitor de Produtos (Contador de Itens)**  
   Simula um leitor que conta produtos ao passarem por um sensor, somando até 10 itens por caixa, atendendo a uma demanda proposta por uma empresa fictícia.

> Todos os projetos foram executados com êxito no ambiente do [SENAI Jandira](https://sp.senai.br/unidade/jandira/).

---

##  Instruções de Execução

### Pré-requisitos

- Placa **ESP32 DevKit v1** (ou similar)
- **Thonny IDE** instalado no computador
- **Drivers da ESP32** instalados
- Acesso aos projetos no **Wokwi** (simulador online)
- Conexão USB entre computador e ESP32

###  Passo a Passo

1. **Instalar o Thonny IDE**  
   Baixe e instale através do site oficial: https://thonny.org/

2. **Configurar o Thonny para ESP32**  
   - Vá em `Ferramentas` > `Placa` > selecione **ESP32**
   - Vá em `Executar` > `Selecionar Interpretador` > **MicroPython (ESP32)**

3. **Conectar a ESP32 ao Thonny**  
   - Conecte a placa ao PC via USB  
   - O Thonny deve reconhecer automaticamente a porta serial

4. **Carregar o código Python**  
   - Abra o arquivo `.py` referente ao projeto que deseja executar
   - Envie para a ESP32 com o botão "Run" (▶️)

5. **Montar o circuito**  
   - Você pode montar fisicamente, seguindo o esquema ou
   - Acessar a **simulação via Wokwi** com o link contido no arquivo `.txt` (nomeado como `projetoX_wokwi.txt`)

6. **Executar o projeto e testar sensores**

---

## Estrutura dos Arquivos

![](./printestrutura)

---
## Tecnologias Utilizadas

-  **ESP32**
-  **Python (MicroPython)**
-  **Thonny IDE**
-  **Wokwi (Simulador online de circuitos)**

---


## 📎 Observações

- Os links de simulação no Wokwi estão nos arquivos `.txt` dentro de cada pasta de projeto.
- O código está adaptado para rodar tanto em simulação quanto em hardware real.
- Para sensores específicos, pode ser necessário ajustar os pinos GPIO no código.

---

## 🏫 Projeto desenvolvido no

[SENAI Jandira – SP](https://sp.senai.br/unidade/jandira/)

---

## Participantes

- [Gustavo Rocha](https://www.linkedin.com/in/gustavo-rocha-gomes-3b1442327/)
- [Victor Hugo](https://github.com/victorhugoaurelianocoltro)
