def getDistance(data, u, t, v):
    bancoU = int(data["Umidade"])
    absValue = int(u) - bancoU
    distanceU = 1 - abs(absValue) / 100

    bancoT = int(data["Temperatura"])
    absValue = int(t) - bancoT
    distanceT = 1 - abs(absValue) / (60 - 0)

    bancoV = int(data["Ventos"])
    absValue = int(v) - bancoV
    distanceV = 1 - abs(absValue) / (315 - 0)

    # Peso 3 - Umidade; Peso 2 - Temperatura; Peso 1 - Ventos
    distanceGeral = ((3*distanceU) + (2*distanceT) + distanceV)/6

    return distanceGeral


def app(umidade, temperatura, ventos):

    with open("data.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    file.close()

    dados = dict()
    distance = []

    for line in lines:
        string = line.split(";")
        for data in string:
            dataDic = data.split(":")
            value = dataDic[1]
            dados[dataDic[0]] = value
        distance.append(getDistance(dados, umidade, temperatura, ventos))

    betterScore = 0
    position = 0
    for i in range(len(distance)):
        if (distance[i] > betterScore):
            position = i
            betterScore = distance[i]

    output = lines[position].split(";")

    descricao = output[0].split(":")
    descricaoName = descricao[1]
    valueOutput = output[4].split(":")
    valueOutputName = valueOutput[1]

    returnString = [descricaoName, valueOutputName]
    return returnString


def writeData(descricao, umidade, temperatura, ventos, resultado):
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write("Descrição:" + descricao + ";Umidade:" + umidade + ";Temperatura:" +
                   temperatura + ";Ventos:" + ventos + ";Resultado:" + resultado + "\n")
    file.close()
