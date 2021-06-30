#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

f = cgi.FieldStorage()

cmd = f.getvalue("x")

#--------------------------------------particular---namespace------------------------------------------------------------------
if "in" in cmd: #for namespace filter
    command,namespace = cmd.split("in")

    if "get" in command or "show" in command: #show resources in a namespace
        #eg-> show pods in <ns>
        if "pod" in command or "pods" in command:
            print(subprocess.getoutput(f"kubectl get pods -n {namespace} --kubeconfig admin.conf"))

        elif "svc" in command or "services" in command or "service" in command:
            print(subprocess.getoutput(f"kubectl get svc -n {namespace} --kubeconfig admin.conf"))

        elif "deployment" in command or 'deploy' in command or 'deployments' in command or ' deploys' in command:
            print(subprocess.getoutput(f"kubectl get deployments -n {namespace} --kubeconfig admin.conf"))

#---------------------------------------------------delete------------------------------------------------------
    elif "delete" in command or 'del' in command or 'remove' in command: #delete resources in a namespace
        #eg-> delete/remove all pods in <ns> or delete pod <name> in <ns>
        if 'pod' in command or 'pods' in cmd: #delete pods in a namespace
            if 'all' in command:
                print(subprocess.getoutput(f'kubectl delete --all pods -n {namespace} --kubeconfig admin.conf'))
            else:
                operation , pod_name = command.split('pod')
                print(subprocess.getoutput(f'kubectl delete po {pod_name} -n {namespace} --kubeconfig admin.conf'))
        

        elif 'service' in command or 'services' in command: #delete sevices in a namespace
            if 'all' in command:
                print(subprocess.getoutput(f'kubectl delete --all svc -n {namespace} --kubeconfig admin.conf'))
            else:
                operation , svc_name = command.split('service')
                print(subprocess.getoutput(f'kubectl delete svc {svc_name} -n {namespace} --kubeconfig admin.conf'))


        elif 'deployment' in command or 'deployments' in command or 'deploy' in command: #delete deployments  in a namespace
            if 'all' in command:
                print(subprocess.getoutput(f'kubectl delete --all deploy -n {namespace} --kubeconfig admin.conf'))
            else:
                operation , deploy_name = command.split('deployment')
                print(subprocess.getoutput(f'kubectl delete deploy {deploy_name} -n {namespace} --kubeconfig admin.conf'))

#------------------------------------------------create----------------------------------------------------------------

    elif 'create' in command or 'run' in command or 'launch' in command: #launch resources in a namespace
        #eg-> launch pod <pod-name> with <img-name> in <namespace>
        if 'pod'  in command and 'image' in command: #launch a pod  in a namespace
            operation,pod_img = command.split('pod')
            pod_name,img = pod_img.split('with')
            no_use,img_name = img.split('image')
            print(subprocess.getoutput(f'kubectl run  {pod_name} --image={img_name} -n {namespace} --kubeconfig admin.conf'))
        

        elif 'deployment' in command and 'image' in command: #launch deployments  in a namespace
            operation,deploy_img = command.split('deployment')
            deploy_name,img = deploy_img.split('with')
            no_use,img_name = img.split('image')
            print(subprocess.getoutput(f'kubectl create  {deploy_name} --image={img_name} -n {namespace} --kubeconfig admin.conf'))

#--------------------------------------------------describe------------------------------------------------------

    elif 'describe' in command: #eg-> describe pods in <namespace>

        if 'pods' in command or 'pod' in command :
            print(subprocess.getoutput(f"kubectl describe pods -n {namespace} --kubeconfig admin.conf"))

        if 'service' in command or 'services' in command or 'svc' in command:
            print(subprocess.getoutput(f"kubectl describe svc -n {namespace} --kubeconfig admin.conf"))

        if 'deployment' in command or 'deploy' in command or 'deployments' in command:
            print(subprocess.getoutput(f"kubectl describe deploy -n {namespace} --kubeconfig admin.conf"))
#-------------------------------default namespace --------------------------------------------------------------

elif "get" in cmd or "show" in cmd: #see resources in  default namespace
    #eg -> show pods 

    if "pod" in cmd or "pods" in cmd :
        print(subprocess.getoutput("kubectl get po --kubeconfig admin.conf"))

    elif "svc" in cmd or "services" in cmd or "service" in cmd:
        print(subprocess.getoutput("kubectl get svc --kubeconfig admin.conf"))

    elif "namespace" in cmd or 'namespaces' in cmd or 'ns' in cmd:
        print(subprocess.getoutput("kubectl get ns --kubeconfig admin.conf"))
    
    elif "deployment" in cmd or 'deploy' in cmd or 'deployments' in cmd or ' deploys' in cmd:
        print(subprocess.getoutput("kubectl get deployments --kubeconfig admin.conf"))


elif 'remove' in cmd or 'delete' in cmd or 'del' in cmd: #delete resources in default namespace
    #eg-> remove pod <name> or remove all pods
    if 'pod' in cmd or 'pods' in cmd: #delete pods in default  namespace
        if 'all' in cmd:
            print(subprocess.getoutput(f'kubectl delete --all pods  --kubeconfig admin.conf'))
        else:
            operation , pod_name = cmd.split('pod')
            print(subprocess.getoutput(f'kubectl delete po {pod_name}  --kubeconfig admin.conf'))
        

    elif 'service' in cmd or 'services' in cmd: #delete sevices in default namespac
        if 'all' in cmd:
            print(subprocess.getoutput(f'kubectl delete --all svc --kubeconfig admin.conf'))
        else:
            operation , svc_name = cmd.split('service')
            print(subprocess.getoutput(f'kubectl delete svc {svc_name} --kubeconfig admin.conf'))


    elif 'deployment' in cmd or 'deployments' in cmd or 'deploy' in cmd: #delete deployments  in default namespace
        if 'all' in cmd:
            print(subprocess.getoutput(f'kubectl delete --all deploy --kubeconfig admin.conf'))
        else:
            operation , deploy_name = cmd.split('deployment')
            print(subprocess.getoutput(f'kubectl delete deploy {deploy_name}  --kubeconfig admin.conf'))

    elif 'namespace' in cmd or 'namespaces' in cmd or 'ns' in cmd: #delete namespaces
        if 'all' in cmd:
            print(subprocess.getoutput(f'kubectl delete --all namespace --kubeconfig admin.conf'))
        else:
            operation,ns_name = cmd.split('namespace')
            print(subprocess.getoutput(f'kubectl delete namespace {ns_name} --kubeconfig admin.conf'))

elif 'create' in cmd or 'run' in cmd or 'launch' in cmd: #launch resources in a namespace
        #eg-> launch pod <pod-name> with <img-name> 
    if 'pod'  in cmd and 'image' in cmd: #launch a pod  in a namespace
        operation,pod_img = cmd.split('pod')
        pod_name,img = pod_img.split('with')
        no_use,img_name = img.split('image')
        print(subprocess.getoutput(f'kubectl run  {pod_name} --image={img_name} --kubeconfig admin.conf'))
    

    elif 'deployment' in cmd and 'image' in cmd: #launch deployments  in a namespace
        operation,deploy_img = cmd.split('deployment')
        deploy_name,img = deploy_img.split('with')
        no_use,img_name = img.split('image')
        print(subprocess.getoutput(f'kubectl create  {deploy_name} --image={img_name} --kubeconfig admin.conf'))       

elif "describe" in cmd: #eg- describe pods
    if 'pods' in cmd or 'pod' in cmd :
        print(subprocess.getoutput("kubectl describe pods --kubeconfig admin.conf"))

    if 'service' in cmd or 'services' in cmd or 'svc' in cmd:
        print(subprocess.getoutput("kubectl describe svc --kubeconfig admin.conf"))

    if 'deployment' in cmd or 'deploy' in cmd or 'deployments' in cmd:
        print(subprocess.getoutput("kubectl describe deploy --kubeconfig admin.conf"))
else:
    print(subprocess.getoutput(cmd+" --kubeconfig admin.conf"))
