import subprocess

def kit_login(user: str, passwd: str, registry: str = "jozu.ml"):
    command = ["kit", "login", registry, "-u", user, "--password-stdin"]
    print(' '.join(command))
    subprocess.run(command, input=passwd, text=True)

def kit_logout(registry: str = "jozu.ml"):
    command = ["kit", "logout", registry]
    print(' '.join(command))
    subprocess.run(command)

def kit_unpack(repo_path_with_tag):
    command = ["kit", "unpack", "-o", repo_path_with_tag]
    print(' '.join(command))
    subprocess.run(command)

def kit_pack(repo_path_with_tag: str):
    command = ["kit", "pack", ".", "-t", repo_path_with_tag]
    print(' '.join(command))
    subprocess.run(command)

def kit_push(repo_path_with_tag):
    command = ["kit", "push", repo_path_with_tag]
    print(' '.join(command))
    subprocess.run(command)

def unpack_collated_data_modelkit(user: str, passwd: str, namespace: str = "jozu-demos",
                                registry: str = "jozu.ml", tag: str = "collated-data-v1"):
    repo_path_with_tag = registry + "/" + namespace + "/" + "titanic-survivability" + ":" + tag
    kit_login(user, passwd, registry)
    kit_unpack(repo_path_with_tag)
    kit_logout()

def pack_and_push_modelkit(user: str, passwd: str, namespace: str, 
                           registry: str = "jozu.ml", tag:str = "latest"):
    repo_path_with_tag = registry + "/" + namespace + "/" + "titanic-survivability" + ":" + tag
    kit_login(user, passwd, registry)
    kit_pack(repo_path_with_tag)
    kit_push(repo_path_with_tag)
    kit_logout()