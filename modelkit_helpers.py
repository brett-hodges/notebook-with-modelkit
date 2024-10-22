import subprocess

def kit_login(user: str, passwd: str, registry: str = "jozu.ml"):
    subprocess.run(["kit", "login", registry, "-u", user, "--password-stdin"], input=passwd, text=True)

def kit_logout(registry: str = "jozu.ml"):
    subprocess.run(["kit", "logout", registry])

def kit_unpack(repo_path_with_tag):
    subprocess.run(["kit", "unpack", "-o", repo_path_with_tag])

def kit_pack(repo_path_with_tag: str):
    subprocess.run(["kit", "pack", ".", "-t", repo_path_with_tag])

def kit_push(repo_path_with_tag):
    subprocess.run(["kit", "push", repo_path_with_tag])

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