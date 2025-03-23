import yaml
import sys

office = sys.argv[1]

with open("anchors.yaml", 'r', encoding='utf8') as stream:
    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            if key == office:
                for key, value in value.items():
                    print(f"{key}: {value}")
    except yaml.YAMLError as exc:
        print(exc)