# TD_BigData_API

Is an API where you can go on 3 different endpoints,
you can go on root (`/`), on `/user` and `/user/one`

## Installation

To implement the API, please follow those instructions :


- First download the .Zip
- Then open your terminal and copie those lines one by one :

```bash
minikube start

kubectl create deployment drinou-minikube --image=princessedrinou/td_bigdata_api

kubectl expose deployment drinou-minikube --type=NodePort --port=5000
```

• Scale it to the number you need and remplace "nb" with the number you choose only :

```bash
kubectl scale deployment drinou-minikube --replicas="nb"
```

• Open the API on your browser :

```bash
minikube service drinou-minikube
```


And you're done ! Enjoy <3
