#Função que calcula a velocidade média
def calcularVelocidadeMedia(distancia, tempo):
    #calcular a velocidade média
    velocidade_media = distancia/tempo
    #exibir o resultado
    print("A velocidade média é {} km/h".format(velocidade_media))
#aqui começa o programa principal
dist = float(input("Informe a distância"))
temp = float(input("Informe o tempo"))
#chamando a função com valores definidos pelo usuário
calcularVelocidadeMedia(dist, temp)
#chamando a função com valores definidos pelo programador
calcularVelocidadeMedia(15,2)

#A associação das variáveis "dist" e "temp" para as variáveis "distancia e tempo" ocorrem através da chamada
# da função CalcularVelocidadeMedia, onde o primeiro valor assume o primeiro valor da função e o segundo
# valor segue o mesmo no caso dist = distancia e temp = tempo