from flask import Flask, render_template
from kubernetes import client, config
from kubernetes.client.rest import ApiException

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def get_service_cluster_ip():
    # Define the Kubernetes service and namespace
    service_name = 'kubernetes'
    namespace = 'default'  # Replace with your namespace if different

    # Load Kubernetes configuration
    try:
        config.load_kube_config()  # Use this for local kubeconfig file
        # config.load_incluster_config() 
         # Use this if running inside a Kubernetes cluster
    except Exception as e:
        print(f"Error loading Kubernetes configuration: {e}")
        return render_template('cluster_ip.html', cluster_ip=None)

    # Create an API client
    v1 = client.CoreV1Api()

    try:
        # Get the service details
        service = v1.read_namespaced_service(name=service_name, namespace=namespace)
        # Extract the Cluster IP
        cluster_ip = service.spec.cluster_ip
    except ApiException as e:
        print(f"Error fetching service details: {e}")
        cluster_ip = None

    # Render the HTML template with the Cluster IP
    return render_template('cluster_ip.html', cluster_ip=cluster_ip)

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)