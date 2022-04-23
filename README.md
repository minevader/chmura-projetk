# Projekt


## Komendy

Logujemy się i tworzymy grupę zasobów
```bash
az login 
```
```bash
az group create -n projekt -l westeurope
```

Tworzymy maszynę virtualną i łączymy się do niej po ssh
```bash
az vm create --resource-group wsb-projekt --name virtualmachine --size "Standard_B1ls" --image "Canonical:0001-com-ubuntu-server-focal:20_04-lts-gen2:latest" --public-ip-sku Standard --admin-username adminek
```
```bash
ssh adminek@[adres publiczny]
```

Aktualizujemy i instalujemy dockera
```bash
sudo apt-get update
```
```bash
sudo apt-get install docker.io
```

Uruchamiamy aplikację
```bash
sudo docker run -p 5000:5000 -d nowy-projekt
```

## Dokumentacja
 - [Docker](https://docs.docker.com/) 
 - [Azure](https://portal.azure.com/)
 - [Flask](https://flask.palletsprojects.com/en/2.0.x/)
