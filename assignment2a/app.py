from kubernetes import client, config
from jinja2 import Template

# Load the Jinja template from file
with open('pod_template.yaml.j2') as file_:
    template_content = file_.read()

# Render the Jinja template with user inputs
template = Template(template_content)

# Example user inputs
user_inputs = {
    'name': 'example-pod-1',
    'app_label': 'example-app',
    'container_name': 'example-container',
    'image': 'nginx:latest',
    'container_port': 80
}

rendered_manifest = template.render(user_inputs)

# Print the rendered manifest (for debugging)
print(rendered_manifest)

# Load the Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes client
api_instance = client.CoreV1Api()

# Convert the rendered YAML to a Python dictionary
import yaml
manifest_dict = yaml.safe_load(rendered_manifest)

# Create the Pod
try:
    api_response = api_instance.create_namespaced_pod(
        namespace='default',
        body=manifest_dict
    )
    print("Pod created. status='%s'" % str(api_response.status))
except client.exceptions.ApiException as e:
    print("Exception when calling CoreV1Api->create_namespaced_pod: %s\n" % e)
