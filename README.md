In Task1,Task 2 and Task 3 1 i.e Assignment 1,2

Step 1:
Make Python file app.py

In that file write python code

Step 2:
Make template folder and in that make html file

In that HTML file write html code.

Step 3:
Run python file with command
For Linux
python3 app.py 


For Task3 we have to dockerize the application and deploy it on minikube.

Deploy under the Kuberenetes cluster
Prerequisite
MiniKube

Installed: MiniKube

Start minikube with command:
minikube start

Retrieve and deploy application

kubectl create deployment hello-app --image=dstar55/docker-app:latest

Expose deployment as a Kubernetes Service

kubectl expose deployment hello-app --type=NodePort --port=8080

Check whether the service is running

kubectl get service hello-app

response should something like:

NAME                TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
hello-app  NodePort   xx.xx.xxx.xxx   <none>        8080:xxxxx/TCP            30sec






