import yaml

my_file = "multidoc.yaml"

with open(my_file, 'r', encoding='utf8') as stream:
    try:
        data = yaml.load_all(stream, Loader= yaml.SafeLoader)
        count = 0
        for yaml_doc in data:
            doc_no = count + 1
            print(f"<<<<< YAML Document {doc_no} >>>>>")
            for k, v in yaml_doc.items():
                print(f"key: {k}")
                print(f"value: {v}")
                print()
            count = count + 1
    except yaml.YAMLError as err:
        print(err)