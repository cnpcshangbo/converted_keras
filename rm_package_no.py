import yaml

with open("environment.yml", "r") as file:
    data = yaml.safe_load(file)

for i, dependency in enumerate(data["dependencies"]):  # Iterate over the list
    if isinstance(dependency, str) and "=" in dependency:
        data["dependencies"][i] = dependency.split("=")[0]  # Modify in place

with open("environment.yml", "w") as file:
    yaml.dump(data, file, default_flow_style=False)
