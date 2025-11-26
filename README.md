# refatoracao-jogos-azar
---
Decidi pegar alguns códigos meus e de amigos meus para refatorar para uma forma de estudo de boas práticas.

---
Principais alterações estudadas:
- Object Calisthenics: Fail-Fast (Prefirimos um if com return no início de função em vez de colocar uma execução completa dentro do if;
- Separação em funções, o melhor exemplo até agora é o do ímpar ou par. Nesse código ele escreveu de 2 a 3 vezes a verificação de ímpar ou par, ajustei para ser uma função com return True or False baseado no jogador 1;
- Troca de If-Else para Match-Case em casos que funciona;
- Criação de fluxos melhores com while True e saída a partir de uma verificação de variável vazia.

Obs. Estou sempre aberto a sugestão de melhorias e caso queira compartilhar o seu código para eu tentar refatorar, eu adoraria!
