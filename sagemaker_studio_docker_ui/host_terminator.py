import os
       
def terminate_host(instance_id):
    is_bash_profile = os.path.isfile("/home/sagemaker-user/.bash_profile")
    is_bashrc = os.path.isfile("/home/sagemaker-user/.bashrc")
    command = f"sdocker terminate-host --instance-id {instance_id} &>> /home/sagemaker-user/.sagemaker_studio_docker_cli/ui_commands.log &"
    bash_comm = ""
    if is_bash_profile:
        bash_comm = "source ~/.bash_profile &>> /home/sagemaker-user/.sagemaker_studio_docker_cli/ui_commands.log && "
    elif is_bashrc:
        bash_comm = "source ~/.bashrc &>> /home/sagemaker-user/.sagemaker_studio_docker_cli/ui_commands.log && "
    
    os.system(bash_comm + command)
