# Cloud Image Extractor

> Note: The project is using services provided from AWS (EC2, S3, DynamoDB and RDS).

### AWS CLI

1. Install ``AWS CLI`` on your system.
2. Use ``aws --version`` to check the version.
3. Set the file with your AWS security credentials.
> Use ``aws configure`` OR manually in folder ``~/.aws/credentials``.

---

### Preparando o projeto

1. Install ``poetry`` on your system
2. ```$ poetry install```
3. ```$ poetry run python cloud_image_extractor/__init__.py```

---

### PyExifTool Dependencies
- PyExifTool runs on **Python 3.6+**
- For PyExifTool to function, ``exiftool`` command-line tool must exist on the system.  If ``exiftool`` is not on the ``PATH``, you can specify the full pathname to it by using ``ExifTool(executable=<full path>)``.
- Your Exiftool version (``exiftool -ver``) >= required version ('12.15'). You can install the latest version of exiftool in **https://exiftool.org/install.html**


### Colaborators:
- Johnson Peixoto
- Livia Lorrana
- Robesvânia Araújo
- Robson Santos